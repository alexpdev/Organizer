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
