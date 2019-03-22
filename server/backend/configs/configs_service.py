from heartbeat.models import Configuration
import json
from logging_service import configs_logging_service as log

def get_all_configs():
    all_configs = Configuration.objects.all()
    data = []
    for x in all_configs:
        temp = {'name': x.NAME }
        data.append(temp)
    log.debug(f"{len(data)} configurations retrieved")
    return data


def create_configs(config_name):
    if Configuration.objects.filter(NAME=config_name).count() == 0:
        new_config = Configuration(
            NAME = config_name,
            IS_DEFAULT = False
        )
        new_config.save()
        log.debug(f'Config with name {config_name} created succesfully')
        return 0
    else:
        log.err('Config already exists')
        return -1


def retrieve_config(config_name):
    config = Configuration.objects.filter(NAME=config_name)
    if(len(config) == 1):
        log.debug(f'config with name {config_name} updated succesfully')
        return 0 #retrieve the config and return it somehow
    else:
        log.err('Config does not exist')
        return -1 #return empty