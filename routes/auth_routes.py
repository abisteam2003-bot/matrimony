from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models import db, User, Profile, AdminUser
from translations import translate

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    lang = session.get('lang', 'ta')
    if request.method == 'POST':
        login_input = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not login_input or not password:
            msg = 'மின்னஞ்சல்/பயனர்பெயர் மற்றும் கடவுச்சொல்லை உள்ளிடவும்' if lang == 'ta' else 'Please enter username/email and password'
            flash(msg, 'danger')
            return render_template('login.html')

        login_lower = login_input.lower()

        # 1. Check if the user is an Administrator (by username or email)
        admin = AdminUser.query.filter(
            (AdminUser.username.ilike(login_input)) | (AdminUser.email.ilike(login_lower))
        ).first()

        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_user'] = admin.username
            admin_msg = 'நிர்வாகியாக வெற்றிகரமாக உள்நுழைந்துள்ளீர்கள்!' if lang == 'ta' else 'Welcome Admin! Logged in successfully.'
            flash(admin_msg, 'success')
            return redirect(url_for('admin.dashboard'))

        # 2. Check if it's a Member (by email or mobile number)
        user = User.query.filter(
            (User.email.ilike(login_lower)) | (User.mobile == login_input)
        ).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_email'] = user.email
            session['user_role'] = user.role
            
            # Check if profile exists
            if user.profile:
                session['profile_id'] = user.profile.profile_id
                session['user_name'] = user.profile.first_name
            else:
                session['user_name'] = 'Member'

            # If user has an in-progress registration, redirect to resume
            if user.registration_status == 'in_progress':
                return redirect(url_for('register.wizard'))

            welcome_msg = translate('login_success', lang)
            flash(welcome_msg, 'success')
            return redirect(url_for('dashboard.overview'))
        else:
            err_msg = 'தவறான பயனர் விவரங்கள் அல்லது கடவுச்சொல்' if lang == 'ta' else 'Invalid username/email or password'
            flash(err_msg, 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    lang = session.get('lang', 'ta')
    session.pop('user_id', None)
    session.pop('user_email', None)
    session.pop('user_role', None)
    session.pop('profile_id', None)
    session.pop('user_name', None)
    session.pop('admin_id', None)
    session.pop('admin_user', None)
    flash(translate('logout_success', lang), 'info')
    return redirect(url_for('index'))
