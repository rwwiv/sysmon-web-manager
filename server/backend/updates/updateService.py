from django.http import FileResponse

def getConfig(requestedName):
    
    imported_file = open(f'../configurations/{requestedName}.xml')
    return FileResponse(imported_file)

def getSysmon(requestedVersion):
    imported_file = open(f'../sysmon/{requestedVersion}.exe')
    return FileResponse(imported_file)
