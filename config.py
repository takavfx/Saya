import yaml
import os
import platform

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


def getLauncherConfig():
    if os.environ.get('SAYA_CONFIG_PATH'):
        config_file = os.path.join(os.environ.get('SAYA_CONFIG_PATH'), 'saya.yaml')
        f = open(config_file, 'r')
        CONFIG = yaml.load(f)
    else:
        f = open(os.path.join(_CURRENTPATH, 'config', 'saya.yaml'), 'r')
        CONFIG = yaml.load(f)

    print CONFIG
    return CONFIG


def getPresetConfig():
    if os.environ.get('SAYA_PRESET_CONFIG_PATH'):
        config_file = os.path.join(os.environ.get('SAYA_PRESET_CONFIG_PATH'), 'saya_preset.yaml')
        f = open(config_file, 'r')
        CONFIG = yaml.laod(f)
    else:
        platform.system() == 'Windows':
            path = os.environ.get('APPDATA')
        platform.system() == 'Linux' or 'Mac':
            path = os.environ.get('HOME')
        f = open(os.path.join(path, 'saya_preset.yaml'), 'r')
        CONFIG = yaml.load(f)


def writeUserConfig():
    pass