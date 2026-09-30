# Premium Bilingual Matrimony Platform (மேட்ரோமணி / Matromani)

A modern, professional, mobile-first **Tamil + English** matrimonial web application built with **Python Flask**, **SQLite**, **SQLAlchemy**, and **Bootstrap 5**.

---

## 🌟 Key Features

### 1. Bilingual System (Default: Pure Unicode Tamil)
- **Default Language**: Tamil (`ta`), with seamless one-click switching to English (`en`).
- **Dynamic Switcher**: Positioned prominently in the top navigation (`தமிழ் | English` on desktop, `தமிழ் / English` on mobile).
- **Session & Cookie Persistence**: Automatically remembers language preference across visits.
- **Server-Side Jinja Translation Dictionary**: Fully localized UI with pure Unicode Tamil terms (no Tanglish).

### 2. Branding & Premium UI/UX
- **Palette**: Deep Burgundy / Rose (`#800020`, `#8B1E3F`) and Warm Gold (`#D4AF37`, `#C5A059`).
- **Style**: Modern, trustworthy, and elegant Indian Matrimonial design.
- **Mobile-First**: Sticky mobile bottom navigation, minimum 48px touch targets, rounded inputs (`14px` border-radius), and soft shadows.

### 3. Income Categorization Engine
- **Standardized Income Categories**:
  - `₹1L+` / `₹1 லட்சம்+`
  - `₹3L+` / `₹3 லட்சம்+`
  - `₹5L+` / `₹5 லட்சம்+`
  - `₹10L+` / `₹10 லட்சம்+`
  - `₹15L+` / `₹15 லட்சம்+`
  - `₹25L+` / `₹25 லட்சம்+`
  - `₹50L+` / `₹50 லட்சம்+`
  - `₹1Cr+` / `₹1 கோடி+`
- **Dynamic Category Detection**: Real-time calculation as users enter annual salary in registration.
- **Privacy Guaranteed**: Exact salary figures remain private; only standardized category badges are shown publicly.

### 4. 8-Step Multi-Step Registration Wizard
- **Progress Tracking**: Visual step circles with progress line (`படி {current} / {total}` or `Step {current} of {total}`).
- **Autosave & Resume**: Background drafts saved to database and session; users can resume anytime.
- **Steps**:
  1. **Basic Details**: Profile for, Bride/Groom, Names, Marital status, Email, Mobile, Password.
  2. **Personal & Birth Details**: Date of birth, Time of birth, Birth city, Height, Weight, Blood group, Religion, Community, Gothram.
  3. **Address Details**: Street address, City, District, State, Country, Pincode.
  4. **Education, Career & Income**: Degree, College, Job title, Company, Location, Salary, Auto Income Category, Privacy toggle.
  5. **Family Details**: Parents' names & occupations, Siblings count, Family type, Status, Values, Ancestral origin (Poorvigam).
  6. **Horoscope Details**: Rasi, Nakshatra, Lagnam, Dosham (Chevvai/Rahu-Ketu), Jathagam chart upload.
  7. **Profile Photos**: Main photo (required) + gallery photos with live client preview.
  8. **Review & Submit**: Summary card with one-click **"Edit / திருத்து"** jump buttons for each section.

### 5. Traditional South Indian 12-Box Astrology Grid (ராசி கட்டம்)
- Responsive 12-box square astrology layout rendering Rasi, Nakshatra, and planetary placements.

### 6. Search & Matching Engine
- Multi-criteria filtering by Bride/Groom, Age, Marital status, Religion, Community, Education, Occupation, Income Category, Location, and Dosham.
- Quick search shortcuts directly on the homepage Hero.

### 7. Member Dashboard & Privacy Controls
- Overview stats: Shortlists count, Interests sent/received count, Profile views.
- Recommended compatible matches.
- Interactive shortlist and interest buttons with instant AJAX feedback.
- Privacy controls to toggle exact income, mobile/email, and photo visibility.

### 8. Admin Portal & Profile Approvals
- Secure admin dashboard with user metrics and verification queue.
- Approve or reject profile submissions.

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- pip

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Application
```bash
python app.py
```
Or double-click `start.bat` on Windows.

The application will be live at:
👉 **http://127.0.0.1:5000**

---

## 🔑 Demo Credentials

| Role | Email / Username | Password |
|---|---|---|
| **Super Admin** | `admin` (or `admin@matromani.com`) | `Admin@123` |
| **Groom Demo** | `karthik.raman@example.com` | `Password123` |
| **Bride Demo** | `priya.soundar@example.com` | `Password123` |
| **Corporate Groom** | `vignesh.nataraj@example.com` | `Password123` |
| **AI Scientist Bride** | `deepa.annamalai@example.com` | `Password123` |

---

## 🗄️ Database Architecture (22 Tables)

All 22 specified tables are implemented in `models.py`:
1. `users`
2. `profiles`
3. `personal_details`
4. `birth_details`
5. `addresses`
6. `education_details`
7. `career_details`
8. `income_details`
9. `income_categories`
10. `family_details`
11. `horoscope_details`
12. `lifestyle_details`
13. `partner_preferences`
14. `profile_photos`
15. `jathagam_files`
16. `shortlists`
17. `interests`
18. `profile_views`
19. `notifications`
20. `privacy_settings`
21. `registration_progress`
22. `admin_users`
