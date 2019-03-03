from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updates/<str:uuid>',views.updates, name='updates'),
    path('multi/install',views.multi, name='multi/install'),
]
