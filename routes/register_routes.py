import os
import json
from datetime import datetime, date
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify, current_app
from werkzeug.utils import secure_filename
from models import (
    db, User, Profile, PersonalDetail, BirthDetail, Address,
    EducationDetail, CareerDetail, IncomeDetail, IncomeCategory,
    FamilyDetail, HoroscopeDetail, LifestyleDetail, PartnerPreference,
    ProfilePhoto, JathagamFile, PrivacySetting, RegistrationProgress
)
from translations import calculate_income_category, RASI_LIST, NAKSHATRA_LIST, translate

register_bp = Blueprint('register', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'webp'}

@register_bp.route('/register')
def wizard():
    # If user already logged in and completed registration, redirect to dashboard
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if user and user.registration_status == 'completed':
            return redirect(url_for('dashboard.overview'))

    return render_template(
        'register.html',
        rasi_list=RASI_LIST,
        nakshatra_list=NAKSHATRA_LIST
    )

@register_bp.route('/api/calculate-income', methods=['POST'])
def calculate_income():
    data = request.get_json() or {}
    amount = data.get('amount', 0)
    cat_en, cat_ta = calculate_income_category(amount)
    return jsonify({
        'success': True,
        'category_en': cat_en,
        'category_ta': cat_ta
    })

@register_bp.route('/api/register/autosave', methods=['POST'])
def autosave():
    data = request.get_json() or {}
    step = data.get('step', 1)
    user_id = session.get('user_id')
    
    # Store in session as well
    draft = session.get('reg_draft', {})
    draft.update(data.get('form_data', {}))
    session['reg_draft'] = draft

    if user_id:
        prog = RegistrationProgress.query.filter_by(user_id=user_id).first()
        if not prog:
            prog = RegistrationProgress(user_id=user_id, current_step=step)
            db.session.add(prog)
        prog.current_step = max(prog.current_step, step)
        prog.step_data_json = json.dumps(draft)
        db.session.commit()

    return jsonify({'success': True, 'message': 'Autosaved successfully'})

@register_bp.route('/api/register/resume', methods=['GET'])
def resume_data():
    user_id = session.get('user_id')
    if user_id:
        prog = RegistrationProgress.query.filter_by(user_id=user_id).first()
        if prog and prog.step_data_json:
            try:
                saved_data = json.loads(prog.step_data_json)
                return jsonify({
                    'resumed': True,
                    'current_step': prog.current_step,
                    'data': saved_data
                })
            except Exception:
                pass
    
    # Fallback to session draft if available
    draft = session.get('reg_draft', {})
    if draft:
        return jsonify({
            'resumed': True,
            'current_step': session.get('reg_current_step', 1),
            'data': draft
        })

    return jsonify({'resumed': False, 'current_step': 1, 'data': {}})

