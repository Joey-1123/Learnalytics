from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    list_filter = ()
    actions = None


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)