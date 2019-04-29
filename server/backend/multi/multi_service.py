from agents.agent_service import update_needs_install
from agents.agent_service import update_needs_uninstall
from agents.agent_service import update_needs_restart
from agents.agent_service import update_config


def multi_sysmon_install(uuids):
    string_uuids = str(uuids.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_install(uuid_string[1:-1])
    return success_flag


def multi_sysmon_uninstall(uuids):
    string_uuids = str(uuids.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_uninstall(uuid_string[1:-1])
    return success_flag


def multi_sysmon_restart(uuids):
    string_uuids = str(uuids.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_restart(uuid_string[1:-1])
    return success_flag
    

def multi_config_set(uuids, config):
    string_uuids = str(uuids.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_config(uuid_string[1:-1], config)
    return success_flag
