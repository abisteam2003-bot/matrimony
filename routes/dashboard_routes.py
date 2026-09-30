from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from models import (
    db, User, Profile, Shortlist, Interest, ProfileView,
    PrivacySetting, IncomeDetail, PersonalDetail, BirthDetail,
    EducationDetail, CareerDetail, FamilyDetail, HoroscopeDetail
)
from translations import translate

dashboard_bp = Blueprint('dashboard', __name__)

def login_required_check():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    return None

@dashboard_bp.route('/dashboard')
def overview():
    redir = login_required_check()
    if redir:
        return redir

    user_id = session['user_id']
    user = User.query.get_or_404(user_id)
    profile = user.profile

    shortlists_count = Shortlist.query.filter_by(user_id=user_id).count()
    sent_interests_count = Interest.query.filter_by(sender_id=user_id).count()
    received_interests_count = Interest.query.filter_by(receiver_id=user_id).count()
    views_count = 0
    if profile:
        views_count = ProfileView.query.filter_by(viewed_profile_id=profile.id).count()

    # Recommended matching profiles (opposite gender)
    matches = []
    if profile:
        target_type = 'groom' if profile.profile_type == 'bride' else 'bride'
        matches = Profile.query.filter_by(profile_type=target_type, status='approved')\
                               .order_by(Profile.created_at.desc()).limit(4).all()

    return render_template(
        'dashboard.html',
        user=user,
        profile=profile,
        shortlists_count=shortlists_count,
        sent_interests_count=sent_interests_count,
        received_interests_count=received_interests_count,
        views_count=views_count,
        matches=matches
    )

@dashboard_bp.route('/dashboard/shortlists')
def shortlists():
    redir = login_required_check()
    if redir:
        return redir

    user_id = session['user_id']
    shortlist_items = Shortlist.query.filter_by(user_id=user_id)\
                                     .order_by(Shortlist.created_at.desc()).all()
    profiles = [item.profile for item in shortlist_items if item.profile]

    return render_template(
        'shortlist.html',
        profiles=profiles
    )

@dashboard_bp.route('/dashboard/interests')
def interests():
    redir = login_required_check()
    if redir:
        return redir

    user_id = session['user_id']
    sent = Interest.query.filter_by(sender_id=user_id)\
                         .order_by(Interest.created_at.desc()).all()
    received = Interest.query.filter_by(receiver_id=user_id)\
                               .order_by(Interest.created_at.desc()).all()

    return render_template(
        'interests.html',
        sent=sent,
        received=received
    )

@dashboard_bp.route('/dashboard/privacy', methods=['GET', 'POST'])
def privacy():
    redir = login_required_check()
    if redir:
        return redir

    lang = session.get('lang', 'ta')
    user_id = session['user_id']
    user = User.query.get_or_404(user_id)
    profile = user.profile

    if not profile.privacy_settings:
        profile.privacy_settings = PrivacySetting(profile_id=profile.id)
        db.session.commit()

    privacy_obj = profile.privacy_settings

    if request.method == 'POST':
        privacy_obj.hide_exact_income = 'hide_exact_income' in request.form
        privacy_obj.hide_mobile = 'hide_mobile' in request.form
        privacy_obj.hide_email = 'hide_email' in request.form
        privacy_obj.photo_visibility = request.form.get('photo_visibility', 'all')
        privacy_obj.horoscope_visibility = request.form.get('horoscope_visibility', 'all')
        
        # Sync with income_details table as well
        if profile.income_details:
            profile.income_details.hide_exact_income = privacy_obj.hide_exact_income

        db.session.commit()
        msg = 'தனியுரிமை அமைப்புகள் புதுப்பிக்கப்பட்டன' if lang == 'ta' else 'Privacy settings updated successfully'
        flash(msg, 'success')
        return redirect(url_for('dashboard.privacy'))

    return render_template(
        'privacy_settings.html',
        privacy=privacy_obj
    )
