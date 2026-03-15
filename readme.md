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

# AI Features Implemented

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

# System Architecture

```
Browser
   │
   ▼
Django Views
   │
   ▼
Database (SQLite)
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

# Project Structure

```
learnalytics/
│
├── manage.py
│
├── learnalytics/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   │
│   └── ai/
│       ├── predictor.py
│       ├── recommender.py
│       ├── analytics.py
│       └── training.py
│
├── visualization/
│   └── graph generation (matplotlib)
│
├── templates/
│
├── static/
│
└── db.sqlite3
```

---

# Database Models

### Student Model

Stores basic student information.

Fields:

```
name
roll_number
created_at
```

---

### Mark Model

Stores subject-wise marks.

Fields:

```
student (ForeignKey)
subject
score
exam_date
```

---

# Visualization

The system uses **Matplotlib** to generate performance charts such as:

* Score trends
* Subject comparison
* Performance distribution

These graphs help visualize academic patterns.

---

# Technologies Used

Backend:

* Django
* Django REST Framework

AI / Data Analysis:

* NumPy
* Rule-Based AI
* Linear Regression

Visualization:

* Matplotlib

Database:

* SQLite

---

# Installation Guide

Clone the repository:

```
git clone <repo-url>
cd learnalytics
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
cd Learnalytics
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```


Run server:

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

# Example Workflow

1. Admin enters student marks
2. Data stored in database
3. AI modules analyze marks
4. Dashboard displays predictions and recommendations

---

# Limitations / Future Improvements

Current system uses simple statistical models. Future improvements could include:

* Machine learning models (Random Forest / XGBoost)
* Student clustering
* Attendance analysis
* Personalized study plans
* Real-time performance alerts

---

# Author

Shubham Panchal
Student Developer | AI & Software Enthusiast
Omkar Tamalwad  
Student Developer  
---

## License
This project is open source and available under the MIT License.

This project is for educational purposes.
