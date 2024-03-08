from PyQt6.QtWidgets import QMainWindow
from ui.py.CreateDBDialogUi import Ui_NewFileDialog
import sqlite3
from db import create_table


class NewFileDialogCls(QMainWindow, Ui_NewFileDialog):
    def __init__(self, obj: object):
        super(NewFileDialogCls, self).__init__()
        self.obj = obj
        self.setupUi(self)

        self.add_actions()

    def cancelButton_action(self):
        self.close()

    def okButton_action(self):
        master_key = self.passwordLine.text()
        db_path = self.pathLine.text()
        con = sqlite3.connect(db_path)

        create_table(con, master_key)

        self.close()

    def add_actions(self):
        self.okButton.clicked.connect(self.okButton_action)
        self.cancelButton.clicked.connect(self.cancelButton_action)
