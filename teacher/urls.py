from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="teacher_dashboard"),
    path("login/", views.teacher_login_view, name="teacher_login"),
    path("logout/", views.logout_view, name="logout"),
    path("report/<int:student_id>/pdf/", views.student_report_pdf, name="student_report_pdf"),
    path("alerts/", views.alerts_view, name="teacher_alerts"),
    path('download-chart/<str:chart_type>/', views.download_chart, name='download_chart'),
]