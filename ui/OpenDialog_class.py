from ui.py.OpenDialogUi import Ui_DialogUI
from PyQt6.QtWidgets import QMainWindow

from db import create_con


class OpenDialogCls(QMainWindow, Ui_DialogUI):
    def __init__(self, obj: object):
        super(OpenDialogCls, self).__init__()
        self.obj = obj
        self.setupUi(self)

        self.add_actions()

    def enterButton_clicked(self):
        try:
            master_key = self.passwordLine.text()
            file_path = self.pathLine.text()

            con = create_con(file_path, master_key)
            if not con:
                pass # TODO need to display error ui

            self.obj.con = con
            self.close()

        except:
            pass # TODO: need to display error ui





    def cancelButton_clicked(self):
        self.close()

    def add_actions(self):
        self.cancelButton.clicked.connect(self.cancelButton_clicked)
