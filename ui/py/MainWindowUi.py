# Form implementation generated from reading ui file 'src/ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 574)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OpenFileButton.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.SaveFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveFileButton.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.SaveFileButton.setObjectName("SaveFileButton")
        self.NewFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NewFileButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.NewFileButton.setObjectName("NewFileButton")
        self.categoryView = QtWidgets.QListView(parent=self.centralwidget)
        self.categoryView.setGeometry(QtCore.QRect(10, 60, 151, 451))
        self.categoryView.setObjectName("categoryView")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 60, 601, 451))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(170, 10, 31, 31))
        self.addButton.setObjectName("addButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFileButton.setText(_translate("MainWindow", "Open"))
        self.SaveFileButton.setText(_translate("MainWindow", "Save"))
        self.SaveFileButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.NewFileButton.setText(_translate("MainWindow", "New"))
        self.NewFileButton.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.addButton.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
