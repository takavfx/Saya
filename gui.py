#!/usr/bin/env python

import os
import webbrowser

from PySide import QtCore, QtGui
from PySide.QtUiTools import QUiLoader

import yaml

import core
import define as DEFINE
import config as Config
import presets as Presets


_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


CONFIG = Config.getLauncherConfig()

class MainWindow(QtCore.QObject):
    """
    Main window class of this tool.
    """

    _windowName   = DEFINE.windowName
    _windowTitle  = DEFINE.windowTitle
    _windowHeight = DEFINE.windowHeight
    _windowWidth  = DEFINE.windowWidth
    toolIcon      = QtGui.QIcon(DEFINE.toolIconPath)


    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = None
        self.initGUI()


    def show(self):
        self.UI.show()

    def initGUI(self):
        loader = QUiLoader()
        self.UI = loader.load(DEFINE.mainUIPath)

        self.createPresetsList() # Create self.presetList <- QListView
        self.setSignals()

        self.UI.setObjectName(self._windowName)
        self.UI.setWindowTitle(self._windowTitle)
        self.UI.setWindowIcon(self.toolIcon)

        self.setApplications()
        self.setProjects()

        self.resetWindowSize()


    def setSignals(self):
        # self.UI.projectComboBox.changed.connect(self.setApplications)
        self.UI.appComboBox.currentIndexChanged.connect(self.setVersions)
        self.UI.appComboBox.currentIndexChanged.connect(self.setOptions)
        self.UI.launchPushButton.clicked.connect(self.launchApp)


    def resetWindowSize(self):
        self.UI.resize(self._windowWidth, self._windowHeight)


    def createPresetsList(self):
        data = Config.getUserConfig()
        self.presetsList = QtGui.QListView()
        model = Presets.PresetsListModel(data=data, config=CONFIG)
        self.presetsList.setModel(model)
        delegate = Presets.PresetsListDelegate()
        self.presetsList.setItemDelegate(delegate)

        self.presetsList.setFrameShadow(QtGui.QFrame.Plain)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.presetsList)
        self.UI.presets.setLayout(layout)


    def setProjects(self):
        self.UI.projectComboBox.clear()
        self.UI.projectComboBox.addItems(CONFIG['projects'].keys())


    def setApplications(self):
        self.UI.appComboBox.clear()
        for app in CONFIG['apps'].keys():
            icon_path = CONFIG['apps'].get(app).get('icon')
            if icon_path:
                self.UI.appComboBox.addItem(QtGui.QIcon(icon_path[0]), app)
            else:
                self.UI.appComboBox.addItem(app)


    def setVersions(self):
        self.UI.versionComboBox.clear()

        currentApp = self.UI.appComboBox.currentText()
        for appItems in CONFIG['apps'].items():
            if currentApp == appItems[0]:
                versions = appItems[1].get('versions').keys()

        self.UI.versionComboBox.addItems(versions)


    def setOptions(self, app=''):
        self.UI.optionComboBox.clear()

        currentApp = self.UI.appComboBox.currentText()
        for appItems in CONFIG['apps'].items():
            if currentApp == appItems[0]:
                options = appItems[1].get('options')
        
        if options:
            self.UI.optionComboBox.addItems(options)
        else:
            self.UI.optionComboBox.addItem('default')


    def getTabIndexByTitle(self, title):
        index = 0
        while index < self.count():
            if self.tabText(index) == title:
                return index

            index += 1

        return None


    def launchApp(self):
        if self.UI.mainTabWidget.currentIndex() == 1:

            project = self.UI.projectComboBox.currentText()
            app     = self.UI.appComboBox.currentText()
            version = self.UI.versionComboBox.currentText()
            option  = self.UI.optionComboBox.currentText()
            
            words = ["\n[[ START LAUNCHING ]] :: ",app, version,"as", option, "mode, on", project, "project."]
            print ' '.join(words)

            exe = CONFIG.get('apps').get(app).get('versions').get(version)
            if not exe:
                print "[[ DEFINITION ERROR ]] :: The app exe is not defined."
                return
            
            cmds = []
            if not option == 'default':
                elemetns = [exe, option]
                cmds = ' '.join(elemetns)
            else:
                cmds = exe

            print "[[ LAUNCH CMDS ]] :: " + cmds[0]

            try:
                core.launch(cmds=cmds)
            except:
                import traceback
                print traceback.format_exc()



def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
