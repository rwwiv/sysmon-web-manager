from django.urls import path
from . import views

urlpatterns = [
    path('config/<str:name>', views.config, name='name'),
    path('sysmon/<str:version>', views.sysmon, name='version'),
]