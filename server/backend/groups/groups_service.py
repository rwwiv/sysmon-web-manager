from heartbeat.models import Group, Sysmon, Configuration, Agent
from logging_service import groups_logging_service as log


def create_group(name, json):
    if not Group.objects.exists(name):
        if not Sysmon.objects.exists(VERSION=json.get('sysmon_version', None)):
            log.err(f'Configuration {json.get("sysmon_version", "ERR")} is not on server')
            return -1
        if not Configuration.objects.exists(NAME=json.get('configuration', None)):
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
            f'Group {name} created successfully and is associated with sysmon version {sysmon.version} '
            f'and configuration {config.name}')
        return 1
    else:
        log.err(f'Group with name {name} already exists')
        return -1


def associate_agent_to_group(group_name, agent_uuid):
    if not Agent.objects.exists(agent_uuid) and not Group.objects.exists(group_name):
        agent = Agent.objects.get(UUID=agent_uuid)
        group = Group.objects.get(NAME=group_name)

        agent.GROUP = group
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
