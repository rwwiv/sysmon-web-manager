from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from authentication_service import validate_user_credentials
from authentication_service import create_new_user
from authentication_service import update_password_for_user
import json

def validate_user(request):
    success_flag = validate_user_credentials(json.loads(request.body))
    if success_flag == 0:
        return HttpResponseForbidden('User failed to authenticate')
    elif success_flag > 0:
        return HttpResponse('User authenticated successfully')
    else:
        return HttpResponseBadRequest('Unexpected error occurred')
def update_password(request):
    success_flag = update_password_for_user(request)
    if success_flag == 0:
        return HttpResponseForbidden('Incorrect username and password')
    elif success_flag > 0:
        return HttpResponse("Users password updated successfully")
    else:
        return HttpResponseBadRequest("Unexpected error occurred")

def create_user(request):
    pass
