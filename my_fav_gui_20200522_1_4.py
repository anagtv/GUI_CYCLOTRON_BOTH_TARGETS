#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license

# Title: PyQt5 lesson 14              Version: 1.0
# Date: 09-01-17                      Language: python3
# Description: pyqt5 gui and opening files
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################
# do something


import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
import matplotlib.pyplot as plt
#import saving_files_summary
#import saving_files_summary_list
import plotting_summary_files_one_target_1_4
import saving_files_summary_list_20200420
import numpy as np
import os
import tfs
from matplotlib.widgets import CheckButtons
import flag_selection
import file_plots
#import datetime
from datetime import time
import saving_trends
import managing_files
import selecting_trends

COLUMNS_SOURCE = ["FILE","DATE","TARGET","FOIL","CURRENT_MAX", "CURRENT_MIN","CURRENT_AVE","CURRENT_STD","VOLTAGE_MAX","VOLTAGE_MIN","VOLTAGE_AVE","VOLTAGE_STD","HFLOW",
    "RATIO_MAX", "RATIO_MIN","RATIO_AVE","RATIO_STD"] 
COLUMNS_VACUUM = ["FILE","DATE","TARGET","FOIL","PRESSURE_MAX","PRESSURE_MIN","PRESSURE_AVE","PRESSURE_STD"]
COLUMNS_MAGNET = ["FILE","DATE","TARGET","FOIL","CURRENT_MAX","CURRENT_MIN","CURRENT_AVE","CURRENT_STD"]
COLUMNS_RF =  ["FILE","DATE","TARGET","FOIL","DEE1_VOLTAGE_MAX","DEE1_VOLTAGE_MIN","DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_MAX","DEE2_VOLTAGE_MIN","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD",
    "FORWARD_POWER_MAX","FORWARD_POWER_MIN","FORWARD_POWER_AVE","FORWARD_POWER_STD","REFLECTED_POWER_MAX","REFLECTED_POWER_MIN","REFLECTED_POWER_AVE","REFLECTED_POWER_STD",
    "PHASE_LOAD_MAX","PHASE_LOAD_MIN","PHASE_LOAD_AVE","PHASE_LOAD_STD"]
COLUMNS_BEAM = ["FILE","DATE","TARGET","FOIL","COLL_CURRENT_L_MAX","COLL_CURRENT_L_MIN","COLL_CURRENT_L_AVE","COLL_CURRENT_L_STD","COLL_CURRENT_R_MAX","COLL_CURRENT_R_MIN","COLL_CURRENT_R_AVE","COLL_CURRENT_R_STD"
    ,"RELATIVE_COLL_CURRENT_L_MAX","RELATIVE_COLL_CURRENT_L_MIN","RELATIVE_COLL_CURRENT_L_AVE","RELATIVE_COLL_CURRENT_L_STD",
    "RELATIVE_COLL_CURRENT_R_MAX","RELATIVE_COLL_CURRENT_R_MIN","RELATIVE_COLL_CURRENT_R_AVE","RELATIVE_COLL_CURRENT_R_STD",
    "TARGET_CURRENT_MAX","TARGET_CURRENT_MIN","TARGET_CURRENT_AVE","TARGET_CURRENT_STD","FOIL_CURRENT_MAX","FOIL_CURRENT_MIN","FOIL_CURRENT_AVE","FOIL_CURRENT_STD",
    "EXTRACTION_LOSSES_MAX","EXTRACTION_LOSSES_MIN","EXTRACTION_LOSSES_AVE","EXTRACTION_LOSSES_STD"]
COLUMNS_EXTRACTION = ["FILE","DATE","TARGET","FOIL","CAROUSEL_POSITION_MAX","CAROUSEL_POSITION_MIN","CAROUSEL_POSITION_AVE","CAROUSEL_POSITION_STD"
    ,"BALANCE_POSITION_MAX","BALANCE_POSITION_MIN","BALANCE_POSITION_AVE","BALANCE_POSITION_STD"]
COLUMNS_TRANSMISSION = ["FILE","DATE","TARGET","TRANSMISSION","FOIL"]
COLUMNS_FILLING = ["FILE","TIME_LIST","DATE","TARGET","RELATIVE_VOLUME"]
COLUMNS_FLUCTUATIONS = ["FILE","TIME_LIST","DATE","TARGET","PRESSURE_FLUCTUATIONS"]


