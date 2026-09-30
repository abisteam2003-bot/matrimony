# -*- coding: utf-8 -*-
"""
Bilingual Translation Dictionary for Matromani (Pure Unicode Tamil + English)
Provides full dictionary and helper for Jinja2 templates.
"""

TRANSLATIONS = {
    # Navigation
    'nav_brand': {
        'en': 'Matromani',
        'ta': 'மேட்ரோமணி'
    },
    'nav_tagline': {
        'en': 'Premium Matrimony',
        'ta': 'பிரீமியம் மேட்ரிமோனி'
    },
    'nav_home': {
        'en': 'Home',
        'ta': 'முகப்பு'
    },
    'nav_search': {
        'en': 'Search Profiles',
        'ta': 'சுயவிவரங்களைத் தேடுக'
    },
    'nav_income_categories': {
        'en': 'Income Categories',
        'ta': 'வருமான வகைகள்'
    },
    'nav_how_it_works': {
        'en': 'How It Works',
        'ta': 'எப்படி செயல்படுகிறது'
    },
    'nav_about': {
        'en': 'About Us',
        'ta': 'எங்களைப் பற்றி'
    },
    'nav_contact': {
        'en': 'Contact',
        'ta': 'தொடர்பு'
    },
    'nav_login': {
        'en': 'Login',
        'ta': 'உள்நுழைவு'
    },
    'nav_register': {
        'en': 'Register',
        'ta': 'பதிவு'
    },
    'nav_dashboard': {
        'en': 'Dashboard',
        'ta': 'டாஷ்போர்டு'
    },
    'nav_my_profile': {
        'en': 'My Profile',
        'ta': 'என் சுயவிவரம்'
    },
    'nav_logout': {
        'en': 'Logout',
        'ta': 'வெளியேறு'
    },
    'nav_admin': {
        'en': 'Admin Portal',
        'ta': 'நிர்வாக மையம்'
    },

    # Homepage Hero
    'hero_title': {
        'en': 'Find Your Perfect Life Partner',
        'ta': 'உங்கள் வாழ்க்கைக்கு ஏற்ற துணையைத் தேடுங்கள்'
    },
    'hero_subtitle': {
        'en': 'Discover genuine matrimonial profiles based on your preferences.',
        'ta': 'உங்கள் விருப்பங்களுக்கு ஏற்ப உண்மையான திருமண சுயவிவரங்களைத் தேடுங்கள்.'
    },
    'btn_find_match': {
        'en': 'Find Your Match',
        'ta': 'உங்கள் துணையைத் தேடுங்கள்'
    },
    'btn_register_free': {
        'en': 'Register Free',
        'ta': 'இலவசமாக பதிவு செய்யுங்கள்'
    },

    # Quick Search Form on Homepage
    'looking_for': {
        'en': 'Looking For',
        'ta': 'தேடும் வரன்'
    },
    'bride': {
        'en': 'Bride',
        'ta': 'மணமகள்'
    },
    'groom': {
        'en': 'Groom',
        'ta': 'மணமகன்'
    },
    'age': {
        'en': 'Age',
        'ta': 'வயது'
    },
    'from': {
        'en': 'From',
        'ta': 'முதல்'
    },
    'to': {
        'en': 'To',
        'ta': 'வரை'
    },
    'religion': {
        'en': 'Religion',
        'ta': 'மதம்'
    },
    'community': {
        'en': 'Community',
        'ta': 'சமூகம்'
    },
    'any_religion': {
        'en': 'Any Religion',
        'ta': 'அனைத்து மதம்'
    },
    'any_community': {
        'en': 'Any Community',
        'ta': 'அனைத்து சமூகம்'
    },
    'search_now': {
        'en': 'Search Now',
        'ta': 'இப்போதே தேடுங்கள்'
    },

    # Income Categories Section
    'income_category_title': {
        'en': 'Explore Profiles by Income',
        'ta': 'வருமான அடிப்படையில் சுயவிவரங்களைத் தேடுங்கள்'
    },
    'income_category_subtitle': {
        'en': 'Filter verified profiles categorized cleanly by annual earning capacity',
        'ta': 'ஆண்டு வருமான வரம்புகளின்படி வகைப்படுத்தப்பட்ட உண்மை வரன்களைப் பாருங்கள்'
    },
    'view_profiles': {
        'en': 'View Profiles',
        'ta': 'சுயவிவரங்களைப் பார்க்க'
    },

    # Trust & Features Section
    'feature_verified_title': {
        'en': '100% Verified Profiles',
        'ta': '100% சரிபார்க்கப்பட்ட சுயவிவரங்கள்'
    },
    'feature_verified_desc': {
        'en': 'Strict verification with government ID, contact, and horoscope checks.',
        'ta': 'அரசு அடையாள அட்டை, தொலைபேசி மற்றும் ஜாதக சரிபார்ப்பு செய்யப்படுகிறது.'
    },
    'feature_privacy_title': {
        'en': 'Strict Privacy Control',
        'ta': 'முழுமையான தனியுரிமை பாதுகாப்பு'
    },
    'feature_privacy_desc': {
        'en': 'Exact income, phone, and photos are displayed strictly per your privacy choices.',
        'ta': 'துல்லிய வருமானம் மற்றும் தொடர்புகள் உங்கள் அனுமதியுடன் மட்டுமே பகிரப்படும்.'
    },
    'feature_horoscope_title': {
        'en': 'Accurate Horoscope Matching',
        'ta': 'துல்லியமான ஜாதகப் பொருத்தம்'
    },
    'feature_horoscope_desc': {
        'en': 'Rasi, Nakshatra, and Dosham compatibility matching by Vedic astrology standards.',
        'ta': 'ராசி, நட்சத்திரம் மற்றும் தோஷங்களுக்கான வேத ஜோதிட வழிகாட்டல்.'
    },
    'feature_tamil_title': {
        'en': 'Tamil Community Network',
        'ta': 'உலகளாவிய தமிழ் சமுதாய இணைப்பு'
    },
    'feature_tamil_desc': {
        'en': 'Trusted by lakhs of Tamil families across India and worldwide.',
        'ta': 'இந்தியா மற்றும் வெளிநாடுகளில் உள்ள பல்லாயிரக்கணக்கான தமிழ் குடும்பங்களின் நம்பிக்கை.'
    },

    # How It Works
    'how_it_works_title': {
        'en': 'How Matromani Works',
        'ta': 'எப்படி செயல்படுகிறது'
    },
    'how_step_1_title': {
        'en': '1. Register Free',
        'ta': '1. இலவசமாக பதிவு செய்யவும்'
    },
    'how_step_1_desc': {
        'en': 'Create your detailed profile in 8 simple steps with autosave support.',
        'ta': 'சுயவிவரத்தை 8 எளிய படிகளில் பூர்த்தி செய்யுங்கள்.'
    },
    'how_step_2_title': {
        'en': '2. Set Preferences',
        'ta': '2. விருப்பங்களை அமைக்கவும்'
    },
    'how_step_2_desc': {
        'en': 'Specify education, career, income brackets, and horoscope parameters.',
        'ta': 'கல்வி, வேலை, வருமானம் மற்றும் ஜாதக விருப்பங்களை நிர்ணயிக்கவும்.'
    },
    'how_step_3_title': {
        'en': '3. Find Matches',
        'ta': '3. பொருத்தமான வரன்களை தேடவும்'
    },
    'how_step_3_desc': {
        'en': 'Explore verified profiles and shortlist those matching your criteria.',
        'ta': 'பொருத்தமான வரன்களைப் பார்த்து விருப்பப்பட்டியலில் சேர்க்கவும்.'
    },
    'how_step_4_title': {
        'en': '4. Connect Safely',
        'ta': '4. பாதுகாப்பாக தொடர்பு கொள்ளவும்'
    },
    'how_step_4_desc': {
        'en': 'Send interests, communicate securely, and take the sacred step forward.',
        'ta': 'விருப்பம் தெரிவித்து, பரஸ்பர சம்மதத்துடன் திருமணத்தை நோக்கி முன்னேறுங்கள்.'
    },

    # Registration Wizard Common
    'reg_wizard_title': {
        'en': 'Create Your Matrimonial Profile',
        'ta': 'உங்கள் திருமண சுயவிவரத்தை உருவாக்குங்கள்'
    },
    'reg_wizard_subtitle': {
        'en': 'Complete your 8-step registration. Your progress is automatically saved.',
        'ta': 'உங்கள் 8-படி பதிவை நிறைவு செய்யுங்கள். உங்கள் விவரங்கள் தானாகவே சேமிக்கப்படும்.'
    },
    'step_progress': {
        'en': 'Step {current} of {total}',
        'ta': 'படி {current} / {total}'
    },
    'autosave_badge': {
        'en': 'Autosaved',
        'ta': 'தானாக சேமிக்கப்பட்டது'
    },
    'resume_notice': {
        'en': 'You have an incomplete registration. We have resumed from where you left off!',
        'ta': 'உங்கள் முந்தைய பதிவு படிவத்திலிருந்து மீண்டும் தொடர்கிறீர்கள்!'
    },

    # Wizard Steps Titles
    'step_1_title': {
        'en': 'Basic Details',
        'ta': 'அடிப்படை விவரங்கள்'
    },
    'step_2_title': {
        'en': 'Personal & Birth Details',
        'ta': 'தனிப்பட்ட மற்றும் பிறப்பு விவரங்கள்'
    },
    'step_3_title': {
        'en': 'Address Details',
        'ta': 'முகவரி விவரங்கள்'
    },
    'step_4_title': {
        'en': 'Education, Career & Income',
        'ta': 'கல்வி, தொழில் மற்றும் வருமான விவரங்கள்'
    },
    'step_5_title': {
        'en': 'Family Details',
        'ta': 'குடும்ப விவரங்கள்'
    },
    'step_6_title': {
        'en': 'Horoscope Details',
        'ta': 'ஜாதக விவரங்கள்'
    },
    'step_7_title': {
        'en': 'Profile Photos',
        'ta': 'சுயவிவரப் புகைப்படங்கள்'
    },
    'step_8_title': {
        'en': 'Review Your Profile',
        'ta': 'உங்கள் சுயவிவரத்தை சரிபார்க்கவும்'
    },

    # Step 1 Fields
    'profile_type': {
        'en': 'Bride / Groom',
        'ta': 'மணமகள் / மணமகன்'
    },
    'profile_created_for': {
        'en': 'Profile Created For',
        'ta': 'யாருக்காக பதிவு செய்கிறீர்கள்?'
    },
    'created_for_self': {
        'en': 'Self',
        'ta': 'சுயம்'
    },
    'created_for_son': {
        'en': 'Son',
        'ta': 'மகன்'
    },
    'created_for_daughter': {
        'en': 'Daughter',
        'ta': 'மகள்'
    },
    'created_for_brother': {
        'en': 'Brother',
        'ta': 'சகோதரர்'
    },
    'created_for_sister': {
        'en': 'Sister',
        'ta': 'சகோதரி'
    },
    'created_for_relative': {
        'en': 'Relative',
        'ta': 'உறவினர்'
    },
    'created_for_friend': {
        'en': 'Friend',
        'ta': 'நண்பர்'
    },
    'first_name': {
        'en': 'First Name',
        'ta': 'முதல் பெயர்'
    },
    'last_name': {
        'en': 'Last Name',
        'ta': 'கடைசி பெயர்'
    },
    'marital_status': {
        'en': 'Marital Status',
        'ta': 'திருமண நிலை'
    },
    'never_married': {
        'en': 'Never Married',
        'ta': 'திருமணம் ஆகாதவர்'
    },
    'divorced': {
        'en': 'Divorced',
        'ta': 'விவாகரத்து ஆனவர்'
    },
    'widowed': {
        'en': 'Widowed',
        'ta': 'துணையை இழந்தவர்'
    },
    'separated': {
        'en': 'Separated',
        'ta': 'பிரிந்து வாழ்பவர்'
    },
    'email': {
        'en': 'Email ID',
        'ta': 'மின்னஞ்சல் முகவரி'
    },
    'mobile': {
        'en': 'Mobile Number',
        'ta': 'மொபைல் எண்'
    },
    'password': {
        'en': 'Password',
        'ta': 'கடவுச்சொல்'
    },
    'confirm_password': {
        'en': 'Confirm Password',
        'ta': 'கடவுச்சொல்லை உறுதிப்படுத்தவும்'
    },

    # Step 2 Fields
    'date_of_birth': {
        'en': 'Date of Birth',
        'ta': 'பிறந்த தேதி'
    },
    'time_of_birth': {
        'en': 'Time of Birth',
        'ta': 'பிறந்த நேரம்'
    },
    'birth_city': {
        'en': 'Place of Birth',
        'ta': 'பிறந்த இடம்'
    },
    'height': {
        'en': 'Height',
        'ta': 'உயரம்'
    },
    'weight': {
        'en': 'Weight (kg)',
        'ta': 'எடை (கிலோ)'
    },
    'blood_group': {
        'en': 'Blood Group',
        'ta': 'இரத்த வகை'
    },
    'mother_tongue': {
        'en': 'Mother Tongue',
        'ta': 'தாய்மொழி'
    },
    'community_caste': {
        'en': 'Community / Caste',
        'ta': 'சமூகம் / பிரிவு'
    },
    'gothram': {
        'en': 'Gothram',
        'ta': 'கோத்திரம்'
    },

    # Step 3 Fields
    'address_1': {
        'en': 'Address Line 1',
        'ta': 'முகவரி 1'
    },
    'address_2': {
        'en': 'Address Line 2 (Optional)',
        'ta': 'முகவரி 2 (விருப்பத்திற்குரியது)'
    },
    'pincode': {
        'en': 'Pincode',
        'ta': 'அஞ்சல் குறியீடு'
    },
    'city': {
        'en': 'City',
        'ta': 'நகரம்'
    },
    'district': {
        'en': 'District',
        'ta': 'மாவட்டம்'
    },
    'state': {
        'en': 'State',
        'ta': 'மாநிலம்'
    },
    'country': {
        'en': 'Country',
        'ta': 'நாடு'
    },

    # Step 4 Fields
    'qualification': {
        'en': 'Highest Qualification',
        'ta': 'உயர்ந்த கல்வித் தகுதி'
    },
    'qualification_details': {
        'en': 'Qualification Details / College',
        'ta': 'கல்வி விவரங்கள் / கல்லூரி'
    },
    'job': {
        'en': 'Occupation',
        'ta': 'தொழில்'
    },
    'company': {
        'en': 'Company / Organization',
        'ta': 'நிறுவனம் / அமைப்பு'
    },
    'working_place': {
        'en': 'Working Place / City',
        'ta': 'பணிபுரியும் இடம்'
    },
    'employment_type': {
        'en': 'Employment Type',
        'ta': 'வேலை வகை'
    },
    'income': {
        'en': 'Annual Income (₹)',
        'ta': 'ஆண்டு வருமானம் (₹)'
    },
    'income_category_detected': {
        'en': 'Calculated Income Category',
        'ta': 'கணக்கிடப்பட்ட வருமான வகை'
    },
    'hide_income_privacy_label': {
        'en': 'Keep exact income hidden (only show category badge publicly)',
        'ta': 'துல்லிய வருமானத்தை மறைக்கவும் (வருமான வகையை மட்டும் பொதுவில் காட்டுக)'
    },

    # Step 5 Fields
    'father_name': {
        'en': 'Father Name',
        'ta': 'தந்தையின் பெயர்'
    },
    'father_occupation': {
        'en': 'Father Occupation',
        'ta': 'தந்தையின் தொழில்'
    },
    'mother_name': {
        'en': 'Mother Name',
        'ta': 'தாயின் பெயர்'
    },
    'mother_occupation': {
        'en': 'Mother Occupation',
        'ta': 'தாயின் தொழில்'
    },
    'brothers': {
        'en': 'Number of Brothers',
        'ta': 'சகோதரர்கள் எண்ணிக்கை'
    },
    'sisters': {
        'en': 'Number of Sisters',
        'ta': 'சகோதரிகள் எண்ணிக்கை'
    },
    'family_type': {
        'en': 'Family Type',
        'ta': 'குடும்ப வகை'
    },
    'nuclear_family': {
        'en': 'Nuclear Family',
        'ta': 'தனிக்குடும்பம்'
    },
    'joint_family': {
        'en': 'Joint Family',
        'ta': 'கூட்டுக் குடும்பம்'
    },
    'family_status': {
        'en': 'Family Status',
        'ta': 'குடும்ப நிலை'
    },
    'middle_class': {
        'en': 'Middle Class',
        'ta': 'நடுத்தர குடும்பம்'
    },
    'upper_middle_class': {
        'en': 'Upper Middle Class',
        'ta': 'உயர் நடுத்தர குடும்பம்'
    },
    'rich_affluent': {
        'en': 'Rich / Affluent',
        'ta': 'பணக்கார / வசதியான குடும்பம்'
    },
    'family_values': {
        'en': 'Family Values',
        'ta': 'குடும்ப மதிப்புகள்'
    },
    'traditional': {
        'en': 'Traditional',
        'ta': 'பாரம்பரியமான'
    },
    'moderate': {
        'en': 'Moderate',
        'ta': 'நடுத்தரமான'
    },
    'liberal': {
        'en': 'Liberal',
        'ta': 'நவீனமான'
    },
    'poorvigam': {
        'en': 'Poorvigam / Ancestral Information',
        'ta': 'பூர்வீக விவரங்கள்'
    },

    # Step 6 Fields
    'rasi': {
        'en': 'Rasi',
        'ta': 'ராசி'
    },
    'nakshatra': {
        'en': 'Nakshatra',
        'ta': 'நட்சத்திரம்'
    },
    'lagnam': {
        'en': 'Lagnam',
        'ta': 'லக்னம்'
    },
    'dosham': {
        'en': 'Dosham',
        'ta': 'தோஷம்'
    },
    'no_dosham': {
        'en': 'No Dosham',
        'ta': 'தோஷம் இல்லை'
    },
    'chevvai_dosham': {
        'en': 'Chevvai (Mars) Dosham',
        'ta': 'செவ்வாய் தோஷம்'
    },
    'rahu_ketu_dosham': {
        'en': 'Rahu / Ketu Dosham',
        'ta': 'ராகு / கேது தோஷம்'
    },
    'dont_know_dosham': {
        'en': 'Don\'t Know',
        'ta': 'தெரியாது'
    },
    'jathagam_photo': {
        'en': 'Jathagam Photo',
        'ta': 'ஜாதகப் படம்'
    },
    'jathagam_photo_hint': {
        'en': 'Upload your horoscope chart image (JPG, PNG - Max 5MB)',
        'ta': 'உங்கள் ஜாதக கட்டத்தின் படத்தை பதிவேற்றவும் (JPG, PNG - அதிகபட்சம் 5MB)'
    },

    # Step 7 Fields
    'profile_photo': {
        'en': 'Profile Photo',
        'ta': 'சுயவிவரப் புகைப்படம்'
    },
    'profile_photo_required': {
        'en': 'Main profile photo is required to build trust.',
        'ta': 'முதன்மை சுயவிவரப் புகைப்படம் அவசியமானது.'
    },
    'additional_photos': {
        'en': 'Additional Photos (Up to 4 more)',
        'ta': 'கூடுதல் புகைப்படங்கள் (மேலும் 4 வரை)'
    },
    'photo_guidelines': {
        'en': 'Upload clear, recent color photos. Formats: JPG, PNG. Max: 5MB each.',
        'ta': 'தெளிவான, சமீபத்திய புகைப்படங்களை பதிவேற்றவும். அதிகபட்சம் 5MB.'
    },

    # Step 8 Review
    'review_title': {
        'en': 'Review Your Profile',
        'ta': 'உங்கள் சுயவிவரத்தை சரிபார்க்கவும்'
    },
    'review_subtitle': {
        'en': 'Please review all entered information before submitting.',
        'ta': 'சமர்ப்பிப்பதற்கு முன் உங்கள் விவரங்களை சரிபார்க்கவும்.'
    },
    'btn_edit': {
        'en': 'Edit',
        'ta': 'திருத்து'
    },
    'btn_submit_profile': {
        'en': 'Submit Profile',
        'ta': 'சுயவிவரத்தை சமர்ப்பிக்கவும்'
    },

    # Common Buttons
    'btn_next': {
        'en': 'Next',
        'ta': 'அடுத்து'
    },
    'btn_previous': {
        'en': 'Previous',
        'ta': 'முந்தையது'
    },
    'btn_save': {
        'en': 'Save',
        'ta': 'சேமிக்க'
    },
    'btn_continue': {
        'en': 'Continue',
        'ta': 'தொடரவும்'
    },
    'btn_cancel': {
        'en': 'Cancel',
        'ta': 'ரத்து'
    },
    'btn_search': {
        'en': 'Search',
        'ta': 'தேடுக'
    },
    'btn_reset': {
        'en': 'Reset',
        'ta': 'மீட்டமை'
    },

    # Profile Card
    'card_view_profile': {
        'en': 'View Profile',
        'ta': 'சுயவிவரத்தைப் பார்க்க'
    },
    'card_shortlist': {
        'en': 'Shortlist',
        'ta': 'விருப்பப்பட்டியலில் சேர்க்க'
    },
    'card_shortlisted': {
        'en': 'Shortlisted',
        'ta': 'சேர்க்கப்பட்டது'
    },
    'card_send_interest': {
        'en': 'Send Interest',
        'ta': 'விருப்பம் தெரிவிக்க'
    },
    'card_interest_sent': {
        'en': 'Interest Sent',
        'ta': 'விருப்பம் அனுப்பப்பட்டது'
    },
    'profile_id_label': {
        'en': 'ID',
        'ta': 'எண்'
    },
    'verified_badge': {
        'en': 'Verified',
        'ta': 'சரிபார்க்கப்பட்டது'
    },

    # Search Page
    'search_page_title': {
        'en': 'Search Matrimonial Profiles',
        'ta': 'திருமண சுயவிவரங்களைத் தேடுங்கள்'
    },
    'search_page_subtitle': {
        'en': 'Refine your search with multiple criteria including caste, income, location and horoscope.',
        'ta': 'சமூகம், வருமானம், இருப்பிடம் மற்றும் ஜாதகம் வாரியாக துல்லியமாக தேடுங்கள்.'
    },
    'filter_bride_groom': {
        'en': 'Bride / Groom',
        'ta': 'மணமகள் / மணமகன்'
    },
    'filter_age': {
        'en': 'Age',
        'ta': 'வயது'
    },
    'filter_height': {
        'en': 'Height',
        'ta': 'உயரம்'
    },
    'filter_marital_status': {
        'en': 'Marital Status',
        'ta': 'திருமண நிலை'
    },
    'filter_religion': {
        'en': 'Religion',
        'ta': 'மதம்'
    },
    'filter_community': {
        'en': 'Community',
        'ta': 'சமூகம்'
    },
    'filter_education': {
        'en': 'Education',
        'ta': 'கல்வி'
    },
    'filter_occupation': {
        'en': 'Occupation',
        'ta': 'தொழில்'
    },
    'filter_income_category': {
        'en': 'Income Category',
        'ta': 'வருமான வகை'
    },
    'filter_country': {
        'en': 'Country',
        'ta': 'நாடு'
    },
    'filter_state': {
        'en': 'State',
        'ta': 'மாநிலம்'
    },
    'filter_district': {
        'en': 'District',
        'ta': 'மாவட்டம்'
    },
    'filter_city': {
        'en': 'City',
        'ta': 'நகரம்'
    },
    'filter_dosham': {
        'en': 'Dosham',
        'ta': 'தோஷம்'
    },
    'profiles_found': {
        'en': 'Profiles Found',
        'ta': 'சுயவிவரங்கள் உள்ளன'
    },
    'no_profiles_found': {
        'en': 'No matching profiles found. Try broadening your filter criteria.',
        'ta': 'பொருத்தமான வரன்கள் இல்லை. உங்கள் தேடல் விருப்பங்களை மாற்றி முயற்சிக்கவும்.'
    },

    # Dashboard Tabs
    'dash_overview': {
        'en': 'Dashboard',
        'ta': 'டாஷ்போர்டு'
    },
    'dash_my_profile': {
        'en': 'My Profile',
        'ta': 'என் சுயவிவரம்'
    },
    'dash_search_matches': {
        'en': 'Search Matches',
        'ta': 'துணையைத் தேடுக'
    },
    'dash_shortlist': {
        'en': 'Shortlist',
        'ta': 'விருப்பப்பட்டியல்'
    },
    'dash_interest_sent': {
        'en': 'Interest Sent',
        'ta': 'அனுப்பிய விருப்பங்கள்'
    },
    'dash_interest_received': {
        'en': 'Interest Received',
        'ta': 'பெற்ற விருப்பங்கள்'
    },
    'dash_profile_views': {
        'en': 'Profile Views',
        'ta': 'சுயவிவர பார்வைகள்'
    },
    'dash_privacy_settings': {
        'en': 'Privacy Settings',
        'ta': 'தனியுரிமை அமைப்புகள்'
    },
    'dash_language': {
        'en': 'Language',
        'ta': 'மொழி'
    },
    'dash_logout': {
        'en': 'Logout',
        'ta': 'வெளியேறு'
    },

    # Privacy Settings
    'privacy_income_title': {
        'en': 'Annual Income Privacy',
        'ta': 'வருமான தனியுரிமை'
    },
    'privacy_income_desc': {
        'en': 'Only display your bracket (e.g. ₹15L+) to public; keep exact figure hidden.',
        'ta': 'துல்லியமான தொகையை மறைத்து வருமான வகையை மட்டும் காட்டவும்.'
    },
    'privacy_contact_title': {
        'en': 'Contact Information Privacy',
        'ta': 'தொடர்பு விவர தனியுரிமை'
    },
    'privacy_contact_desc': {
        'en': 'Mobile number and email are revealed only when you accept an interest.',
        'ta': 'உங்கள் மொபைல் மற்றும் மின்னஞ்சல் சம்மதம் தெரிவித்த பிறகே பகிரப்படும்.'
    },
    'privacy_photo_title': {
        'en': 'Photo Visibility',
        'ta': 'புகைப்பட தெரிவுநிலை'
    },
    'privacy_photo_all': {
        'en': 'Visible to all visitors',
        'ta': 'அனைவருக்கும் காண்பிக்கலாம்'
    },
    'privacy_photo_members': {
        'en': 'Visible to logged in members only',
        'ta': 'உள்நுழைந்த உறுப்பினர்களுக்கு மட்டும்'
    },
    'privacy_photo_request': {
        'en': 'Visible on request only',
        'ta': 'கோரிக்கை விடுத்தால் மட்டும்'
    },

    # Notifications & Toasts
    'interest_sent_success': {
        'en': 'Interest expressed successfully!',
        'ta': 'உங்கள் விருப்பம் வெற்றிகரமாக தெரிவிக்கப்பட்டது!'
    },
    'shortlist_added_success': {
        'en': 'Profile added to your shortlist!',
        'ta': 'சுயவிவரம் உங்கள் விருப்பப்பட்டியலில் சேர்க்கப்பட்டது!'
    },
    'shortlist_removed_success': {
        'en': 'Profile removed from your shortlist.',
        'ta': 'சுயவிவரம் விருப்பப்பட்டியலில் இருந்து நீக்கப்பட்டது.'
    },
    'login_success': {
        'en': 'Welcome back!',
        'ta': 'நல்வரவு! வெற்றிகரமாக உள்நுழைந்துள்ளீர்கள்.'
    },
    'logout_success': {
        'en': 'You have been logged out safely.',
        'ta': 'வெற்றிகரமாக வெளியேறிவிட்டீர்கள்.'
    },
    'profile_submitted_success': {
        'en': 'Your matrimonial profile has been submitted successfully for verification!',
        'ta': 'உங்கள் சுயவிவரம் சரிபார்ப்பிற்காக வெற்றிகரமாக சமர்ப்பிக்கப்பட்டது!'
    },

    # Auth Pages
    'login_title': {
        'en': 'Member Login',
        'ta': 'உறுப்பினர் உள்நுழைவு'
    },
    'login_subtitle': {
        'en': 'Enter your registered email and password to access your dashboard.',
        'ta': 'உங்கள் கணக்கைத் திறக்க மின்னஞ்சல் மற்றும் கடவுச்சொல்லை உள்ளிடவும்.'
    },
    'no_account_text': {
        'en': 'Don\'t have an account yet?',
        'ta': 'இன்னும் கணக்கு தொடங்கவில்லையா?'
    },
    'register_now': {
        'en': 'Register Now for Free',
        'ta': 'இலவசமாக பதிவு செய்யுங்கள்'
    },
    'forgot_password': {
        'en': 'Forgot Password?',
        'ta': 'கடவுச்சொல் மறந்துவிட்டதா?'
    },

    # Admin Portal
    'admin_title': {
        'en': 'Matromani Admin Portal',
        'ta': 'மேட்ரோமணி நிர்வாக போர்டல்'
    },
    'admin_stats_total_users': {
        'en': 'Total Users',
        'ta': 'மொத்த பயனர்கள்'
    },
    'admin_stats_pending_approval': {
        'en': 'Pending Approvals',
        'ta': 'நிலுவையில் உள்ளவை'
    },
    'admin_stats_approved': {
        'en': 'Approved Profiles',
        'ta': 'ஒப்புதல் பெற்றவை'
    },
    'admin_action_approve': {
        'en': 'Approve',
        'ta': 'ஒப்புதல் அளி'
    },
    'admin_action_reject': {
        'en': 'Reject',
        'ta': 'நிராகரி'
    },
    'admin_profile_status': {
        'en': 'Status',
        'ta': 'நிலை'
    },

    # Footer
    'footer_about_text': {
        'en': 'Matromani is Tamil Nadu\'s trusted premium matrimonial platform connecting compatible souls with dignity, culture, and high standards of privacy.',
        'ta': 'மேட்ரோமணி என்பது தமிழ் கலாச்சார பாரம்பரியம் மற்றும் தனியுரிமை பாதுகாப்புடன் சிறந்த வாழ்க்கை துணையை கண்டறிய உதவும் முன்னணி தளமாகும்.'
    },
    'footer_quick_links': {
        'en': 'Quick Links',
        'ta': 'விரைவு இணைப்புகள்'
    },
    'footer_legal': {
        'en': 'Privacy Policy & Terms',
        'ta': 'தனியுரிமை கொள்கை & விதிமுறைகள்'
    },
    'footer_copyright': {
        'en': 'All rights reserved. Designed with pride for the Tamil community.',
        'ta': 'அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை. தமிழ் சமுதாயத்திற்காக பெருமையுடன் வடிவமைக்கப்பட்டது.'
    },
    'language_display_desktop': {
        'en': 'தமிழ் | English',
        'ta': 'தமிழ் | English'
    },
    'language_display_mobile': {
        'en': 'தமிழ் / English',
        'ta': 'தமிழ் / English'
    }
}

