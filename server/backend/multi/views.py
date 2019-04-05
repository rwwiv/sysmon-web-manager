from django.shortcuts import HttpResponse
from django.http import Http404, JsonResponse,HttpResponseBadRequest
from .multiService import multi_sysmon_install
from .multiService import multi_sysmon_uninstall
from .multiService import multi_sysmon_restart

def install(request):
    if request.method == 'POST':
        failures = multi_sysmon_install(request)
        if(failures < 0):
            return HttpResponse(f"Multi install failed for {failures * -1} agents selected")
        else:
            return HttpResponse("Multi install succesful")


def uninstall(request):
    if request.method == 'POST':
        failures = multi_sysmon_uninstall(request)
        if(failures < 0):
            return HttpResponse(f'Multi uninstall failed for {failures * -1} agents selected')
        else:
            return HttpResponse("Multi uninstall succesful")


def restart(request):
    if request.method == 'POST':
        failures = multi_sysmon_restart(request)
        if(failures < 0):
            return HttpResponse(f'Multi restart failed for {failures * -1} agents selected')
        else:
            return HttpResponse("Multi restart successful")
