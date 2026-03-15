from django.shortcuts import render, get_object_or_404

from .models import Student
from .ai.predictor import PerformancePredictor
from .ai.recommender import SubjectRecommender


def student_dashboard(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    marks = student.marks.select_related("subject")

    scores = [m.score for m in marks]

    risk = PerformancePredictor.risk_level(scores)

    predicted = PerformancePredictor.predicted_next_score(scores)

    weak_subjects = SubjectRecommender.weak_subjects(marks)

    recommendations = SubjectRecommender.study_recommendations(
        weak_subjects
    )

    context = {
        "student": student,
        "marks": marks,
        "risk": risk,
        "predicted_score": predicted,
        "weak_subjects": weak_subjects,
        "recommendations": recommendations,
    }

    return render(request, "students/dashboard.html", context)