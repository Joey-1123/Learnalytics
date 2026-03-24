from django.db import models


class Feedback(models.Model):
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="feedbacks",
        null=True,
        blank=True
    )
    subject = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
