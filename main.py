# -*- coding: utf-8 -*- #

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from qfluentwidgets import setThemeColor, FluentTranslator
from qframelesswindow.utils import getSystemAccentColor

from dialog import message
from mainUI import Ui_Dialog
from win32api import GetLastError
from win32gui import (FindWindow, ShowWindow, MessageBox,
                      GetWindowText, SetWindowText)
from win32con import *
from qframelesswindow import *
#from PyQt5.QtWidgets import QDialog as Window
import sys
if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:
    from qframelesswindow import AcrylicWindow as Window
elif sys.getwindowsversion().major == 6 and sys.getwindowsversion().minor == 1:
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window


class Demo(Ui_Dialog, Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        try:
            self.setTitleBar(StandardTitleBar(self))
            self.setupUi(self)
            self.initUI()
            self.thisHwnd = FindWindow(None, self.windowTitle())
            self.hwnd = 0
        except Exception as e:
            message('错误！', f'{e.__class__.__name__}: {e.args if len(e.args) > 1 else e.args[0]}', None, "关闭", None, 1, True, False)
            sys.exit(-1)

    def initUI(self):
        self.titleBar.maxBtn.hide()
        self.titleBar.setDoubleClickEnabled(False)
        self.titleBar.titleLabel.setStyleSheet("""
                    QLabel{
                        background: transparent;
                        font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
                        padding: 0 4px;
                    }
                """)
        if sys.platform in ["win32", "darwin"]:
            setThemeColor(getSystemAccentColor())

        self.Find.clicked.connect(self.FindF)
        self.Tset_2.clicked.connect(self.changeTitle)
        self.hide_2.clicked.connect(self.hideWin)
        self.mini_2.clicked.connect(self.minWin)
        self.restore_2.clicked.connect(self.reWin)
        self.max_2.clicked.connect(self.maxWin)

        self.titleBar.iconLabel.hide()

        self.setLayout(self.verticalLayout)
        self.titleBar.raise_()
        
    def maxWin(self):
        ShowWindow(self.hwnd, SW_MAXIMIZE)
        
    def reWin(self):
        ShowWindow(self.hwnd, SW_RESTORE)
        
    def minWin(self):
        ShowWindow(self.hwnd, SW_MINIMIZE)
        
    def hideWin(self):
        ShowWindow(self.hwnd, SW_HIDE)
        
    def changeTitle(self):
        try:
            if not self.chT_2.text():
                message('警告', "请输入要设置的标题！", self, '确定', None, 2, True, False)
                return
            SetWindowText(self.hwnd, self.chT_2.text())
            message("提示", "设置完成！", self, '确定', None, 2, True, False)
        except Exception as e:
            message('错误！', f'{e.__class__.__name__}: {e.args if len(e.args) > 1 else e.args[0]}', None, "关闭", None, 1, True, False)
        
    def FindF(self):
        self.title = (self.titleInput.text() if self.titleInput.text() else
               None)
        self.cls = (self.classInput.text() if self.classInput.text() else
             None)
        try:
            self.hwnd = (int(eval(self.handleInput.text())) if self.handleInput.text() else
                    None)
        except (TypeError, NameError, ValueError, SyntaxError):
            message("错误", "输入的数据无效！", self, '确定', None, 2, True, False)
            return
        if self.hwnd == None:
            self.hwnd = FindWindow(self.cls, self.title)
        if self.hwnd == 0:
            message("错误", "输入的数据无效！", self, '确定', None, 2, True, False)
            return
        self.chT_2.setText(GetWindowText(self.hwnd))
        self.Hset_2.setText(str(self.hwnd))

if __name__ == '__main__':
    try:
        app = QApplication([])
        trans = FluentTranslator()
        app.installTranslator(trans)
        win = Demo()
        win.show()
        app.exec_()
    except Exception as e:
        message('错误！', f'{e.__class__.__name__}: {e.args if len(e.args) > 1 else e.args[0]}', None, "关闭", None, 1, True, False)
        sys.exit(-1)
