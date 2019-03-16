from heartbeat.models import Agent
import json
from logging_service import agents_logging_service as log

def get_all_agents():
    all_agents = Agent.objects.all()
    data = []
    for x in all_agents:
        temp = {
            'uuid': x.UUID,
            'ip_address': x.IP_ADDRESS,
            'online': x.ONLINE,
            'sysmon_version_current': x.SYSMON_VERSION_CURRENT,
            'sysmon_version_new': x.SYSMON_VERSION_NEW,
            'config_name_current': x.CONFIG_NAME_CURRENT,
            'config_name_new': x.CONFIG_NAME_NEW,
            'exec_running': x.EXEC_RUNNING,
            'exec_last_running_at': x.EXEC_LAST_RUNNING_AT,
            'needs_install': x.NEEDS_INSTALL,
            'new_agent': not x.ATTEMPTED_INSTALL
        }
        data.append(temp)
    log.debug(f"{len(data)}agents retrieved")
    return data


def update_needs_install(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_INSTALL = True
        retrieved_agent.ATTEMPTED_INSTALL = True
        retrieved_agent.save()
        return 0
    except:
        log.err(f"Failed to update needs install flag for {requested_uuid}")
        return -1


def update_needs_restart(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_RESTART = True
        retrieved_agent.save()
        return 0
    except:
        log.err(f"Failed to update needs restart flag for {requested_uuid}")
        return -1

def update_needs_uninstall(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_UNINSTALL = True
        retrieved_agent.save()
        return 0
    except:
        log.err(f"Failed to update needs uninstall flag for {requested_uuid}")
        return -1