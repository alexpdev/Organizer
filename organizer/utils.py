from os.path import dirname, join, abspath
from PyQt6 import QtWidgets,QtCore,QtGui
from PyQt6.QtWidgets import (QMainWindow, QApplication, QTableWidget,
                            QPushButton, QLabel, QMenu, QWidget,
                            QListWidget, QHBoxLayout, QVBoxLayout, QGridLayout,
                            QTableWidgetItem, QFileDialog)



PROJECT_DIR = dirname(dirname(abspath(__file__)))
DB_DIR = join(PROJECT_DIR,"data")
DB_FILE = join(DB_DIR,"files.db")
Qt = QtCore.Qt
QListWidgetItem = QtWidgets.QListWidgetItem
TableWidgetItem = QTableWidgetItem
Widgets = QtWidgets
Core = QtCore
Gui = QtGui
MainWindow = QMainWindow
Application = QApplication
TableWidget = QTableWidget
PushButton = QPushButton
Label = QLabel
Menu = QMenu
Widget = QWidget
ListWidget = QListWidget
HLayout = QHBoxLayout
VLayout = QVBoxLayout
GLayout = QGridLayout

QFileDialog = QFileDialog


# class MainWindow(QMainWindow):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class Application(QApplication):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class TableWidget(QTableWidget):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class PushButton(QPushButton):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class Label(QLabel):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class Menu(QMenu):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class Widget(QWidget):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class ListWidget(QListWidget):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class HBoxLayout(QHBoxLayout):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class VBoxLayout(QVBoxLayout):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

# class GridLayout(QGridLayout):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)
