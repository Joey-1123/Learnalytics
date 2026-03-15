from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Min, Max, Count, FloatField
from django.db.models.functions import Coalesce

from students.models import Student, Mark


def home_view(request):
    return render(request, "home.html")


@login_required(login_url="/admin/login/")
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