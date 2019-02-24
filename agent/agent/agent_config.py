import os
import configparser
import yaml

base_path = os.getcwd()
env_config_filepath = f'{base_path}\\..\\resources\\config.yml'
env_config = None
with open(env_config_filepath, 'r') as env_config_file:
    try:
        env_config = yaml.load(env_config_file)
    except yaml.YAMLError as exc:
        exit(-1)
try:
    user_config_file = f'{base_path}\\..\\config.ini'
    user_config = configparser.ConfigParser()
    user_config.read(user_config_file)
except:
    exit(-1)
