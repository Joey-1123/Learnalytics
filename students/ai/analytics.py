import statistics

class ClassAnalytics:

    @staticmethod
    def class_average(scores):

        if not scores:
            return 0

        return round(statistics.mean(scores), 2)

    @staticmethod
    def topper(students_scores):

        if not students_scores:
            return None

        return max(students_scores, key=lambda x: x["average"])

    @staticmethod
    def weak_students(students_scores, threshold=40):

        return [
            student
            for student in students_scores
            if student["average"] < threshold
        ]
