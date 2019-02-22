from django.shortcuts import HttpResponse
from .updateService import getConfig
from .updateService import getSysmon

def config(request, name):
    configResponse = getConfig(name)
    return configResponse

def sysmon(request, version):
    sysmonResponse = getSysmon(version)
    return sysmonResponse
