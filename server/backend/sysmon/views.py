import json
from django.shortcuts import HttpResponse, Http404
from django.http import JsonResponse, HttpResponseBadRequest
from .sysmon_service import get_all_sysmons
from .sysmon_service import retrieve_and_create_sysmon

def index(request):
    if request.method == 'GET':
        return JsonResponse(get_all_sysmons(), safe=False)
    elif request.method == 'POST':
        if 'sysmon_repo' in json.loads(request.body).keys():
            if retrieve_and_create_sysmon(json.loads(request.body)['sysmon_repo']) >= 0:
                return HttpResponse('Successfully created sysmon')
            else:
                return HttpResponseBadRequest('Something went wrong when retrieving sysmon')
        else:
            return HttpResponseBadRequest('Link for repo not in request')
    else:
        raise Http404()