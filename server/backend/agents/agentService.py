from heartbeat.models import Agent


def get_all_agents():
    all_agents = Agent.objects.all()
    data = []
    for x in all_agents:
        temp = {
            'uuid': x.UUID,
            'online': x.ONLINE,
            'sysmon_version': x.SYSMON_VERSION_CURRENT,
            'config_name': x.CONFIG_NAME_CURRENT,
            'exec_running': x.EXEC_RUNNING,
            'exec_last_running_at': x.EXEC_LAST_RUNNING_AT
        }
        data.append(temp)
    return data
