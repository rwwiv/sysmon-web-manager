from heartbeat.models import Agent
import json
from agents.agentService import update_needs_install
from agents.agentService import update_needs_uninstall
from agents.agentService import update_needs_restart
from agents.agentService import update_config

def multi_sysmon_install(UUIDs):
    string_uuids = str(UUIDs.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_install(uuid_string[1:-1])
    return success_flag

def multi_sysmon_uninstall(UUIDs):
    string_uuids = str(UUIDs.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_uninstall(uuid_string[1:-1])
    return success_flag


def multi_sysmon_restart(UUIDs):
    string_uuids = str(UUIDs.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_restart(uuid_string[1:-1])
    return success_flag
    

def multi_config_set(UUIDs, config):
    string_uuids = str(UUIDs.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_config(uuid_string[1:-1], config)
    return success_flag