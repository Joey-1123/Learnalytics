from django.contrib import admin
from .models import Student, Mark, Grade


class MarkInline(admin.TabularInline):
    model = Mark
    extra = 1


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name", "section")
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "roll_number", "grade")
    search_fields = ("name", "roll_number")
    list_filter = ("grade",)
    inlines = [MarkInline]
    actions = None


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "score")
    list_filter = ("subject",)
    search_fields = ("student__name", "subject")
    actions = None
