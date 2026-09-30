from flask import Blueprint, render_template, request, session, jsonify
from models import (
    db, Profile, PersonalDetail, BirthDetail, Address,
    EducationDetail, CareerDetail, IncomeDetail, IncomeCategory,
    HoroscopeDetail, Shortlist, Interest
)
from translations import INCOME_CATEGORIES_DATA, RASI_LIST

search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    lang = session.get('lang', 'ta')
    user_id = session.get('user_id')

    # Query params
    profile_type = request.args.get('profile_type', '').strip().lower()
    age_from = request.args.get('age_from', type=int)
    age_to = request.args.get('age_to', type=int)
    marital_status = request.args.get('marital_status', '').strip()
    religion = request.args.get('religion', '').strip()
    community = request.args.get('community', '').strip()
    education = request.args.get('education', '').strip()
    occupation = request.args.get('occupation', '').strip()
    income_category = request.args.get('income_category', '').strip()
    city = request.args.get('city', '').strip()
    district = request.args.get('district', '').strip()
    state = request.args.get('state', '').strip()
    country = request.args.get('country', '').strip()
    dosham = request.args.get('dosham', '').strip()

    query = Profile.query.filter(Profile.status.in_(['approved', 'active']))

    # Filter by Bride / Groom
    if profile_type:
        query = query.filter(Profile.profile_type == profile_type)

    # Filter by Personal details
    if marital_status or religion or community:
        query = query.join(PersonalDetail, Profile.id == PersonalDetail.profile_id)
        if marital_status:
            query = query.filter(PersonalDetail.marital_status.ilike(f"%{marital_status}%"))
        if religion:
            query = query.filter(PersonalDetail.religion.ilike(f"%{religion}%"))
        if community:
            query = query.filter(PersonalDetail.community.ilike(f"%{community}%"))

    # Filter by Location / Address
    if city or district or state or country:
        query = query.join(Address, Profile.id == Address.profile_id)
        if city:
            query = query.filter(Address.city.ilike(f"%{city}%"))
        if district:
            query = query.filter(Address.district.ilike(f"%{district}%"))
        if state:
            query = query.filter(Address.state.ilike(f"%{state}%"))
        if country:
            query = query.filter(Address.country.ilike(f"%{country}%"))

    # Filter by Education
    if education:
        query = query.join(EducationDetail, Profile.id == EducationDetail.profile_id)
        query = query.filter(EducationDetail.qualification.ilike(f"%{education}%"))

    # Filter by Career
    if occupation:
        query = query.join(CareerDetail, Profile.id == CareerDetail.profile_id)
        query = query.filter(CareerDetail.job.ilike(f"%{occupation}%"))

    # Filter by Income Category
    if income_category:
        query = query.join(IncomeDetail, Profile.id == IncomeDetail.profile_id)
        query = query.filter(IncomeDetail.income_category == income_category)

    # Filter by Horoscope / Dosham
    if dosham:
        query = query.join(HoroscopeDetail, Profile.id == HoroscopeDetail.profile_id)
        if dosham == 'No Dosham':
            query = query.filter(HoroscopeDetail.dosham == 'No Dosham')
        elif dosham == 'Chevvai Dosham':
            query = query.filter(HoroscopeDetail.dosham.ilike('%Chevvai%'))
        elif dosham == 'Rahu-Ketu Dosham':
            query = query.filter(HoroscopeDetail.dosham.ilike('%Rahu%'))

    profiles = query.order_by(Profile.created_at.desc()).all()

    # Filter in-memory for age if provided (since age is calculated from date_of_birth)
    if age_from or age_to:
        filtered = []
        for p in profiles:
            p_age = p.age
            if age_from and p_age < age_from:
                continue
            if age_to and p_age > age_to:
                continue
            filtered.append(p)
        profiles = filtered

    # User's shortlist & sent interests map for button active states
    shortlisted_ids = set()
    interest_sent_ids = set()
    if user_id:
        sl = Shortlist.query.filter_by(user_id=user_id).all()
        shortlisted_ids = {s.profile_id for s in sl}
        sent = Interest.query.filter_by(sender_id=user_id).all()
        # Map receiver user id to their profile id
        for it in sent:
            if it.receiver and it.receiver.profile:
                interest_sent_ids.add(it.receiver.profile.id)

    # Distinct communities, religions, cities for filter dropdowns
    all_religions = [r[0] for r in db.session.query(PersonalDetail.religion).distinct().all() if r[0]]
    all_communities = [c[0] for c in db.session.query(PersonalDetail.community).distinct().all() if c[0]]
    all_cities = [ct[0] for ct in db.session.query(Address.city).distinct().all() if ct[0]]

    return render_template(
        'search.html',
        profiles=profiles,
        total_count=len(profiles),
        income_categories=INCOME_CATEGORIES_DATA,
        shortlisted_ids=shortlisted_ids,
        interest_sent_ids=interest_sent_ids,
        religions=all_religions,
        communities=all_communities,
        cities=all_cities,
        current_filters=request.args
    )

@search_bp.route('/income-categories')
def income_categories_page():
    categories_with_counts = []
    for cat in INCOME_CATEGORIES_DATA:
        count = Profile.query.join(IncomeDetail, Profile.id == IncomeDetail.profile_id)\
                             .filter(IncomeDetail.income_category == cat['name'])\
                             .filter(Profile.status.in_(['approved', 'active']))\
                             .count()
        categories_with_counts.append({
            'name': cat['name'],
            'name_tamil': cat['name_tamil'],
            'min': cat['min'],
            'max': cat['max'],
            'count': count
        })

    return render_template(
        'income_categories.html',
        categories=categories_with_counts
    )
