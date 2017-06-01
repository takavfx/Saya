#!/usr/bin/env python

import os
import webbrowser

from PySide import QtCore, QtGui, QtSvg
from PySide.QtUiTools import QUiLoader

import yaml

import define as DEFINE


_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


if os.environ.get('SAYA_CONFIG'):
    f = open(os.environ.get('SAYA_CONFIG'), 'r')
    CONFIG = yaml.load(f)
else:
    f = open(os.path.join(_CURRENTPATH, 'config', 'saya.yaml'), 'r')
    CONFIG = yaml.load(f)
    print CONFIG



class MainWindow(QtGui.QMainWindow):
    """
    Main window class of this tool.
    """

    _windowName   = DEFINE.windowName
    _windowTitle  = DEFINE.windowTitle
    _windowHeight = DEFINE.windowHeight
    _windowWidth  = DEFINE.windowWidth
    # toolIcon    = QtGui.QIcon(DEFINE.mantleIconPath)


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initGUI()


    def initGUI(self):
        loader = QUiLoader()
        self.UI = loader.load(DEFINE.mainUIPath)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.UI)
        self.setLayout(layout)

        self.setObjectName(self._windowName)
        self.setWindowTitle(self._windowTitle)

        self.setCentralWidget(self.UI)

        self.setSignals()

        self.setApplications()
        self.setProjects()

        self.resetWindowSize()



    def setSignals(self):
        # self.UI.projectComboBox.changed.connect(self.setApplications)
        self.UI.appComboBox.currentIndexChanged.connect(self.setVersions)
        self.UI.appComboBox.currentIndexChanged.connect(self.setOptions)
        self.UI.launchPushButton.clicked.connect(self.launchApp)


    def resetWindowSize(self):
        self.resize(self._windowWidth, self._windowHeight)


    def setProjects(self):
        self.UI.projectComboBox.clear()
        self.UI.projectComboBox.addItems(CONFIG['projects'].keys())


    def setApplications(self):
        self.UI.appComboBox.clear()
        self.UI.appComboBox.addItems(CONFIG['apps'].keys())


    def setVersions(self):
        self.UI.versionComboBox.clear()

        currentApp = self.UI.appComboBox.currentText()
        for appItems in CONFIG['apps'].items():
            print appItems
            if currentApp == appItems[0]:
                versions = appItems[1].get('Versions').keys()

        self.UI.versionComboBox.addItems(versions)


    def setOptions(self, app=''):
        self.UI.optionComboBox.clear()

        currentApp = self.UI.appComboBox.currentText()
        for appItems in CONFIG['apps'].items():
            if currentApp == appItems[0]:
                options = appItems[1].get('Options')
        
        if options:
            self.UI.optionComboBox.addItems(options)
        else:
            self.UI.optionComboBox.addItem('default')


    def launchApp(self):
        app = self.UI.appComboBox.currentText()
        print 'Launch ' + app


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
