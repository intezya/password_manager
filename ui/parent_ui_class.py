from PyQt6.QtWidgets import QMainWindow


class BaseUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.add_actions()


    def add_actions(self) -> None:
        pass
