import os
import configparser

base_path = os.path.dirname(__package__)
config_file = base_path.join(['conf', 'config.ini'])

if not os.path.exists(config_file):
    config_file = base_path.join('config.ini')

config_parser = configparser.ConfigParser()
config = config_parser.read(config_file)

# Service variables
service_name = 'SysMonagerAgent'
display_name = 'SysMonager Agent'

# Sysmon variables
__sysmon_conf = config['sysmon']
sysmon_version = __sysmon_conf['SysmonVersion']
sysmon_exe = base_path.join(f'sysmon_{sysmon_version}.exe')
sysmon_config = __sysmon_conf['ConfigName']
sysmon_config_file = base_path.join(f'sysmon_config_{sysmon_config}.xml')
sysmon_last_running = __sysmon_conf['LastRunning']
sysmon_checked_running = __sysmon_conf.getboolean('CheckedRunning')

# HTTP variables
__http_conf = config['http']
auth_user = __http_conf['AuthUser']
auth_pass = __http_conf['AuthPass']
uuid = __http_conf['AgentUUID']
url = __http_conf['URL']
api_heartbeat = '/api/heartbeat'
api_get_sysmon = '/api/updates/sysmon'
api_get_config = '/api/updates/config'
