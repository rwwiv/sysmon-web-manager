from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from .agent_service import get_all_agents
from .agent_service import update_needs_install
from .agent_service import update_needs_restart
from .agent_service import update_needs_uninstall
from .agent_service import update_config
from logging_service import agents_logging_service as log


def index(request):
    if request.method == 'GET':
        log.debug('GET request received at agents endpoint')
        return JsonResponse(get_all_agents(), safe=False)
    else:
        log.warn('Request with no mapping received raising a 404')
        raise Http404()


def updates(request, uuid):
    if request.method == 'PATCH':
        log.debug(f'PATCH request for {uuid} received')
        
        success = update_needs_install(uuid)
        
        if success > 0:
            return HttpResponse("successful update")
        else:
            return HttpResponseBadRequest("update failed")

    elif request.method == 'POST':
        log.debug(f'POST request for {uuid} received')
        
        success = update_needs_restart(uuid)
        
        if success > 0:
            return HttpResponse("successful update")
        elif success == 1:
            return HttpResponseBadRequest("No default config or sysmon version on server please make these before attempting an install")
        else:
            return HttpResponseBadRequest("update failed")

    elif request.method == 'DELETE':
        log.debug(f'DELETE request for {uuid} recieved')
        
        success = update_needs_uninstall(uuid)
        
        if success == 0:
            return HttpResponse("successful update")
        else:
            return HttpResponseBadRequest("update failed")
    else:
        log.warn('Request with no mapping received raising 404')
        raise Http404()


def set_config(request, uuid, name):
    if request.method == 'PATCH':
        log.debug(f'Config update received for agent {uuid} with config {name}')
        success = update_config(uuid, name)

        if success == 0:
            return HttpResponse("successful update")
        else:
            return HttpResponseBadRequest("Update failed")
    else:
        log.warn('Request with no mapping received raising 404')
        raise Http404()



