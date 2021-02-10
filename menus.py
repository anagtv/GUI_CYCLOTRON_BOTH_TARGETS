from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
from PyQt5 import QtCore, QtWidgets
import file_plots
import pandas as pd
import datetime
from datetime import timedelta
import numpy as np

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
        self.openPlotEx = QAction('&Plot Extraction/Collimators', self)
        self.openPlotColTarget = QAction('&Plot Target/Collimators',self)
    
def adding_plot_actions(self):
        editorMenu = self.mainMenu.addMenu('&Plot Individual Files')
        editorMenu.addAction(self.openPlotI)
        editorMenu.addAction(self.openPlotIV)
        editorMenu.addAction(self.openPlotM)
        editorMenu.addAction(self.openPlotRF)
        editorMenu.addAction(self.openPlotRFPower)
        editorMenu.addAction(self.openPlotEx)
        editorMenu.addAction(self.openPlotColTarget)

def plot_menu_source(self):
        self.openPlotI_S = QAction('&Plot Collimators/Ion Source', self)
        self.openPlotIV_S = QAction('&Plot Vacuum/Magnet vs Ion Source', self)
        self.openPlotRF_S = QAction('&Plot RF vs Ion Source', self)
        self.openPlotEx_S = QAction('&Plot Extraction vs Ion Source', self)
        self.openPlotI.setShortcut('Ctrl+E')
        self.openPlotI.setStatusTip('Plot files')

def plot_source_actions(self):
    ...
        #self.openPlotI_S.triggered.connect(file_plots.file_plot_collimators_source)
        #self.openPlotIV_S.triggered.connect(file_plots.file_plot_vacuum_source)
        #self.openPlotRF_S.triggered.connect(file_plots.file_plot_rf_source)
        #self.openPlotEx_S.triggered.connect(file_plots.file_plot_extraction_source)

def adding_plot_source(self):
        editorMenu_S = self.mainMenu.addMenu('&Plot Individual Files (Source)')
        editorMenu_S.addAction(self.openPlotI_S)
        editorMenu_S.addAction(self.openPlotIV_S)
        editorMenu_S.addAction(self.openPlotRF_S)
        editorMenu_S.addAction(self.openPlotEx_S)

def edit_menu(self):
        self.plotMenu = self.mainMenu.addMenu('&Edit Trends Plots')
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


def adding_edit_actions(self):
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
    #
def removing_adding_gap(self):
    time_list = (list(range(len(self.tfs_input.FILE))))
    if self.flag_no_gap == "1":
        try:
           ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/10)]   
           ticks_to_use_list = time_list[::int(len(self.tfs_input.FILE)/10)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
        except:
           ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/2)]   
           ticks_to_use_list = time_list[::int(len(self.tfs_input.FILE)/2)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
    else: 
        ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/15)]   
        ticks_to_use_list = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/15)] 
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)

def getting_foil_change_position(sel_system,index_foil,index_foil_sorted,unique_index_foil):
    for i in range(len(index_foil)):
        checking_value = (index_foil[i] == list(range(min(index_foil[i]), max(index_foil[i])+1)))
        if len(index_foil) == 1:
           checking_value =  checking_value[0]
        if checking_value == True:
            sel_system.horizontal_mark_plot.append(index_foil_sorted_position[i][0])
            sel_system.horizontal_value_plot.append(unique_index_foil_1[i])
        else: 
           for j in range(len(index_foil_1[i])):
                sel_system.check_line(index_foil_1[i][j],unique_index_foil_1[i],i,index_foil_sorted_1_position[i][j])
           sel_system.horizontal_mark_plot.append(sel_system_1.verification_position)
           sel_system.horizontal_value_plot.append(sel_system_1.valuei)
           sel_system.counter.append(sel_system_1.counteri)

def removing_days_adding_weeks(self): 
    x_values = []
    week_number = []
    for i in range(0,len(self.tfs_input.DATE),10):
        x = i
        x_values.append(i)
        self.sc3.axes.text(x-0.3, self.set_configuration,self.tfs_input.DATE.iloc[i][5:], fontsize=12,rotation=90)
    for i in range(0,len(self.tfs_input),1):
           date_to_week = datetime.datetime.strptime(self.tfs_input.DATE.iloc[i],"%Y-%m-%d")
           week_number.append(date_to_week.isocalendar()[1])
    #
