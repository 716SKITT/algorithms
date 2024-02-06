from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.scrollArea_Delete_Files = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_Delete_Files.setGeometry(QtCore.QRect(0, 370, 481, 300))
        self.scrollArea_Delete_Files.setStyleSheet("margin: 5 0 5 10;")
        self.scrollArea_Delete_Files.setWidgetResizable(True)
        self.scrollArea_Delete_Files.setObjectName("scrollArea_Delete_Files")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 459, 278))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.scrollArea_Delete_Files.setWidget(self.scrollAreaWidgetContents_2)

        # Add_File_Button нужна для выбора файла из проводника
        self.Add_File_Button = QtWidgets.QPushButton(self.tab)
        self.Add_File_Button.setGeometry(QtCore.QRect(380, 320, 91, 31))
        self.Add_File_Button.setObjectName("Add_File_Button")

        # Exclude_File_Button нужна для удаления файла из списка выбраных
        self.Exclude_File_Button = QtWidgets.QPushButton(self.tab)
        self.Exclude_File_Button.setGeometry(QtCore.QRect(270, 320, 91, 31))
        self.Exclude_File_Button.setObjectName("Exclude_File_Button")

        self.checkBox_Delete_Files = QtWidgets.QCheckBox(self.tab)
        self.checkBox_Delete_Files.setGeometry(QtCore.QRect(10, 210, 471, 51))
        self.checkBox_Delete_Files.setTristate(False)
        self.checkBox_Delete_Files.setObjectName("checkBox_Delete_Files")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 265, 491, 31))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Add_File_Button.setText(_translate("MainWindow", "Choose File"))
        self.Exclude_File_Button.setText(_translate("MainWindow", "Delete File"))
        self.checkBox_Delete_Files.setText(_translate("MainWindow", "Удалять файлы при активации"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\">Добавьте или уберите файлы из списка для удаленя ниже</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.Add_File_Button.clicked.connect(self.getFileName)

    def getFileName(self):
        filename = QFileDialog.getOpenFileName(None, "Выбрать файл", ".", "All Files(*)")

        def files1():

            def lastik():
                file_path = filename
                lastroad = file_path.split('\\')[-1]
                print(lastroad)

            with open('data.txt', 'a', encoding="utf8") as file:
                file.write(filename + '\n')
            with open('data.txt', 'r', encoding="utf8") as file:
                text = file.readlines()
            lasted = open("data.txt", "r")

        print(filename)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())