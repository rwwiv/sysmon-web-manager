from django.http import FileResponse, HttpResponseBadRequest

from .update_service import get_config
from .update_service import get_sysmon


def config(request, name):
    config_response = get_config(name)
    if config_response != -1:
        return FileResponse(config_response)
    else:
        return HttpResponseBadRequest("Config did not exist.")


def sysmon(request, version):
    sysmon_response = get_sysmon(version)
    if sysmon_response != -1:
        return FileResponse(sysmon_response)
    else:
        return HttpResponseBadRequest("Sysmon version did not exist.")
