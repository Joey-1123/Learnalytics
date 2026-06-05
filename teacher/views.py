"""
Teacher views — dashboard, PDF reports, alerts, grade filtering.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Count, FloatField
from django.db.models.functions import Coalesce
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
import io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import weasyprint

from students.models import Student, Mark, Grade
from students.ai.predictor import PerformancePredictor


# --- AUTHENTICATION VIEWS ---

def admin_login_view(request):
    logout(request)
    return redirect('/admin/login/')


def teacher_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'teacher/teacher_login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# --- DASHBOARD VIEWS ---

def home_view(request):
    return render(request, "home.html")


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

    grade_id = request.GET.get("grade") or ""
    q = (request.GET.get("q") or "").strip()
    selected_id = request.GET.get("student_id")

    students_qs = Student.objects.all()
    if grade_id:
        students_qs = students_qs.filter(grade_id=grade_id)

    matched_students = Student.objects.none()
    if q:
        matched_students = Student.objects.filter(
            name__icontains=q
        ).order_by("name")[:30]
        if grade_id:
            matched_students = matched_students.filter(grade_id=grade_id)

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

    grades = Grade.objects.all()
    alerts = PerformancePredictor.low_performance_students(threshold=40)

    return render(
        request,
        "dashboard.html",
        {
            "total_students": total_students,
            "total_marks": total_marks,
            "weak_subjects_count": weak_subjects_count,
            "q": q,
            "grade_id": grade_id,
            "grades": grades,
            "matched_students": matched_students,
            "selected_student": selected_student,
            "marks_list": marks_list,
            "subject_report": subject_report,
            "alerts": alerts,
        },
    )


@login_required(login_url="/authentication/login/teacher/")
def student_report_pdf(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    marks = Mark.objects.filter(student=student).order_by("subject")
    scores = [m.score for m in marks]

    subject_report = (
        Mark.objects.filter(student=student)
        .values("subject")
        .annotate(
            entries=Count("id"),
            avg=Coalesce(Avg("score"), 0.0, output_field=FloatField()),
            min_score=Coalesce(Min("score"), 0.0, output_field=FloatField()),
            max_score=Coalesce(Max("score"), 0.0, output_field=FloatField()),
        )
        .order_by("subject")
    )

    risk = PerformancePredictor.risk_level(scores)
    predicted = PerformancePredictor.predicted_next_score(scores)

    html = render_to_string("teacher/report_pdf.html", {
        "student": student,
        "marks": marks,
        "subject_report": subject_report,
        "risk": risk,
        "predicted_score": predicted,
    })

    pdf = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="report_{student.roll_number}.pdf"'
    return response


@login_required(login_url="/authentication/login/teacher/")
def alerts_view(request):
    threshold = int(request.GET.get("threshold", 40))
    alerts = PerformancePredictor.low_performance_students(threshold=threshold)
    return render(request, "teacher/alerts.html", {"alerts": alerts, "threshold": threshold})


def download_chart(request, chart_type):
    plt.figure(figsize=(8, 5))
    plt.style.use('dark_background')
    fig = plt.gcf()
    fig.patch.set_facecolor('#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')

    LEARNALYTICS_CYAN = '#06b6d4'
    LEARNALYTICS_ORANGE = '#f97316'
    LEARNALYTICS_GREEN = '#22c55e'
    LEARNALYTICS_BLUE = '#3b82f6'

    if chart_type == 'bar':
        subjects = ['DSA', 'Math', 'Science']
        averages = [60, 25, 35]
        bars = plt.bar(subjects, averages, color=LEARNALYTICS_CYAN)
        plt.title('Subject-wise Average Marks', color='#fff', pad=20, fontweight='bold')
        plt.tick_params(colors='#94a3b8')
    elif chart_type == 'pie':
        labels = ['Math', 'DSA', 'Science']
        sizes = [50, 25, 25]
        colors = [LEARNALYTICS_ORANGE, LEARNALYTICS_BLUE, LEARNALYTICS_GREEN]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
                startangle=140, textprops={'color': "w", 'weight': 'bold'},
                wedgeprops={'linewidth': 3, 'edgecolor': '#0a0a0a'})
        plt.title('Marks Distribution (All Subjects)', color='#fff', pad=20, fontweight='bold')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=150)
    plt.close()
    buf.seek(0)

    response = HttpResponse(buf.read(), content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="Learnalytics_{chart_type}.png"'
    return response
