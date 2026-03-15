from django.db import models

class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
