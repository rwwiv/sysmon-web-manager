from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.creation, name='create_group'),
    path('', views.index, name="index"),
    path('<str:agent>/<str:group>',views.associate, name='associate'),
]
