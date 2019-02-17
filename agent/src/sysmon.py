import subprocess

import sysmon_config


def install_sysmon():
    print(subprocess
          .call(f'{sysmon_config.cwd}\\{sysmon_config.sysmon_exec_name}'
                f' -accepteula -i {sysmon_config.cwd}\\..\\{sysmon_config.config_file_name}', shell=True))


def update_sysmon_config():
    print(subprocess
          .call(f'{sysmon_config.cwd}\\{sysmon_config.sysmon_exec_name}'
                f' -c {sysmon_config.cwd}\\..\\{sysmon_config.config_file_name}', shell=True))


def uninstall_sysmon():
    print(subprocess
          .call(f'{sysmon_config.cwd}\\..\\{sysmon_config.sysmon_exec_name} -u', shell=True))
