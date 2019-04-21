import os
import requests


from django.apps import AppConfig
from django.db.models.signals import post_migrate


class HeartbeatConfig(AppConfig):
    name = 'heartbeat'

    def ready(self):
        from models.models import Configuration
        if not post_migrate:
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
                Configuration(NAME='Swift On Security', IS_DEFAULT=True).save()
