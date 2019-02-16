from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('updates/', include('updates.urls')),
    path('heartbeat/', include('heartbeat.urls')),
    path('admin/', admin.site.urls),
]
