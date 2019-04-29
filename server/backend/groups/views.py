from urllib.parse import unquote_plus

from django.shortcuts import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest, Http404
from .groups_service import create_group
from .groups_service import get_all_groups
from .groups_service import associate_agent_to_group
from .groups_service import update_group
from .groups_service import get_single_group
import json
from logging_service import groups_logging_service as log


def index(request):
    if request.method == 'GET':
        log.debug('Get request received at groups endpoint')
        return JsonResponse(get_all_groups(), safe=False)
    else:
        log.warn('Request with no mapping received raising 404')
        return Http404()


def single_group(request, name):
    decoded_name = unquote_plus(name)
    if request.method == 'GET':
        return JsonResponse(get_single_group(decoded_name), safe=False)
    if request.method == 'POST':
        log.debug('Post request received at groups endpoint')
        success_flag = create_group(decoded_name, json.loads(request.body.decode('utf-8')))
        if success_flag < 0:
            return HttpResponseBadRequest(f"Creation of group {decoded_name} failed")
        else:
            return HttpResponse(f'Creation of group {decoded_name} succeeded')
    if request.method == 'PUT':
        log.debug('Put request received at groups endpoint')
        success_flag = update_group(decoded_name, json.loads(request.body.decode('utf-8')))
        if success_flag < 0:
            return HttpResponseBadRequest(f"Update of group {decoded_name} failed")
        else:
            return HttpResponse(f'Update of group {decoded_name} succeeded')
    else:
        log.warn('Request with no mapping received raising 404')
        return Http404()


def associate(request, agent, group):
    if request.method == 'PATCH':
        log.debug('Patch request received at groups endpoint')
        success_flag = associate_agent_to_group(group, agent)
        if success_flag < 0:
            return HttpResponseBadRequest(f'association of agent {agent} to group {group} failed')
        else:
            return HttpResponse(f'association of agent {agent} to group {group} succeeded')
    else:
        log.warn('Request with no mapping received raising 404')
        return Http404()
