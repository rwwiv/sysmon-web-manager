import json

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError

from users import user_service


def create(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        if user_service.create_user(body.get('username'), body.get('password')) >= 0:
            return HttpResponse('Created new user')
        else:
            return HttpResponseServerError('Could not create user')


def auth(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        if user_service.validate_user(body.get('username'), body.get('password')) >= 0:
            return HttpResponse('OK')
        else:
            return HttpResponseNotAllowed('User not authenticated')
