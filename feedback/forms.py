from django import forms
from .models import Feedback
from students.models import Student


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    roll_number = forms.IntegerField(required=True, min_value=1)
    difficulty = forms.IntegerField(required=True, min_value=1, max_value=5)

    class Meta:
        model = Feedback
        fields = ["name", "roll_number", "subject", "difficulty", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        roll_number = cleaned_data.get("roll_number")

        if name and roll_number is not None:
            student = Student.objects.filter(roll_number=roll_number).first()
            if not student:
                raise forms.ValidationError("Student record not found. Please register first.")

            if student.name.strip().lower() != name.strip().lower():
                raise forms.ValidationError("Name and roll number do not match a registered student.")

            cleaned_data["student"] = student

        return cleaned_data