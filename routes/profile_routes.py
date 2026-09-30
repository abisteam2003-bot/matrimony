from datetime import datetime
from flask import Blueprint, render_template, request, session, jsonify, abort, redirect, url_for, flash
from models import (
    db, Profile, User, Shortlist, Interest, ProfileView,
    PersonalDetail, BirthDetail, Address, EducationDetail,
    CareerDetail, IncomeDetail, FamilyDetail, HoroscopeDetail,
    PrivacySetting, Notification
)
from translations import translate

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<profile_id>')
def view_profile(profile_id):
    lang = session.get('lang', 'ta')
    user_id = session.get('user_id')

    profile = Profile.query.filter_by(profile_id=profile_id).first_or_404()

    # Track profile view if viewer is logged in and not viewing self
    if user_id and profile.user_id != user_id:
        pv = ProfileView(viewer_id=user_id, viewed_profile_id=profile.id)
        db.session.add(pv)
        db.session.commit()

    is_shortlisted = False
    interest_status = None
    can_view_contact = False

    if user_id:
        sl = Shortlist.query.filter_by(user_id=user_id, profile_id=profile.id).first()
        is_shortlisted = bool(sl)

        # Check interest between current user and profile owner
        interest = Interest.query.filter(
            ((Interest.sender_id == user_id) & (Interest.receiver_id == profile.user_id)) |
            ((Interest.sender_id == profile.user_id) & (Interest.receiver_id == user_id))
        ).first()

        if interest:
            interest_status = interest.status
            if interest.status == 'accepted':
                can_view_contact = True
        
        # Self profile view can always view contact
        if profile.user_id == user_id:
            can_view_contact = True

    return render_template(
        'profile_detail.html',
        profile=profile,
        is_shortlisted=is_shortlisted,
        interest_status=interest_status,
        can_view_contact=can_view_contact
    )

@profile_bp.route('/api/shortlist/toggle', methods=['POST'])
def toggle_shortlist():
    lang = session.get('lang', 'ta')
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'login_required': True, 'error': 'Please login to shortlist / உள்நுழையவும்'}), 401

    data = request.get_json() or {}
    profile_id_num = data.get('profile_id')
    if not profile_id_num:
        return jsonify({'success': False, 'error': 'Profile ID missing'}), 400

    existing = Shortlist.query.filter_by(user_id=user_id, profile_id=profile_id_num).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({
            'success': True,
            'shortlisted': False,
            'message': translate('shortlist_removed_success', lang)
        })
    else:
        new_sl = Shortlist(user_id=user_id, profile_id=profile_id_num)
        db.session.add(new_sl)
        db.session.commit()
        return jsonify({
            'success': True,
            'shortlisted': True,
            'message': translate('shortlist_added_success', lang)
        })

@profile_bp.route('/api/interest/send', methods=['POST'])
def send_interest():
    lang = session.get('lang', 'ta')
    sender_id = session.get('user_id')
    if not sender_id:
        return jsonify({'success': False, 'login_required': True, 'error': 'Please login to express interest / உள்நுழையவும்'}), 401

    data = request.get_json() or {}
    target_profile_id = data.get('profile_id')
    target_profile = Profile.query.get(target_profile_id)
    if not target_profile:
        return jsonify({'success': False, 'error': 'Profile not found'}), 404

    receiver_id = target_profile.user_id
    if sender_id == receiver_id:
        return jsonify({'success': False, 'error': 'Cannot send interest to yourself'}), 400

    # Check if already sent
    existing = Interest.query.filter_by(sender_id=sender_id, receiver_id=receiver_id).first()
    if existing:
        return jsonify({'success': True, 'already_sent': True, 'message': 'Interest already expressed'})

    interest = Interest(
        sender_id=sender_id,
        receiver_id=receiver_id,
        status='pending',
        message=data.get('message', 'Interested in your profile')
    )
    db.session.add(interest)

    # Add notification for receiver
    sender_user = User.query.get(sender_id)
    sender_name = sender_user.profile.full_name if sender_user and sender_user.profile else "A member"
    notif = Notification(
        user_id=receiver_id,
        title=f"New Interest Received from {sender_name}",
        title_tamil=f"{sender_name} உங்களிடம் விருப்பம் தெரிவித்துள்ளார்",
        message=f"{sender_name} has expressed interest in connecting with you.",
        message_tamil=f"{sender_name} உங்கள் சுயவிவரத்தில் ஆர்வம் காட்டியுள்ளார்.",
        link=f"/profile/{sender_user.profile.profile_id}" if sender_user and sender_user.profile else "/dashboard/interests"
    )
    db.session.add(notif)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': translate('interest_sent_success', lang)
    })

@profile_bp.route('/api/interest/respond', methods=['POST'])
def respond_interest():
    lang = session.get('lang', 'ta')
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Login required'}), 401

    data = request.get_json() or {}
    interest_id = data.get('interest_id')
    action = data.get('action')  # accept, decline

    interest = Interest.query.get(interest_id)
    if not interest or interest.receiver_id != user_id:
        return jsonify({'success': False, 'error': 'Invalid request'}), 400

    if action == 'accept':
        interest.status = 'accepted'
    elif action == 'decline':
        interest.status = 'declined'
    
    db.session.commit()
    msg = 'விருப்பம் ஏற்றுக்கொள்ளப்பட்டது' if lang == 'ta' else 'Interest accepted'
    return jsonify({'success': True, 'status': interest.status, 'message': msg})
