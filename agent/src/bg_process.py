import requests
import uuid
import json
import os
import win32serviceutil
from datetime import datetime
from threading import Thread, Lock


from agent_config import config_parser, config
import agent_config


from sysmon import ServiceState, \
            update_sysmon_config, \
            install_sysmon, \
            uninstall_sysmon, \
            check_sysmon_state

__auth = (config.auth_user, config.auth_pass)
__lock = Lock()


def run():
    if agent_config.uuid is None:
        __setup()
    __heartbeat()


def __setup():
    config['http']['AgentUUID'] = str(uuid.uuid4())
    response = requests.post(f'{agent_config.url}{agent_config.api_heartbeat}/{agent_config.uuid}')
    r_json = json.loads(response.json())

    config['sysmon']['SysmonVersion'] = r_json['sysmon_version']
    config['sysmon']['ConfigName'] = r_json['agent_config']

    with open(config.config_file, 'w') as config_file:
        config_parser.write(config_file)


def __heartbeat():
    if check_sysmon_state() != ServiceState.running:

        now = datetime.now()
        config['sysmon']['LastRunning'] = now
        sysmon_state_bool = False
        __data = {
            'sysmon_version': agent_config.sysmon_version,
            'agent_config': agent_config.sysmon_config,
            'exec_running': sysmon_state_bool,
            'exec_last_running_at': now
        }
    else:
        sysmon_state_bool = True
        __data = {
            'sysmon_version': agent_config.sysmon_version,
            'agent_config': agent_config.sysmon_config,
            'exec_running': sysmon_state_bool
        }

    response = requests.put(f'{agent_config.url}{agent_config.api_heartbeat}/{agent_config.uuid}',
                            auth=__auth,
                            data=__data)
    r_json = json.load(response.json())
    threads = []
    if r_json['updates_needed']['sysmon']:
        threads.append(Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)))
    if r_json['updates_needed']['config']:
        threads.append(Thread(target=__update_config, args=(r_json['updates_needed']['agent_config'],)))
    if r_json['restart']:
        win32serviceutil.RestartService(f'sysmon_{agent_config.sysmon_version}')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=60)


def __update_sysmon(version):
    response = requests.get(f'{agent_config.url}{agent_config.api_get_sysmon}/{version}')
    with open(f'sysmon_{version}.exe', 'wb') as new_file:
        new_file.write(bytes(response.content))
    uninstall_sysmon()
    os.remove(f'sysmon_{agent_config.sysmon_version}.exe')
    config['SysmonVersion'] = version
    __lock.acquire()
    with open('conf/config.ini', 'w') as config_file:
        config_parser.write(config_file)
    install_sysmon()
    __lock.release()


def __update_config(name):
    response = requests.get(f'{agent_config.url}{agent_config.api_get_sysmon}/{name}')
    with open(f'agent_config_{name}.xml', 'wb') as new_file:
        new_file.write(bytes(response.content))
    os.remove(f'{agent_config.sysmon_config_file}')
    config['ConfigName'] = name
    __lock.acquire()
    with open('conf/config.ini', 'w') as config_file:
        config_parser.write(config_file)
    update_sysmon_config()
    __lock.release()
