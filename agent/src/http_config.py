import configparser

__config = configparser.ConfigParser().read('resources/config.ini')['http']

auth_user = __config['AuthUser']
auth_pass = __config['AuthPass']
agent_uuid = None if (__config['AgentUUID'] == 'None') else __config['AgentUUID']
base_url = __config['BaseURL']
api_heartbeat = __config['ApiHeartbeat']
api_get_sysmon = __config['ApiGetSysmon']
api_get_config = __config['ApiGetConfig']
