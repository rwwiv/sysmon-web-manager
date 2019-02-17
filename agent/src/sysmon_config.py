import os
import configparser

__config = configparser.ConfigParser().read('../config.ini')['sysmon']

sysmon_version = None if (__config['SysmonVersion'] == 'None') else __config['SysmonVerision']
config_name = None if (__config['SysmonVersion'] == 'None') else __config['SysmonVerision']

cwd = os.getcwd()
sysmon_exec_name = f'sysmon_{sysmon_version}.exe'
config_file_name = f'sysmon_config_{config_name}.xml'
