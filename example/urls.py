from django.urls import path
from .views import time_complexity_view

urlpatterns = [
    path('', time_complexity_view, name='time_complexity'),
]
