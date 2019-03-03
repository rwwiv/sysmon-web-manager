from django.http import FileResponse


def get_config(requested_name):
    imported_file = open(f'../configurations/agent_config_{requested_name}.xml', 'rb')
    return FileResponse(imported_file)


def get_sysmon(requested_version):
    imported_file = open(f'../sysmon/sysmon_{requested_version}.exe', 'rb')
    return FileResponse(imported_file)
