from heartbeat.models import Configuration
import json
from logging_service import configs_logging_service as log

def get_all_configs():
    all_configs = Configuration.objects.all()
    data = []
    for x in all_configs:
        temp = {'name': x.NAME, 
                'is_default': x.IS_DEFAULT}
        data.append(temp)
    log.debug(f"{len(data)} configurations retrieved")
    return data


def create_configs(config_name):
    if Configuration.objects.filter(NAME=config_name).count() == 0:
        new_config = Configuration(
            NAME = config_name,
            IS_DEFAULT = False
        )
        with open(f'../configuration_files/{config_name}.xml','w+'):
            pass
        new_config.save()
        log.debug(f'Config with name {config_name} created succesfully')
        return 0
    else:
        log.err('Config already exists')
        return -1


def retrieve_config(config_name):
    config = Configuration.objects.filter(NAME=config_name)
    if(len(config) == 1):
        config_retrieved = ''
        with open(f"../configuration_files/{config_name}.xml") as config:
            for line in config.readlines():
                config_retrieved += line
        
        return config_retrieved
    else:
        log.err('Config does not exist')
        raise Exception

def update_config(config_name, config_body):
    config = Configuration.objects.filter(NAME=config_name)

    if(len(config) == 1):
        with open(f"../configuration_files/{config_name}.xml","a") as config:
            config.truncate(0)
            for line in config_body.decode("utf-8").split('\n'):
                config.write(f'{line}\n')
        pass
    else:
        log.err('Config does not exist')
        raise Exception
