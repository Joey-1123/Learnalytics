from django.urls import path
from . import views

urlpatterns = [
    path("bar-chart/", views.bar_chart, name="bar-chart"),
    path("pie-chart/", views.pie_chart, name="pie-chart"),
    path("trend/<int:student_id>/", views.trend_chart, name="trend_chart"),
]