from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models import db, AdminUser, User, Profile, IncomeCategory
from translations import translate

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    lang = session.get('lang', 'ta')
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        admin = AdminUser.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_user'] = admin.username
            flash('Admin login successful / நிர்வாகியாக உள்நுழைந்துள்ளீர்கள்', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials / தவறான நிர்வாகி விவரங்கள்', 'danger')

    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('admin_id'):
        return redirect(url_for('admin.login'))

    total_users = User.query.count()
    total_profiles = Profile.query.count()
    pending_profiles = Profile.query.filter_by(status='pending').count()
    approved_profiles = Profile.query.filter_by(status='approved').count()

    recent_profiles = Profile.query.order_by(Profile.created_at.desc()).limit(10).all()

    return render_template(
        'admin/dashboard.html',
        total_users=total_users,
        total_profiles=total_profiles,
        pending_profiles=pending_profiles,
        approved_profiles=approved_profiles,
        recent_profiles=recent_profiles
    )

@admin_bp.route('/profiles')
def profiles_list():
    if not session.get('admin_id'):
        return redirect(url_for('admin.login'))

    status_filter = request.args.get('status', 'all')
    query = Profile.query
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)

    profiles = query.order_by(Profile.created_at.desc()).all()

    return render_template(
        'admin/profiles.html',
        profiles=profiles,
        current_status=status_filter
    )

@admin_bp.route('/profile/<int:profile_id>/approve', methods=['POST'])
def approve_profile(profile_id):
    if not session.get('admin_id'):
        return redirect(url_for('admin.login'))

    profile = Profile.query.get_or_404(profile_id)
    profile.status = 'approved'
    db.session.commit()
    flash(f"Profile {profile.profile_id} approved successfully", 'success')
    return redirect(request.referrer or url_for('admin.profiles_list'))

@admin_bp.route('/profile/<int:profile_id>/reject', methods=['POST'])
def reject_profile(profile_id):
    if not session.get('admin_id'):
        return redirect(url_for('admin.login'))

    profile = Profile.query.get_or_404(profile_id)
    profile.status = 'rejected'
    db.session.commit()
    flash(f"Profile {profile.profile_id} rejected", 'warning')
    return redirect(request.referrer or url_for('admin.profiles_list'))

@admin_bp.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('admin_user', None)
    flash('Logged out of admin panel', 'info')
    return redirect(url_for('admin.login'))
