from django.shortcuts import HttpResponse
from .updateService import getConfig
from .updateService import getSysmon

def config(request, name):
    return HttpResponse("Updates/config endpoint")

def sysmon(request, version):
    return HttpResponse("Updates/sysmon endpoint")
