from django.urls import path
from . import views

urlpatterns = [
    path('user/validate', views.validate_user, name='index'),
    path('user/password', views.update_password, name='updates'),
    path('user/create', views.create_user, name='set_config')
]
