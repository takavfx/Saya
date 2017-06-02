import os

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))

mainUIPath = os.path.join(_CURRENTPATH, 'ui', 'main.ui')
print mainUIPath

version = 'v0.1.0'

windowName = 'sayaMainWindow'
windowTitle = 'Saya ' + version
windowHeight = 600
windowWidth = 350
toolIconPath = os.path.join(_CURRENTPATH, 'static', 'gear.svg')
