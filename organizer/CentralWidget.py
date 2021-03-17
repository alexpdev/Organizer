from organizer.utils import Widget


class CentralWidget(Widget):
    def __init__(self,walker,parent=None):
        super().__init__(parent=parent)
        self.walker = walker


    def _selection_made(self,result):
        print(dir(self))
        print(self.children())
        print("SIGNAL SENT")
        for child in self.children():
            if hasattr(child,"ident"):
                if child.ident == "FileTable":
                    child.addDir(result)
                    print("FOUND FILE TABLE")

    def addWalker(self,walker):
        self.walker = walker

