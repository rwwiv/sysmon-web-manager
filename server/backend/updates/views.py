from django.shortcuts import HttpResponse

def config(request):
    return HttpResponse("Updates/config endpoint")

def sysmon(request):
    return HttpResponse("Updates/sysmon endpoint")
