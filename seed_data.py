import os
from datetime import date, datetime
from models import (
    db, User, Profile, PersonalDetail, BirthDetail, Address,
    EducationDetail, CareerDetail, IncomeCategory, IncomeDetail,
    FamilyDetail, HoroscopeDetail, LifestyleDetail, PartnerPreference,
    ProfilePhoto, PrivacySetting, RegistrationProgress, AdminUser,
    Shortlist, Interest
)
from translations import INCOME_CATEGORIES_DATA

def seed_database(app):
    with app.app_context():
        # Ensure database tables exist
        db.create_all()

        # Seed Income Categories if empty
        if IncomeCategory.query.count() == 0:
            for cat in INCOME_CATEGORIES_DATA:
                ic = IncomeCategory(
                    name=cat['name'],
                    name_tamil=cat['name_tamil'],
                    min_amount=cat['min'],
                    max_amount=cat['max'],
                    display_order=cat['order']
                )
                db.session.add(ic)
            db.session.commit()
            print("Seeded Income Categories.")

        # Seed Superadmin if not exists
        if not AdminUser.query.filter_by(username='admin').first():
            admin = AdminUser(
                username='admin',
                email='admin@matromani.com',
                role='superadmin'
            )
            admin.set_password('Admin@123')
            db.session.add(admin)
            db.session.commit()
            print("Seeded Admin User: admin@matromani.com / Admin@123")

        # Check if users already seeded
        if User.query.count() > 0:
            print("Users already seeded.")
            return

        # Sample Profiles Data
        sample_profiles_data = [
            {
                "email": "karthik.raman@example.com",
                "mobile": "9840112345",
                "password": "Password123",
                "profile_id": "MAT-10001",
                "profile_type": "groom",
                "profile_created_for": "Self",
                "first_name": "Karthik",
                "last_name": "Ramanathan",
                "gender": "Male",
                "status": "approved",
                "about_me": "Tech enthusiast, classical music lover, and grounded individual seeking a like-minded life partner to share life's joys with mutual respect and understanding.",
                "marital_status": "Never Married",
                "height": "5 ft 11 in (180 cm)",
                "weight": "74",
                "blood_group": "B+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Brahmin - Iyer",
                "gothram": "Koushika",
                "dob": date(1995, 6, 15),
                "tob": "07:30 AM",
                "birth_city": "Chennai",
                "address_1": "14, 4th Main Road, Gandhi Nagar, Adyar",
                "city": "Chennai",
                "district": "Chennai",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "600020",
                "qualification": "B.Tech + M.S (Computer Science)",
                "qualification_details": "Anna University & Univ. of Texas",
                "job": "Staff Software Engineer",
                "company": "Amazon Cloud Services",
                "working_place": "Chennai",
                "employment_type": "Private Sector",
                "annual_income": 2800000.0,
                "income_cat": "₹25L+",
                "father_name": "Ramanathan Sundaram",
                "father_occ": "Retired Bank General Manager",
                "mother_name": "Lakshmi Ramanathan",
                "mother_occ": "Homemaker",
                "brothers": 1,
                "sisters": 0,
                "family_type": "Nuclear",
                "family_status": "Upper Middle Class",
                "family_values": "Traditional",
                "poorvigam": "Thanjavur",
                "rasi": "Mesham (Aries)",
                "nakshatra": "Ashwini",
                "lagnam": "Mithunam",
                "dosham": "No Dosham",
                "avatar": "/static/images/groom_1.svg"
            },
            {
                "email": "priya.soundar@example.com",
                "mobile": "9841223456",
                "password": "Password123",
                "profile_id": "MAT-10002",
                "profile_type": "bride",
                "profile_created_for": "Self",
                "first_name": "Priya",
                "last_name": "Soundararajan",
                "gender": "Female",
                "status": "approved",
                "about_me": "Dedicated doctor who cherishes family values, traditional arts, and traveling. Looking for a supportive, educated, and caring partner with cultural roots.",
                "marital_status": "Never Married",
                "height": "5 ft 4 in (163 cm)",
                "weight": "56",
                "blood_group": "O+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Mudaliar",
                "gothram": "Siva",
                "dob": date(1998, 9, 22),
                "tob": "10:15 AM",
                "birth_city": "Coimbatore",
                "address_1": "28, Race Course Road",
                "city": "Coimbatore",
                "district": "Coimbatore",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "641018",
                "qualification": "MBBS, M.D (Pediatrics)",
                "qualification_details": "PSG Institute of Medical Sciences",
                "job": "Pediatric Consultant",
                "company": "Apollo Multi-Specialty Hospital",
                "working_place": "Coimbatore",
                "employment_type": "Private Sector",
                "annual_income": 1400000.0,
                "income_cat": "₹10L+",
                "father_name": "Dr. Soundararajan K",
                "father_occ": "Senior Surgeon",
                "mother_name": "Vasuki Soundararajan",
                "mother_occ": "School Principal",
                "brothers": 0,
                "sisters": 1,
                "family_type": "Nuclear",
                "family_status": "Upper Middle Class",
                "family_values": "Moderate",
                "poorvigam": "Coimbatore",
                "rasi": "Rishabam (Taurus)",
                "nakshatra": "Rohini",
                "lagnam": "Simmam",
                "dosham": "No Dosham",
                "avatar": "/static/images/bride_1.svg"
            },
            {
                "email": "vignesh.nataraj@example.com",
                "mobile": "9842334567",
                "password": "Password123",
                "profile_id": "MAT-10003",
                "profile_type": "groom",
                "profile_created_for": "Son",
                "first_name": "Vignesh",
                "last_name": "Natarajan",
                "gender": "Male",
                "status": "approved",
                "about_me": "Chartered Accountant currently working with a Big 4 firm. Balanced mindset, fitness enthusiast, passionate about entrepreneurship and South Indian heritage.",
                "marital_status": "Never Married",
                "height": "5 ft 10 in (178 cm)",
                "weight": "72",
                "blood_group": "A+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Chettiar",
                "gothram": "Pirandamalai",
                "dob": date(1994, 11, 8),
                "tob": "04:45 PM",
                "birth_city": "Madurai",
                "address_1": "72, Alagarkovil Main Road, Tallakulam",
                "city": "Madurai",
                "district": "Madurai",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "625002",
                "qualification": "B.Com, ACA (Chartered Accountant)",
                "qualification_details": "Loyola College Chennai & ICAI",
                "job": "Associate Director - Advisory",
                "company": "PricewaterhouseCoopers (PwC)",
                "working_place": "Bangalore",
                "employment_type": "Private Sector",
                "annual_income": 3600000.0,
                "income_cat": "₹25L+",
                "father_name": "Natarajan Alagappan",
                "father_occ": "Industrialist & Real Estate",
                "mother_name": "Visalakshi Natarajan",
                "mother_occ": "Homemaker",
                "brothers": 1,
                "sisters": 1,
                "family_type": "Joint",
                "family_status": "Rich / Affluent",
                "family_values": "Traditional",
                "poorvigam": "Karaikudi",
                "rasi": "Kadagam (Cancer)",
                "nakshatra": "Poosam",
                "lagnam": "Thulaam",
                "dosham": "Chevvai Dosham",
                "avatar": "/static/images/groom_2.svg"
            },
            {
                "email": "deepa.annamalai@example.com",
                "mobile": "9843445678",
                "password": "Password123",
                "profile_id": "MAT-10004",
                "profile_type": "bride",
                "profile_created_for": "Self",
                "first_name": "Deepa",
                "last_name": "Annamalai",
                "gender": "Female",
                "status": "approved",
                "about_me": "AI Research Scientist working on cutting-edge neural networks. Love reading Tamil literature, playing the veena, and exploring nature trails.",
                "marital_status": "Never Married",
                "height": "5 ft 5 in (165 cm)",
                "weight": "54",
                "blood_group": "A1B+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Nadar",
                "gothram": "Kalingarayan",
                "dob": date(1997, 3, 14),
                "tob": "08:10 AM",
                "birth_city": "Madurai",
                "address_1": "15, Marina Coastal View",
                "city": "Singapore",
                "district": "Central",
                "state": "Singapore",
                "country": "Singapore",
                "pincode": "018981",
                "qualification": "M.Sc Data Science & AI",
                "qualification_details": "National University of Singapore (NUS)",
                "job": "Senior Machine Learning Engineer",
                "company": "Tech Global Solutions",
                "working_place": "Singapore",
                "employment_type": "Private Sector",
                "annual_income": 6200000.0,
                "income_cat": "₹50L+",
                "father_name": "Annamalai Muthuraj",
                "father_occ": "Export Business Owner",
                "mother_name": "Karpagavalli Annamalai",
                "mother_occ": "Professor of Botany",
                "brothers": 1,
                "sisters": 0,
                "family_type": "Nuclear",
                "family_status": "Upper Middle Class",
                "family_values": "Moderate",
                "poorvigam": "Sivakasi",
                "rasi": "Simmam (Leo)",
                "nakshatra": "Makam",
                "lagnam": "Dhanusu",
                "dosham": "No Dosham",
                "avatar": "/static/images/bride_2.svg"
            },
            {
                "email": "aravindh.senthil@example.com",
                "mobile": "9844556789",
                "password": "Password123",
                "profile_id": "MAT-10005",
                "profile_type": "groom",
                "profile_created_for": "Brother",
                "first_name": "Aravindh",
                "last_name": "Senthilvel",
                "gender": "Male",
                "status": "approved",
                "about_me": "Mechanical Design Engineer leading automotive EV systems. Warm-hearted, values simplicity, family ethics, and outdoor adventure.",
                "marital_status": "Never Married",
                "height": "5 ft 9 in (175 cm)",
                "weight": "70",
                "blood_group": "O-",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Kongu Vellalar Gounder",
                "gothram": "Porulanthai",
                "dob": date(1996, 7, 30),
                "tob": "06:20 AM",
                "birth_city": "Salem",
                "address_1": "45, Saradha College Road",
                "city": "Salem",
                "district": "Salem",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "636016",
                "qualification": "B.E (Mechanical) & MS CAD/CAM",
                "qualification_details": "PSG Tech Coimbatore",
                "job": "Lead Automotive Engineer",
                "company": "Hyundai R&D Center",
                "working_place": "Chennai",
                "employment_type": "Private Sector",
                "annual_income": 1250000.0,
                "income_cat": "₹10L+",
                "father_name": "Senthilvel Chinnusamy",
                "father_occ": "Agriculturalist & Landowner",
                "mother_name": "Chitra Senthilvel",
                "mother_occ": "Homemaker",
                "brothers": 1,
                "sisters": 0,
                "family_type": "Nuclear",
                "family_status": "Upper Middle Class",
                "family_values": "Traditional",
                "poorvigam": "Erode",
                "rasi": "Kanni (Virgo)",
                "nakshatra": "Hastham",
                "lagnam": "Kumbam",
                "dosham": "No Dosham",
                "avatar": "/static/images/groom_3.svg"
            },
            {
                "email": "meenakshi.sundaram@example.com",
                "mobile": "9845667890",
                "password": "Password123",
                "profile_id": "MAT-10006",
                "profile_type": "bride",
                "profile_created_for": "Daughter",
                "first_name": "Meenakshi",
                "last_name": "Sundaram",
                "gender": "Female",
                "status": "approved",
                "about_me": "Architect with a creative soul. Enjoys sustainable architecture, watercolor painting, temple heritage tours, and cozy family weekends.",
                "marital_status": "Never Married",
                "height": "5 ft 3 in (160 cm)",
                "weight": "52",
                "blood_group": "B-",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Pillai",
                "gothram": "Kasyapa",
                "dob": date(1999, 1, 18),
                "tob": "11:55 AM",
                "birth_city": "Tiruchirappalli",
                "address_1": "12, Thillai Nagar 10th Cross",
                "city": "Tiruchirappalli",
                "district": "Tiruchirappalli",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "620018",
                "qualification": "B.Arch (Architecture)",
                "qualification_details": "School of Architecture & Planning, Anna University",
                "job": "Architectural Designer",
                "company": "Studio Urban Crafts",
                "working_place": "Chennai",
                "employment_type": "Private Sector",
                "annual_income": 850000.0,
                "income_cat": "₹5L+",
                "father_name": "Sundaram Natarajan",
                "father_occ": "Retired PWD Executive Engineer",
                "mother_name": "Vasantha Sundaram",
                "mother_occ": "Government High School Teacher",
                "brothers": 1,
                "sisters": 0,
                "family_type": "Nuclear",
                "family_status": "Middle Class",
                "family_values": "Traditional",
                "poorvigam": "Thanjavur",
                "rasi": "Thulaam (Libra)",
                "nakshatra": "Swathi",
                "lagnam": "Mesham",
                "dosham": "Rahu-Ketu Dosham",
                "avatar": "/static/images/bride_3.svg"
            },
            {
                "email": "saravanan.murugan@example.com",
                "mobile": "9846778901",
                "password": "Password123",
                "profile_id": "MAT-10007",
                "profile_type": "groom",
                "profile_created_for": "Self",
                "first_name": "Saravanan",
                "last_name": "Murugesan",
                "gender": "Male",
                "status": "approved",
                "about_me": "Fintech executive who believes in high ambition, ethical living, and deep family commitments. Love tennis, world history, and carnatic flute.",
                "marital_status": "Never Married",
                "height": "6 ft 0 in (183 cm)",
                "weight": "78",
                "blood_group": "O+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Thevar",
                "gothram": "Shiva",
                "dob": date(1992, 5, 20),
                "tob": "03:15 AM",
                "birth_city": "Madurai",
                "address_1": "Tower 4, DIFC Gate Avenue",
                "city": "Dubai",
                "district": "DIFC",
                "state": "Dubai",
                "country": "UAE",
                "pincode": "00000",
                "qualification": "B.Tech + MBA (Finance)",
                "qualification_details": "IIT Madras & IIM Ahmedabad",
                "job": "Vice President - Capital Markets",
                "company": "Middle East Digital Financial Services",
                "working_place": "Dubai",
                "employment_type": "Private Sector",
                "annual_income": 12000000.0,
                "income_cat": "₹1Cr+",
                "father_name": "Murugesan Thangavel",
                "father_occ": "Transport & Logistics Business",
                "mother_name": "Vijaya Murugesan",
                "mother_occ": "Homemaker",
                "brothers": 1,
                "sisters": 1,
                "family_type": "Nuclear",
                "family_status": "Rich / Affluent",
                "family_values": "Moderate",
                "poorvigam": "Usilampatti",
                "rasi": "Dhanusu (Sagittarius)",
                "nakshatra": "Moolam",
                "lagnam": "Kadagam",
                "dosham": "No Dosham",
                "avatar": "/static/images/groom_4.svg"
            },
            {
                "email": "kavitha.balan@example.com",
                "mobile": "9847889012",
                "password": "Password123",
                "profile_id": "MAT-10008",
                "profile_type": "bride",
                "profile_created_for": "Self",
                "first_name": "Kavitha",
                "last_name": "Balachandran",
                "gender": "Female",
                "status": "approved",
                "about_me": "Corporate professional with a sunny disposition. Enjoys gardening, classical dance (Bharatanatyam), and cooking traditional Tamil recipes.",
                "marital_status": "Never Married",
                "height": "5 ft 4 in (163 cm)",
                "weight": "55",
                "blood_group": "A+",
                "mother_tongue": "Tamil",
                "religion": "Hindu",
                "community": "Naidu",
                "gothram": "Sri Krishna",
                "dob": date(1998, 4, 12),
                "tob": "09:40 AM",
                "birth_city": "Tirunelveli",
                "address_1": "34, High Ground",
                "city": "Tirunelveli",
                "district": "Tirunelveli",
                "state": "Tamil Nadu",
                "country": "India",
                "pincode": "627011",
                "qualification": "B.Com, ACS (Company Secretary)",
                "qualification_details": "Ethiraj College & ICSI",
                "job": "Assistant Manager - Compliance",
                "company": "Tata Consultancy Services (TCS)",
                "working_place": "Chennai",
                "employment_type": "Private Sector",
                "annual_income": 950000.0,
                "income_cat": "₹5L+",
                "father_name": "Balachandran Rangasamy",
                "father_occ": "Retired Indian Railways Officer",
                "mother_name": "Radha Balachandran",
                "mother_occ": "Homemaker",
                "brothers": 0,
                "sisters": 1,
                "family_type": "Nuclear",
                "family_status": "Middle Class",
                "family_values": "Traditional",
                "poorvigam": "Tirunelveli",
                "rasi": "Kumbam (Aquarius)",
                "nakshatra": "Sadhayam",
                "lagnam": "Rishabam",
                "dosham": "No Dosham",
                "avatar": "/static/images/bride_4.svg"
            }
        ]

        # Insert profiles into database
        for item in sample_profiles_data:
            user = User(
                email=item['email'],
                mobile=item['mobile'],
                role='user',
                is_active=True,
                is_verified=True,
                registration_status='completed'
            )
            user.set_password(item['password'])
            db.session.add(user)
            db.session.flush()

            profile = Profile(
                user_id=user.id,
                profile_id=item['profile_id'],
                profile_type=item['profile_type'],
                profile_created_for=item['profile_created_for'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                gender=item['gender'],
                status=item['status'],
                about_me=item['about_me']
            )
            db.session.add(profile)
            db.session.flush()

            # Personal
            p_det = PersonalDetail(
                profile_id=profile.id,
                marital_status=item['marital_status'],
                height=item['height'],
                weight=item['weight'],
                blood_group=item['blood_group'],
                mother_tongue=item['mother_tongue'],
                religion=item['religion'],
                community=item['community'],
                gothram=item['gothram']
            )
            db.session.add(p_det)

            # Birth
            b_det = BirthDetail(
                profile_id=profile.id,
                date_of_birth=item['dob'],
                time_of_birth=item['tob'],
                birth_city=item['birth_city'],
                birth_state='Tamil Nadu',
                birth_country='India'
            )
            db.session.add(b_det)

            # Address
            addr = Address(
                profile_id=profile.id,
                address_1=item['address_1'],
                city=item['city'],
                district=item['district'],
                state=item['state'],
                country=item['country'],
                pincode=item['pincode']
            )
            db.session.add(addr)

            # Education
            edu = EducationDetail(
                profile_id=profile.id,
                qualification=item['qualification'],
                qualification_details=item['qualification_details'],
                education_field='Professional'
            )
            db.session.add(edu)

            # Career
            car = CareerDetail(
                profile_id=profile.id,
                job=item['job'],
                company=item['company'],
                working_place=item['working_place'],
                employment_type=item['employment_type']
            )
            db.session.add(car)

            # Income
            cat_obj = IncomeCategory.query.filter_by(name=item['income_cat']).first()
            inc = IncomeDetail(
                profile_id=profile.id,
                annual_income=item['annual_income'],
                income_category=item['income_cat'],
                category_id=cat_obj.id if cat_obj else None,
                hide_exact_income=True
            )
            db.session.add(inc)

            # Family
            fam = FamilyDetail(
                profile_id=profile.id,
                father_name=item['father_name'],
                father_occupation=item['father_occ'],
                mother_name=item['mother_name'],
                mother_occupation=item['mother_occ'],
                brothers=item['brothers'],
                sisters=item['sisters'],
                family_type=item['family_type'],
                family_status=item['family_status'],
                family_values=item['family_values'],
                poorvigam=item['poorvigam']
            )
            db.session.add(fam)

            # Horoscope
            horo = HoroscopeDetail(
                profile_id=profile.id,
                rasi=item['rasi'],
                nakshatra=item['nakshatra'],
                lagnam=item['lagnam'],
                dosham=item['dosham'],
                chevvai_dosham=(item['dosham'] == 'Chevvai Dosham'),
                rahu_ketu_dosham=(item['dosham'] == 'Rahu-Ketu Dosham')
            )
            db.session.add(horo)

            # Lifestyle
            life = LifestyleDetail(
                profile_id=profile.id,
                diet='Vegetarian',
                smoking='No',
                drinking='No'
            )
            db.session.add(life)

            # Partner Preference
            pref = PartnerPreference(
                profile_id=profile.id,
                preferred_age_min=22 if item['gender'] == 'Male' else 26,
                preferred_age_max=28 if item['gender'] == 'Male' else 32,
                preferred_marital_status='Never Married',
                preferred_religion='Hindu',
                preferred_community=item['community'],
                dosham_expectation='Matches well'
            )
            db.session.add(pref)

            # Photo
            photo = ProfilePhoto(
                profile_id=profile.id,
                file_path=item['avatar'],
                is_primary=True
            )
            db.session.add(photo)

            # Privacy
            priv = PrivacySetting(
                profile_id=profile.id,
                hide_exact_income=True,
                hide_mobile=True,
                hide_email=True,
                hide_full_address=True,
                photo_visibility='all',
                horoscope_visibility='all'
            )
            db.session.add(priv)

            # Registration progress
            prog = RegistrationProgress(
                user_id=user.id,
                current_step=8,
                is_completed=True
            )
            db.session.add(prog)

        db.session.commit()
        print("Successfully seeded all sample profiles!")

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    seed_database(app)
