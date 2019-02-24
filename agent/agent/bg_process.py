import requests
import uuid
import json
import os
import win32serviceutil
import yaml
from datetime import datetime
from threading import Thread, Lock


from agent_config import env_config, env_config_filepath, user_config


from sysmon import ServiceState, \
            update_sysmon_config, \
            install_sysmon, \
            uninstall_sysmon, \
            check_sysmon_state

__auth = (user_config['http']['auth_user'], user_config['http']['auth_pass'])
__lock = Lock()
__protocol = "http"


def run():
    if env_config['http']['uuid'] is None:
        __setup()
    __heartbeat()


def __setup():
    env_config['http']['uuid'] = str(uuid.uuid4())
    response = requests.post(f'{__protocol}://{user_config["http"]["url"]}'
                             f'{env_config["http"]["api"]["heartbeat"]}'
                             f'/{env_config["http"]["uuid"]}')
    r_json = response.json()
    with open(env_config_filepath, 'w') as env_config_file:
        yaml.dump(env_config, env_config_file)
    env_config['agent']['sysmon_version'] = r_json['sysmon_version']
    env_config['agent']['config_name'] = r_json['config_name']
    with open(env_config_filepath, 'w') as env_config_file:
        yaml.dump(env_config, env_config_file)


def __heartbeat():
    if check_sysmon_state() != ServiceState.running:
        if not env_config['agent']['checked_exec_running']:
            time_stopped = datetime.now()
            env_config['agent']['exec_last_running'] = time_stopped
            env_config['agent']['checked_exec_running'] = True
            with open(env_config_filepath, 'w') as env_config_file:
                yaml.dump(env_config, env_config_file)
        else:
            time_stopped = env_config['agent']['exec_last_running']
        sysmon_state_bool = False
        __data = {
            'sysmon_version': env_config['agent']['sysmon_version'],
            'config_name': env_config['agent']['config_name'],
            'exec_running': sysmon_state_bool,
            'exec_last_running_at': time_stopped
        }
    else:
        sysmon_state_bool = True
        env_config['http']['checked_exec_running'] = False
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __data = {
            'sysmon_version': env_config['agent']['sysmon_version'],
            'config_name': env_config['agent']['config_name'],
            'exec_running': sysmon_state_bool
        }
    print(__data)
    response = requests.put(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["heartbeat"]}'
                            f'/{env_config["http"]["uuid"]}',
                            auth=__auth,
                            data=__data)
    r_json = response.json()
    threads = []
    if r_json['updates_needed']['sysmon']:
        threads.append(Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)))
    if r_json['updates_needed']['config']:
        threads.append(Thread(target=__update_config, args=(r_json['updates_needed']['config_name'],)))
    if r_json['restart']:
        win32serviceutil.RestartService(f'sysmon_{env_config["agent"]["sysmon_version"]}')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=60)


def __update_sysmon(version):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["updates"]["sysmon"]}'
                            f'/{version}')
    with open(f'sysmon_{version}.exe', 'wb') as new_file:
        new_file.write(bytes(response.content))
    uninstall_sysmon()
    os.remove(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe')
    env_config["agent"]["sysmon_version"] = version
    __lock.acquire()
    with open(env_config_filepath, 'w') as env_config_file:
        yaml.dump(env_config, env_config_file)
    install_sysmon()
    __lock.release()


def __update_config(name):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["updates"]["config"]}'
                            f'/{name}')
    with open(f'agent_config_{name}.xml', 'wb') as new_file:
        new_file.write(bytes(response.content))
    os.remove(f'agent_config_{env_config["agent"]["config_name"]}.xml')
    env_config["agent"]["config_name"] = name
    __lock.acquire()
    with open(env_config_filepath, 'w') as env_config_file:
        yaml.dump(env_config, env_config_file)
    update_sysmon_config()
    __lock.release()
