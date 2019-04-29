import requests
import uuid
import os
import win32serviceutil
import yaml
from threading import Thread, Lock

from agent_config import env_config, env_config_filepath, user_config

from sysmon import update_sysmon_config, \
    install_sysmon, \
    uninstall_sysmon, \
    check_sysmon_running

__auth = (user_config['http']['auth_user'], user_config['http']['auth_pass'])
__env_config_lock = Lock()
__config_lock = Lock()
__sysmon_lock = Lock()
__protocol = "http"

__env_config_agent = env_config['agent']
__env_config_api = env_config['api']
__env_config_sysmon = env_config['sysmon']
__env_config_testing = env_config['testing']


def __write_yaml():
    with open(env_config_filepath, 'w') as env_config_file:
        yaml.dump(env_config, env_config_file)


def run():
    if __env_config_agent['uuid'] is None:
        try:
            __setup()
            __env_config_api['retry'] = 0
            __write_yaml()
        except ConnectionError:
            print('Could not reach server, trying again.')
            __env_config_api['retry'] += 1
            __write_yaml()
    try:
        __heartbeat()
        __env_config_api['retry'] = 0
        __write_yaml()
    except ConnectionError:
        print('Could not reach server, trying again.')
        __env_config_api['retry'] += 1
        __write_yaml()


def testing_run():
    if __env_config_testing['config_built']:
        try:
            __heartbeat()
            __env_config_api['retry'] = 0
            __write_yaml()
        except ConnectionError:
            print('Could not reach server, trying again.')
            __env_config_api['retry'] += 1
            __write_yaml()
            pass
    else:
        __build_initial_config()
        __env_config_testing['config_built'] = True
        __write_yaml()
        try:
            __setup()
            __env_config_api['retry'] = 0
            __write_yaml()
        except ConnectionError:
            print('Could not reach server, trying again.')
            __env_config_api['retry'] += 1
            __write_yaml()
            pass


def __setup():
    requests.post(f'{__protocol}://{user_config["http"]["url"]}'
                  f'{__env_config_api["heartbeat"]}'
                  f'/{__env_config_agent["uuid"]}')


def __build_initial_config():
    __env_config_agent['uuid'] = str(uuid.uuid4())
    __env_config_agent['checked_exec_running'] = False
    __env_config_sysmon['config_name'] = None
    __env_config_sysmon['version'] = None
    __env_config_sysmon['installed'] = False
    __write_yaml()


def __build_request_dict():
    __data = {
        'installed': __env_config_sysmon['installed']
    }
    if not __env_config_sysmon['installed']:
        return __data
    if not check_sysmon_running():
        __data['exec_running'] = False
        __data['exec_last_running_at'] = __env_config_agent['exec_last_running']
    else:
        __env_config_agent['checked_exec_running'] = False
        __write_yaml()
        __data['exec_running'] = True
    if __env_config_agent['sysmon_version'] is not None:
        __data['sysmon_version'] = __env_config_agent['sysmon_version']
    if __env_config_agent['config_name'] is not None:
        __data['config_name'] = __env_config_agent['config_name']
    return __data


def __heartbeat():
    response = requests.put(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{__env_config_api["heartbeat"]}'
                            f'/{__env_config_agent["uuid"]}',
                            # auth=__auth,
                            json=__build_request_dict())
    r_json = response.json()
    if r_json.get('install', False):
        if r_json['updates_needed']['sysmon'] and r_json['updates_needed']['config']:
            __initial_install(r_json['updates_needed']['sysmon_version'], r_json['updates_needed']['config_name'])
    else:
        threads = []
        if r_json.get('updates_needed', False):
            if r_json['updates_needed'].get('sysmon', False):
                threads.append(Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)))
            if r_json['updates_needed'].get('config', False):
                threads.append(Thread(target=__update_config, args=(r_json['updates_needed']['config_name'],)))
        if r_json.get('restart', False):
            win32serviceutil.RestartService(f'sysmon_{env_config["agent"]["sysmon_version"]}')
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=60)
    if r_json.get('uninstall', False):
        uninstall_sysmon()
        __env_config_sysmon['installed'] = False
        __env_config_lock.acquire()
        __write_yaml()
        __env_config_lock.release()


def __update_sysmon(version):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{__env_config_api["updates"]["sysmon"]}'
                            f'/{version}')
    if not os.path.isfile(f'sysmon_{version}.exe'):
        __sysmon_lock.acquire()
        with open(f'sysmon_{version}.exe', 'wb') as new_file:
            new_file.write(bytes(response.content))
        __sysmon_lock.release()
        uninstall_sysmon()
        __env_config_agent['sysmon_version'] = version
        __env_config_lock.acquire()
        __write_yaml()
        __env_config_lock.release()
        install_sysmon()
        __env_config_sysmon['installed'] = True
        __env_config_lock.acquire()
        __write_yaml()
        __env_config_lock.release()
        try:
            os.remove(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe')
        except OSError:
            pass
    elif check_sysmon_running():
        pass
    else:
        install_sysmon()
        __env_config_sysmon['installed'] = True
        __env_config_lock.acquire()
        __write_yaml()
        __env_config_lock.release()


def __update_config(name):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{__env_config_api["updates"]["config"]}'
                            f'/{name}')
    if not os.path.isfile(f'agent_config_{name}.xml'):
        __sysmon_lock.acquire()
        with open(f'agent_config_{name}.xml', 'wb') as new_file:
            new_file.write(bytes(response.content))
        __sysmon_lock.release()
        env_config["agent"]["config_name"] = name
        __env_config_lock.acquire()
        __write_yaml()
        __env_config_lock.release()
        update_sysmon_config()
        try:
            os.remove(f'agent_config_{env_config["agent"]["config_name"]}.xml')
        except OSError:
            pass
    else:
        update_sysmon_config()


def __initial_install(version, name):
    config_response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                                   f'{__env_config_api["updates"]["config"]}'
                                   f'/{name}')
    if not os.path.isfile(f'agent_config_{name}.xml'):
        with open(f'agent_config_{name}.xml', 'wb') as new_file:
            new_file.write(bytes(config_response.content))
        env_config["agent"]["config_name"] = name
        __write_yaml()
    sysmon_response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                                   f'{__env_config_api["updates"]["sysmon"]}'
                                   f'/{version}')
    if not os.path.isfile(f'sysmon_{version}.exe'):
        with open(f'sysmon_{version}.exe', 'wb') as new_file:
            new_file.write(bytes(sysmon_response.content))
        uninstall_sysmon()
        __env_config_agent['sysmon_version'] = version
        __write_yaml()
    install_sysmon()
    __env_config_sysmon['installed'] = True
    __env_config_lock.acquire()
    __write_yaml()
    __env_config_lock.release()
