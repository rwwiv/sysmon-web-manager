from models.models import Agent
from models.models import Sysmon
from models.models import Configuration
from logging_service import heartbeat_logging_service as log
import json


def build_json_response(retrieved_agent):
    if retrieved_agent.GROUP is None:  # agent has no group
        updates_data = {
            'sysmon': retrieved_agent.SYSMON_VERSION_NEW != retrieved_agent.SYSMON_VERSION_CURRENT,
            'config': retrieved_agent.CONFIG_NAME_NEW != retrieved_agent.CONFIG_NAME_CURRENT,
        }
        if updates_data['sysmon']:
            updates_data['sysmon_version'] = retrieved_agent.SYSMON_VERSION_NEW
        if updates_data['config']:
            updates_data['config_name'] = retrieved_agent.CONFIG_NAME_NEW
    else:
        updates_data = {
            'sysmon': retrieved_agent.GROUP.SYSMON != retrieved_agent.SYSMON_VERSION_CURRENT,
            'config': retrieved_agent.GROUP.CONFIGURATION != retrieved_agent.CONFIG_NAME_CURRENT,
        }
        if updates_data['sysmon']:
            updates_data['sysmon_version'] = retrieved_agent.GROUP.SYSMON
        if updates_data['config']:
            updates_data['config_name'] = retrieved_agent.GROUP.CONFIGURATION
    return {
        'updates_needed': updates_data,
        'uninstall': retrieved_agent.NEEDS_UNINSTALL,
        'restart': retrieved_agent.NEEDS_RESTART,
        'install': retrieved_agent.NEEDS_INSTALL
    }


def update_agent_status(requested_uuid, incoming_request):
    retrieved_agent = Agent.objects.get(UUID=requested_uuid)
    persist_data = json.loads(incoming_request.body)

    if not (persist_data.get('installed', False) or retrieved_agent.NEEDS_INSTALL):
        data = {}
    else:
        if persist_data.get('installed', False):
            retrieved_agent.NEEDS_INSTALL = False
        data = build_json_response(retrieved_agent)

    retrieved_agent.SYSMON_VERSION_CURRENT = persist_data.get('sysmon_version', '')
    retrieved_agent.CONFIG_NAME_CURRENT = persist_data.get('config_name', '')
    retrieved_agent.EXEC_RUNNING = persist_data.get('exec_running', False)
    retrieved_agent.EXEC_LAST_RUNNING_AT = persist_data.get('exec_last_running_at', '')
    retrieved_agent.save()
        
    return data


def create_agent(requested_uuid, remote_addr):
    if Agent.objects.filter(UUID=requested_uuid).count() == 0:
        new_agent = Agent(UUID=requested_uuid,
                          IP_ADDRESS=remote_addr,
                          ONLINE=True,
                          SYSMON_VERSION_CURRENT="",
                          SYSMON_VERSION_NEW="",
                          CONFIG_NAME_CURRENT="",
                          CONFIG_NAME_NEW="",
                          EXEC_RUNNING=False,  # sysmon should not be running when the agent calls in
                          NEEDS_INSTALL=False,
                          NEEDS_UNINSTALL=False,
                          NEEDS_RESTART=False,
                          ATTEMPTED_INSTALL=False)
        new_agent.save()
        log.debug(f'Agent with UUID{requested_uuid} created succesfully')
        return 0
    else:
        log.err('Agent already exists')
        return -1
