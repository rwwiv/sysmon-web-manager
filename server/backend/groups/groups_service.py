from models.models import Group, Sysmon, Configuration, Agent
from logging_service import groups_logging_service as log


def create_group(name, json):
    if not Group.objects.filter(NAME=name).exists():
        if not Sysmon.objects.filter(VERSION=json.get('sysmon_version')).exists():
            log.err(f'Sysmon version {json.get("sysmon_version", "ERR")} is not on server')
            return -1
        if not Configuration.objects.filter(NAME=json.get('configuration')).exists():
            log.err(f'Configuration {json.get("configuration", "ERR")} is not on server')
            return -1
        if json.get('sysmon_version', False):
            sysmon = Sysmon.objects.get(VERSION=json.get('sysmon_version'))
        else:
            log.err('Sysmon version not in json object')
            return -1
        if json.get('configuration', False):
            config = Configuration.objects.get(NAME=json.get('configuration'))
        else:
            log.err('Config name not in json object')
            return -1
        new_group = Group(NAME=name,
                          CONFIGURATION=config,
                          SYSMON=sysmon)
        new_group.save()
        log.debug(
            f'Group {name} created successfully and is associated with sysmon version {sysmon} '
            f'and configuration {config}')
        return 1
    else:
        log.err(f'Group with name {name} already exists')
        return -1


def associate_agent_to_group(group_name, agent_uuid):
    if Agent.objects.filter(UUID=agent_uuid).exists() and Group.objects.filter(NAME=group_name).exists():
        agent = Agent.objects.get(UUID=agent_uuid)
        group = Group.objects.get(NAME=group_name)

        agent.GROUP = group
        agent.CONFIG_NAME_NEW = group.CONFIGURATION.NAME
        agent.SYSMON_VERSION_NEW = group.SYSMON.VERSION
        agent.save()
        log.debug(f'associated agent{agent_uuid} with group {group_name}')
        return 1
    else:
        log.err(f'failed to associated agent{agent_uuid} with group {group_name}')
        return -1


def get_all_groups():
    groups = Group.objects.all()
    data = []
    for group in groups:
        temp = {
            'name': group.NAME,
            'configuration': group.CONFIGURATION.NAME,
            'sysmon': group.SYSMON.VERSION
        }  
        data.append(temp)
    log.debug(f'{len(data)} groups retrieved')
    return data


def get_single_group(name):
    if Group.objects.filter(NAME=name).exists():
        group = Group.objects.get(NAME=name)
        return {
            'configuration': group.CONFIGURATION.NAME,
            'sysmon': group.SYSMON.VERSION
        }


def update_group(name, json):
    if Group.objects.filter(NAME=name).exists():
        if not Sysmon.objects.filter(VERSION=json.get('sysmon_version')).exists():
            log.err(f'Sysmon version {json.get("sysmon_version", "ERR")} is not on server')
            return -1
        if not Configuration.objects.filter(NAME=json.get('configuration')).exists():
            log.err(f'Configuration {json.get("configuration", "ERR")} is not on server')
            return -1
        if json.get('sysmon_version', False):
            sysmon = Sysmon.objects.get(VERSION=json.get('sysmon_version'))
        else:
            log.err('Sysmon version not in json object')
            return -1
        if json.get('configuration', False):
            config = Configuration.objects.get(NAME=json.get('configuration'))
        else:
            log.err('Config name not in json object')
            return -1
        group = Group.objects.get(NAME=name)
        group.CONFIGURATION = config
        group.SYSMON = sysmon
        group.save()
        log.debug(
            f'Group {name} updated successfully and is associated with sysmon version {sysmon} '
            f'and configuration {config}')
        return 1
    else:
        log.err(f'Group with name {name} does not exist')
        return -1

