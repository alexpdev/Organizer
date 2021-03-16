#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from os.path import dirname, abspath, join
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
sys.path.append(dirname(dirname(abspath(__file__))))
from src.sqlite import Walker,sql3,dbfile


class Window(QMainWindow):

    def __init__(self,app,walker,parent=None):
        super().__init__(parent=parent)
        self.app = app
        self.walker = walker
        self.central = QWidget(self)
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.table1 = QTableWidget(parent=self.central)
        self.centLayout.addWidget(self.table1)
        self.table1.setHorizontalHeaderLabels(walker.headers)
        print(self.table1.horizontalHeader())
        rows = walker.sql_select_all()
        count = 10
        for j,row in enumerate(rows):
            if count <= 0:
                break
            r = self.table1.rowCount()
            self.table1.insertRow(r)
            for i,col in enumerate(row):
                item = QTableWidgetItem(0)
                if isinstance(col,str):
                    item.setText(col)
                else:
                    item.setText(str(col))
                print(item.text())
                self.table1.setItem(r,i,item)
            print(self.table1.rowAt(r))
            count -= 1



if __name__ == '__main__':
    walker = Walker(dbfile=dbfile)
    app = QApplication(sys.argv)
    window = Window(app,walker,parent=None)
    window.show()
    sys.exit(app.exec())
