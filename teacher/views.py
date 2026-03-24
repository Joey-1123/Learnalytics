from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Count, FloatField
from django.db.models.functions import Coalesce
from django.contrib import messages
from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
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

def download_chart(request, chart_type):
    # Set the figure and background
    plt.figure(figsize=(8, 5))
    plt.style.use('dark_background')
    fig = plt.gcf()
    fig.patch.set_facecolor('#0a0a0a') # Matches your card background
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')

    # Brand Colors
    LEARNALYTICS_CYAN = '#06b6d4'
    LEARNALYTICS_ORANGE = '#f97316'
    LEARNALYTICS_GREEN = '#22c55e'
    LEARNALYTICS_BLUE = '#3b82f6'

    if chart_type == 'bar':
        subjects = ['DSA', 'Math', 'Science']
        averages = [60, 25, 35]
        
        # Apply the solid Cyan to all bars
        bars = plt.bar(subjects, averages, color=LEARNALYTICS_CYAN)
        
        plt.title('Subject-wise Average Marks', color='#fff', pad=20, fontweight='bold')
        plt.tick_params(colors='#94a3b8') # Muted gray for axis numbers
        
    elif chart_type == 'pie':
        labels = ['Math', 'DSA', 'Science']
        sizes = [50, 25, 25]
        # Use your vibrant brand palette
        colors = [LEARNALYTICS_ORANGE, LEARNALYTICS_BLUE, LEARNALYTICS_GREEN]
        
        # 'wedgeprops' adds that clean dark line between slices
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, 
                startangle=140, textprops={'color':"w", 'weight':'bold'},
                wedgeprops={'linewidth': 3, 'edgecolor': '#0a0a0a'})
        
        plt.title('Marks Distribution (All Subjects)', color='#fff', pad=20, fontweight='bold')

    # Save with high quality
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=150)
    plt.close()
    buf.seek(0)

    response = HttpResponse(buf.read(), content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="Learnalytics_{chart_type}.png"'
    return response