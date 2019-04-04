from django.http import FileResponse, HttpResponseBadRequest


def get_config(requested_name):
    try:
        imported_file = open(f'../configuration_files/agent_config_{requested_name}.xml', 'rb')
        return FileResponse(imported_file)
    except:
        return HttpResponseBadRequest("config did not exist")


def get_sysmon(requested_version):
    imported_file = open(f'../sysmon/sysmon_{requested_version}.exe', 'rb')
    return FileResponse(imported_file)
