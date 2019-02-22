from django.urls import path
from . import views

urlpatterns = [
    path('config/<str:name>', views.config, name="config"),
    path('sysmon/<str:version>', views.sysmon, name='sysmon'),
]