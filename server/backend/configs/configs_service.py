import base64

from heartbeat.models import Configuration
import json
from logging_service import configs_logging_service as log
import os


def get_all_configs():
    all_configs = Configuration.objects.all()
    data = []
    for x in all_configs:
        temp = {'name': x.NAME, 
                'default': x.IS_DEFAULT}
        data.append(temp)
    log.debug(f"{len(data)} configurations retrieved")
    return data


def create_config(config_body):
    if 'name' in config_body.keys()\
            and 'content' in config_body.keys()\
            and 'default' in config_body.keys():
        config_name = config_body['name']
        if Configuration.objects.filter(NAME=config_name).count() == 0:
            if config_body['default']:
                Configuration.objects.update(IS_DEFAULT=False)
            new_config = Configuration(
                NAME=config_name,
                IS_DEFAULT=config_body['default']
            )
            if not os.path.exists('../configuration_files'):
                os.makedirs('../configuration_files')

            with open(f'../configuration_files/agent_config_{config_name}.xml', 'wb') as config:
                config.write(base64.b64decode((config_body['content'])))
            new_config.save()
            log.debug(f'Config with name {config_name} created succesfully')
            return 0
        else:
            log.err(f'Config {config_name} already exists')
            return -1
    else:
        log.err('Request body invalid')
        return -1


def retrieve_config(config_name):
    config = Configuration.objects.filter(NAME=config_name)
    if len(config) == 1:
        with open(f"../configuration_files/agent_config_{config_name}.xml", 'rb') as config_file:
            base64_encoded_content = base64.b64encode(config_file.read())
            log.debug(f'{config_name} config retrieved')
            data = {
                'content': base64_encoded_content.decode('utf-8'),
                'default': config[0].IS_DEFAULT
            }
            return data
    else:
        log.err(f'Config {config_name} does not exist')
        raise Exception


def update_config(config_body):
    if 'name' in config_body.keys() and 'content' in config_body.keys() and 'default' in config_body:
        config_name = config_body['name']
        if Configuration.objects.filter(NAME=config_name).count() != 0:
            if config_body['default']:
                Configuration.objects.update(IS_DEFAULT=False)
            new_config = Configuration(
                NAME=config_name,
                IS_DEFAULT=config_body['default']
            )
            if not os.path.exists('../configuration_files'):
                os.makedirs('../configuration_files')

            with open(f'../configuration_files/agent_config_{config_name}.xml', 'wb') as config:
                config.truncate(0)
                config.write(base64.b64decode((config_body['content'])))
            new_config.save()
            log.debug(f'Config with name {config_name} created successfully')
            return 0
        else:
            log.err(f'Config {config_name} does not exist')
            return -1
    else:
        log.err('Request body invalid')
        return -1

