from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
from PyQt5 import QtCore, QtWidgets
import file_plots
def main_menu(self):
        self.mainMenu = self.menuBar()
        self.main_widget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.main_widget)
        self.scrollArea.setWidgetResizable(True)

def open_menu(self):
        self.openFile = QAction('Open File', self)
        self.openFolder = QAction('Open Folder', self)
        self.loadFileT = QAction ('&Load Trend Folder',self)
        self.openFile.setShortcut('Ctrl+O')
        self.openFile.setStatusTip('Open File')

def open_menu_actions(self):
        self.openFile.triggered.connect(self.file_open_message)
        self.openFolder.triggered.connect(self.file_folder)
        self.loadFileT.triggered.connect(self.file_output)
        self.statusBar()

def adding_open_actions(self):
        self.fileMenu = self.mainMenu.addMenu('&File')
        self.menuBar().addMenu(self.fileMenu)
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.openFolder)
        self.fileMenu.addAction(self.loadFileT)

def plot_menu(self):
        self.openPlotI = QAction('&Plot Ion Source', self)
        self.openPlotIV = QAction('&Plot Ion Source/Vacuum', self)
        self.openPlotM = QAction('&Plot Magnet', self)
        self.openPlotRF = QAction('&Plot RF', self)
        self.openPlotRFPower = QAction('&Plot RF Power', self)
        self.openPlotEx = QAction('&Plot Extraction', self)
        self.openPlotCol = QAction('&Plot Collimators',self)
        self.openPlotColTarget = QAction('&Plot Target/Collimators',self)
    


def adding_plot_actions(self):
        editorMenu = self.mainMenu.addMenu('&Plot Individual Files')
        editorMenu.addAction(self.openPlotI)
        editorMenu.addAction(self.openPlotIV)
        editorMenu.addAction(self.openPlotM)
        editorMenu.addAction(self.openPlotRF)
        editorMenu.addAction(self.openPlotRFPower)
        editorMenu.addAction(self.openPlotEx)
        editorMenu.addAction(self.openPlotCol)
        editorMenu.addAction(self.openPlotColTarget)

def plot_menu_source(self):
        self.openPlotI_S = QAction('&Plot Collimators/Ion Source', self)
        self.openPlotIV_S = QAction('&Plot Vacuum/Magnet vs Ion Source', self)
        self.openPlotRF_S = QAction('&Plot RF vs Ion Source', self)
        self.openPlotEx_S = QAction('&Plot Extraction vs Ion Source', self)
        self.openPlotI.setShortcut('Ctrl+E')
        self.openPlotI.setStatusTip('Plot files')


def plot_source_actions(self):
        self.openPlotI_S.triggered.connect(file_plots.file_plot_collimators_source)
        self.openPlotIV_S.triggered.connect(file_plots.file_plot_vacuum_source)
        self.openPlotRF_S.triggered.connect(file_plots.file_plot_rf_source)
        self.openPlotEx_S.triggered.connect(file_plots.file_plot_extraction_source)

def adding_plot_source(self):
        editorMenu_S = self.mainMenu.addMenu('&Plot Individual Files (Source)')
        editorMenu_S.addAction(self.openPlotI_S)
        editorMenu_S.addAction(self.openPlotIV_S)
        editorMenu_S.addAction(self.openPlotRF_S)
        editorMenu_S.addAction(self.openPlotEx_S)

def edit_menu(self):
        self.editplotmax = QAction('&Remove Max/Min Values',self)
        self.resetplotmax = QAction('&Add Max/Min Values',self)
        self.editplottarget1 = QAction('&Remove Target 1',self)
        self.editplottarget4 = QAction('&Remove Target 4',self)
        self.editplottarget1_add = QAction('&Add Target 1',self)
        self.editplottarget4_add = QAction('&Add Target 4',self)
        self.editplotweek = QAction('&Add Week/Remove days',self)
        self.editplotday = QAction('&Add day/Remove week',self)
        self.editplottime = QAction('&Add day gap',self)
        self.editplottime_remove = QAction('&Remove day gap',self)

def edit_actions(self):      
        self.editplotmax.triggered.connect(self.flag_max)
        self.resetplotmax.triggered.connect(self.flag_max_reset)
        self.editplottarget1.triggered.connect(self.flag_target1)
        self.editplottarget4.triggered.connect(self.flag_target4)
        self.editplottarget1_add.triggered.connect(self.flag_target1_add)
        self.editplottarget4_add.triggered.connect(self.flag_target4_add)
        self.editplotweek.triggered.connect(self.flag_week)
        self.editplotday.triggered.connect(self.flag_day)
        self.editplottime.triggered.connect(self.flag_day_gap)
        self.editplottime_remove.triggered.connect(self.flag_no_day_gap)

def adding_edit_actions(self):
        self.plotMenu = self.mainMenu.addMenu('&Edit Trends Plots')
        self.plotMenu.addAction(self.editplottime)
        self.plotMenu.addAction(self.editplottime_remove)
        self.plotMenu.addAction(self.editplotmax)
        self.plotMenu.addAction(self.resetplotmax)
        self.plotMenu.addAction(self.editplottarget1)
        self.plotMenu.addAction(self.editplottarget4)
        self.plotMenu.addAction(self.editplottarget1_add)
        self.plotMenu.addAction(self.editplottarget4_add)
        self.plotMenu.addAction(self.editplotweek)
        self.plotMenu.addAction(self.editplotday)

def remove_menu(self):                
        self.removeRow = QAction('&Remove selected row', self)
        self.removeCol = QAction('&Remove selected column', self)

def remove_menu_action(self):
        self.editorRemove = self.mainMenu.addMenu('&Remove')
        self.editorRemove.addAction(self.removeRow)
        #self.editorRemove.addAction(plotting_data.removeCol)
        self.editorRemove.triggered.connect(self.remove_row)


