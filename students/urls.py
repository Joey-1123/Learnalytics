from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/<int:student_id>/", views.student_dashboard, name="dashboard"),
    path('students/', views.student_list_json, name='student_json'),
]