from ui.py.OpenDialogUi import Ui_DialogUI
from PyQt6.QtWidgets import QMainWindow

from db import create_con

from ui.utils import DisplayDB

class OpenDialogCls(QMainWindow, Ui_DialogUI):
    def __init__(self, obj: object):
        super(OpenDialogCls, self).__init__()
        self.obj = obj

        self.setupUi(self)

        self.add_actions()

    def enterButton_clicked(self):
        master_key = self.passwordLine.text()
        file_path = self.pathLine.text()

        con = create_con(file_path, master_key)

        if not con:
            print('[DEBUG] Wrong password or unsupported DB!')
            return  # TODO need to display error ui

        self.obj.con = con

        self.close()

        DisplayDB(self.obj)

    def cancelButton_clicked(self):
        self.close()

    def add_actions(self):
        self.cancelButton.clicked.connect(self.cancelButton_clicked)
        self.okButton.clicked.connect(self.enterButton_clicked)
