#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from organizer.DirSelect import DirSelect, DirSelectButton
from organizer.FileTable import FileTable
from organizer.CentralWidget import CentralWidget
from organizer.utils import VLayout, MainWindow, Application
from organizer.Walker import Walker


class Window(MainWindow):

    def __init__(self,app,walker,parent=None):
        super().__init__(parent=parent)
        self.resize(600,800)
        self.app = app
        self.walker = walker
        self.central = CentralWidget(self.walker,parent=None)
        self.centLayout = VLayout()
        self.central.setLayout(self.centLayout)
        self.table = FileTable(0,4,parent=self.central)
        self.centLayout.addWidget(self.table)
        self.dirSelect = DirSelect(self.central)
        self.button = DirSelectButton(self.dirSelect,self.table,"Select Folders",self.central)
        self.centLayout.addWidget(self.dirSelect)
        self.centLayout.addWidget(self.button)
        self.setCentralWidget(self.central)

if __name__ == '__main__':
    walker = Walker()
    app = Application(sys.argv)
    window = Window(app,walker,parent=None)
    window.show()
    sys.exit(app.exec())
