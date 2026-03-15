import io
from django.db.models.functions import Coalesce
from django.db.models import FloatField

import matplotlib
matplotlib.use("Agg")  # important for Django/server rendering

import matplotlib.pyplot as plt
from django.db.models import Avg, Count
from django.http import HttpResponse

from students.models import Mark


def bar_chart(request):
    """
    Subject-wise average marks (all students).
    URL example: /visualization/bar-chart/
    """
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
        ax.set_ylim(0, 100)  # assuming marks out of 100
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
    """
    Marks distribution by subject (counts of mark entries per subject).
    URL example: /visualization/pie-chart/
    """
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