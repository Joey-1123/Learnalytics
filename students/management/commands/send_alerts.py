from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from students.ai.predictor import PerformancePredictor
from students.models import Student


class Command(BaseCommand):
    help = "Email low performance alerts for students below threshold"

    def add_arguments(self, parser):
        parser.add_argument("--threshold", type=int, default=40)
        parser.add_argument("--email", type=str, default="")

    def handle(self, *args, **options):
        threshold = options["threshold"]
        email = options["email"]
        alerts = PerformancePredictor.low_performance_students(threshold=threshold)

        if not alerts:
            self.stdout.write(self.style.SUCCESS("No low-performance students found."))
            return

        lines = ["Low Performance Report", "=" * 30, ""]
        for student, avg in alerts:
            lines.append(f"{student.name} (Roll: {student.roll_number}) — Avg: {avg}")
        body = "\n".join(lines)

        if email:
            send_mail(
                subject=f"Low Performance Alerts ({len(alerts)} students)",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS(f"Emailed {len(alerts)} alerts to {email}"))
        else:
            self.stdout.write(body)
            self.stdout.write(self.style.WARNING("Pass --email to send via email"))
