import json
from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from .support_service import get_sysmon_versioning_repo_link
from .support_service import get_sysmon_download_link
from .support_service import get_initial_config_download_link
from .support_service import update_sysmon_versioning_repo_link
from .support_service import update_sysmon_download_link
from .support_service import update_initial_config_download_link


def sysmon_version_repo(request):
    if request.method == 'GET':
        link = get_sysmon_versioning_repo_link()
        if link:
            return JsonResponse({'link': link})
        else:
            return HttpResponseBadRequest('Link was empty check support page')
    elif request.method == 'POST':
        request_json = json.loads(request.body)
        if 'link' in request_json.keys():
            success_flag = update_sysmon_versioning_repo_link(request_json['link'])
            if success_flag >= 0:
                return HttpResponse('Successfully updated sysmon versioning repository link')
            else:
                return HttpResponseBadRequest('Failed to update sysmon versioning reposity link')
        else:
            return HttpResponseBadRequest('Malformed JSON link field required')
    else:
        raise Http404()


def sysmon_download(request):
    if request.method == 'GET':
        link = get_sysmon_download_link()
        if link:
            return JsonResponse({'link': link})
        else:
            return HttpResponseBadRequest('Link was empty check support page')
    elif request.method == 'POST':
        request_json = json.loads(request.body)
        if 'link' in request_json.keys():
            success_flag = update_sysmon_download_link(request_json['link'])
            if success_flag >= 0:
                return HttpResponse('Successfully updated sysmon download link')
            else:
                return HttpResponseBadRequest('Failed to update sysmon download link')
        else:
            return HttpResponseBadRequest('Malformed JSON link field required')
    else:
        raise Http404()


def configs_download(request):
    if request.method == 'GET':
        link = get_initial_config_download_link()
        if link:
            return JsonResponse({'link': link})
        else:
            return HttpResponseBadRequest('Link was empty check support page')
    elif request.method == 'POST':
        request_json = json.loads(request.body)
        if 'link' in request_json.keys():
            success_flag = update_initial_config_download_link(request_json['link'])
            if success_flag >= 0:
                return HttpResponse('Successfully updated sysmon config link')
            else:
                return HttpResponseBadRequest('Failed to update sysmon config link')
        else:
            return HttpResponseBadRequest('Malformed JSON link field required')
    else:
        raise Http404()