@register_bp.route('/api/register/step/<int:step_num>', methods=['POST'])
def save_step(step_num):
    data = request.form.to_dict()
    user_id = session.get('user_id')

    # Update draft in session
    draft = session.get('reg_draft', {})
    draft.update(data)
    session['reg_draft'] = draft
    session['reg_current_step'] = step_num + 1

    # Step 1: Basic Details & Account Creation
    if step_num == 1:
        email = data.get('email', '').strip().lower()
        mobile = data.get('mobile', '').strip()
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        profile_type = data.get('profile_type', 'bride')
        profile_created_for = data.get('profile_created_for', 'Self')
        marital_status = data.get('marital_status', 'Never Married')

        # Validations
        if not email or not mobile or not first_name or not last_name:
            return jsonify({'success': False, 'error': 'All basic fields are mandatory / அனைத்து அடிப்படை விவரங்களும் அவசியமானது'}), 400

        if password and confirm_password and password != confirm_password:
            return jsonify({'success': False, 'error': 'Passwords do not match / கடவுச்சொற்கள் பொருந்தவில்லை'}), 400

        if not user_id:
            # Check unique email & mobile
            if User.query.filter_by(email=email).first():
                return jsonify({'success': False, 'error': 'Email is already registered / மின்னஞ்சல் ஏற்கனவே பயன்பாட்டில் உள்ளது'}), 400
            if User.query.filter_by(mobile=mobile).first():
                return jsonify({'success': False, 'error': 'Mobile is already registered / மொபைல் எண் ஏற்கனவே பயன்பாட்டில் உள்ளது'}), 400

            user = User(
                email=email,
                mobile=mobile,
                role='user',
                registration_status='in_progress'
            )
            user.set_password(password or 'Password123')
            db.session.add(user)
            db.session.flush()

            # Create profile
            gender = 'Female' if profile_type.lower() == 'bride' else 'Male'
            count = Profile.query.count() + 10001
            profile_code = f"MAT-{count}"
            
            profile = Profile(
                user_id=user.id,
                profile_id=profile_code,
                profile_type=profile_type.lower(),
                profile_created_for=profile_created_for,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                status='pending'
            )
            db.session.add(profile)
            db.session.flush()

            # Add initial personal detail
            p_det = PersonalDetail(profile_id=profile.id, marital_status=marital_status)
            db.session.add(p_det)

            # Registration progress
            prog = RegistrationProgress(
                user_id=user.id,
                current_step=2,
                step_data_json=json.dumps(draft)
            )
            db.session.add(prog)

            db.session.commit()
            session['user_id'] = user.id
            session['profile_id'] = profile.profile_id
            session['user_name'] = profile.first_name
        else:
            user = User.query.get(user_id)
            if user and user.profile:
                user.profile.first_name = first_name
                user.profile.last_name = last_name
                user.profile.profile_type = profile_type.lower()
                user.profile.profile_created_for = profile_created_for
                if user.profile.personal_details:
                    user.profile.personal_details.marital_status = marital_status
                db.session.commit()

        return jsonify({'success': True, 'next_step': 2})

    # For steps 2-8, ensure user exists
    if not user_id:
        return jsonify({'success': False, 'error': 'Session expired. Please restart step 1.'}), 400

    user = User.query.get(user_id)
    profile = user.profile

    if step_num == 2:
        # Personal & Birth Details
        dob_str = data.get('date_of_birth')
        tob_str = data.get('time_of_birth')
        birth_city = data.get('birth_city')
        height = data.get('height')
        weight = data.get('weight')
        blood_group = data.get('blood_group')
        mother_tongue = data.get('mother_tongue', 'Tamil')
        religion = data.get('religion', 'Hindu')
        community = data.get('community')
        gothram = data.get('gothram')

        # Update Personal
        if not profile.personal_details:
            profile.personal_details = PersonalDetail(profile_id=profile.id)
        profile.personal_details.height = height
        profile.personal_details.weight = weight
        profile.personal_details.blood_group = blood_group
        profile.personal_details.mother_tongue = mother_tongue
        profile.personal_details.religion = religion
        profile.personal_details.community = community
        profile.personal_details.gothram = gothram

        # Update Birth
        dob_val = None
        if dob_str:
            try:
                dob_val = datetime.strptime(dob_str, '%Y-%m-%d').date()
            except ValueError:
                dob_val = date(1998, 1, 1)

        if not profile.birth_details:
            profile.birth_details = BirthDetail(
                profile_id=profile.id,
                date_of_birth=dob_val or date(1998, 1, 1),
                time_of_birth=tob_str,
                birth_city=birth_city
            )
        else:
            if dob_val:
                profile.birth_details.date_of_birth = dob_val
            profile.birth_details.time_of_birth = tob_str
            profile.birth_details.birth_city = birth_city

        db.session.commit()
        return jsonify({'success': True, 'next_step': 3})

    elif step_num == 3:
        # Address Details
        address_1 = data.get('address_1', '')
        address_2 = data.get('address_2', '')
        pincode = data.get('pincode', '')
        city = data.get('city', '')
        district = data.get('district', '')
        state = data.get('state', 'Tamil Nadu')
        country = data.get('country', 'India')

        if not profile.address:
            profile.address = Address(
                profile_id=profile.id,
                address_1=address_1,
                address_2=address_2,
                pincode=pincode,
                city=city,
                district=district,
                state=state,
                country=country
            )
        else:
            profile.address.address_1 = address_1
            profile.address.address_2 = address_2
            profile.address.pincode = pincode
            profile.address.city = city
            profile.address.district = district
            profile.address.state = state
            profile.address.country = country

        db.session.commit()
        return jsonify({'success': True, 'next_step': 4})

    elif step_num == 4:
        # Education, Career & Income
        qualification = data.get('qualification', '')
        qualification_details = data.get('qualification_details', '')
        job = data.get('job', '')
        company = data.get('company', '')
        working_place = data.get('working_place', '')
        employment_type = data.get('employment_type', 'Private Sector')
        income_val = data.get('income', '0')
        hide_income = 'hide_exact_income' in data

        try:
            annual_inc = float(income_val)
        except ValueError:
            annual_inc = 500000.0

        cat_en, _ = calculate_income_category(annual_inc)
        cat_obj = IncomeCategory.query.filter_by(name=cat_en).first()

        # Education
        if not profile.education_details:
            profile.education_details = EducationDetail(
                profile_id=profile.id,
                qualification=qualification,
                qualification_details=qualification_details
            )
        else:
            profile.education_details.qualification = qualification
            profile.education_details.qualification_details = qualification_details

        # Career
        if not profile.career_details:
            profile.career_details = CareerDetail(
                profile_id=profile.id,
                job=job,
                company=company,
                working_place=working_place,
                employment_type=employment_type
            )
        else:
            profile.career_details.job = job
            profile.career_details.company = company
            profile.career_details.working_place = working_place
            profile.career_details.employment_type = employment_type

        # Income
        if not profile.income_details:
            profile.income_details = IncomeDetail(
                profile_id=profile.id,
                annual_income=annual_inc,
                income_category=cat_en,
                category_id=cat_obj.id if cat_obj else None,
                hide_exact_income=hide_income
            )
        else:
            profile.income_details.annual_income = annual_inc
            profile.income_details.income_category = cat_en
            profile.income_details.category_id = cat_obj.id if cat_obj else None
            profile.income_details.hide_exact_income = hide_income

        db.session.commit()
        return jsonify({'success': True, 'next_step': 5, 'detected_category': cat_en})

    elif step_num == 5:
        # Family Details
        father_name = data.get('father_name', '')
        father_occ = data.get('father_occupation', '')
        mother_name = data.get('mother_name', '')
        mother_occ = data.get('mother_occupation', '')
        brothers = int(data.get('brothers', 0) or 0)
        sisters = int(data.get('sisters', 0) or 0)
        family_type = data.get('family_type', 'Nuclear')
        family_status = data.get('family_status', 'Middle Class')
        family_values = data.get('family_values', 'Traditional')
        poorvigam = data.get('poorvigam', '')

        if not profile.family_details:
            profile.family_details = FamilyDetail(
                profile_id=profile.id,
                father_name=father_name,
                father_occupation=father_occ,
                mother_name=mother_name,
                mother_occupation=mother_occ,
                brothers=brothers,
                sisters=sisters,
                family_type=family_type,
                family_status=family_status,
                family_values=family_values,
                poorvigam=poorvigam
            )
        else:
            profile.family_details.father_name = father_name
            profile.family_details.father_occupation = father_occ
            profile.family_details.mother_name = mother_name
            profile.family_details.mother_occupation = mother_occ
            profile.family_details.brothers = brothers
            profile.family_details.sisters = sisters
            profile.family_details.family_type = family_type
            profile.family_details.family_status = family_status
            profile.family_details.family_values = family_values
            profile.family_details.poorvigam = poorvigam

        db.session.commit()
        return jsonify({'success': True, 'next_step': 6})

    elif step_num == 6:
        # Horoscope Details
        rasi = data.get('rasi', '')
        nakshatra = data.get('nakshatra', '')
        lagnam = data.get('lagnam', '')
        dosham = data.get('dosham', 'No Dosham')

        if not profile.horoscope_details:
            profile.horoscope_details = HoroscopeDetail(
                profile_id=profile.id,
                rasi=rasi,
                nakshatra=nakshatra,
                lagnam=lagnam,
                dosham=dosham,
                chevvai_dosham=(dosham == 'Chevvai Dosham'),
                rahu_ketu_dosham=(dosham == 'Rahu-Ketu Dosham')
            )
        else:
            profile.horoscope_details.rasi = rasi
            profile.horoscope_details.nakshatra = nakshatra
            profile.horoscope_details.lagnam = lagnam
            profile.horoscope_details.dosham = dosham
            profile.horoscope_details.chevvai_dosham = (dosham == 'Chevvai Dosham')
            profile.horoscope_details.rahu_ketu_dosham = (dosham == 'Rahu-Ketu Dosham')

        # Handle horoscope file upload if present
        if 'jathagam_photo' in request.files:
            file = request.files['jathagam_photo']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"jathagam_{profile.id}_{file.filename}")
                upload_dir = current_app.config['UPLOAD_FOLDER']
                os.makedirs(upload_dir, exist_ok=True)
                file_path = os.path.join(upload_dir, filename)
                file.save(file_path)
                rel_path = f"/static/uploads/{filename}"
                profile.horoscope_details.jathagam_photo = rel_path
                jfile = JathagamFile(profile_id=profile.id, file_path=rel_path, file_name=filename)
                db.session.add(jfile)

        db.session.commit()
        return jsonify({'success': True, 'next_step': 7})

    elif step_num == 7:
        # Profile Photo Uploads
        upload_dir = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_dir, exist_ok=True)

        if 'profile_photo' in request.files:
            file = request.files['profile_photo']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"profile_{profile.id}_{int(datetime.utcnow().timestamp())}_{file.filename}")
                file_path = os.path.join(upload_dir, filename)
                file.save(file_path)
                rel_path = f"/static/uploads/{filename}"
                
                # Check if primary photo exists, if so update it, else create
                curr_primary = profile.photos.filter_by(is_primary=True).first()
                if curr_primary:
                    curr_primary.file_path = rel_path
                else:
                    new_photo = ProfilePhoto(profile_id=profile.id, file_path=rel_path, is_primary=True)
                    db.session.add(new_photo)

        # Additional photos
        additional_files = request.files.getlist('additional_photos')
        for file in additional_files:
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"gallery_{profile.id}_{int(datetime.utcnow().timestamp())}_{file.filename}")
                file_path = os.path.join(upload_dir, filename)
                file.save(file_path)
                new_photo = ProfilePhoto(profile_id=profile.id, file_path=f"/static/uploads/{filename}", is_primary=False)
                db.session.add(new_photo)

        db.session.commit()
        return jsonify({'success': True, 'next_step': 8})

    elif step_num == 8:
        # Final Step: Review & Submission
        about_me = data.get('about_me', '')
        if about_me:
            profile.about_me = about_me

        user.registration_status = 'completed'
        profile.status = 'approved'  # Approved so user immediately sees their active profile!
        
        # Partner preferences defaults
        if not profile.partner_preferences:
            pref = PartnerPreference(
                profile_id=profile.id,
                preferred_religion=profile.personal_details.religion if profile.personal_details else 'Hindu',
                preferred_community=profile.personal_details.community if profile.personal_details else None
            )
            db.session.add(pref)

        # Privacy settings defaults
        if not profile.privacy_settings:
            priv = PrivacySetting(
                profile_id=profile.id,
                hide_exact_income=True,
                hide_mobile=True,
                hide_email=True
            )
            db.session.add(priv)

        # Mark progress completed
        prog = RegistrationProgress.query.filter_by(user_id=user.id).first()
        if prog:
            prog.is_completed = True
            prog.current_step = 8

        db.session.commit()

        # Clear registration session draft
        session.pop('reg_draft', None)
        session.pop('reg_current_step', None)

        lang = session.get('lang', 'ta')
        return jsonify({
            'success': True,
            'completed': True,
            'message': translate('profile_submitted_success', lang),
            'redirect_url': url_for('dashboard.overview')
        })

    return jsonify({'success': False, 'error': 'Invalid step number'}), 400
