# src/utils.py
import json

def load_api_key():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config['api_key']
