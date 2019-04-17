import os

import requests
from django.apps import AppConfig


class UpdatesConfig(AppConfig):
    name = 'updates'

    def ready(self):
        if not os.listdir('../configuration_files'):
            with('../configuration_files/agent_config_default.xml', 'wb') as config:
                config.write(bytes(
                    requests
                    .get('https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml')
                    .content
                ))
        if not os.listdir('../sysmon'):
            sysmon_version_markdown_raw = requests.get('https://raw.githubusercontent.com/Neo23x0/'
                                                       'sysmon-version-history/master/README.md')\
                .content\
                .readlines()
            sysmon_version_markdown = [line.strip() for line in sysmon_version_markdown_raw]
            sysmon_version = ""
            for line in sysmon_version_markdown:
                if line.startsWith('##'):
                    sysmon_version = line.split('##v')[1]
            with(f'../sysmon/sysmon_{sysmon_version}.exe', 'wb') as sysmon:
                sysmon.write(bytes(
                    requests.get('https://download.sysinternals.com/files/Sysmon.zip').content
                ))
