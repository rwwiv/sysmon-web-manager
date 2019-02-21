from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse
from .agentService import getAllAgents

def index(request):
    if(request.method == 'GET'):
        values = getAllAgents() 
        return JsonResponse(values, safe=False)
    elif(request.method == 'POST'):
        return HttpResponse("pong")
    else:
        raise Http404()