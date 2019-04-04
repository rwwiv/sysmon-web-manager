from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def create_user(username, password):
    if username is not None and password is not None:
        User.objects.create_user(username=username, password=password)
        return 0
    else:
        return -1


def validate_user(username, password):
    if username is not None and password is not None:
        user = authenticate(username=username, password=password)
        if user is not None:
            return 0
        else:
            return -1

