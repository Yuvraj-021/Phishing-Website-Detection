from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from viewblacklistpg import Ui_viewblacklistpg
import csv
import sys


class Main(QtWidgets.QMainWindow, Ui_viewblacklistpg):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    
    def displayTable(self):
        # path = QFileDialog.getOpenFileName(None, 'Open a file', '', '')
        path = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'All Files (*.*)')
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())