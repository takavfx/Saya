from PySide import QtCore, QtGui

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

        app = self.__items.get('presets').get((self.__items.get('presets').keys()[index.row()])).get('app')[0]

        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.__items.get('presets')):
            return None

        if role == QtCore.Qt.DisplayRole:
            return app

        elif role == QtCore.Qt.UserRole:
            return self.__config.get('apps').get(app).get('icon', [''])[0]
        else:
            return None

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled



class PresetsListDelegate(QtGui.QStyledItemDelegate):
    """
    Custom list delegate for Presets.
    """
    def __init__(self, parent=None):
        super(PresetsListDelegate, self).__init__(parent)


    def paint(self, painter, option, index):

        icon_width = 60
        margin = 5

        if option.state & QtGui.QStyle.State_Selected:
            bgBrush = QtGui.QBrush(QtGui.QColor(60,60,60))
            bgPen   = QtGui.QPen(QtGui.QColor(60,60,60), 0.5, QtCore.Qt.SolidLine)
            painter.setPen(bgPen)
            painter.setBrush(bgBrush)
            painter.drawRect(option.rect)

        name = index.data(QtCore.Qt.DisplayRole)
        thumbName = index.data(QtCore.Qt.UserRole)
        thumbImage = QtGui.QPixmap(thumbName).scaled(icon_width, icon_width)
        rect = QtCore.QRect(option.rect.left(),
                            option.rect.top(),
                            icon_width,
                            icon_width)
        painter.drawPixmap(rect, thumbImage)

        color = QtGui.QColor(QtCore.Qt.white)
        pen = QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        rect = QtCore.QRect(option.rect.left()+icon_width+margin,
                            option.rect.top(),
                            option.rect.width()-icon_width+margin,
                            option.rect.height())
        painter.drawText(rect,
                        QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter,
                        "App : " + name)

        

    def sizeHint(self, option, index):
        return QtCore.QSize(100, 60)