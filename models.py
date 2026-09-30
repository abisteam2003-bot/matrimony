from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    mobile = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user')  # user, admin
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    registration_status = db.Column(db.String(20), default='in_progress')  # in_progress, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='all, delete-orphan')
    registration_progress = db.relationship('RegistrationProgress', backref='user', uselist=False, cascade='all, delete-orphan')
    sent_interests = db.relationship('Interest', foreign_keys='Interest.sender_id', backref='sender', lazy='dynamic')
    received_interests = db.relationship('Interest', foreign_keys='Interest.receiver_id', backref='receiver', lazy='dynamic')
    shortlists = db.relationship('Shortlist', backref='user', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    profile_id = db.Column(db.String(30), unique=True, nullable=False, index=True)  # e.g., MAT-10001
    profile_type = db.Column(db.String(20), nullable=False)  # bride, groom
    profile_created_for = db.Column(db.String(50), nullable=False)  # Self, Son, Daughter, etc.
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # Female, Male
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, hidden
    about_me = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Component Details Relationships
    personal_details = db.relationship('PersonalDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    birth_details = db.relationship('BirthDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    address = db.relationship('Address', backref='profile', uselist=False, cascade='all, delete-orphan')
    education_details = db.relationship('EducationDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    career_details = db.relationship('CareerDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    income_details = db.relationship('IncomeDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    family_details = db.relationship('FamilyDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    horoscope_details = db.relationship('HoroscopeDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    lifestyle_details = db.relationship('LifestyleDetail', backref='profile', uselist=False, cascade='all, delete-orphan')
    partner_preferences = db.relationship('PartnerPreference', backref='profile', uselist=False, cascade='all, delete-orphan')
    privacy_settings = db.relationship('PrivacySetting', backref='profile', uselist=False, cascade='all, delete-orphan')
    photos = db.relationship('ProfilePhoto', backref='profile', lazy='dynamic', cascade='all, delete-orphan')
    jathagam_files = db.relationship('JathagamFile', backref='profile', lazy='dynamic', cascade='all, delete-orphan')
    views_received = db.relationship('ProfileView', foreign_keys='ProfileView.viewed_profile_id', backref='viewed_profile', lazy='dynamic')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def primary_photo(self):
        photo = self.photos.filter_by(is_primary=True).first()
        if photo:
            return photo.file_path
        first = self.photos.first()
        if first:
            return first.file_path
        # Return fallback avatar depending on gender
        if self.gender == 'Female' or self.profile_type == 'bride':
            return '/static/images/avatar_female.svg'
        return '/static/images/avatar_male.svg'

    @property
    def age(self):
        if self.birth_details and self.birth_details.date_of_birth:
            today = datetime.today()
            dob = self.birth_details.date_of_birth
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return 26  # Default fallback


class PersonalDetail(db.Model):
    __tablename__ = 'personal_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    marital_status = db.Column(db.String(50), nullable=False, default='Never Married')
    height = db.Column(db.String(30), nullable=True)  # e.g., 5 ft 6 in / 168 cm
    weight = db.Column(db.String(20), nullable=True)  # e.g., 65 kg
    blood_group = db.Column(db.String(10), nullable=True)
    mother_tongue = db.Column(db.String(50), default='Tamil')
    religion = db.Column(db.String(50), default='Hindu')
    community = db.Column(db.String(80), nullable=True)  # Caste/Community
    sub_community = db.Column(db.String(80), nullable=True)
    gothram = db.Column(db.String(80), nullable=True)


class BirthDetail(db.Model):
    __tablename__ = 'birth_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    time_of_birth = db.Column(db.String(30), nullable=True)
    birth_city = db.Column(db.String(80), nullable=True)
    birth_state = db.Column(db.String(80), nullable=True)
    birth_country = db.Column(db.String(80), default='India')


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    address_1 = db.Column(db.String(255), nullable=False)
    address_2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False, default='Tamil Nadu')
    country = db.Column(db.String(100), nullable=False, default='India')
    pincode = db.Column(db.String(20), nullable=False)


class EducationDetail(db.Model):
    __tablename__ = 'education_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    qualification = db.Column(db.String(120), nullable=False)  # B.Tech, MBBS, MBA, etc.
    qualification_details = db.Column(db.String(255), nullable=True)  # College / Stream
    education_field = db.Column(db.String(100), nullable=True)


class CareerDetail(db.Model):
    __tablename__ = 'career_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    job = db.Column(db.String(120), nullable=False)  # Software Engineer, Doctor, etc.
    company = db.Column(db.String(150), nullable=True)
    working_place = db.Column(db.String(120), nullable=False)  # Chennai, Bangalore, Singapore, etc.
    employment_type = db.Column(db.String(60), nullable=False, default='Private Sector')  # Private, Government, Business, Self Employed


class IncomeCategory(db.Model):
    __tablename__ = 'income_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)  # ₹1L+, ₹3L+, etc.
    name_tamil = db.Column(db.String(80), nullable=False)  # ₹1 லட்சம்+, etc.
    min_amount = db.Column(db.Float, nullable=False)  # numeric min annual in INR
    max_amount = db.Column(db.Float, nullable=True)   # numeric max annual in INR
    display_order = db.Column(db.Integer, default=0)

    # Relationships
    incomes = db.relationship('IncomeDetail', backref='category_ref', lazy='dynamic')


class IncomeDetail(db.Model):
    __tablename__ = 'income_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    annual_income = db.Column(db.Float, nullable=False)  # Exact amount in INR
    income_category = db.Column(db.String(50), nullable=False)  # ₹1L+, ₹3L+, ₹5L+, ₹10L+, etc.
    category_id = db.Column(db.Integer, db.ForeignKey('income_categories.id'), nullable=True)
    currency = db.Column(db.String(10), default='INR')
    hide_exact_income = db.Column(db.Boolean, default=True)  # Privacy requirement: never show exact unless allowed


class FamilyDetail(db.Model):
    __tablename__ = 'family_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    father_name = db.Column(db.String(100), nullable=True)
    father_occupation = db.Column(db.String(120), nullable=True)
    mother_name = db.Column(db.String(100), nullable=True)
    mother_occupation = db.Column(db.String(120), nullable=True)
    brothers = db.Column(db.Integer, default=0)
    brothers_married = db.Column(db.Integer, default=0)
    sisters = db.Column(db.Integer, default=0)
    sisters_married = db.Column(db.Integer, default=0)
    family_type = db.Column(db.String(50), default='Nuclear')  # Nuclear, Joint
    family_status = db.Column(db.String(50), default='Middle Class')  # Middle Class, Upper Middle Class, Rich, Affluent
    family_values = db.Column(db.String(50), default='Traditional')  # Traditional, Moderate, Liberal
    poorvigam = db.Column(db.String(150), nullable=True)  # Ancestral origin


class HoroscopeDetail(db.Model):
    __tablename__ = 'horoscope_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    rasi = db.Column(db.String(80), nullable=True)  # Mesham, Rishabam, etc.
    nakshatra = db.Column(db.String(80), nullable=True)  # Ashwini, Bharani, etc.
    nakshatra_padam = db.Column(db.Integer, nullable=True)  # 1, 2, 3, 4
    lagnam = db.Column(db.String(80), nullable=True)
    dosham = db.Column(db.String(100), default='No Dosham')  # No Dosham, Chevvai Dosham, Rahu-Ketu Dosham
    chevvai_dosham = db.Column(db.Boolean, default=False)
    rahu_ketu_dosham = db.Column(db.Boolean, default=False)
    jathagam_photo = db.Column(db.String(255), nullable=True)


class LifestyleDetail(db.Model):
    __tablename__ = 'lifestyle_details'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    diet = db.Column(db.String(50), default='Vegetarian')  # Vegetarian, Non-Vegetarian, Eggetarian
    smoking = db.Column(db.String(50), default='No')
    drinking = db.Column(db.String(50), default='No')
    hobbies = db.Column(db.String(255), nullable=True)


class PartnerPreference(db.Model):
    __tablename__ = 'partner_preferences'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    preferred_age_min = db.Column(db.Integer, default=21)
    preferred_age_max = db.Column(db.Integer, default=32)
    preferred_height_min = db.Column(db.String(20), nullable=True)
    preferred_height_max = db.Column(db.String(20), nullable=True)
    preferred_marital_status = db.Column(db.String(100), default='Never Married')
    preferred_religion = db.Column(db.String(100), default='Hindu')
    preferred_community = db.Column(db.String(150), nullable=True)
    preferred_education = db.Column(db.String(150), nullable=True)
    preferred_occupation = db.Column(db.String(150), nullable=True)
    preferred_income = db.Column(db.String(100), nullable=True)
    preferred_location = db.Column(db.String(150), nullable=True)
    dosham_expectation = db.Column(db.String(100), default='Does not matter')


class ProfilePhoto(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    is_primary = db.Column(db.Boolean, default=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


class JathagamFile(db.Model):
    __tablename__ = 'jathagam_files'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(150), nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    profile = db.relationship('Profile', backref='shortlisted_by')


class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, declined
    message = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProfileView(db.Model):
    __tablename__ = 'profile_views'

    id = db.Column(db.Integer, primary_key=True)
    viewer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    viewed_profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False)
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    viewer = db.relationship('User', foreign_keys=[viewer_id])


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    title_tamil = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    message_tamil = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(255), nullable=True)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class PrivacySetting(db.Model):
    __tablename__ = 'privacy_settings'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False, unique=True)
    hide_exact_income = db.Column(db.Boolean, default=True)
    hide_mobile = db.Column(db.Boolean, default=True)  # hidden from non-connected
    hide_email = db.Column(db.Boolean, default=True)
    hide_full_address = db.Column(db.Boolean, default=True)
    photo_visibility = db.Column(db.String(30), default='all')  # all, members_only, on_request
    horoscope_visibility = db.Column(db.String(30), default='all')


class RegistrationProgress(db.Model):
    __tablename__ = 'registration_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    current_step = db.Column(db.Integer, default=1)
    step_data_json = db.Column(db.Text, nullable=True)  # JSON cache for partial wizard saves
    is_completed = db.Column(db.Boolean, default=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AdminUser(db.Model):
    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='superadmin')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
