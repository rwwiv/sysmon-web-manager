from models.models import Sysmon
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

def retrieve_and_create_sysmon(link):
    sysmon_folder = '../sysmon'
    try:
        if not os.path.exists(sysmon_folder):
            os.makedirs(sysmon_folder)
        if not os.listdir(sysmon_folder):
            sysmon_version_markdown_raw = requests.get(link)\
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
            if Sysmon.objects.filter(IS_CURRENT=True).exists():
                old_version = Sysmon.objects.get(IS_CURRENT=True)
                old_version.IS_CURRENT = False
                old_version.save()
            if not Sysmon.objects.filter(VERSION=sysmon_version).exists():
                new_sysmon_record = Sysmon(VERSION=sysmon_version, IS_CURRENT=True)
                new_sysmon_record.save()
        return 1
    except:
        return -1
