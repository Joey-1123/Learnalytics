from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "difficulty", "created_at")
    list_filter = ("subject", "difficulty")
    search_fields = ("subject",)
    search_fields = ("subject", "description")
    list_filter = ()
    actions = None

    def has_change_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request):
        return False
    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]
    