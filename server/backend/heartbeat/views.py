from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse
from .heartbeatService import update_agent_status
from .heartbeatService import create_agent

def index(request, id):
    if(request.method == 'PUT'):
        values = update_agent_status(id, request)
        return JsonResponse(values)
    elif(request.method == 'POST'):
        values = create_agent(id)
        return JsonResponse(values)
    else:
        raise Http404()