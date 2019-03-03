from django.urls import path
from . import views

urlpatterns = [
    path('install', views.install, name='install'),
]