from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Student
from .ai.predictor import PerformancePredictor
from .ai.recommender import SubjectRecommender
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def logout_view(request):
    logout(request)
    return redirect('home')


@api_view(['GET'])
def student_list_json(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


def student_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None and hasattr(user, 'student_profile'):
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid student credentials.")
    return render(request, 'students/student_login.html')


@login_required(login_url='/students/login/')
def student_dashboard(request):
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        messages.error(request, "No student profile found.")
        return redirect('home')

    marks = student.marks.select_related()
    scores = [m.score for m in marks]
    risk = PerformancePredictor.risk_level(scores)
    predicted = PerformancePredictor.predicted_next_score(scores)
    weak_subjects = SubjectRecommender.weak_subjects(marks)
    recommendations = SubjectRecommender.study_recommendations(weak_subjects)

    by_subject = PerformancePredictor.scores_by_subject(marks)

    context = {
        "student": student,
        "marks": marks,
        "risk": risk,
        "predicted_score": predicted,
        "weak_subjects": weak_subjects,
        "recommendations": recommendations,
        "by_subject": by_subject,
    }
    return render(request, "students/dashboard.html", context)
