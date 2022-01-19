
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainmenu(object):
    
    
    def openmaindetectpage(self):
        from main import Ui_MainDetectPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainDetectPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openwhitelistawebsitepage(self):
        from addwhitelistpg import Ui_addwhitelistpg
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addwhitelistpg()
        self.ui.setupUi(self.window)
        self.window.show()

    def openBlacklistawebsitepage(self):
        from addblacklistpg import Ui_addblacklistpage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addblacklistpage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openviewblacklistawebsitepage(self):
        from viewblacklistpg import Sheet
        self.window = QtWidgets.QMainWindow()
        self.ui = Sheet()
        # self.ui.setupUi(self.window)
        # self.window.show()

    def openviewwhitelistawebsitepage(self):
        from viewwhitelistpg import Sheet
        self.window = QtWidgets.QMainWindow()
        self.ui = Sheet()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 231, 61))
        self.label.setStyleSheet("font: 24pt \"Algerian\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 201, 111))
        self.pushButton.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(217, 0, 4);" "border-color: rgb(255, 255, 255);\n""border-radius:5px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openmaindetectpage)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 290, 201, 111))
        self.pushButton_3.setStyleSheet("background-color: rgb(193, 208, 255);\n"
"font: 10pt \"Times New Roman\";""border-color: rgb(255, 255, 255);\n""border-radius:5px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openBlacklistawebsitepage)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 160, 201, 111))
        self.pushButton_2.setStyleSheet("font: 10pt \"Times New Roman\";\n"
"background-color: rgb(250, 210, 52);""border-color: rgb(255, 255, 255);\n""border-radius:5px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openwhitelistawebsitepage)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 290, 201, 111))
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 10pt \"Times New Roman\";\n"
"background-color: rgb(255, 85, 127);\n"
"background-color: rgb(0, 85, 0);\n"
"background-color: rgb(107, 213, 0);""border-color: rgb(255, 255, 255);\n""border-radius:5px")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openviewblacklistawebsitepage)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 971, 601))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ss4.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 420, 201, 111))
        self.pushButton_5.setStyleSheet("background-color: rgb(7, 195, 240);\n"
"font: 10pt \"Times New Roman\";\n""border-color: rgb(255, 255, 255);\n""border-radius:5px"
"")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openviewwhitelistawebsitepage)
        self.pushButton_3.clicked.connect(self.openBlacklistawebsitepage)
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 30))
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
        self.label.setText(_translate("MainWindow", "MAIN MENU"))
        self.pushButton.setText(_translate("MainWindow", "DETECT A WEBSITE"))
        self.pushButton_3.setText(_translate("MainWindow", "BLACKLIST A WEBSITE"))
        self.pushButton_2.setText(_translate("MainWindow", "WHITELIST A WEBSITE"))
        self.pushButton_4.setText(_translate("MainWindow", "VIEW BLACKLISTS"))
        self.pushButton_5.setText(_translate("MainWindow", "VIEW WHITELISTS"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainmenu = QtWidgets.QMainWindow()
    ui = Ui_mainmenu()
    ui.setupUi(mainmenu)
    mainmenu.show()
    sys.exit(app.exec_())
