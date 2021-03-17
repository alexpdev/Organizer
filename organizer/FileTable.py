from pathlib import Path
from organizer.utils import TableWidget, TableWidgetItem

class FileTable(TableWidget):
    def __init__(self,rows,cols,parent=None):
        super().__init__(rows,cols,parent=parent)
        self.ident = "FileTable"
        self.fileDirs = []
        self.dirs_walked = []
        self.walker = parent.walker
        self.setHorizontalHeaderLabels(self.walker.headers)

    def contents(self):
        """ collect all value pairs in the table to use as phrase.table """
        vals = []
        for num in range(self.rowCount()):
            for col in range(self.columnCount()):
                item = self.item(num,col)
                vals.append(item)
        return vals


    def addDir(self,path):
        self.fileDirs.append(path)
        self.contents()
        path = Path(path)
        lst = []
        action = lambda x: lst.append(self.walker.track(str(x)).format_order())
        self.walker.walk(path,action)
        self.populate_rows(lst)

    def populate_rows(self,lst):
        for row in lst:
            r = self.rowCount()
            self.setRowCount(r+1)
            for i,col in enumerate(row):
                item = TableWidgetItem(str(col),0)
                self.setItem(r,i,item)




