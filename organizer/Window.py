#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from os.path import dirname, abspath, join
sys.path.append(dirname(dirname(abspath(__file__))))
from organizer.DirSelect import DirSelect, DirSelectButton
from organizer.FileTable import FileTable
from organizer.CentralWidget import CentralWidget
from organizer.utils import Widget, VLayout, HLayout, GLayout, MainWindow, Application,TableWidgetItem
from organizer.Walker import Walker


class Window(MainWindow):

    def __init__(self,app,walker,parent=None):
        super().__init__(parent=parent)
        self.resize(600,800)
        self.app = app
        self.walker = walker
        self.central = CentralWidget(self.walker,parent=None)
        self.central.addWalker(self.walker)
        self.centLayout = VLayout()
        self.hlayout = HLayout()
        self.glayout = GLayout()
        self.central.setLayout(self.centLayout)
        self.table = FileTable(0,4,parent=self.central)
        self.centLayout.addWidget(self.table)
        self.dirSelect = DirSelect(self.central)
        self.button = DirSelectButton(self.dirSelect,self.table,"Select Folders",self.central)
        self.hlayout.addWidget(self.dirSelect)
        self.centLayout.addLayout(self.hlayout)
        self.centLayout.addWidget(self.button)
        self.setCentralWidget(self.central)


    # def populate_rows(self):
    #     labels = self.walker.headers
    #     self.table.setHorizontalHeaderLabels(labels)
    #     rows = self.walker.get_all()
    #     for row in rows:
    #         r = self.table.rowCount()
    #         self.table.setRowCount(r+1)
    #         for i,col in enumerate(row):
    #             item = TableWidgetItem(str(col),0)
    #             self.table.setItem(r,i,item)






if __name__ == '__main__':
    walker = Walker()
    app = Application(sys.argv)
    window = Window(app,walker,parent=None)
    window.show()
    sys.exit(app.exec())
