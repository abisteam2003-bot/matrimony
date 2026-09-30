import unittest
import json
from app import create_app
from models import db, User, Profile, IncomeCategory, IncomeDetail
from translations import calculate_income_category, translate

class MatromaniTestSuite(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_homepage_and_translations(self):
        # Default language should be Tamil ('ta')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('உங்கள் வாழ்க்கைக்கு ஏற்ற துணையைத் தேடுங்கள்'.encode('utf-8'), response.data)

        # English switch
        response_en = self.client.get('/?lang=en')
        self.assertEqual(response_en.status_code, 200)
        self.assertIn(b'Find Your Perfect Life Partner', response_en.data)

    def test_income_calculator_engine(self):
        cat1, _ = calculate_income_category(150000)
        self.assertEqual(cat1, '₹1L+')

        cat2, _ = calculate_income_category(400000)
        self.assertEqual(cat2, '₹3L+')

        cat3, _ = calculate_income_category(800000)
        self.assertEqual(cat3, '₹5L+')

        cat4, _ = calculate_income_category(1200000)
        self.assertEqual(cat4, '₹10L+')

        cat5, _ = calculate_income_category(2000000)
        self.assertEqual(cat5, '₹15L+')

        cat6, _ = calculate_income_category(3500000)
        self.assertEqual(cat6, '₹25L+')

        cat7, _ = calculate_income_category(7500000)
        self.assertEqual(cat7, '₹50L+')

        cat8, _ = calculate_income_category(15000000)
        self.assertEqual(cat8, '₹1Cr+')

    def test_search_and_income_categories(self):
        # Search route
        res = self.client.get('/search')
        self.assertEqual(res.status_code, 200)

        # Search with income category filter
        res_filter = self.client.get('/search?income_category=%E2%82%B925L%2B')
        self.assertEqual(res_filter.status_code, 200)

        # Dedicated Income categories route
        res_cat = self.client.get('/income-categories')
        self.assertEqual(res_cat.status_code, 200)
        self.assertIn(b'₹1Cr+', res_cat.data)

    def test_profile_detail_and_privacy(self):
        # View sample profile MAT-10001
        res = self.client.get('/profile/MAT-10001')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'MAT-10001', res.data)
        # Verify contact protected when not logged in
        self.assertIn(b'Contact Details Protected', res.data)

    def test_registration_step_1_and_autosave(self):
        # Step 1 submission test
        unique_email = f"test_{int(__import__('time').time())}@example.com"
        res = self.client.post('/api/register/step/1', data={
            'profile_type': 'bride',
            'profile_created_for': 'Self',
            'first_name': 'Ananya',
            'last_name': 'Sundaram',
            'marital_status': 'Never Married',
            'email': unique_email,
            'mobile': f"99{int(__import__('time').time())%100000000:08d}",
            'password': 'Password123',
            'confirm_password': 'Password123'
        })
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['next_step'], 2)

    def test_admin_portal(self):
        # Admin login page
        res = self.client.get('/admin/login')
        self.assertEqual(res.status_code, 200)

        # Admin login POST
        res_login = self.client.post('/admin/login', data={
            'username': 'admin',
            'password': 'Admin@123'
        }, follow_redirects=True)
    def test_login_as_admin_from_main_login(self):
        # Test logging in as admin directly from /login using username 'admin'
        res = self.client.post('/login', data={
            'email': 'admin',
            'password': 'Admin@123'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Manage Profiles', res.data)

if __name__ == '__main__':
    unittest.main()
