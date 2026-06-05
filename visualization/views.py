import io
from django.db.models.functions import Coalesce
from django.db.models import FloatField

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from django.db.models import Avg, Count
from django.http import HttpResponse

from students.models import Mark


def bar_chart(request):
    qs = (
        Mark.objects.values("subject")
        .annotate(avg=Coalesce(Avg("score"), 0.0, output_field=FloatField()))
        .order_by("subject")
    )
    labels = [row["subject"] for row in qs]
    values = [float(row["avg"]) for row in qs]

    fig, ax = plt.subplots(figsize=(7, 4))
    if labels:
        ax.bar(labels, values)
        ax.set_title("Subject-wise Average Marks")
        ax.set_ylabel("Average Marks")
        ax.set_ylim(0, 100)
        ax.tick_params(axis="x", labelrotation=20)
    else:
        ax.text(0.5, 0.5, "No marks data available", ha="center", va="center")
        ax.set_axis_off()

    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")


def pie_chart(request):
    qs = (
        Mark.objects.values("subject")
        .annotate(cnt=Count("id"))
        .order_by("subject")
    )
    labels = [row["subject"] for row in qs]
    sizes = [int(row["cnt"]) for row in qs]

    fig, ax = plt.subplots(figsize=(6, 6))
    if labels:
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        ax.set_title("Marks Distribution (All Subjects)")
    else:
        ax.text(0.5, 0.5, "No marks data available", ha="center", va="center")
        ax.set_axis_off()

    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")


def trend_chart(request, student_id):
    from io import BytesIO
    marks = Mark.objects.filter(student_id=student_id).order_by("exam_date")
    if not marks:
        return HttpResponse("No data", content_type="text/plain")

    subjects = set(m.subject for m in marks)
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#0a0a0a")
    ax.set_facecolor("#0a0a0a")

    colors = ["#06b6d4", "#f97316", "#22c55e", "#3b82f6", "#a855f7", "#ec4899"]
    for i, subject in enumerate(sorted(subjects)):
        subj_marks = [m for m in marks if m.subject == subject]
        dates = [m.exam_date for m in subj_marks]
        scores = [m.score for m in subj_marks]
        ax.plot(dates, scores, marker="o", label=subject,
                color=colors[i % len(colors)], linewidth=2)

    ax.set_title("Performance Trends", color="#fff", fontweight="bold")
    ax.set_ylabel("Score", color="#94a3b8")
    ax.set_xlabel("Exam Date", color="#94a3b8")
    ax.tick_params(colors="#94a3b8")
    ax.legend(facecolor="#1e293b", labelcolor="#fff")
    ax.set_ylim(0, 100)

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", facecolor=fig.get_facecolor(), dpi=150)
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")
