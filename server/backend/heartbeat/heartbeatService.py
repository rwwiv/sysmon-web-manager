from heartbeat.models import agent
import json

def getSysmonVersion():
    return "ExampleSysmonVersion"

def getConfigName():
    return "ExampleConfigName"

def updateAgentStatus(UUID):
    return

def createAgent(requestedUUID):
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
    
    data = {}
    data ['sysmon_version'] = getSysmonVersion()
    data ['config_name'] = getConfigName()

    return data