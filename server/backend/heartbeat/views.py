from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse
from .heartbeatService import updateAgentStatus
from .heartbeatService import createAgent

def index(request, id):
    if(request.method == 'PUT'):
        values = updateAgentStatus(id, request) 
        return JsonResponse(values)
    elif(request.method == 'POST'):
        values = createAgent(id)
        return JsonResponse(values)
    else:
        raise Http404()