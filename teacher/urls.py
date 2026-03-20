from django.urls import path
from . import views  # Import all views from the current app

urlpatterns = [
    # Main Dashboard Path
    path("dashboard/", views.dashboard, name="teacher_dashboard"),
    
    # Login and Logout paths (assuming they are in this app)
    path("login/", views.teacher_login_view, name="teacher_login"),
    path("logout/", views.logout_view, name="logout"),
]