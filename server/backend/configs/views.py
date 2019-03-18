from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse("Ping")
