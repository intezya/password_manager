from ui.py.MainWindowUi import Ui_MainWindow

from ui.OpenDialog_class import OpenDialogCls
from ui.CreateDBDialog_class import NewFileDialogCls
from ui.NewEntry_class import NewEntryDialogCls

from ui.utils import CreateNewFile, OpenFile, SaveDB

from PyQt6.QtWidgets import QMainWindow


class MainWindowCls(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowCls, self).__init__()
        self.opened = False
        self.con = None

        self.setupUi(self)
        self.add_actions()

    def add_actions(self):
        self.OpenFileButton.clicked.connect(self.OpenFileButton_clicked)
        self.NewFileButton.clicked.connect(self.NewFileButton_clicked)
        self.SaveFileButton.clicked.connect(self.SaveFileButton_clicked)
        self.addButton.clicked.connect(self.addButton_clicked)

    def OpenFileButton_clicked(self):
        file_path = OpenFile(self)
        print(file_path)  # TODO: delete this line

        if file_path != '':
            self.openDialog = OpenDialogCls(self)
            self.openDialog.pathLine.setText(file_path)

            self.openDialog.show()

    def NewFileButton_clicked(self):
        file_path = CreateNewFile(self)
        print(file_path)  # TODO: delete this line

        self.newFileDialog = NewFileDialogCls(self)
        self.newFileDialog.pathLine.setText(file_path)
        self.newFileDialog.show()

    def SaveFileButton_clicked(self):
        if self.opened:
            print('saved') # TODO: delete this line
            SaveDB(self)

    def addButton_clicked(self):
        if self.opened:
            self.newEntryDialog = NewEntryDialogCls(self)
            self.newEntryDialog.show()
