import csv
from django.core.management.base import BaseCommand, CommandError
from students.models import Student, Mark, Grade


class Command(BaseCommand):
    help = "Import students and marks from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="Path to CSV file")
        parser.add_argument(
            "--type", choices=["students", "marks"], default="students",
            help="Import type: students (default) or marks"
        )

    def handle(self, *args, **options):
        path = options["file"]
        import_type = options["type"]
        try:
            with open(path, newline="") as f:
                reader = csv.DictReader(f)
                if import_type == "students":
                    self._import_students(reader)
                else:
                    self._import_marks(reader)
        except FileNotFoundError:
            raise CommandError(f"File not found: {path}")

    def _import_students(self, reader):
        count = 0
        for row in reader:
            name = row.get("name", "").strip()
            roll = row.get("roll_number", "").strip()
            grade_name = row.get("grade_name", "").strip()
            grade_section = row.get("grade_section", "").strip()
            if not name or not roll:
                self.stdout.write(self.style.WARNING(f"Skipping row: missing name or roll_number"))
                continue
            grade = None
            if grade_name:
                grade, _ = Grade.objects.get_or_create(
                    name=grade_name,
                    section=grade_section or "",
                )
            Student.objects.update_or_create(
                roll_number=int(roll),
                defaults={"name": name, "grade": grade},
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"Imported {count} students"))

    def _import_marks(self, reader):
        count = 0
        for row in reader:
            roll = row.get("roll_number", "").strip()
            subject = row.get("subject", "").strip()
            score = row.get("score", "").strip()
            if not roll or not subject or not score:
                self.stdout.write(self.style.WARNING("Skipping row: missing fields"))
                continue
            student = Student.objects.filter(roll_number=int(roll)).first()
            if not student:
                self.stdout.write(self.style.WARNING(f"Student roll {roll} not found, skipping"))
                continue
            Mark.objects.create(
                student=student,
                subject=subject,
                score=float(score),
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"Imported {count} marks"))
