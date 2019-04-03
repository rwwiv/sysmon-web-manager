from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseBadRequest, JsonResponse
from .configs_service import get_all_configs
from .configs_service import create_configs
from .configs_service import retrieve_config
from logging_service import configs_logging_service as log
from .configs_service import update_config


def index(request):
    if request.method == 'GET':
        log.debug("GET request recieved at configs endpoint")
        return JsonResponse(get_all_configs(), safe=False)

def configs(request, name):
    if request.method == 'POST':
        log.debug(f"POST request recieved at configs endpoint for {name} config") 
        if create_configs(name) >= 0:
            return HttpResponse('Succesfully created config')
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        log.debug(f"GET request recieved at configs endpoint for {name} config")
        try:
            config = retrieve_config(name)
            log.debug("Config succesfully retrieved and set to be returned")
            return HttpResponse(config)
        except:
            log.err("Config was not retrieved properly")
            return HttpResponseBadRequest()
        
    elif request.method == 'PUT':
        log.debug(f"PUT request recieved at configs endpoint for {name} config")
        try:
            update_config(name, request.body)
            log.debug("Config was updated succesfully")
            return HttpResponse("Config updated sucessfully")
        except:
            log.err("Config was not updated succesfully")
            return HttpResponseBadRequest()

        

