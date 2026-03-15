from django.shortcuts import render, redirect
from .models import Feedback


def feedback_form(request):
    error = None

    if request.method == "POST":
        subject = (request.POST.get("subject") or "").strip()
        difficulty_raw = (request.POST.get("difficulty") or "").strip()
        description = (request.POST.get("description") or "").strip()

        if not subject:
            error = "Subject is required."
        else:
            try:
                difficulty = int(difficulty_raw)
                if difficulty < 1 or difficulty > 5:
                    error = "Difficulty must be between 1 and 5."
            except ValueError:
                error = "Difficulty must be a number."

        if not error:
            Feedback.objects.create(subject=subject, difficulty=difficulty, description=description)
            return redirect("feedback_success")

    return render(request, "feedback_form.html", {"error": error})


def feedback_success(request):
    return render(request, "success.html")