from django.shortcuts import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest, Http404
from .groups_service import create_group
from .groups_service import get_all_groups
from .groups_service import associate_agent_to_group
import json
from logging_service import groups_logging_service as log

def index(request):
    if request.method == 'GET':
        return JsonResponse(get_all_groups(), safe=False)
    else:
        log.warn('Request with no mapping recieved raising 404')
        return Http404()

def creation(request, name):
    if request.method == 'POST':
        success_flag = create_group(name,json.loads(request.body.decode('utf-8')))
        if success_flag < 0:
            return HttpResponseBadRequest(f"Creation of group {name} failed")
        else:
            return HttpResponse(f'Creation of group {name} succeded')
    else:
        log.warn('Request with no mapping recieved raising 404')
        return Http404()


def associate(request, agent, group):
    if request.method == 'PATCH':
        success_flag = associate_agent_to_group(group, agent)
        if success_flag < 0:
            return HttpResponseBadRequest(f'association of agent {agent} to group {group} failed')
        else:
            return HttpResponse(f'association of agent {agent} to group {group} succeded')
    else:
        log.warn('Request with no mapping recieved raising 404')
        return Http404()