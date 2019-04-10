from django.shortcuts import HttpResponse
from django.http import HttpResponseBadRequest, Http404
from .groups_service import create_group
import json

def index(request, name):
    if request.method == 'POST':
        success_flag = create_group(name,json.loads(request.body.decode('utf-8')))
        if success_flag < 0:
            return HttpResponseBadRequest(f"Creation of group {name} failed")
        else:
            return HttpResponse(f'Creation of group {name} succeded')
    else:
        return Http404()
