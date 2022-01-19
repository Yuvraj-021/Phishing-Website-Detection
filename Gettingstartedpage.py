

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def openWindow(self):
        from mainmenu import Ui_mainmenu
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainmenu()
        self.ui.setupUi(self.window)
        Gettingstartedpage.hide();
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 700)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 571, 111))
        self.label.setStyleSheet("font: 24pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 341, 351))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".vscode/Images/1.jpg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 510, 221, 81))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 170, 0);""border-color: rgb(255, 255, 255);\n""border-radius:5px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow) 
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 951, 641))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ss4.png"))
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 30))
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
        self.label.setText(_translate("MainWindow", "PHISHING WEBSITE DETECTION"))
        self.pushButton.setText(_translate("MainWindow", "Get Started"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gettingstartedpage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Gettingstartedpage)
    Gettingstartedpage.show()
    sys.exit(app.exec_())
