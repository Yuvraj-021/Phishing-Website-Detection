 
from PyQt5 import QtCore, QtGui, QtWidgets
from csv import writer
 

class Ui_addwhitelistpg(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -230, 1461, 1111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ss4.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 291, 51))
        self.label.setStyleSheet("font: 24pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 91, 16))
        self.label_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 220, 391, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 270, 211, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 10pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getText);
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
        self.label.setText(_translate("MainWindow", "ADD WHITELIST"))
        self.label_3.setText(_translate("MainWindow", "Enter URL"))
        self.pushButton.setText(_translate("MainWindow", "ADD WHITELIST"))


    def getText(self): 
        url = self.textEdit.toPlainText()
        list=[url,'Legitimate']
        with open('Legitimatesites.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(list)
            f_object.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWhitelistpage = QtWidgets.QMainWindow()
    ui = Ui_addwhitelistpg()
    ui.setupUi(AddWhitelistpage)
    AddWhitelistpage.show()
    sys.exit(app.exec_())
