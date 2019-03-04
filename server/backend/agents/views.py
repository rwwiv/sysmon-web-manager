from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from .agentService import get_all_agents
from .agentService import  update_needs_install
from .agentService import update_needs_restart

def index(request):
    if request.method == 'GET':
        values = get_all_agents()
        return JsonResponse(values, safe=False)
    elif request.method == 'POST':
        return HttpResponse("pong")

    else:
        raise Http404()


def updates(request,uuid):
    if request.method == 'PATCH':
        success =  update_needs_install(uuid)
        if(success == 0):
            return HttpResponse("succesful update")
        else:
            return HttpResponseBadRequest("update failed")
    elif request.method == 'POST':
        success = update_needs_restart(uuid)
        if(success == 0):
            return HttpResponse("succesful update")
        else:
            return HttpResponseBadRequest("update failed")

