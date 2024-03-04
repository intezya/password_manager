from ui.py.MainWindowUi import Ui_MainWindow
from PyQt6 import QtWidgets

class MainWindowCls(BaseUI, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.add_actions()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowCls()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())