#matplotlib.use('Qt5Agg')

class UpdateFrame(QFrame):
    def __init__(self, parent=None):
        super(UpdateFrame, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        for i in range(25):
            listFrame = QFrame()
            listFrame.setStyleSheet('background-color: white;'
                                    'border: 20px solid #20b2aa;'
                                    'border-radius: 0px;'
                                    'margin: 2px;'
                                    'padding: 2px')
            listFrame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            listFrame.setGeometry(50, 50, 1500, 1000)
            
            layout.addWidget(listFrame)

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        frameWidget = UpdateFrame(self)
        self.setWindowTitle("Cyclotron Analysis")
        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))
        #
        self.mainMenu = self.menuBar()
        self.main_widget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.main_widget)
        self.scrollArea.setWidgetResizable(True)

        # INIALIZE VARIABLE
        self.flags()
        self.initial_df()
        # STARTING MENUS
        #
        self.open_menu()
        self.open_menu_actions()
        #
        self.edit_menu()
        self.edit_actions()
        #
        self.plot_menu()
        self.plot_actions()
        #
        self.plot_menu_source()
        self.plot_source_actions()
        #
        self.remove_menu()
        #
        self.adding_open_actions()
        self.adding_edit_actions()
        self.adding_plot_actions()
        self.adding_plot_source()
        self.remove_menu_action()
        #
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        lay = QtWidgets.QVBoxLayout(self.main_widget)   
        self.home(lay)
        self.setMinimumSize(1000, 800)

    def flags(self): 
        self.current_row = 0
        self.current_row_folder = 0
        self.current_row_statistics = 0
        self.current_row_analysis = 0 
        self.row_to_plot = 0
        self.current_row_observables = 0
        self.current_row_observables_tab3 = 0      
        self.target_1_value = 0
        self.target_4_value = 0
        self.max_min_value = 0        
        self.week_value = 0
        self.day_value = 1
        self.flag_no_gap = 1

    def initial_df(self):               
        self.df_source = pd.DataFrame(columns=COLUMNS_SOURCE)
        self.df_vacuum = pd.DataFrame(columns=COLUMNS_VACUUM)
        self.df_magnet = pd.DataFrame(columns=COLUMNS_MAGNET)
        self.df_beam = pd.DataFrame(columns=COLUMNS_BEAM )
        self.df_rf = pd.DataFrame(columns=COLUMNS_RF)
        self.df_extraction = pd.DataFrame(columns=COLUMNS_EXTRACTION)
        self.df_transmission = pd.DataFrame(columns=COLUMNS_TRANSMISSION)
        self.df_filling_volume = pd.DataFrame(columns=COLUMNS_FILLING)
        self.df_pressure_fluctuations = pd.DataFrame(columns=COLUMNS_FLUCTUATIONS)

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
    
    def plot_actions(self):
        self.openPlotI.setShortcut('Ctrl+E')
        self.openPlotI.setStatusTip('Plot files')
        self.openPlotI.triggered.connect(self.file_plot)
        self.openPlotIV.triggered.connect(self.setting_plot_vacuum)
        self.openPlotM.triggered.connect(file_plots.file_plot_magnet)
        self.openPlotRF.triggered.connect(self.setting_plot_RF)
        self.openPlotRFPower.triggered.connect(self.setting_plot_RF_power)
        self.openPlotEx.triggered.connect(file_plots.file_plot_extraction)
        self.openPlotCol.triggered.connect(file_plots.file_plot_collimation)
        self.openPlotColTarget.triggered.connect(file_plots.file_plot_collimation_target)

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
        self.editorRemove.addAction(self.removeCol)
        self.editorRemove.triggered.connect(self.remove_row)

    def file_plot(self):
        file_plots.file_plot(self)

    def setting_plot_vacuum(self):
        self.x_values = self.file_df.Time
        self.y_values_left = self.file_df.Vacuum_P.astype(float)*1e5
        self.y_values_right = self.file_df.Arc_I.astype(float)
        self.label_left = r"Vacuum P [$10^{-5}$ mbar]"
        self.label_right = "Source Current [mA]"
        file_plots.file_plot_vacuum(self)

    def setting_plot_RF(self):
        self.x_values = self.file_df.Time 
        self.y_values_left_1 = self.file_df.Dee_1_kV.astype(float)
        self.y_values_left_2 = self.file_df.Dee_2_kV.astype(float)
        self.legend_left_1 = "Dee1"
        self.legend_left_2 = "Dee2"
        self.label_left = "Voltage [kV]"
        self.y_values_right_1 = self.file_df.Flap1_pos.astype(float)
        self.y_values_right_2 = self.file_df.Flap2_pos.astype(float)
        self.legend_right_1 = "Flap1"
        self.legend_right_2 = "Flap2"
        self.label_right = "Position [%]"
        file_plots.file_plot_two_functions(self)

    def setting_plot_RF_power(self):
        self.x_values = self.file_df.Time
        self.y_values_left_1 = self.file_df.RF_fwd_W.astype(float)
        self.y_values_left_2 = self.file_df.RF_refl_W.astype(float)
        self.legend_left_1 = "Forwared"
        self.legend_left_2 = "Reflected"
        self.label_left = "Power [kW]"
        self.y_values_right = self.file_df.Phase_load.astype(float)
        self.legend_right = "Phase load"
        self.label_right = "Phase load"
        file_plots.file_plot_two_one_functions(self)

    def home(self, main_layout):
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        # Add tabs
        self.tabs.addTab(self.tab1,"Individual Files")
        self.tabs.addTab(self.tab3,"Counter")
        self.tabs.addTab(self.tab2,"Trends")        
        # 
        widget = QtWidgets.QWidget(self.tab1)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        # TAB 1
        self.tab1_layout()
        self.tab1_selection()
        self.tab1_data()
        # TAB 2
        self.tab2_layout()
        self.tab2_selection()
        self.tab2_data()
        # TAB 3
        self.tab3_layout()
        self.tab3_data()
        # Add tabs to widget
        main_layout.addWidget(self.tabs)
        # Add tabs to widget
        main_layout.addWidget(self.tabs)
        #self.setLayout(self.layout)
       
    # TAB PARAMETERES

    def tab1_layout(self):
        self.tab1.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab1.main_layout.setAlignment(Qt.AlignTop)
        self.tab1.scroll = QtWidgets.QScrollArea()
        self.tab1.setLayout(self.tab1.main_layout)

        self.sc1 = Canvas(width=15, height=24, dpi=100, parent=self.tab1)   
        self.sc1.setGeometry(QtCore.QRect(20, 10, 1100, 500))
        self.toolbar_tab1 = NavigationToolbar(self.sc1, self.tab1)
        self.toolbar_tab1.setGeometry(QtCore.QRect(20, 520, 1450, 50))

        self.table_summary_log = QtWidgets.QTableWidget(self.tab1)
        self.table_summary_log.setGeometry(QtCore.QRect(1130, 10, 340, 500))
        self.table_summary_log.setRowCount(20)
        self.table_summary_log.setColumnCount(2)

        self.btn = QPushButton('Cyclotron trends', self.tab1)
        self.btn.setGeometry(QtCore.QRect(20, 740, 1450, 25))
        self.btn.clicked.connect(self.folder_analyze)

        self.tableWidget = QTableWidget(self.tab1)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(30)
        self.tableWidget.setGeometry(QtCore.QRect(20, 580, 1450, 150))

        self.tableWidget_logfiles = QTableWidget(self.tab1)
        self.tableWidget_logfiles.setRowCount(4)
        self.tableWidget_logfiles.setColumnCount(1500)
        self.tableWidget_logfiles.setGeometry(QtCore.QRect(20, 780, 1450, 140))

    def tab1_data(self):   
        observables = ["Time","Vacuum [10e-5 mbar]", "Current [A]", "Ion source [mA]", "Dee 1 Voltage [kV]", "Dee 2 Voltage [kV]","Flap 1 pos [%]","Flap 2 pos [%]","Fwd Power [kW]","Refl Power [kW]","Extraction position [%]","Balance position [%]", "Foil Number",r"Foil current [uA]", r"Target current [uA]", r"Collimator current l [uA]"
        , r"Collimator current r [uA]", "Collimator current l rel[%]", "Collimator current r rel [%]","Target current rel [%]"]
        self.table_summary_log.setHorizontalHeaderLabels(["Observable","Instant value"])
        for i in range(len(observables)):
          self.table_summary_log.setItem(self.current_row_observables,0, QTableWidgetItem(observables[i]))
          self.current_row_observables += 1
        self.table_summary_log.setColumnWidth(0,180)
        self.table_summary_log.setColumnWidth(1,140)
        folder_labels = ["Cyclotron","Number of logs"]
        file_numbers = list(range(1,1499))
        for number in file_numbers:
            folder_labels.append(str(number))
        folder_labels.append("Path")
        self.tableWidget_logfiles.setHorizontalHeaderLabels(folder_labels)     
        self.tableWidget.setHorizontalHeaderLabels(["File Name","Cyclotron","Date","Target","Number of Sparks (Dee 1)","Number of Sparks (Dee 2)","Average vacuum [mbar]", "Magnet current [A]", "Ion source [mA]", "Dee 1 Voltage [V]", "Dee 2 Voltage [V]", "Target current [uA]", "Foil current [uA]", "Collimator l current [uA]", "Collimator r current [uA]","Relative Collimators current/Foil [%]", "Relative Target current/Foil [%]","Path"])
        header2 = self.tableWidget.horizontalHeader()  
        header2.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 

    def tab1_selection(self):
        selection = self.tableWidget.selectionModel()
        selection.selectionChanged.connect(self.handleSelectionFile)
        self.show()
        self.selection_folder = self.tableWidget_logfiles.selectionModel()
        self.selection_folder.selectionChanged.connect(self.handleSelectionFolder)
        self.show()
    
    def tab2_layout(self):
        self.tab2.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.main_layout)
        self.widget_tab2 = QtWidgets.QWidget(self.tab2)
        self.widget_tab2.setGeometry(QtCore.QRect(250, 20, 1500, 251))
        self.widget_tab2.setObjectName("widget")
        self.sc3 = Canvas_tab2(width=15, height=20, dpi=100, parent=self.tab2) 
        self.sc3.setGeometry(QtCore.QRect(280, 10, 1200, 820))
        self.toolbar_tab2 = NavigationToolbar(self.sc3, self.tab2)
        self.toolbar_tab2.setGeometry(QtCore.QRect(280, 800, 1200, 30))
        self.tablefiles_tab2 = QtWidgets.QTableWidget(self.tab2)
        self.tablefiles_tab2.setGeometry(QtCore.QRect(20, 10, 250, 500))
        self.tablefiles_tab2.setObjectName("tableWidget")
        self.tablefiles_tab2.setRowCount(20)
        self.tablefiles_tab2.setColumnCount(2)
        self.tablefiles_tab2.setColumnWidth(0, 80)
        self.tablefiles_tab2.setColumnWidth(1, 150)
        self.tablestatistic_tab2 = QtWidgets.QTableWidget(self.tab2) 
        self.tablestatistic_tab2.setGeometry(QtCore.QRect(20, 530, 250, 300))
        self.tablestatistic_tab2.setRowCount(11)
        self.tablestatistic_tab2.setColumnCount(2)
        self.tablestatistic_tab2.setColumnWidth(0, 110)
        self.tablestatistic_tab2.setColumnWidth(1, 115)     
        
    def tab2_data(self):
        self.tablefiles_tab2.setHorizontalHeaderLabels(["Component","File"])
        self.tablestatistic_tab2.setHorizontalHeaderLabels(["Information","Summary"]) 
        self.tablestatistic_tab2.setObjectName("tableView")
   
    def tab2_selection(self):
        self.selection_component = self.tablefiles_tab2.selectionModel()
        self.selection_component.selectionChanged.connect(selecting_trends.handleSelectionChanged_variabletoplot)
        self.show()
        self.selection_component_summary = self.tablestatistic_tab2.selectionModel()
        self.selection_component.selectionChanged.connect(self.handleSelectionChanged_variabletoanalyze)
        self.show()


    def tab3_layout(self):
        self.tab3.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab3.setLayout(self.tab3.main_layout)
        self.sc4 = Canvas(width=15, height=24, dpi=100, parent=self.tab3)   
        self.sc4.setGeometry(QtCore.QRect(20, 10, 1100, 500))
        self.toolbar_tab3 = NavigationToolbar(self.sc4, self.tab3)
        self.toolbar_tab3.setGeometry(QtCore.QRect(20, 560, 1650, 50))       
        self.tableWidget_tab3 = QTableWidget(self.tab3)
        self.tableWidget_tab3.setRowCount(10)
        self.tableWidget_tab3.setColumnCount(17)
        self.tableWidget_tab3.setGeometry(QtCore.QRect(20, 630, 1750, 150))
        
        header_tab3 = self.tableWidget_tab3.horizontalHeader()  
        header_tab3.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        self.tableWidget_maintenance_tab3 = QTableWidget(self.tab3)
        self.tableWidget_maintenance_tab3.setRowCount(10)
        self.tableWidget_maintenance_tab3.setColumnCount(17)
        self.tableWidget_maintenance_tab3.setGeometry(QtCore.QRect(20, 810, 1750, 150))
        #self.tableWidget_maintenance_tab3.setHorizontalHeaderLabels(measurements_maintenance)
        header_tab3_maintenance = self.tableWidget_maintenance_tab3.horizontalHeader()  
        header_tab3_maintenance.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 

    def tab3_data(self):
        observables = ["Time","Vacuum [10e-5 mbar]", "Current [A]", "Ion source [mA]", "Dee 1 Voltage [kV]", "Dee 2 Voltage [kV]","Flap 1 pos [%]","Flap 2 pos [%]","Fwd Power [kW]","Refl Power [kW]","Extraction position [%]","Balance position [%]", "Foil Number",r"Foil current [uA]", r"Target current [uA]", r"Collimator current l [uA]"
        , r"Collimator current r [uA]", "Collimator current l rel[%]", "Collimator current r rel [%]","Target current rel [%]"]
        self.tableWidget_tab3.setHorizontalHeaderLabels(observables)

    #FLAGS

    def flag_max(self):
        self.max_min_value = 1
        handleSelectionChanged_variabletoplot.handleSelectionChanged_variabletoplot
        self.sc3.draw()
        self.sc3.show()

    def flag_max_reset(self):
        self.max_min_value = 0

    def flag_target4(self):
        self.target_4_value = 1
        
    def flag_target4_add(self):
        self.target_4_value = 0
        
    def flag_week(self):
        self.week_value = 1
        self.day_value = 0

    def flag_day(self):
        self.week_value = 0
        self.day_value = 1

    def flag_target1(self):
        self.target_1_value = 1

    def flag_target1_add(self):
        self.target_1_value = 0
        
    def flag_no_day_gap(self):
        self.flag_no_gap = 1 

    def flag_day_gap(self):
        self.flag_no_gap = 0

    # FUNCTIONS USING A CONNECT 
    
    def remove_row(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.tableWidget.removeRow(index.row())
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.current_row = self.current_row -1
    

    def file_folder(self):
        # Opening input folder
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        #Sort the logfiles in a folder 
        self.lis_files = []
        self.lis_files_names = []
        for logfile in os.listdir(self.dir_):
            [self.target_number,self.date_stamp,self.name,self.file_number] = saving_files_summary_list_20200420.get_headers(os.path.join(self.dir_,logfile))
            self.lis_files.append(self.file_number)
        self.lis_files.sort()
        for logfile in self.lis_files:
            self.lis_files_names.append(str(logfile) + ".log")
        #Shows the cyclotron name and the logifles in the table
        self.tableWidget_logfiles.setItem(self.current_row_folder,0, QTableWidgetItem(self.name))
        self.tableWidget_logfiles.setItem(self.current_row_folder,1, QTableWidgetItem(str(len(self.lis_files))))
        for i in range(len(self.lis_files)):
            self.tableWidget_logfiles.setItem(self.current_row_folder,i+2, QTableWidgetItem(self.lis_files_names[i]))
        self.tableWidget_logfiles.setItem(self.current_row_folder,1499, QTableWidgetItem(self.dir_))
        # Move the position for writing the data
        self.current_row_folder += 1

    def file_open_message(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName_completed, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS","All Files (*);;Python Files (*.py)", options=options)
        managing_files.file_open(self)
        managing_files.file_open_summary(self)
        first_row = [self.file_number,self.name,self.date_stamp,self.target_number]
        beam_summary = [self.df_vacuum.PRESSURE_AVE,self.df_magnet.CURRENT_AVE,self.df_source.CURRENT_AVE,self.df_rf.DEE1_VOLTAGE_AVE,self.df_rf.DEE2_VOLTAGE_AVE,
        self.df_beam.TARGET_CURRENT_AVE,self.df_beam.FOIL_CURRENT_AVE,self.df_beam.COLL_CURRENT_L_AVE,self.df_beam.COLL_CURRENT_R_AVE,self.df_beam.RELATIVE_COLL_CURRENT_AVE,
        self.df_beam.RELATIVE_TARGET_CURRENT_AVE]
        self.tableWidget.setItem(self.current_row,4, QTableWidgetItem(str(len(self.voltage_dee_1))))
        self.tableWidget.setItem(self.current_row,5, QTableWidgetItem(str(len(self.voltage_dee_2))))
        for i in range(4):
             self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(first_row[i]))
        for i in range(6,17):
             print (beam_summary[i-6].iloc[self.current_row])
             self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(str(round(beam_summary[i-6].iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(self.fileName_completed))
        self.datos = [self.tableWidget.item(0,0).text()]    
        self.current_row += 1


    def file_output(self,values):
        #Computing or just displaying trends
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        components = ["Source","Vacuum","Magnet","RF","Extraction","Beam"]
        file_components = [["table_summary_source.out"],["table_summary_vacuum.out"],["table_summary_magnet.out"],["table_summary_rf.out"],["table_summary_extraction.out"],["table_summary_beam.out"]]
        file_components_columns = [["Current","Voltage","Ratio","Source Performance"],["Pressure"],["Magnet Current"],["Dee Voltage","Power","Flap"],["Caroussel"],["Absolute Collimator","Relative Collimator","Absolute Target","Relative Target","Extraction losses","Transmission"]]
        source_summary_path = os.path.join(self.output_path,file_components[0][0])
        if (os.path.isfile(source_summary_path) == False): 
            saving_trends.getting_summary(self,self.fileName_individual,self.output_path)
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0        
        
    def folder_analyze(self,values):
        #When pressed on Cyclotron trends
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    def handleSelectionChanged_variabletoanalyze(self):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()

    def handleSelectionFile(self, selected, deselected):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.fileName = index.sibling(index.row(),18).data()
        self.row_to_plot = index.row()
        managing_files.file_open(self)
 

    def handleSelectionFolder(self, selected, deselected):
        index=(self.tableWidget_logfiles.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.fileName_folder= index.sibling(index.row(),1499).data()
        try:
           self.fileName_completed = os.path.join(self.fileName_folder,self.fileName)
        except: 
           self.fileName_completed = ""
        try:
             managing_files.file_open(self)
             managing_files.file_open_summary(self)
             first_row = [self.file_number,self.name,self.date_stamp,self.target_number]
             beam_summary = [self.df_vacuum.PRESSURE_AVE,self.df_magnet.CURRENT_AVE,self.df_source.CURRENT_AVE,self.df_rf.DEE1_VOLTAGE_AVE,self.df_rf.DEE2_VOLTAGE_AVE,
             self.df_beam.TARGET_CURRENT_AVE,self.df_beam.FOIL_CURRENT_AVE,self.df_beam.COLL_CURRENT_L_AVE,self.df_beam.COLL_CURRENT_R_AVE,self.df_beam.RELATIVE_COLL_CURRENT_AVE,
             self.df_beam.RELATIVE_TARGET_CURRENT_AVE]
             self.tableWidget.setItem(self.current_row,4, QTableWidgetItem(str(len(self.voltage_dee_1))))
             self.tableWidget.setItem(self.current_row,5, QTableWidgetItem(str(len(self.voltage_dee_2))))
             for i in range(4):
                  self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(first_row[i]))
             for i in range(6,17):
                  print (beam_summary[i-6].iloc[self.current_row])
                  self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(str(round(beam_summary[i-6].iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(self.fileName_completed))
             self.datos = [self.tableWidget.item(0,0).text()]    
             self.current_row += 1
        except:
            # Exception for computing trends
            print ("before the for loop")
            for index3 in self.tableWidget_logfiles.selectionModel().selectedRows():
                 print (index3)
                 print('Row %d is selected' % index3.row())
                 self.fileName_folder = index.sibling(index.row(),1499).data()
                 self.fileName_number = self.tableWidget_logfiles.item(index3.row(),1).text()
                 self.fileName_individual = []
                 self.fileName_individual.append(self.fileName_folder)
                 print ("NUMBER OF FILES")
                 print (self.fileName_number)
                 for i in range(int(self.fileName_number)):
                    self.fileName_individual.append(self.tableWidget_logfiles.item(index3.row(),i+2).text())

    def onpick(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         points = tuple(zip(xdata[ind], ydata[ind]))
         self.coordinates_x = xdata[ind][0]
         [self.target_number,self.date_stamp,self.name,self.file_number] = saving_files_summary_list_20200420.get_headers(str(self.fileName))
         self.irradiation_values = saving_files_summary_list_20200420.get_irradiation_information(str(self.fileName))
         self.file_df = saving_files_summary_list_20200420.get_data(self.irradiation_values)
         [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(self.file_df)
         time = saving_files_summary_list_20200420.get_time(self.file_df,current)
         foil_number = saving_files_summary_list_20200420.get_foil_number(self.file_df,current) 
         df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(self.file_df,current,self.target_number,target_current,time,foil_number)
         self.table_summary_log.setItem(0,1, QTableWidgetItem(str(self.file_df.Time.iloc[self.coordinates_x])))
         self.table_summary_log.setItem(1,1, QTableWidgetItem(str(self.file_df.Vacuum_P.astype(float).iloc[self.coordinates_x]*1e5)))
         function_names = [self.file_df.Magnet_I,self.file_df.Arc_I,self.file_df.Dee_1_kV,self.file_df.Dee_2_kV,
         self.file_df.Flap1_pos,self.file_df.Flap2_pos,self.file_df.RF_fwd_W,self.file_df.RF_refl_W,
         self.file_df.Extr_pos,self.file_df.Balance,self.file_df.Foil_No,self.file_df.Foil_I,self.file_df.Target_I,self.file_df.Coll_l_I,self.file_df.Coll_r_I]
         for i in range (2,17):
            print (i)
            self.table_summary_log.setItem(i,1, QTableWidgetItem(str(function_names[i-2][self.coordinates_x])))
         self.table_summary_log.setItem(17,1, QTableWidgetItem(str(round(df_subsystem_beam.Coll_l_rel[self.coordinates_x],2))))
         self.table_summary_log.setItem(18,1, QTableWidgetItem(str(round(df_subsystem_beam.Coll_r_rel[self.coordinates_x],2))))
         self.table_summary_log.setItem(19,1, QTableWidgetItem(str(round(df_subsystem_beam.Target_rel[self.coordinates_x],2))))
         self.current_row_statistics += 1




class Canvas_alternative(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.ax = plt.subplots()
        self.l0, = self.ax.plot(t, s0, visible=False, lw=2, color='k', label='2 Hz')
        self.l1, = self.ax.plot(t, s1, lw=2, color='r', label='4 Hz')
        self.l2, = self.ax.plot(t, s2, lw=2, color='g', label='6 Hz')
        plt.subplots_adjust(left=0.2)
        lines = [self.l0, self.l1, self.l2]
        rax = plt.axes([0.05, 0.4, 0.1, 0.15])
        labels = ["Time","Current"]
        check = CheckButtons(rax, labels, visibility)



class Canvas(FigureCanvas):

    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        #fig, (ax1, ax2) = plt.subplots(nrows=2)
        self.fig, self.axes = plt.subplots(nrows=1,ncols=2)
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes[0].tick_params(labelsize=16)
        self.axes[1].tick_params(labelsize=16)
        #self.axes[2].tick_params(labelsize=10)
        plt.xticks(rotation=90)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)


class Canvas_tab2(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(1, sharex=True)
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes.tick_params(labelsize=16)
        plt.xticks(rotation=90)
        #self.axes[1].tick_params(labelsize=10)
        #self.axes[2].tick_params(labelsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