# Rasi and Nakshatra lists in Tamil & English
RASI_LIST = [
    {'en': 'Mesham (Aries)', 'ta': 'மேஷம்'},
    {'en': 'Rishabam (Taurus)', 'ta': 'ரிஷபம்'},
    {'en': 'Mithunam (Gemini)', 'ta': 'மிதுனம்'},
    {'en': 'Kadagam (Cancer)', 'ta': 'கடகம்'},
    {'en': 'Simmam (Leo)', 'ta': 'சிம்மம்'},
    {'en': 'Kanni (Virgo)', 'ta': 'கன்னி'},
    {'en': 'Thulaam (Libra)', 'ta': 'துலாம்'},
    {'en': 'Viruchigam (Scorpio)', 'ta': 'விருச்சிகம்'},
    {'en': 'Dhanusu (Sagittarius)', 'ta': 'தனுசு'},
    {'en': 'Makaram (Capricorn)', 'ta': 'மகரம்'},
    {'en': 'Kumbam (Aquarius)', 'ta': 'கும்பம்'},
    {'en': 'Meenam (Pisces)', 'ta': 'மீனம்'}
]

NAKSHATRA_LIST = [
    {'en': 'Ashwini', 'ta': 'அசுவினி'},
    {'en': 'Bharani', 'ta': 'பரணி'},
    {'en': 'Karthigai', 'ta': 'கார்த்திகை'},
    {'en': 'Rohini', 'ta': 'ரோகிணி'},
    {'en': 'Mrigashirsham', 'ta': 'மிருகசீரிஷம்'},
    {'en': 'Thiruvathirai', 'ta': 'திருவாதிரை'},
    {'en': 'Punarpoosam', 'ta': 'புனர்பூசம்'},
    {'en': 'Poosam', 'ta': 'பூசம்'},
    {'en': 'Aayilyam', 'ta': 'ஆயில்யம்'},
    {'en': 'Makam', 'ta': 'மகம்'},
    {'en': 'Pooram', 'ta': 'பூரம்'},
    {'en': 'Uthiram', 'ta': 'உத்திரம்'},
    {'en': 'Hastham', 'ta': 'அஸ்தம்'},
    {'en': 'Chithirai', 'ta': 'சித்திரை'},
    {'en': 'Swathi', 'ta': 'சுவாதி'},
    {'en': 'Visakam', 'ta': 'விசாகம்'},
    {'en': 'Anusham', 'ta': 'அனுஷம்'},
    {'en': 'Kettai', 'ta': 'கேட்டை'},
    {'en': 'Moolam', 'ta': 'மூலம்'},
    {'en': 'Pooradam', 'ta': 'பூராடம்'},
    {'en': 'Uthiradam', 'ta': 'உத்திராடம்'},
    {'en': 'Thiruvonam', 'ta': 'திருவோணம்'},
    {'en': 'Avittam', 'ta': 'அவிட்டம்'},
    {'en': 'Sadhayam', 'ta': 'சதயம்'},
    {'en': 'Poorattathi', 'ta': 'பூரட்டாதி'},
    {'en': 'Uthirattathi', 'ta': 'உத்திரட்டாதி'},
    {'en': 'Revathi', 'ta': 'ரேவதி'}
]

