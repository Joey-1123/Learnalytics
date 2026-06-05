# Learnalytics – AI-Powered Student Performance Analytics

Learnalytics is a Django-based academic analytics platform that analyzes student marks and generates insights using classical AI techniques (without Large Language Models).

The system collects student performance data and applies statistical analysis and rule-based AI to predict academic risk, forecast future scores, and identify weak subjects.

---

## Project Goals

This project demonstrates how Artificial Intelligence techniques can be applied to education analytics using structured data.

Key goals:

* Analyze student marks
* Detect weak academic areas
* Predict future performance
* Identify at-risk students
* Visualize academic trends

The system uses **classical AI techniques such as statistics, regression, and rule-based inference**, rather than LLM-based AI.

---

## AI Features Implemented

### 1. Performance Risk Prediction

Located in:

```
students/ai/predictor.py
```

The system calculates student risk levels based on their marks.

Logic used:

* Average score calculation
* Threshold-based classification

Example rule:

```
Average < 40 → High Risk
Average < 60 → Medium Risk
Average ≥ 60 → Low Risk
```

This allows teachers to quickly detect struggling students.

---

### 2. Future Score Prediction

The system estimates the **next exam score** using **Linear Regression**.

Implementation:

```
numpy.polyfit()
```

The algorithm fits a trend line to the student's previous marks and predicts the next point.

Example:

```
Marks: 45, 50, 55
Prediction: ~60
```

This helps estimate academic trajectory.

---

### 3. Weak Subject Detection

Located in:

```
students/ai/recommender.py
```

Subjects where the student scored below the pass threshold are flagged.

Rule:

```
Score < 40 → Weak Subject
```

The system then generates study recommendations.

Example Output:

```
Weak Subjects: Mathematics
Recommendation: Focus additional study hours on Mathematics
```

---

### 4. Class Analytics

Located in:

```
students/ai/analytics.py
```

Provides statistical insights such as:

* Class average
* Top performer
* Students below threshold

This enables quick performance overview.

---

## Platform Features

### Grade Groups
Students are grouped by grade and section (`Grade` model). The teacher dashboard can filter students by grade.

### Student Portal
Students can log in at `/students/login/` using their own credentials (created during seed: `student101`/`student123`). They see their marks, risk level, predicted score, weak subjects, and study recommendations.

### CSV Import
Bulk-import students or marks from a CSV file:

```
uv run python manage.py import_csv students.csv --type students
uv run python manage.py import_csv marks.csv --type marks
```

### PDF Report Cards
Teachers can download individual student report cards as PDF files from the dashboard.

### Performance Trends
A line chart showing score trajectory over time per student/subject, available at `/visualization/trend/<student_id>/`.

### Low-Performance Alerts
The teacher dashboard highlights students below a configurable threshold. A dedicated alerts page is at `/teacher/alerts/`. Email alerts can be sent via a management command:

```
uv run python manage.py send_alerts --threshold 40 --email teacher@school.com
```

---

## System Architecture

```
Browser
   │
   ▼
Django Views
   │
   ▼
Database (SQLite / PostgreSQL)
   │
   ▼
AI Modules (students/ai)
   │
   ├── predictor.py
   ├── recommender.py
   └── analytics.py
   │
   ▼
Templates / Dashboard
```

The AI modules act as a **service layer** between database and user interface.

---

## Database Models

### Grade Model
Groups students into classes/sections.

Fields: `name`, `section`

### Student Model
Stores basic student information with optional grade and user account.

Fields: `name`, `roll_number`, `grade` (FK), `user` (OneToOne), `created_at`

### Mark Model
Stores subject-wise marks.

Fields: `student` (FK), `subject`, `score`, `exam_date`

---

## Project Structure

```
learnalytics/
├── manage.py
├── pyproject.toml
├── uv.lock
│
├── learnalytics/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── models.py              # Grade, Student, Mark
│   ├── views.py               # Student portal, JSON API
│   ├── admin.py
│   ├── urls.py
│   ├── serializers.py
│   ├── management/commands/
│   │   ├── seed_data.py       # Idempotent test data seeder
│   │   ├── import_csv.py      # Bulk import from CSV
│   │   └── send_alerts.py     # Email low-perf alerts
│   │
│   └── ai/
│       ├── predictor.py
│       ├── recommender.py
│       └── analytics.py
│
├── teacher/
│   ├── views.py               # Dashboard, PDF reports, alerts, charts
│   └── urls.py
│
├── visualization/
│   └── views.py               # Bar, pie, trend charts (matplotlib)
│
├── templates/
│   ├── home.html
│   ├── dashboard.html         # Teacher dashboard
│   ├── students/
│   │   ├── dashboard.html     # Student portal
│   │   └── student_login.html
│   └── teacher/
│       ├── alerts.html
│       └── report_pdf.html
│
├── static/
│   └── css/
│       ├── variables.css
│       ├── home.css
│       └── teacher.css
│
└── db.sqlite3 / Postgree  #based on local dev or production  update according to it
```

---

## Technologies Used

Backend:
* Django 6.0
* Django REST Framework
* WeasyPrint (PDF generation)

AI / Data Analysis:
* NumPy
* Rule-Based AI
* Linear Regression

Visualization:
* Matplotlib

Database:
* Supabase (PostgreSQL) in production
* SQLite for local development

Package Management:
* uv

---

## Installation Guide

Prerequisites: Python >= 3.12, [uv](https://docs.astral.sh/uv/)

Clone the repository:

```
git clone <repo-url>
cd Learnalytics
```

Install dependencies:

```
uv sync
```

Run migrations:

```
uv run python manage.py migrate
```

Seed test data:

```
uv run python manage.py seed_data
```

Run server:

```
uv run python manage.py runserver
```

Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Switching Databases

Toggle between PostgreSQL and SQLite:

```
python ../toggle_db.py   # if toggle_db.py is one level up
```

---

## Seed Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Teacher | `teacher` | `teacher123` |
| Students | `student101` — `student110` | `student123` |

---

## Deployment (Render)

The project is configured for Render with native uv support. Set the build command to:

```
uv sync --no-dev
```

And start command to:

```
uv run gunicorn learnalytics.wsgi:application --bind 0.0.0.0:8000
```

---

## Limitations / Future Improvements

Current system uses simple statistical models. Future improvements could include:

* Machine learning models (Random Forest / XGBoost)
* Student clustering
* Attendance analysis
* Personalized study plans
* Real-time performance alerts
* Parent portal

---

## Author
**Shubham Panchal** — [github.com/Joey-1123](https://github.com/Joey-1123)
Student Developer | AI & Software Enthusiast

**Omkar Tamalwad** — [github.com/Omii-004](https://github.com/Omii-004)
Student Developer | AI Student

## License

This project is open source and available under the MIT License. This project is for educational purposes.
