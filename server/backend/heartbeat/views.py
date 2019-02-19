from django.shortcuts import HttpResponse
from django.http import Http404

def index(request, id):
    if(request.method == 'PUT'):
        sysmon_version = 'sysmon_version'
        config_name = 'config name'
        exec_running = True
        exec_last_running_at = '2019-02-17T14:27:39.129Z'
        return HttpResponse(f"Put request with id {id} recieved \n and request params sysmon_version {sysmon_version} config_name {config_name} exec_running {exec_running} exec_last_running_at {exec_last_running_at}")
    elif(request.method == 'GET'):
        return HttpResponse(f"Get request with id {id} revieved")
    else:
        raise Http404()