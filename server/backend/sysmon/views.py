import json
from django.shortcuts import HttpResponse, Http404
from django.http import JsonResponse, HttpResponseBadRequest
from .sysmon_service import get_all_sysmons
from .sysmon_service import retrieve_and_create_sysmon

def index(request):
    if request.method == 'GET':
        return JsonResponse(get_all_sysmons(), safe=False)
    elif request.method == 'POST':
        if retrieve_and_create_sysmon() >= 0:
            return HttpResponse('Successfully created sysmon')
        else:
            return HttpResponseBadRequest('Something went wrong when retrieving sysmon')
    else:
        raise Http404()
