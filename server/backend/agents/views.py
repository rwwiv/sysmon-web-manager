from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse
from .agentService import get_all_agents


def index(request):
    if request.method == 'GET':
        values = get_all_agents()
        return JsonResponse(values, safe=False)
    elif request.method == 'POST':
        return HttpResponse("pong")
    else:
        raise Http404()
