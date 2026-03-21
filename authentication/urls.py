from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    # Teacher login 
    path('teacher-login/', views.teacher_login_view, name='teacher_login'),

    # About page
    path('about/', views.about, name='about'),

    # Password reset views with rate limiting
    path(
        'password-reset/',
        ratelimit(key='ip', rate='3/m', method='POST', block=False)(
            auth_views.PasswordResetView.as_view(
                template_name='auth/password_reset.html'
            )
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]