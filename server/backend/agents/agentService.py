from heartbeat.models import agent
import json

def getAllAgents():
    allAgents = agent.objects.all()
    data = []
    for x in allAgents:
        temp = {}
        temp['uuid'] = x.UUID
        temp['online'] = x.ONLINE
        temp['sysmon_version'] = x.SYSMON_VERSION_CURRENT
        temp['config_name'] = x.CONFIG_NAME_CURRENT
        temp['exec_running'] = x.EXEC_RUNNING
        temp['exec_last_running_at'] = x.EXEC_LAST_RUNNING_AT
        data.append(temp)
    return data