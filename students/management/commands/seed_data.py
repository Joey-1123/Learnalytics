import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student, Mark, Grade
from feedback.models import Feedback


class Command(BaseCommand):
    help = "Seed test data: admin, teacher, grades, students with marks"

    def handle(self, *args, **options):
        self._create_users()
        self._create_grades()
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

    def _create_grades(self):
        grades_data = [
            ("Grade 10", "A"),
            ("Grade 10", "B"),
            ("Grade 11", "A"),
        ]
        for name, section in grades_data:
            Grade.objects.get_or_create(name=name, section=section)
        self.stdout.write(f"  Created {len(grades_data)} grades")

    def _create_students(self):
        students_data = [
            ("Aarav Sharma", 101, "Grade 10", "A"),
            ("Priya Patel", 102, "Grade 10", "A"),
            ("Rohan Singh", 103, "Grade 10", "B"),
            ("Ananya Gupta", 104, "Grade 10", "B"),
            ("Vikram Joshi", 105, "Grade 11", "A"),
            ("Sneha Reddy", 106, "Grade 11", "A"),
            ("Arjun Nair", 107, "Grade 10", "A"),
            ("Kavya Iyer", 108, "Grade 10", "B"),
            ("Rahul Verma", 109, "Grade 11", "A"),
            ("Isha Kapoor", 110, "Grade 10", "A"),
        ]
        for name, roll, gname, gsection in students_data:
            grade = Grade.objects.filter(name=gname, section=gsection).first()
            student, created = Student.objects.get_or_create(
                roll_number=roll, defaults={"name": name, "grade": grade}
            )
            if not created:
                student.grade = grade
                student.save()
            user, u_created = User.objects.get_or_create(
                username=f"student{roll}",
                defaults={"first_name": name.split()[0], "last_name": name.split()[-1] if len(name.split()) > 1 else ""},
            )
            if u_created:
                user.set_password("student123")
                user.save()
            student.user = user
            student.save()
        self.stdout.write(f"  Created {len(students_data)} students with login credentials")

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
