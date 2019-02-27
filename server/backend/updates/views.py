from .updateService import get_config
from .updateService import get_sysmon


def config(request, name):
    config_response = get_config(name)
    return config_response


def sysmon(request, version):
    sysmon_response = get_sysmon(version)
    return sysmon_response
