import requests
import uuid
import json
import time
import os
import configparser
import win32serviceutil
from apscheduler.schedulers.background import BackgroundScheduler
from enum import Enum
from datetime import datetime
from threading import Thread, Lock

import http_config
import sysmon_config

import sysmon

__config_parser = configparser.ConfigParser()
__config = __config_parser.read('../resources/config.ini')
__auth = (http_config.auth_user, http_config.auth_pass)
__lock = Lock()


class ServiceState(Enum):
    starting = 0
    stopping = 1
    stopped = 2
    running = 3


def run():
    if http_config.agent_uuid is None:
        __setup()
    __heartbeat()


def __setup():
    __config['http']['AgentUUID'] = str(uuid.uuid4())
    response = requests.post(f'{http_config.base_url}{http_config.api_heartbeat}/{http_config.agent_uuid}')
    r_json = json.loads(response.json())

    __config['sysmon']['SysmonVersion'] = r_json['sysmon_version']
    __config['sysmon']['ConfigName'] = r_json['config_name']

    with open('../resources/config.ini', 'w') as config_file:
        __config_parser.write(config_file)


def __heartbeat():
    sysmon_state = __check_sysmon_state()
    if sysmon_state != ServiceState.running:
        now = datetime.now()
        __config['sysmon']['LastRunning'] = now
        sysmon_state_bool = False
        __data = {
            'sysmon_version': sysmon_config.sysmon_version,
            'config_name': sysmon_config.config_name,
            'exec_running': sysmon_state_bool,
            'exec_last_running_at': now
        }
    else:
        sysmon_state_bool = True
        __data = {
            'sysmon_version': sysmon_config.sysmon_version,
            'config_name': sysmon_config.config_name,
            'exec_running': sysmon_state_bool
        }

    response = requests.put(f'{http_config.base_url}{http_config.api_heartbeat}/{http_config.agent_uuid}',
                            auth=__auth,
                            data=__data)
    r_json = json.load(response.json())
    threads = []
    if r_json['updates_needed']['sysmon']:
        threads.append(Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)))
    if r_json['updates_needed']['config']:
        threads.append(Thread(target=__update_config, args=(r_json['updates_needed']['config_name'],)))
    if r_json['restart']:
        win32serviceutil.RestartService(f'sysmon_{sysmon_config.sysmon_version}')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=60)


def __update_sysmon(version):
    response = requests.get(f'{http_config.base_url}{http_config.api_get_sysmon}/{version}')
    with open(f'sysmon_{version}.exe', 'wb') as new_file:
        new_file.write(bytes(response.content))
    sysmon.uninstall_sysmon()
    os.remove(f'sysmon_{sysmon_config.sysmon_version}.exe')
    __config['SysmonVersion'] = version
    __lock.acquire()
    with open('resources/config.ini', 'w') as config_file:
        __config_parser.write(config_file)
    sysmon.install_sysmon()
    __lock.release()


def __update_config(name):
    response = requests.get(f'{http_config.base_url}{http_config.api_get_sysmon}/{name}')
    with open(f'sysmon_config_{name}.xml', 'wb') as new_file:
        new_file.write(bytes(response.content))
    os.remove(f'{sysmon_config.config_file_name}')
    __config['ConfigName'] = name
    __lock.acquire()
    with open('resources/config.ini', 'w') as config_file:
        __config_parser.write(config_file)
    sysmon.update_sysmon_config()
    __lock.release()


def __check_sysmon_state():
    try:
        status = win32serviceutil.QueryServiceStatus(f'sysmon_{sysmon_config.sysmon_version}')
    except:
        return ServiceState.stopped
    else:
        switch = {
            # see https://docs.microsoft.com/en-us/windows/desktop/api/winsvc/ns-winsvc-_service_status for reference
            5: ServiceState.stopping,
            6: ServiceState.stopping,
            7: ServiceState.stopped,
            4: ServiceState.running,
            2: ServiceState.starting,
            3: ServiceState.stopping,
            1: ServiceState.stopped
        }
        return switch[status[1]]
