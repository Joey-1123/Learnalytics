from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("login/", views.student_login_view, name="student_login"),
    path("logout/", views.logout_view, name="student_logout"),
    path('students/', views.student_list_json, name='student_json'),
]