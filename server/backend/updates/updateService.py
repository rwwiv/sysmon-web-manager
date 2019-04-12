from django.http import FileResponse, HttpResponseBadRequest
from logging_service import updates_logging_service as log


def get_config(requested_name):
    try:
        imported_file = open(f'../configuration_files/agent_config_{requested_name}.xml', 'rb')
        log.debug(f'Configuration {requested_name} retrieved')
        return FileResponse(imported_file)
    except:
        log.err(f'Configuration {requested_name} could not be retrieved')
        return HttpResponseBadRequest("config did not exist")


def get_sysmon(requested_version):
    try:
        imported_file = open(f'../sysmon/sysmon_{requested_version}.exe', 'rb')
        log.debug(f'Sysmon version {requested_version} retrieved')
        return FileResponse(imported_file)
    except:
        log.err(f'Sysmon version {requested_version} could not be retrieved')
        return HttpResponseBadRequest("Sysmon version did not exist")