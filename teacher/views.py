from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Count, FloatField
from django.db.models.functions import Coalesce
from django.contrib import messages

from students.models import Student, Mark

# --- AUTHENTICATION VIEWS ---

def teacher_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard') # Redirects to the dashboard view below
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'teacher/teacher_login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


# --- DASHBOARD VIEWS ---

def home_view(request):
    return render(request, "home.html")

# Updated to use your new teacher login URL
@login_required(login_url="/authentication/login/teacher/")
def dashboard(request):
    total_students = Student.objects.count()
    total_marks = Mark.objects.count()

    weak_subjects_qs = (
        Mark.objects.values("subject")
        .annotate(avg=Coalesce(Avg("score"), 0.0, output_field=FloatField()))
        .filter(avg__lt=40)
        .order_by("subject")
    )
    weak_subjects_count = weak_subjects_qs.count()

    q = (request.GET.get("q") or "").strip()
    selected_id = request.GET.get("student_id")

    matched_students = Student.objects.none()
    if q:
        matched_students = Student.objects.filter(
            name__icontains=q
        ).order_by("name")[:30]

    selected_student = None
    subject_report = []
    marks_list = []

    if selected_id:
        selected_student = Student.objects.filter(id=selected_id).first()
        if selected_student:
            marks_list = Mark.objects.filter(student=selected_student).order_by("subject")

            subject_report = (
                Mark.objects.filter(student=selected_student)
                .values("subject")
                .annotate(
                    entries=Count("id"),
                    avg=Coalesce(Avg("score"), 0.0, output_field=FloatField()),
                    min_score=Coalesce(Min("score"), 0.0, output_field=FloatField()),
                    max_score=Coalesce(Max("score"), 0.0, output_field=FloatField()),
                )
                .order_by("subject")
            )

    return render(
        request,
        "dashboard.html",
        {
            "total_students": total_students,
            "total_marks": total_marks,
            "weak_subjects_count": weak_subjects_count,
            "q": q,
            "matched_students": matched_students,
            "selected_student": selected_student,
            "marks_list": marks_list,
            "subject_report": subject_report,
        },
    )