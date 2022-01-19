

from gettext import gettext
from sqlite3 import Row
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from openpyxl import load_workbook
from csv import writer
 

class Ui_addblacklistpage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 311, 81))
        self.label.setStyleSheet("font: 24pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 951, 601))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ss4.png"))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 210, 391, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 175, 131, 21))
        self.label_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 280, 211, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 10pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getText);
        self.label_2.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADD BLACKLIST"))
        self.label_3.setText(_translate("MainWindow", "Enter URL"))
        self.pushButton.setText(_translate("MainWindow", "ADD BLACKLIST"))

        
    def getText(self): 
        url = self.textEdit.toPlainText()
        list=[url,'Phishing']
        # writer.close()
        with open('abc.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()
        

    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Addblacklistpage = QtWidgets.QMainWindow()
    ui = Ui_addblacklistpage()
    ui.setupUi(Addblacklistpage)
    Addblacklistpage.show()
    sys.exit(app.exec_())
