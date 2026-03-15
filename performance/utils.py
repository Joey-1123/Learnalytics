from django.db.models import Avg, FloatField
from django.db.models.functions import Coalesce
from students.models import Mark

def get_weak_subjects():
    return list(
        Mark.objects.values("subject")
        .annotate(average=Coalesce(Avg("score"), 0.0, output_field=FloatField()))
        .filter(average__lt=40)
        .order_by("subject")
    )