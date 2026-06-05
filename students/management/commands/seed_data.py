import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student, Mark
from feedback.models import Feedback


class Command(BaseCommand):
    help = "Seed test data: 1 admin, 1 teacher, dummy students with marks"

    def handle(self, *args, **options):
        self._create_users()
        self._create_students()
        self._create_marks()
        self._create_feedback()
        self.stdout.write(self.style.SUCCESS("Done."))

    def _create_users(self):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@test.com", "admin123")
            self.stdout.write("  Created admin user (admin / admin123)")
        else:
            self.stdout.write("  Admin user already exists")

        if not User.objects.filter(username="teacher").exists():
            User.objects.create_user("teacher", "teacher@test.com", "teacher123")
            self.stdout.write("  Created teacher user (teacher / teacher123)")
        else:
            self.stdout.write("  Teacher user already exists")

    def _create_students(self):
        students_data = [
            ("Aarav Sharma", 101),
            ("Priya Patel", 102),
            ("Rohan Singh", 103),
            ("Ananya Gupta", 104),
            ("Vikram Joshi", 105),
            ("Sneha Reddy", 106),
            ("Arjun Nair", 107),
            ("Kavya Iyer", 108),
            ("Rahul Verma", 109),
            ("Isha Kapoor", 110),
        ]
        for name, roll in students_data:
            Student.objects.get_or_create(
                roll_number=roll, defaults={"name": name}
            )
        self.stdout.write(f"  Created {len(students_data)} students")

    def _create_marks(self):
        if Mark.objects.exists():
            self.stdout.write("  Marks already exist, skipping")
            return
        subjects = ["Mathematics", "Science", "English", "History"]
        students = Student.objects.all()
        count = 0
        for student in students:
            for subj in subjects:
                Mark.objects.create(
                    student=student,
                    subject=subj,
                    score=round(random.uniform(20, 100), 1),
                )
                count += 1
        self.stdout.write(f"  Created {count} mark entries")

    def _create_feedback(self):
        feedbacks = [
            ("Mathematics", 4, "Need more practice problems"),
            ("Science", 2, "Understood the concepts well"),
            ("English", 3, "Grammar could be improved"),
        ]
        student = Student.objects.first()
        for subj, diff, desc in feedbacks:
            Feedback.objects.get_or_create(
                student=student,
                subject=subj,
                defaults={"difficulty": diff, "description": desc},
            )
        self.stdout.write(f"  Created {len(feedbacks)} feedback entries")
