from organizer.utils import ListWidget, PushButton, QFileDialog, Qt, QListWidgetItem



class DirSelect(ListWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.ident = "DirSelect"
        self.items = []

    def add_item(self,item):
        item = QListWidgetItem()
        self.addItem(item)
        self.items.append(item)

class DirSelectButton(PushButton):
    def __init__(self,dirSelect,listWidget,text,parent=None):
        super().__init__(parent=parent)
        self.ident = "DirSelectButton"
        self.setText(text)
        self.dirWidget = dirSelect
        self.listWidget = listWidget
        self.pressed.connect(self.select_folder)

    def setAtties(self,text=None,widget=None):
        if text:
            self.setText(text)
        if widget:
            self.dirWidget = widget

    def select_folder(self):
        filedialog = QFileDialog()
        result = filedialog.getExistingDirectory()
        self.dirWidget.add_item(result)
        self.parent()._selection_made(result)

