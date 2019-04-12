from heartbeat.models import Group, Sysmon, Configuration, Agent
from logging_service import groups_logging_service as log

def create_group(name, json):
    try:
        group = Group.objects.get(NAME=name)
        log.err(f'Group {name} already exists')
        return -1
        
    except Exception as e:
        try:
            sysmon = Sysmon.objects.get(VERSION = json['sysmon_version'])
            try:
                config = Configuration.objects.get(NAME = json['configuration'])
                new_group = Group(NAME = name,
                                  CONFIGURATION = config,
                                  SYSMON = sysmon)
                new_group.save()
                log.debug(f'Group {name} created succesfully and is associated with sysmon version {sysmon.version} and configuration {config.name}')
                return 1
            except Exception as e:
                log.err(f'Configuration {config.name} is not on server')
                return -1
        except Exception as e:
            log.err(f'sysmon version {sysmon.version} is not on server')
            return -1


def associate_agent_to_group(group_name, agent_uuid):
    try:
        agent = Agent.objects.get(UUID=agent_uuid)
        group = Group.objects.get(NAME=group_name)

        agent.GROUP = group
        agent.save()
        log.debug(f'associated agent{agent_uuid} with group {group_name}')
        return 1
    except:
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
    
        