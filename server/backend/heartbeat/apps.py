import os
import time
import zipfile
import requests

from django.apps import AppConfig
from io import StringIO


class HeartbeatConfig(AppConfig):
    name = 'heartbeat'

    def ready(self):
        config_folder = '../configuration_files'

        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        if not os.listdir(config_folder):
            with open(f'{config_folder}/agent_config_default.xml', 'wb') as config:
                config.write(bytes(
                    requests
                    .get('https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml')
                    .content
                ))
                
