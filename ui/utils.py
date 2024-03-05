import sqlite3

from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem

from db import getAllInfo, writeDB

def CreateNewFile(self):
    file_path = QFileDialog.getSaveFileName(self, "Save File", "/", "Data Base File (*.db)")[0]
    # if file_path:
    #     with open(file_path, 'w') as file:
    #         pass

    return file_path


def OpenFile(self):
    db_path = QFileDialog.getOpenFileName(self, "Open File", "/", "Data Base File (*.db)")[0]

    return db_path


def DisplayDB(self: object) -> None:
    # Comes from OpenFileButton_clicked

    print(self.con)

    data = getAllInfo(self)
    print(data)
    self.tableWidget.setRowCount(len(data))
    self.tableWidget.setColumnCount(len(data[0]))

    for row, rowData in enumerate(data):
        for col, value in enumerate(rowData):
            item = QTableWidgetItem(str(value))
            self.tableWidget.setItem(row, col, item)


def SaveDB(self: object) -> None:
    # TODO: realise saving DB
    values = []
    data = []

    for row in range(self.tableWidget.rowCount()):
        for column in range(self.tableWidget.columnCount()):
            try:
                item = self.tableWidget.item(row, column)
                # while len(values) !=
                value = item.text()
            except Exception:
                value = ""
            values.append(value)
            # print(values)
            if len(values) == 5:
                data.append([item for item in values])
                values = []
    try:
        if data:
            writeDB(self, data)
        else: print(unluck)
    except Exception as e:
        print(e)


