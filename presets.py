from PySide import QtCore, QtGui


ICON_ROLE    = QtCore.Qt.UserRole
PROJECT_ROLE = QtCore.Qt.UserRole + 1
VERSION_ROLE = QtCore.Qt.UserRole + 2
OPTION_ROLE  = QtCore.Qt.UserRole + 3


class PresetsListModel(QtCore.QAbstractListModel):

    def __init__(self, parent=None, data=[], config=[]):
        super(PresetsListModel, self).__init__(parent)
        self.__items = data
        self.__config = config


    def clearItems(self):
        self.__items = []
        self.__config = []


    def addItem(self, data):
        self.__items.append(data.get('presets').keys())


    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.__items.get('presets'))


    def data(self, index, role=QtCore.Qt.DisplayRole):

        preset = self.__items.get('presets').keys()[index.row()]
        app = self.__items.get('presets').get(preset).get('app')[0]

        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.__items.get('presets')):
            return None

        if role == QtCore.Qt.DisplayRole:
            return app

        elif role == ICON_ROLE:
            return self.__config.get('apps').get(app).get('icon', [''])[0]

        elif role == PROJECT_ROLE:
            return self.__items.get('presets').get(preset).get('project', [''])[0]

        elif role == VERSION_ROLE:
            return self.__items.get('presets').get(preset).get('version', [''])[0]

        elif role == OPTION_ROLE:
            return self.__items.get('presets').get(preset).get('option', [''])[0]

        else:
            return None

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled



class PresetsListDelegate(QtGui.QStyledItemDelegate):
    """
    Custom list delegate for Presets.
    """

    item_width  = 100
    item_height = 60
    margin = 5
    icon_width = 60

    def __init__(self, parent=None):
        super(PresetsListDelegate, self).__init__(parent)



    def drawAppIcon(self, painter, rect, icon):

        iconImage = QtGui.QPixmap(icon).scaled(self.icon_width, self.icon_width)
        rect = QtCore.QRect(rect.left(),
                            rect.top(),
                            self.icon_width,
                            self.icon_width)
        painter.drawPixmap(rect, iconImage)


    def drawProjectName(self, painter, rect, project):

        color = QtGui.QColor(QtCore.Qt.white)
        pen = QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        rect = QtCore.QRect(rect.left()+self.icon_width+self.margin,
                            rect.top()-15,
                            rect.width()-self.icon_width+self.margin,
                            rect.height())
        painter.drawText(rect,
                        QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft,
                        "Porject : " + project)


    def drawAppName(self, painter, rect, app, version):

        color = QtGui.QColor(QtCore.Qt.white)
        pen = QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        rect = QtCore.QRect(rect.left()+self.icon_width+self.margin,
                            rect.top(),
                            rect.width()-self.icon_width+self.margin,
                            rect.height())
        painter.drawText(rect,
                        QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft,
                        "App : " + app + " " + version)


    def drawOptionName(self, painter, rect, option):

        color = QtGui.QColor(QtCore.Qt.white)
        pen = QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        rect = QtCore.QRect(rect.left()+self.icon_width+self.margin,
                            rect.top()+15,
                            rect.width()-self.icon_width+self.margin,
                            rect.height())
        painter.drawText(rect,
                        QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft,
                        "Option : " + option)


    def paint(self, painter, option, index):

        if option.state & QtGui.QStyle.State_Selected:
            bgBrush = QtGui.QBrush(QtGui.QColor(60,60,60))
            bgPen   = QtGui.QPen(QtGui.QColor(60,60,60), 0.5, QtCore.Qt.SolidLine)
            painter.setPen(bgPen)
            painter.setBrush(bgBrush)
            painter.drawRect(option.rect)

        icon    = index.data(ICON_ROLE)
        app     = index.data(QtCore.Qt.DisplayRole)
        project = index.data(PROJECT_ROLE)
        version = index.data(VERSION_ROLE)
        opname  = index.data(OPTION_ROLE)

        ## Draw icon
        self.drawAppIcon(painter, option.rect, icon)
        ## Draw project text
        self.drawProjectName(painter, option.rect, project)
        ## Draw application text
        self.drawAppName(painter, option.rect, app, version)
        ## Draw version text
        self.drawOptionName(painter, option.rect, opname)
        


    def sizeHint(self, option, index):
        return QtCore.QSize(self.item_width, self.item_height)