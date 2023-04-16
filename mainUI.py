# -*- coding: utf-8 -*- #

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class ui(QDialog):
    def __init__(self, parent = None):
        super(ui, self).__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(410, 350)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.setFont(font)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.Find = QPushButton(self)
        self.Find.setGeometry(QtCore.QRect(280, 150, 75, 23))
        self.Find.setAutoDefault(False)
        self.Find.setDefault(True)
        self.Find.setObjectName("Find")
        self.inputTip = QLabel(self)
        self.inputTip.setGeometry(QtCore.QRect(50, 130, 311, 16))
        self.inputTip.setObjectName("inputTip")
        self.groupBox = QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 371, 111))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.FindIn = QVBoxLayout(self.layoutWidget)
        self.FindIn.setContentsMargins(0, 0, 0, 0)
        self.FindIn.setObjectName("FindIn")
        self._title = QSplitter(self.layoutWidget)
        self._title.setOrientation(QtCore.Qt.Horizontal)
        self._title.setObjectName("_title")
        self.titleTip = QLabel(self._title)
        self.titleTip.setObjectName("titleTip")
        self.titleInput = QLineEdit(self._title)
        self.titleInput.setObjectName("titleInput")
        self.FindIn.addWidget(self._title)
        self._class = QSplitter(self.layoutWidget)
        self._class.setOrientation(QtCore.Qt.Horizontal)
        self._class.setObjectName("_class")
        self.classTip = QLabel(self._class)
        self.classTip.setObjectName("classTip")
        self.classInput = QLineEdit(self._class)
        self.classInput.setObjectName("classInput")
        self.FindIn.addWidget(self._class)
        self._handle = QSplitter(self.layoutWidget)
        self._handle.setOrientation(QtCore.Qt.Horizontal)
        self._handle.setObjectName("_handle")
        self.handleTip = QLabel(self._handle)
        self.handleTip.setObjectName("handleTip")
        self.handleInput = QLineEdit(self._handle)
        self.handleInput.setObjectName("handleInput")
        self.FindIn.addWidget(self._handle)
        self.setWindow = QGroupBox(self)
        self.setWindow.setGeometry(QtCore.QRect(20, 180, 371, 121))
        self.setWindow.setObjectName("setWindow")
        self.layoutWidget1 = QWidget(self.setWindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 351, 56))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Set = QVBoxLayout(self.layoutWidget1)
        self.Set.setContentsMargins(0, 0, 0, 0)
        self.Set.setObjectName("Set")
        self.title = QSplitter(self.layoutWidget1)
        self.title.setOrientation(QtCore.Qt.Horizontal)
        self.title.setObjectName("title")
        self.titleT = QLabel(self.title)
        self.titleT.setObjectName("titleT")
        self.chT = QLineEdit(self.title)
        self.chT.setObjectName("chT")
        self.Tset = QPushButton(self.title)
        self.Tset.setAutoDefault(False)
        self.Tset.setObjectName("Tset")
        self.Set.addWidget(self.title)
        self.handle = QSplitter(self.layoutWidget1)
        self.handle.setOrientation(QtCore.Qt.Horizontal)
        self.handle.setObjectName("handle")
        self.hanleT = QLabel(self.handle)
        self.hanleT.setObjectName("hanleT")
        self.Hset = QLineEdit(self.handle)
        self.Hset.setReadOnly(True)
        self.Hset.setObjectName("Hset")
        self.Set.addWidget(self.handle)
        self.layoutWidget2 = QWidget(self.setWindow)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 80, 351, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Ctrl = QHBoxLayout(self.layoutWidget2)
        self.Ctrl.setContentsMargins(0, 0, 0, 0)
        self.Ctrl.setObjectName("Ctrl")
        self.hide = QPushButton(self.layoutWidget2)
        self.hide.setAutoDefault(False)
        self.hide.setObjectName("hide")
        self.Ctrl.addWidget(self.hide)
        self.mini = QPushButton(self.layoutWidget2)
        self.mini.setAutoDefault(False)
        self.mini.setObjectName("mini")
        self.Ctrl.addWidget(self.mini)
        self.restore = QPushButton(self.layoutWidget2)
        self.restore.setAutoDefault(False)
        self.restore.setObjectName("restore")
        self.Ctrl.addWidget(self.restore)
        self.max = QPushButton(self.layoutWidget2)
        self.max.setAutoDefault(False)
        self.max.setObjectName("max")
        self.Ctrl.addWidget(self.max)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        self.pushButton.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.titleInput, self.classInput)
        self.setTabOrder(self.classInput, self.handleInput)
        self.setTabOrder(self.handleInput, self.Find)
        self.setTabOrder(self.Find, self.chT)
        self.setTabOrder(self.chT, self.Tset)
        self.setTabOrder(self.Tset, self.Hset)
        self.setTabOrder(self.Hset, self.hide)
        self.setTabOrder(self.hide, self.mini)
        self.setTabOrder(self.mini, self.restore)
        self.setTabOrder(self.restore, self.max)
        self.setTabOrder(self.max, self.pushButton)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "桌面窗口管理器"))
        self.setWhatsThis(_translate("Dialog", "桌面窗口管理器是一款系统工具，利用它，您可以自定义桌面上窗口的大小、标题等信息，让您的桌面更具有个性色彩。"))
        self.Find.setToolTip(_translate("Dialog", "查找标题所指的窗口。"))
        self.Find.setText(_translate("Dialog", "查找(&F)..."))
        self.inputTip.setText(_translate("Dialog", "上面三个选项填一个即可，也可以三个都填"))
        self.groupBox.setTitle(_translate("Dialog", "查找窗口"))
        self.titleTip.setText(_translate("Dialog", "窗口标题："))
        self.classTip.setText(_translate("Dialog", "窗口类："))
        self.handleTip.setText(_translate("Dialog", "窗口句柄："))
        self.handleInput.setPlaceholderText(_translate("Dialog", "句柄是一个独一无二的整数，用来标识窗口"))
        self.setWindow.setTitle(_translate("Dialog", "设置窗口"))
        self.titleT.setText(_translate("Dialog", "窗口标题："))
        self.Tset.setText(_translate("Dialog", "设置(&S)"))
        self.hanleT.setText(_translate("Dialog", "窗口句柄："))
        self.hide.setText(_translate("Dialog", "隐藏(&H)"))
        self.mini.setText(_translate("Dialog", "最小化(&M)"))
        self.restore.setText(_translate("Dialog", "向下还原(&R)"))
        self.max.setText(_translate("Dialog", "最大化(&A)"))
        self.pushButton.setText(_translate("Dialog", "关闭(&C)"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainUI = ui()
    mainUI.show()
    app.exec_()
    del sys
