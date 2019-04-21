from django.urls import path
from . import views

urlpatterns = [
    path('links/sysmon/repo', views.sysmon_version_repo, name='sysmon_version_repo'),
    path('links/sysmon/download', views.sysmon_download, name='sysmon_download_repo'),
    path('links/configs/download', views.configs_download, name='configs_download'),
]