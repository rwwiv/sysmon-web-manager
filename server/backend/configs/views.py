from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import HttpResponse

from logging_service import configs_logging_service as log
from .configs_service import create_configs, get_all_configs, retrieve_config, update_config


def index(request):
    if request.method == 'GET':
        log.debug("GET request received at configs endpoint")
        return JsonResponse(get_all_configs(), safe=False)


def configs(request, name):
    if request.method == 'POST':
        log.debug(f"POST request recieved at configs endpoint for {name} config") 
        if create_configs(name,request.body) >= 0:
            return HttpResponse('Succesfully created config')
        else:
            return HttpResponseBadRequest()

    elif request.method == 'GET':
        log.debug(f"GET request received at configs endpoint for {name} config")
        try:
            config = retrieve_config(name)
            log.debug("Config successfully retrieved and set to be returned")
            return HttpResponse(config)
        except:
            log.err("Config was not retrieved properly")
            return HttpResponseBadRequest()
        
    elif request.method == 'PUT':
        log.debug(f"PUT request received at configs endpoint for {name} config")
        try:
            update_config(name, request.body)
            log.debug("Config was updated successfully")
            return HttpResponse("Config updated successfully")
        except:
            log.err("Config was not updated successfully")
            return HttpResponseBadRequest()

        

