import subprocess
import win32serviceutil
from enum import Enum
from datetime import datetime

import yaml

from agent_config import env_config, env_config_filepath


class ServiceState(Enum):
    starting = 0
    stopping = 1
    stopped = 2
    running = 3


def install_sysmon():
    print(subprocess.call(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe '
                          f'-accepteula -i agent_config_{env_config["agent"]["config_name"]}.xml', shell=True))


def update_sysmon_config():
    print(subprocess.call(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe '
                          f'-c agent_config_{env_config["agent"]["config_name"]}.xml', shell=True))


def uninstall_sysmon():
    print(subprocess.call(f'sysmon_{env_config["agent"]["sysmon_version"]}.exe -u', shell=True))


def check_sysmon_running():
    try:
        status = win32serviceutil.QueryServiceStatus(f'sysmon_{env_config["agent"]["sysmon_version"]}')
    except WindowsError:
        status_enum = ServiceState.stopped
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
        status_enum = switch[status[1]]
        if status_enum != ServiceState.running:
            if not env_config['agent']['checked_exec_running']:
                time_stopped = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                env_config['agent']['exec_last_running'] = time_stopped
                env_config['agent']['checked_exec_running'] = True
                with open(env_config_filepath, 'w') as env_config_file:
                    yaml.dump(env_config, env_config_file)
            return False
        else:
            return True
