
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import Dialog, MessageBox
from PyQt5.sip import wrappertype as _type

# def message(caption: str, text: str, parent = None):
#     return Dialog(caption, text, parent).exec()

def message(caption: str, text: str, parent: QWidget | None = None, yesButtonText: str | None = None, cancelButtonText: str | None = None, type: int = 1,
            showYesButton: bool = True, showCancelButton: bool = True):
    """
    显示一个对话框
    :param caption: 对话框的标题
    :param text: 对话框的文本
    :param parent: 对话框的父窗口
    :param yesButtonText: “确定”按钮的文本，不指定则为默认
    :param cancelButtonText: “取消”按钮的文本，不指定则为默认
    :param type: 对话框类型：1为弹出式对话框，2为遮罩式对话框，默认为1
    :param showYesButton: 显示确定按钮
    :param showCancelButton: 显示取消按钮
    """
    if type == 1:
        _d = Dialog(caption, text, parent)
    elif type == 2:
        _d = MessageBox(caption, text, parent)
    else:
        _d = Dialog(caption, text, parent)
    if not showYesButton:
        _d.yesButton.hide()
        _d.buttonLayout.insertStretch(0, 1)
    if not showCancelButton:
        _d.cancelButton.hide()
        _d.buttonLayout.insertStretch(0, 1)
    if yesButtonText != None:
        _d.yesButton.setText(yesButtonText)
    if cancelButtonText != None:
        _d.cancelButton.setText(cancelButtonText)
    return _d.exec()