from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from .agentService import get_all_agents
from .agentService import update_needs_install
from .agentService import update_needs_restart
from .agentService import update_needs_uninstall
from .agentService import update_config
from logging_service import agents_logging_service as log


def index(request):
    if request.method == 'GET':
        log.debug('GET request recieved at agents endpoint')
        return JsonResponse(get_all_agents(), safe=False)
    else:
        log.warn('Request with no mapping recieved raising a 404')
        raise Http404()


def updates(request, uuid):
    if request.method == 'PATCH':
        log.debug(f'PATCH request for {uuid} recieved')
        
        success = update_needs_install(uuid)
        
        if success == 0:
            return HttpResponse("succesful update")
        else:
            return HttpResponseBadRequest("update failed")

    elif request.method == 'POST':
        log.debug(f'POST request for {uuid} recieved')
        
        success = update_needs_restart(uuid)
        
        if success == 0:
            return HttpResponse("succesful update")
        else:
            return HttpResponseBadRequest("update failed")

    elif request.method == 'DELETE':
        log.debug(f'DELETE request for {uuid} recieved')
        
        success = update_needs_uninstall(uuid)
        
        if success == 0:
            return HttpResponse("succesful update")
        else:
            return HttpResponseBadRequest("update failed")
    else:
        log.warn('Request with no mapping recieved raising 404')
        raise Http404()


def set_config(request, uuid, name):
    if request.method == 'PATCH':
        log.debug(f'Config update recieved for agent {uuid} with config {name}')
        success = update_config(uuid, name)

        if success == 0:
            return HttpResponse("Succesful update")
        else:
            return HttpResponseBadRequest("Update failed")
    else:
        log.warn('Request with no mapping recieved raising 404')
        raise Http404()



