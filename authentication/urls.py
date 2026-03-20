from django.urls import path
from . import views

urlpatterns = [
    path('teacher-login/', views.teacher_login_view, name='teacher_login'),
    path('about/', views.about, name='about'),
    path('login/teacher/', views.teacher_login_view, name='teacher_login'),
]
