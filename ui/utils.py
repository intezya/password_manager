from PyQt6.QtWidgets import QFileDialog

def CreateNewFile(self):
    file_path = QFileDialog.getSaveFileName(self, "Save File", "/", "Data Base File (*.db)")[0]
    # if file_path:
    #     with open(file_path, 'w') as file:
    #         pass

    return file_path


def OpenFile(self):
    db_path = QFileDialog.getOpenFileName(self, "Open File", "/", "Data Base File (*.db)")[0]

    return db_path