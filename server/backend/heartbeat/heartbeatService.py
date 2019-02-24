from heartbeat.models import agent
import json


def get_sysmon_version():
    return "sysmon"


def get_config_name():
    return "example"


def get_sysmon_update_flag():
    return False


def get_config_update_flag():
    return False


def update_agent_status(requested_uuid, incoming_request):
    retrieved_agent = agent.objects.get(UUID=requested_uuid)
    
    updates_data = {
        'sysmon': get_sysmon_update_flag(),
        'sysmon_version': retrieved_agent.SYSMON_VERSION_CURRENT,
        'config': get_config_update_flag(),
        'config_name': retrieved_agent.CONFIG_NAME_CURRENT
    }

    data = {
        'updates_needed': updates_data,
        'uninstall': retrieved_agent.NEEDS_UNINSTALL,
        'restart': retrieved_agent.NEEDS_RESTART,
        'install': retrieved_agent.NEEDS_INSTALL
    }

    persist_data = json.loads(incoming_request.body)
    if('sysmon_version' in persist_data):
        retrieved_agent.SYSMON_VERSION_CURRENT = persist_data['sysmon_version']
    if('config_name' in persist_data):
        retrieved_agent.CONFIG_NAME_CURRENT = persist_data['config_name']
    if('exec_running' in persist_data):
        retrieved_agent.EXEC_RUNNING = persist_data['exec_running']
    if('exec_last_running_at' in persist_data):
        retrieved_agent.EXEC_LAST_RUNNING_AT = persist_data['exec_last_running_at']

    retrieved_agent.save()
    return data


def create_agent(requested_uuid):
    if agent.objects.filter(UUID=requested_uuid).count() == 0:
        new_agent = agent(UUID=requested_uuid,
                          # TODO record the IP address(es) of the origin of the request
                          IPV4_ADDRESS="",
                          IPV6_ADDRESS="",
                          ONLINE=True,
                          SYSMON_VERSION_CURRENT="",
                          SYSMON_VERSION_NEW="",
                          CONFIG_NAME_CURRENT="",
                          CONFIG_NAME_NEW="",
                          EXEC_RUNNING=False,  # sysmon should not be running when the agent calls in
                          NEEDS_UNINSTALL=False,
                          NEEDS_RESTART=False)
        new_agent.save()
    else:
        print("Agent already existed")

    data = {
        'sysmon_version': get_sysmon_version(),
        'config_name': get_config_name()
    }
    return data
