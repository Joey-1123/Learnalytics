import numpy as np
import joblib
from pathlib import Path
from students.models import Mark

MODEL_PATH = Path("students/ai/student_score_model.pkl")


class ModelTrainer:

    @staticmethod
    def load_training_data():
        """
        Prepare dataset from database
        X = exam index
        y = score
        """

        marks = Mark.objects.all().order_by("student", "exam_date")

        X = []
        y = []

        student_exam_count = {}

        for mark in marks:

            sid = mark.student_id

            if sid not in student_exam_count:
                student_exam_count[sid] = 0

            exam_number = student_exam_count[sid]

            X.append([exam_number])
            y.append(mark.score)

            student_exam_count[sid] += 1

        return np.array(X), np.array(y)

    @staticmethod
    def train():

        X, y = ModelTrainer.load_training_data()

        if len(X) < 5:
            return None

        # simple linear regression
        coefficients = np.polyfit(X.flatten(), y, 1)

        model = {
            "slope": coefficients[0],
            "intercept": coefficients[1]
        }

        joblib.dump(model, MODEL_PATH)

        return model

    @staticmethod
    def load_model():

        if MODEL_PATH.exists():
            return joblib.load(MODEL_PATH)

        return None