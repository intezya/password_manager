from PyQt6.QtWidgets import QMainWindow
from ui.py.NewEntryUi import Ui_addNewEntry

from db import AddEntry

def GetAndClearFields(self: object) -> dict[str, str]:
    title = self.titleLine.text()
    username = self.usernameLine.text()
    password = self.passwordLine.text()
    link = self.linkLine.text()
    notes = self.notesLine.text()

    self.titleLine.setText("")
    self.usernameLine.setText("")
    self.passwordLine.setText("")
    self.linkLine.setText("")
    self.notesLine.setText("")

    return {"title": title,
            "username": username,
            "password": password,
            "link": link,
            "notes": notes}


class NewEntryDialogCls(QMainWindow, Ui_addNewEntry):
    def __init__(self, obj: object):
        super(NewEntryDialogCls, self).__init__()
        self.obj = obj
        self.setupUi(self)

        self.add_actions()

    def cancelButton_action(self):
        self.close()

    def addButton_action(self):
        info = GetAndClearFields(self)

        print(f'[DEBUG] Info added: {info}')

        AddEntry(self.obj, info)

        self.close()

    def add_actions(self):
        self.cancelButton.clicked.connect(self.cancelButton_action)
        self.addButton.clicked.connect(self.addButton_action)
