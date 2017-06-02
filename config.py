import yaml
import os

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


def getConfig():
    if os.environ.get('SAYA_CONFIG_PATH'):
        config_file = os.path.join(os.environ.get('SAYA_CONFIG_PATH'), 'saya.yaml')
        f = open(config_file, 'r')
        CONFIG = yaml.load(f)
    else:
        f = open(os.path.join(_CURRENTPATH, 'config', 'saya.yaml'), 'r')
        CONFIG = yaml.load(f)

    print CONFIG
    return CONFIG
