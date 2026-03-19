from django.contrib import admin
from .models import Student, Mark

class MarkInline(admin.TabularInline):
    model = Mark
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "roll_number")
    search_fields = ("name", "roll_number")
    inlines = [MarkInline]
    list_filter = ()
    actions = None
    

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "score")
    list_filter = ("subject",)
    search_fields = ("student__name", "subject")
    list_filter = ()
    actions = None