# Standard Income Categories
INCOME_CATEGORIES_DATA = [
    {'name': '₹1L+', 'name_tamil': '₹1 லட்சம்+', 'min': 100000, 'max': 300000, 'order': 1},
    {'name': '₹3L+', 'name_tamil': '₹3 லட்சம்+', 'min': 300000, 'max': 500000, 'order': 2},
    {'name': '₹5L+', 'name_tamil': '₹5 லட்சம்+', 'min': 500000, 'max': 1000000, 'order': 3},
    {'name': '₹10L+', 'name_tamil': '₹10 லட்சம்+', 'min': 1000000, 'max': 1500000, 'order': 4},
    {'name': '₹15L+', 'name_tamil': '₹15 லட்சம்+', 'min': 1500000, 'max': 2500000, 'order': 5},
    {'name': '₹25L+', 'name_tamil': '₹25 லட்சம்+', 'min': 2500000, 'max': 5000000, 'order': 6},
    {'name': '₹50L+', 'name_tamil': '₹50 லட்சம்+', 'min': 5000000, 'max': 10000000, 'order': 7},
    {'name': '₹1Cr+', 'name_tamil': '₹1 கோடி+', 'min': 10000000, 'max': 999999999, 'order': 8}
]

def calculate_income_category(amount):
    """Determine income category based on numeric annual income amount."""
    try:
        amt = float(amount)
    except (ValueError, TypeError):
        return '₹3L+', '₹3 லட்சம்+'
    
    if amt >= 10000000:
        return '₹1Cr+', '₹1 கோடி+'
    elif amt >= 5000000:
        return '₹50L+', '₹50 லட்சம்+'
    elif amt >= 2500000:
        return '₹25L+', '₹25 லட்சம்+'
    elif amt >= 1500000:
        return '₹15L+', '₹15 லட்சம்+'
    elif amt >= 1000000:
        return '₹10L+', '₹10 லட்சம்+'
    elif amt >= 500000:
        return '₹5L+', '₹5 லட்சம்+'
    elif amt >= 300000:
        return '₹3L+', '₹3 லட்சம்+'
    else:
        return '₹1L+', '₹1 லட்சம்+'


def translate(key, lang='ta', **kwargs):
    """Lookup translation key. Defaults to Tamil ('ta') as per user specifications."""
    if lang not in ('ta', 'en'):
        lang = 'ta'
    
    entry = TRANSLATIONS.get(key)
    if entry and lang in entry:
        val = entry[lang]
        if kwargs:
            try:
                return val.format(**kwargs)
            except Exception:
                return val
        return val
    # If key missing in dict, return key itself gracefully
    return key
