from django.shortcuts import HttpResponse

from .multi_service import multi_sysmon_install


def install(request):
    if request.method == 'POST':
        failures = multi_sysmon_install(request)
        if(failures < 0):
                return HttpResponse(f"Multi install failed for {failures * -1} agents selected")
        else:
                return HttpResponse("Multi install succesful")
