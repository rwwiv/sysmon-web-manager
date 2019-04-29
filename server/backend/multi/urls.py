from django.urls import path
from . import views

urlpatterns = [
    path('install', views.install, name='install'),
    path('uninstall', views.uninstall, name='uninstall'),
    path('restart', views.restart, name='restart'),
]