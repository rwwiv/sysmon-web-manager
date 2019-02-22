import subprocess
import win32serviceutil
from enum import Enum

import agent_config


class ServiceState(Enum):
    starting = 0
    stopping = 1
    stopped = 2
    running = 3


def install_sysmon():
    print(subprocess.call(f'{agent_config.sysmon_exe} -accepteula -i {agent_config.sysmon_config_file}', shell=True))


def update_sysmon_config():
    print(subprocess.call(f'{agent_config.sysmon_exe} -c {agent_config.sysmon_config_file}', shell=True))


def uninstall_sysmon():
    print(subprocess.call(f'{agent_config.sysmon_exe} -u', shell=True))


def check_sysmon_state():
    try:
        status = win32serviceutil.QueryServiceStatus(f'sysmon_{agent_config.sysmon_version}')
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
