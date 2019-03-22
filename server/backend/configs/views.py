from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseBadRequest
from .configs_service import get_all_configs
from .configs_service import create_configs
from .configs_service import retrieve_config
from logging_service import configs_logging_service as log

def index(request):
    if request.method == 'GET':
        log.debug("GET request recieved at configs endpoint")
        return get_all_configs()

def configs(request, name):
    if request.method == 'POST':
        log.debug(f"POST request recieved at configs endpoint for {name} config") 
        if create_configs(name) >= 0:
            return HttpResponse('Succesfully created config')
        else:
            return HttpResponseBadRequest()
    elif request.method == 'GET':
        log.debug(f"GET request recieved at configs endpoint for {name} config")
        if retrieve_config(name) >= 0:
            return HttpResponse('Config retrieved succesfully but not returned as this is not set up fully yet')
        else:
            return HttpResponseBadRequest()
    elif request.method == 'PUT':
        log.debug(f"PUT request recieved at configs endpoint for {name} config")
        return HttpResponse('Endpoint reached for updating a configs xml but this service is not setup yet')


        

