from PyQt6.QtWidgets import QApplication
from ui.MainWindow_class import MainWindowCls


class PasswordManager(MainWindowCls):
    pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec())
