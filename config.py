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

    print "\n[[ LOADING ]] :: Loading launcher config data."
    print CONFIG
    return CONFIG



def getUserConfig():
    if os.environ.get('SAYA_USER_CONFIG_PATH'):
        config_file = os.path.join(os.environ.get('SAYA_USER_CONFIG_PATH'), 'saya_user.yaml')
        f = open(config_file, 'r')
        CONFIG = yaml.laod(f)
    else:
        if platform.system() == 'Windows':
            path = os.environ.get('APPDATA')
        elif platform.system() == 'Linux' or 'Mac':
            path = os.environ.get('HOME')
        f = open(os.path.join(path, 'saya_user.yaml'), 'r')
        CONFIG = yaml.load(f)

    print "\n[[ LOADING ]] :: Loading Preset config data."
    print CONFIG
    return CONFIG


def parseUserData(data):
    for i in range(len(data)):
        project = data[i].get('project')
        application = data[i].get('application')
        version = data[i].get('version')
        option = data[i].get('option')



def writeUserConfig():
    pass