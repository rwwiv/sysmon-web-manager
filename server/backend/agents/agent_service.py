from models.models import Agent, Configuration, Sysmon
from logging_service import agents_logging_service as log


def get_all_agents():
    agents = Agent.objects.all()
    data = []
    for agent in agents:
        temp = {
            'uuid': agent.UUID,
            'ip_address': agent.IP_ADDRESS,
            'online': agent.ONLINE,
            'sysmon_version_current': agent.SYSMON_VERSION_CURRENT,
            'sysmon_version_new': agent.SYSMON_VERSION_NEW,
            'config_name_current': agent.CONFIG_NAME_CURRENT,
            'config_name_new': agent.CONFIG_NAME_NEW,
            'exec_running': agent.EXEC_RUNNING,
            'exec_last_running_at': agent.EXEC_LAST_RUNNING_AT,
            'needs_install': agent.NEEDS_INSTALL,
            'new_agent': not agent.ATTEMPTED_INSTALL,
        }
        if agent.GROUP is not None:
            temp['group'] = agent.GROUP.NAME
        data.append(temp)
    log.debug(f"{len(data)} agents retrieved")
    return data


def update_needs_install(requested_uuid):
    if Sysmon.objects.filter(IS_CURRENT=True).exists() and Configuration.objects.filter(IS_DEFAULT=True).exists():
        try:
            retrieved_agent = Agent.objects.get(UUID=requested_uuid)
            retrieved_agent.NEEDS_INSTALL = True
            retrieved_agent.ATTEMPTED_INSTALL = True
            retrieved_agent.NEEDS_RESTART = False
            retrieved_agent.NEEDS_UNINSTALL = False
            retrieved_agent.save()
            log.debug(f"Agent {requested_uuid} needs install flag updated")
            return 1
        except:
            log.err(f"Failed to update needs install flag for {requested_uuid}")
            return -1
    else:
        return 0

def update_needs_restart(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_RESTART = True
        retrieved_agent.NEEDS_INSTALL = False
        retrieved_agent.NEEDS_UNINSTALL = False
        retrieved_agent.save()
        log.debug(f"Agent {requested_uuid} needs restart flag updated")
        return 0
    except:
        log.err(f"Failed to update needs restart flag for {requested_uuid}")
        return -1


def update_needs_uninstall(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_UNINSTALL = True
        retrieved_agent.ATTEMPTED_INSTALL = False
        retrieved_agent.NEEDS_INSTALL = False
        retrieved_agent.NEEDS_RESTART = False
        retrieved_agent.save()
        log.debug(f"Agent {requested_uuid} needs uninstall flag updated")
        return 0
    except:
        log.err(f"Failed to update needs uninstall flag for {requested_uuid}")
        return -1


def update_config(uuid, name):
    try:
        retrieved_agent = Agent.objects.get(UUID=uuid)
        retrieved_config = Configuration.objects.get(NAME=name)
        retrieved_agent.CONFIG_NAME_NEW = retrieved_config.NAME
        retrieved_agent.save()
        log.debug(f"Agent {uuid} configuration set to {name}")
        return 0
    except:
        log.err(f"Failed to associate {name} config to agent {uuid}")
        return -1
