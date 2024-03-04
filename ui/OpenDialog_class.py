from ui.py.OpenDialogUi import Ui_DialogUI
from PyQt6.QtWidgets import QMainWindow


class OpenDialogCls(QMainWindow, Ui_DialogUI):
    def __init__(self, obj: object):
        super(OpenDialogCls, self).__init__()
        self.obj = obj
        self.setupUi(self)

        self.add_actions()

    ...

    def add_actions(self):
        pass
