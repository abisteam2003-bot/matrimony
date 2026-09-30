import os
from flask import Flask, render_template, request, session, redirect, url_for
from config import Config
from models import db, Profile, IncomeCategory, IncomeDetail, User
from seed_data import seed_database
from translations import translate, INCOME_CATEGORIES_DATA, RASI_LIST

# Import blueprints
from routes.auth_routes import auth_bp
from routes.register_routes import register_bp
from routes.search_routes import search_bp
from routes.profile_routes import profile_bp
from routes.dashboard_routes import dashboard_bp
from routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Language Middleware & Context Processor
    @app.before_request
    def handle_language():
        # Allow switching via query parameter ?lang=ta or ?lang=en
        req_lang = request.args.get('lang')
        if req_lang in ('ta', 'en'):
            session['lang'] = req_lang
        elif 'lang' not in session:
            # Default to Tamil as required
            session['lang'] = 'ta'

    @app.context_processor
    def inject_translation_helper():
        current_lang = session.get('lang', 'ta')
        def t(key, **kwargs):
            return translate(key, current_lang, **kwargs)
        return dict(
            t=t,
            current_lang=current_lang,
            income_categories_global=INCOME_CATEGORIES_DATA
        )

    # Language Switcher Route
    @app.route('/set-language/<lang_code>')
    def set_language(lang_code):
        if lang_code in ('ta', 'en'):
            session['lang'] = lang_code
        # Redirect back to referring page or homepage
        next_page = request.referrer or url_for('index')
        return redirect(next_page)

    # Homepage Route
    @app.route('/')
    def index():
        featured_profiles = Profile.query.filter_by(status='approved')\
                                         .order_by(Profile.created_at.desc())\
                                         .limit(8).all()
        
        # Calculate profile counts for income categories
        cat_stats = []
        for cat in INCOME_CATEGORIES_DATA:
            count = Profile.query.join(IncomeDetail, Profile.id == IncomeDetail.profile_id)\
                                 .filter(IncomeDetail.income_category == cat['name'])\
                                 .filter(Profile.status.in_(['approved', 'active']))\
                                 .count()
            cat_stats.append({
                'name': cat['name'],
                'name_tamil': cat['name_tamil'],
                'count': count
            })

        return render_template(
            'index.html',
            featured_profiles=featured_profiles,
            income_categories=cat_stats,
            rasi_list=RASI_LIST
        )

    # Static Informational Pages
    @app.route('/how-it-works')
    def how_it_works():
        return render_template('how_it_works.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            # Handle contact form submission
            lang = session.get('lang', 'ta')
            msg = 'உங்கள் செய்தி பெறப்பட்டது! விரைவில் தொடர்பு கொள்வோம்.' if lang == 'ta' else 'Thank you! Your message has been received.'
            return render_template('contact.html', success_message=msg)
        return render_template('contact.html')

    # Seed initial data
    seed_database(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
