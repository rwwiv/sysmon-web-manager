import re

from models.models import Sysmon, Global_Variables
from support import support_service
import os
import zipfile
import requests
from io import StringIO


def get_all_sysmons():
    all_sysmons = Sysmon.objects.all()
    data = []
    for sysmon in all_sysmons:
        temp = {'version': sysmon.VERSION,
                'is_current': sysmon.IS_CURRENT}
        data.append(temp)
    return data


def retrieve_and_create_sysmon():
    sysmon_folder = '../sysmon'
    if not support_service.get_sysmon_versioning_repo_link():
        support_service.update_sysmon_versioning_repo_link('https://raw.githubusercontent.com/Neo23x0/sysmon-version-history/master/README.md')
    repo_link = support_service.get_sysmon_versioning_repo_link()

    if not support_service.get_sysmon_download_link():
        support_service.update_sysmon_download_link('https://download.sysinternals.com/files/Sysmon.zip')
    download_link = support_service.get_sysmon_download_link()

    try:
        if not os.path.exists(sysmon_folder):
            os.makedirs(sysmon_folder)
        if not os.listdir(sysmon_folder):
            sysmon_version_markdown_raw = requests.get(repo_link)\
                .content\
                .decode()
            sysmon_version_markdown_readline = StringIO(sysmon_version_markdown_raw).readlines()
            sysmon_version_markdown = [line.strip() for line in sysmon_version_markdown_readline]
            sysmon_version = ""
            for line in sysmon_version_markdown:
                if line.startswith('## v'):
                    sysmon_version = line.split('## v')[1]
                    break
            sysmon_zip = bytes(requests.get(download_link).content)
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
            if Sysmon.objects.filter(IS_CURRENT=True).exists():
                old_version = Sysmon.objects.get(IS_CURRENT=True)
                old_version.IS_CURRENT = False
                old_version.save()
            if not Sysmon.objects.filter(VERSION=sysmon_version).exists():
                new_sysmon_record = Sysmon(VERSION=sysmon_version, IS_CURRENT=True)
                new_sysmon_record.save()
        else:
            newest_version = ''
            for file in os.listdir(sysmon_folder):
                regex = re.search("sysmon_(.+?).exe", file)
                if regex:
                    Sysmon(VERSION=regex.group(1),IS_CURRENT=False).save()
                    if regex.group(1) > newest_version:
                        newest_version = regex.group(1)
            sysmon_record = Sysmon.objects.get(VERSION=newest_version)
            sysmon_record.IS_CURRENT = True
            sysmon_record.save()
        return 1
    except Exception as e:
        return -1
