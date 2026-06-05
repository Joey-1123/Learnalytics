import numpy as np
from collections import defaultdict


class PerformancePredictor:

    FAIL_THRESHOLD = 40
    WARNING_THRESHOLD = 60

    @staticmethod
    def average(scores):
        if not scores:
            return 0
        return float(np.mean(scores))

    @classmethod
    def risk_level(cls, scores):
        avg = cls.average(scores)
        if avg < cls.FAIL_THRESHOLD:
            return "high"
        elif avg < cls.WARNING_THRESHOLD:
            return "medium"
        return "low"

    @classmethod
    def predicted_next_score(cls, scores):
        if len(scores) < 2:
            return cls.average(scores)
        x = np.arange(len(scores))
        y = np.array(scores)
        slope, intercept = np.polyfit(x, y, 1)
        next_exam = len(scores)
        prediction = slope * next_exam + intercept
        return round(float(prediction), 2)

    @classmethod
    def scores_by_subject(cls, marks):
        by_subject = defaultdict(list)
        for m in marks:
            by_subject[m.subject].append(m.score)
        return dict(by_subject)

    @classmethod
    def low_performance_students(cls, threshold=40):
        from students.models import Student, Mark
        from django.db.models import Avg
        results = []
        for student in Student.objects.all():
            avg = Mark.objects.filter(student=student).aggregate(
                avg=Avg("score")
            )["avg"]
            if avg is not None and avg < threshold:
                results.append((student, round(float(avg), 1)))
        return sorted(results, key=lambda x: x[1])