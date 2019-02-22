from heartbeat.models import agent
import json

def getSysmonVersion():
    return "ExampleSysmonVersion"

def getConfigName():
    return "ExampleConfigName"

def getSysmonUpdateFlag():
    return False

def getConfigUpdateFlag():
    return False

def updateAgentStatus(requestedUUID, incomingRequest):
    retrievedAgent = agent.objects.get(UUID=requestedUUID)
    
    updatesData = {}
    updatesData ['sysmon'] = getSysmonUpdateFlag()
    updatesData ['sysmon_version'] = retrievedAgent.SYSMON_VERSION_CURRENT
    updatesData ['config'] = getConfigUpdateFlag()
    updatesData ['config_name'] = retrievedAgent.CONFIG_NAME_CURRENT

    data = {}
    data ['updates_needed'] = updatesData
    data ['uninstall'] = retrievedAgent.NEEDS_UNINSTALL
    data ['restart'] = retrievedAgent.NEEDS_RESTART

    persistData = json.loads(incomingRequest.body)
    retrievedAgent.SYSMON_VERSION_CURRENT = persistData['sysmon_version']
    retrievedAgent.CONFIG_NAME_CURRENT = persistData['config_name']
    retrievedAgent.EXEC_RUNNING = persistData['exec_running']
    retrievedAgent.EXEC_LAST_RUNNING_AT = persistData['exec_last_running_at']

    retrievedAgent.save()
    return data

def createAgent(requestedUUID):

    if(agent.objects.filter(UUID=requestedUUID).count() == 0):
        newAgent = agent(UUID = requestedUUID,
        IPV4_ADDRESS = "",
        IPV6_ADDRESS = "",
        ONLINE = True,
        SYSMON_VERSION_CURRENT = "",
        SYSMON_VERSION_NEW = "",
        CONFIG_NAME_CURRENT = "",
        CONFIG_NAME_NEW = "",
        EXEC_RUNNING = True)
        newAgent.save()
    else:
        print("Agent already existed")

    
    
    data = {}
    data ['sysmon_version'] = getSysmonVersion()
    data ['config_name'] = getConfigName()

    return data