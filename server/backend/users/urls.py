from django.urls import path
from . import views

urlpatterns = [
    path('users/create', views.create),
    path('users/auth', views.auth)
]
