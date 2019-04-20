from models.models import Global_Variables


def get_sysmon_versioning_repo_link():
    try:
        variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_versioning_repo')
        return variable.VARIABLE_VALUE
    except:
        return ''

def get_sysmon_download_link():
    try:
        variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_download')
        return variable.VARIABLE_VALUE
    except:
        return ''



def get_initial_config_download_link():
    try:
        variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_config')
        return variable.VARIABLE_VALUE
    except:
        return ''



def update_sysmon_versioning_repo_link(link):
    if Global_Variables.objects.filter(VARIABLE_TYPE='sysmon_versioning_repo').exists():
        try:
            variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_versioning_repo')
            variable.VARIABLE_VALUE = link
            variable.save()
            return 1
        except:
            return -1
    else:
        try:
            new_variable = Global_Variables(VARIABLE_TYPE='sysmon_versioning_repo',
                                            VARIABLE_VALUE=link)
            new_variable.save()
            return 1
        except:
            return -1


def update_sysmon_download_link(link):
    if Global_Variables.objects.filter(VARIABLE_TYPE='sysmon_download').exists():
        try:
            variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_download')
            variable.VARIABLE_VALUE = link
            variable.save()
            return 1
        except:
            return -1
    else:
        try:
            new_variable = Global_Variables(VARIABLE_TYPE='sysmon_download',
                                            VARIABLE_VALUE=link)
            new_variable.save()
            return 1
        except:
            return -1


def update_initial_config_download_link(link):
    if Global_Variables.objects.filter(VARIABLE_TYPE='sysmon_config').exists():
        try:
            variable = Global_Variables.objects.get(VARIABLE_TYPE='sysmon_config')
            variable.VARIABLE_VALUE = link
            variable.save()
            return 1
        except:
            return -1
    else:
        try:
            new_variable = Global_Variables(VARIABLE_TYPE='sysmon_config',
                                            VARIABLE_VALUE=link)
            new_variable.save()
            return 1
        except:
            return -1

