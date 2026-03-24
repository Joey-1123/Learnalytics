from django.test import TestCase
from django.urls import reverse
from students.models import Student
from .models import Feedback


class FeedbackFormTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="John Doe", roll_number=101)

    def test_feedback_saved_for_existing_student(self):
        response = self.client.post(
            reverse("feedback_form"),
            {
                "name": "John Doe",
                "roll_number": 101,
                "subject": "Data Structures",
                "difficulty": 4,
                "description": "Challenging but fair",
            },
        )
        self.assertRedirects(response, reverse("feedback_success"))
        self.assertTrue(Feedback.objects.filter(student=self.student, subject="Data Structures").exists())

    def test_feedback_rejected_for_nonexistent_student(self):
        response = self.client.post(
            reverse("feedback_form"),
            {
                "name": "Ghost",
                "roll_number": 999,
                "subject": "Algorithms",
                "difficulty": 3,
                "description": "Test",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student record not found")
        self.assertFalse(Feedback.objects.filter(subject="Algorithms").exists())

    def test_feedback_rejected_when_name_roll_mismatch(self):
        response = self.client.post(
            reverse("feedback_form"),
            {
                "name": "Wrong Name",
                "roll_number": 101,
                "subject": "Math",
                "difficulty": 2,
                "description": "Test",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Name and roll number do not match")
        self.assertFalse(Feedback.objects.filter(subject="Math").exists())

