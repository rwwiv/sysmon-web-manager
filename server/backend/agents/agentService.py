from heartbeat.models import Agent
import json

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
    return data

def update_needs_install(requested_uuid):
    try:
        retrieved_agent = Agent.objects.get(UUID=requested_uuid)
        retrieved_agent.NEEDS_INSTALL = True
        retrieved_agent.ATTEMPTED_INSTALL = True
        retrieved_agent.save()
        return 0
    except:
        return -1