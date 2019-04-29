from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.single_group, name='single_group'),
    path('', views.index, name="index"),
    path('<str:agent>/<str:group>', views.associate, name='associate'),
]
