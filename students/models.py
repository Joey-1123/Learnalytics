import django.db
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    roll_number = django.db.models.PositiveIntegerField(unique=True)

    created_at = django.db.models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["roll_number"]

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Mark(django.db.models.Model):

    student = django.db.models.ForeignKey(
        Student,
        on_delete=django.db.models.CASCADE,
        related_name="marks"
    )

    subject = django.db.models.CharField(max_length=100)

    score = django.db.models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    exam_date = django.db.models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "subject", "exam_date")
        indexes = [
            django.db.models.Index(fields=["student"]),
            django.db.models.Index(fields=["subject"]),
        ]

    def __str__(self):
        return f"{self.student.name} - {self.subject} ({self.score})"