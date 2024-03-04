from PyQt6.QtWidgets import QApplication
from ui.MainWindow_class import MainWindowCls



class PasswordManager(MainWindowCls):
    def __init__(self):
        super(PasswordManager, self).__init__()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec())
