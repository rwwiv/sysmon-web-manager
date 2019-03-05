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


def __build_request_dict():
    __data = {}
    if not env_config['agent']['installed']:
        return __data
    if not check_sysmon_running():
        __data = {
            'exec_running': False,
            'exec_last_running_at': env_config['agent']['exec_last_running']
        }
    else:
        env_config['http']['checked_exec_running'] = False
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __data = {
            'exec_running': True
        }
    if env_config['agent']['sysmon_version'] is not None:
        __data['sysmon_version'] = env_config['agent']['sysmon_version']
    if env_config['agent']['config_name'] is not None:
        __data['config_name'] = env_config['agent']['config_name']
    return __data


def __heartbeat():
    response = requests.put(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["heartbeat"]}'
                            f'/{env_config["http"]["uuid"]}',
                            # auth=__auth,
                            json=__build_request_dict())
    r_json = response.json()
    if ('install' in r_json) & r_json['install'] & (not env_config['agent']['installed']):
        threads = [
            Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)),
            Thread(target=__update_config, args=(r_json['updates_needed']['config_name'],))
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=60)
    elif env_config['agent']['installed']:
        pass
    else:
        threads = []
        if ('sysmon' in r_json['updates_needed']) & r_json['updates_needed']['sysmon']:
            threads.append(Thread(target=__update_sysmon, args=(r_json['updates_needed']['sysmon_version'],)))
        if ('config' in r_json['updates_needed']) & r_json['updates_needed']['config']:
            threads.append(Thread(target=__update_config, args=(r_json['updates_needed']['config_name'],)))
        if ('restart' in r_json) & r_json['restart']:
            win32serviceutil.RestartService(f'sysmon_{env_config["agent"]["sysmon_version"]}')
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=60)
    if ('uninstall' in r_json) & r_json['uninstall']:
        env_config['agent']['installed'] = False
        __env_config_lock.acquire()
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __env_config_lock.release()
        uninstall_sysmon()


def __update_sysmon(version):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["updates"]["sysmon"]}'
                            f'/{version}')
    if not os.path.isfile(f'sysmon_{version}.exe'):
        __sysmon_lock.acquire()
        with open(f'sysmon_{version}.exe', 'wb') as new_file:
            new_file.write(bytes(response.content))
        __sysmon_lock.release()
        uninstall_sysmon()
        env_config['agent']['sysmon_version'] = version
        env_config['agent']['installed'] = True
        __env_config_lock.acquire()
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __env_config_lock.release()
        install_sysmon()
        try:
            os.remove(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe')
        except OSError:
            pass
    elif check_sysmon_running():
        pass
    else:
        env_config['agent']['installed'] = True
        __env_config_lock.acquire()
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __env_config_lock.release()
        install_sysmon()


def __update_config(name):
    response = requests.get(f'{__protocol}://{user_config["http"]["url"]}'
                            f'{env_config["http"]["api"]["updates"]["config"]}'
                            f'/{name}')
    if not os.path.isfile(f'agent_config_{name}.xml'):
        __config_lock.acquire()
        with open(f'agent_config_{name}.xml', 'wb') as new_file:
            new_file.write(bytes(response.content))
        __config_lock.release()
        env_config["agent"]["config_name"] = name
        __env_config_lock.acquire()
        with open(env_config_filepath, 'w') as env_config_file:
            yaml.dump(env_config, env_config_file)
        __env_config_lock.release()
        update_sysmon_config()
        try:
            os.remove(f'agent_config_{env_config["agent"]["config_name"]}.xml')
        except OSError:
            pass
    else:
        update_sysmon_config()
