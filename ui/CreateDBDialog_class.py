from PyQt6.QtWidgets import QMainWindow
from ui.py.CreateDBDialogUi import Ui_NewFileDialog


class NewFileDialogCls(QtWidgets.QMainWindow, Ui_NewFileDialog):
    def __init__(self):
        super(NewFileDialogCls, self).__init__()
        self.setupUi(self)

        self.add_actions()



    def cancelButton_action(self):
        pass

    def okButton_action(self):
        pass

    def add_actions(self):
        self.okButton.clicked.connect(self.okButton_action)
        self.cancelButton.clicked.connect(self.cancelButton_action)
