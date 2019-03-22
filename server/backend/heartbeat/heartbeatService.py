from heartbeat.models import Agent
from heartbeat.models import Sysmon
from heartbeat.models import Configuration
from logging_service import heartbeat_logging_service as log
from os import listdir
import json
import ipaddress


def get_sysmon_version():
    # return Sysmon.objects.get(IS_CURRENT=True)
    return "8.04"


def get_config_name():
    # return Configuration.objects.get(IS_DEFAULT=True)
    return "gifnoc"


def get_sysmon_update_flag(server_version, client_version):
    return client_version != server_version


def get_config_update_flag(server_version, client_version):
    return client_version != server_version


def update_agent_status(requested_uuid, incoming_request):
    retrieved_agent = Agent.objects.get(UUID=requested_uuid)
    persist_data = json.loads(incoming_request.body)
    
    if persist_data.get('installed', False):
        retrieved_agent.NEEDS_INSTALL = False
        updates_data = {
            'sysmon': get_sysmon_update_flag(retrieved_agent.SYSMON_VERSION_NEW, retrieved_agent.SYSMON_VERSION_CURRENT),
            'config': get_config_update_flag(retrieved_agent.CONFIG_NAME_NEW, retrieved_agent.CONFIG_NAME_CURRENT),
        }
        if updates_data['sysmon']:
            updates_data['sysmon_verion'] = retrieved_agent.SYSMON_VERSION_NEW
        if updates_data['config']:
            updates_data['config_name'] = retrieved_agent.CONFIG_NAME_NEW
        data = {
            'updates_needed': updates_data,
            'uninstall': retrieved_agent.NEEDS_UNINSTALL,
            'restart': retrieved_agent.NEEDS_RESTART,
            'install': retrieved_agent.NEEDS_INSTALL
        }
    elif retrieved_agent.NEEDS_INSTALL:
        updates_data = {
            'sysmon': get_sysmon_update_flag(retrieved_agent.SYSMON_VERSION_NEW, retrieved_agent.SYSMON_VERSION_CURRENT),
            'sysmon_version': retrieved_agent.SYSMON_VERSION_NEW.NAME,
            'config': get_config_update_flag(retrieved_agent.CONFIG_NAME_NEW, retrieved_agent.CONFIG_NAME_CURRENT),
            'config_name': retrieved_agent.CONFIG_NAME_NEW.NAME
        }
        data = {
            'updates_needed': updates_data,
            'uninstall': retrieved_agent.NEEDS_UNINSTALL,
            'restart': retrieved_agent.NEEDS_RESTART,
            'install': retrieved_agent.NEEDS_INSTALL
        }
    else:
        data = {}

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
                          SYSMON_VERSION_NEW=get_sysmon_version(),
                          CONFIG_NAME_CURRENT="",
                          CONFIG_NAME_NEW=get_config_name(),
                          EXEC_RUNNING=False,  # sysmon should not be running when the agent calls in
                          NEEDS_INSTALL=False,
                          NEEDS_UNINSTALL=False,
                          NEEDS_RESTART=False,
                          ATTEMPTED_INSTALL=False)
        new_agent.save()
        log.debug(f'Agent with UUID{requested_uuid} created succesfully')
    else:
        log.err('Agent already exists')

    data = {
        'sysmon_version': get_sysmon_version(),
        'config_name': get_config_name()
        # 'sysmon_version': get_sysmon_version().NAME,
        # 'config_name': get_config_name().NAME
    }
    return data
