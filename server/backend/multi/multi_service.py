from agents.agent_service import update_needs_install


def multi_sysmon_install(UUIDs):
    string_uuids = str(UUIDs.body)
    string_uuids = string_uuids[3:-2]
    success_flag = 0
    for uuid_string in string_uuids.split(','):
        success_flag += update_needs_install(uuid_string[1:-1])
    return success_flag
