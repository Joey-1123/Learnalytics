import numpy as np


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