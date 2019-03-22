from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:uuid>', views.updates, name='updates'),
]
