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
        sysmon_folder = '../sysmon'

        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        if not os.listdir(config_folder):
            with open(f'{config_folder}/agent_config_default.xml', 'wb') as config:
                config.write(bytes(
                    requests
                    .get('https://github.com/SwiftOnSecurity/sysmon-config/blob/master/sysmonconfig-export.xml')
                    .content
                ))
        if not os.path.exists(sysmon_folder):
            os.makedirs(sysmon_folder)
        if not os.listdir(sysmon_folder):
            sysmon_version_markdown_raw = requests.get('https://raw.githubusercontent.com/Neo23x0/'
                                                       'sysmon-version-history/master/README.md')\
                .content\
                .decode()
            sysmon_version_markdown_readline = StringIO(sysmon_version_markdown_raw).readlines()
            sysmon_version_markdown = [line.strip() for line in sysmon_version_markdown_readline]
            sysmon_version = ""
            for line in sysmon_version_markdown:
                if line.startswith('## v'):
                    sysmon_version = line.split('## v')[1]
                    break
            sysmon_zip = bytes(requests.get('https://download.sysinternals.com/files/Sysmon.zip').content)
            with open(f'{sysmon_folder}/sysmon.zip', 'wb') as sysmon:
                sysmon.write(sysmon_zip)
            if os.path.isfile(f'{sysmon_folder}/sysmon.zip'):
                with zipfile.ZipFile(f'{sysmon_folder}/sysmon.zip', 'r') as zip_ref:
                    zip_ref.extractall(sysmon_folder)
            if os.path.isfile(f'{sysmon_folder}/Sysmon.exe'):
                os.rename(f'{sysmon_folder}/Sysmon.exe', f'../sysmon/sysmon_{sysmon_version}.exe')
            for file in os.listdir(sysmon_folder):
                if file != f'sysmon_{sysmon_version}.exe':
                    os.remove(os.path.join(sysmon_folder, file))
