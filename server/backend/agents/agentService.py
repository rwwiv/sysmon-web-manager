from heartbeat.models import Agent


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
            'exec_last_running_at': x.EXEC_LAST_RUNNING_AT
        }
        data.append(temp)
    return data
