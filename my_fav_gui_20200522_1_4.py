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

        # Set the frame widget to be part of the scroll area

        
        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))
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
        #
        
        self.df_source = pd.DataFrame(columns=COLUMNS_SOURCE)
        self.df_vacuum = pd.DataFrame(columns=COLUMNS_VACUUM)
        self.df_magnet = pd.DataFrame(columns=COLUMNS_MAGNET)
        self.df_beam = pd.DataFrame(columns=COLUMNS_BEAM )
        self.df_rf = pd.DataFrame(columns=COLUMNS_RF)
        self.df_extraction = pd.DataFrame(columns=COLUMNS_EXTRACTION)
        self.df_transmission = pd.DataFrame(columns=COLUMNS_TRANSMISSION)
        self.df_filling_volume = pd.DataFrame(columns=COLUMNS_FILLING)
        self.df_pressure_fluctuations = pd.DataFrame(columns=COLUMNS_FLUCTUATIONS)
        
        editplotmax = QAction('&Remove Max/Min Values',self)
        resetplotmax = QAction('&Add Max/Min Values',self)
        editplottarget1 = QAction('&Remove Target 1',self)
        editplottarget4 = QAction('&Remove Target 4',self)
        editplottarget1_add = QAction('&Add Target 1',self)
        editplottarget4_add = QAction('&Add Target 4',self)
        editplotweek = QAction('&Add Week/Remove days',self)
        editplotday = QAction('&Add day/Remove week',self)
        editplottime = QAction('&Add day gap',self)
        editplottime_remove = QAction('&Remove day gap',self)
        editplotmax.triggered.connect(self.flag_max)
        resetplotmax.triggered.connect(self.flag_max_reset)
        editplottarget1.triggered.connect(self.flag_target1)
        editplottarget4.triggered.connect(self.flag_target4)
        editplottarget1_add.triggered.connect(self.flag_target1_add)
        editplottarget4_add.triggered.connect(self.flag_target4_add)
        editplotweek.triggered.connect(self.flag_week)
        editplotday.triggered.connect(self.flag_day)
        editplottime.triggered.connect(self.flag_day_gap)
        editplottime_remove.triggered.connect(self.flag_no_day_gap)

        openPlotI = QAction('&Plot Ion Source', self)
        openPlotIV = QAction('&Plot Ion Source/Vacuum', self)
        openPlotM = QAction('&Plot Magnet', self)
        openPlotRF = QAction('&Plot RF', self)
        openPlotRFPower = QAction('&Plot RF Power', self)
        openPlotEx = QAction('&Plot Extraction', self)
        openPlotCol = QAction('&Plot Collimators',self)
        openPlotColTarget = QAction('&Plot Target/Collimators',self)
        loadFileT = QAction ('&Load Trend Folder',self)
        #openPlotI_trend = QAction('&Plot Ion Source', self)
        #openPlotVM_trend = QAction('&Plot Vacuum/Magnet', self)
        #openPlotRF_trend = QAction('&Plot RF', self)      
        openPlotI.setShortcut('Ctrl+E')
        openPlotI.setStatusTip('Plot files')
        openPlotI.triggered.connect(self.file_plot)
        openPlotIV.triggered.connect(self.setting_plot_vacuum)
        openPlotM.triggered.connect(file_plots.file_plot_magnet)
        openPlotRF.triggered.connect(self.setting_plot_RF)
        openPlotRFPower.triggered.connect(self.setting_plot_RF_power)
        openPlotEx.triggered.connect(file_plots.file_plot_extraction)
        openPlotCol.triggered.connect(file_plots.file_plot_collimation)
        openPlotColTarget.triggered.connect(file_plots.file_plot_collimation_target)
        loadFileT.triggered.connect(self.file_output)

        openPlotI_S = QAction('&Plot Collimators/Ion Source', self)
        openPlotIV_S = QAction('&Plot Vacuum/Magnet vs Ion Source', self)
        openPlotRF_S = QAction('&Plot RF vs Ion Source', self)
        openPlotEx_S = QAction('&Plot Extraction vs Ion Source', self)
        openPlotI.setShortcut('Ctrl+E')
        openPlotI.setStatusTip('Plot files')
        openPlotI_S.triggered.connect(file_plots.file_plot_collimators_source)
        openPlotIV_S.triggered.connect(file_plots.file_plot_vacuum_source)
        openPlotRF_S.triggered.connect(file_plots.file_plot_rf_source)
        openPlotEx_S.triggered.connect(file_plots.file_plot_extraction_source)



        openFile = QAction('Open File', self)
        openFolder = QAction('Open Folder', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open_message)
        openFolder.triggered.connect(self.file_folder)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        #fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(openFolder)
        fileMenu.addAction(loadFileT)

        editorMenu = mainMenu.addMenu('&Plot Individual Files')
        editorMenu.addAction(openPlotI)
        editorMenu.addAction(openPlotIV)
        editorMenu.addAction(openPlotM)
        editorMenu.addAction(openPlotRF)
        editorMenu.addAction(openPlotRFPower)
        editorMenu.addAction(openPlotEx)
        editorMenu.addAction(openPlotCol)
        editorMenu.addAction(openPlotColTarget)

        editorMenu_S = mainMenu.addMenu('&Plot Individual Files (Source)')
        editorMenu_S.addAction(openPlotI_S)
        editorMenu_S.addAction(openPlotIV_S)
        editorMenu_S.addAction(openPlotRF_S)
        editorMenu_S.addAction(openPlotEx_S)


        plotMenu = mainMenu.addMenu('&Edit Trends Plots')
        plotMenu.addAction(editplottime)
        plotMenu.addAction(editplottime_remove)
        plotMenu.addAction(editplotmax)
        plotMenu.addAction(resetplotmax)
        plotMenu.addAction(editplottarget1)
        plotMenu.addAction(editplottarget4)
        plotMenu.addAction(editplottarget1_add)
        plotMenu.addAction(editplottarget4_add)
        plotMenu.addAction(editplotweek)
        plotMenu.addAction(editplotday)
        
        

        editorRemove = mainMenu.addMenu('&Remove')
        removeRow = QAction('&Remove selected row', self)
        removeCol = QAction('&Remove selected column', self)
        editorRemove.addAction(removeRow)
        editorRemove.addAction(removeCol)
        editorRemove.triggered.connect(self.remove_row)
    

        #editorMenuT = mainMenu.addMenu('&Plot Trends')
        #editorMenuT.addAction(openPlotI_trend)
        #editorMenuT.addAction(openPlotVM_trend)
        #editorMenuT.addAction(openPlotRF_trend)
        self.setWindowTitle("Cyclotron Analysis")

        self.fileMenu = QtWidgets.QMenu('&File', self)
        self.fileMenu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.fileMenu)
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        #self.help_menu.addAction('&About', self.about)
        #self.main_widget = QtWidgets.QWidget(self)
       

        self.main_widget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.main_widget)
        self.scrollArea.setWidgetResizable(True)

        #self.scrollArea.setObjectName("scrollArea")
        #self.scrollArea.setEnabled(True)
        #self.horizontalLayout.addWidget(self.main_widget)

        lay = QtWidgets.QVBoxLayout(self.main_widget)
        #layout = QtWidgets.QVBoxLayout(self)
        #layout.addWidget(self.scrollArea)
        
        #centralWidget.setObjectName("centralWidget")
        #self.main_widget.setLayout(self.horizontalLayout)
        
        self.df_subsystem_source_all = []
        self.df_subsystem_vacuum_all = []
        self.df_subsystem_magnet_all = []
        self.df_subsystem_rf_all = []
        self.df_subsystem_extraction_all = []
        self.df_subsystem_beam_all = []
        self.df_subsystem_pressure_all = []

        #l = QtWidgets.QVBoxLayout(self.main_widget)
        #m = QtWidgets.QVBoxLayout(self.plot_widget)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.home(lay)
        self.setMinimumSize(1000, 800)
        #self.resize(450, 100)

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
        self.legend_right = self.fileName[-8:-4]
        self.label_right = "Phase load"
        file_plots.file_plot_two_one_functions(self)





    def home(self, main_layout):

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        #self.tab4 = QtWidgets.QWidget()
        #self.tab5 = QtWidgets.QWidget()
        #self.tabs.resize(300,200)

         # Add tabs
        self.tabs.addTab(self.tab1,"Individual Files")
        self.tabs.addTab(self.tab3,"Counter")
        self.tabs.addTab(self.tab2,"Trends")
        #self.tabs.addTab(self.tab4,"Maintenance")
        #self.tabs.addTab(self.tab5,"Maintenance (Plots")
        
        # Create first tab
        self.tab1.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab1.main_layout.setAlignment(Qt.AlignTop)
        self.tab1.scroll = QtWidgets.QScrollArea()
        #self.tab1.main_layout.setGeometry(QtCore.QRect(20, 600, 200, 200))
        self.tab1.setLayout(self.tab1.main_layout)

        # tab 2: for trend analysis
        self.tab2.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.main_layout)

        # tab 3 for diagnosics 
        self.tab3.main_layout = QtWidgets.QVBoxLayout(self)
        #self.tab1.main_layout.setGeometry(QtCore.QRect(20, 600, 200, 200))
        self.tab3.setLayout(self.tab3.main_layout)

       

         # TAB 1

        #self.scrollArea = QtWidgets.QScrollArea(parent=self.tab1)
        #self.scrollArea.setGeometry(QtCore.QRect(50, 50, 1490, 900))

        self.sc1 = Canvas(width=15, height=24, dpi=100, parent=self.tab1)   
        self.sc1.setGeometry(QtCore.QRect(20, 10, 1100, 500))
        self.toolbar_tab1 = NavigationToolbar(self.sc1, self.tab1)
        self.toolbar_tab1.setGeometry(QtCore.QRect(20, 520, 1450, 50))
        self.tablefiles_tab1 = QtWidgets.QTableWidget(self.tab1)
        self.tablefiles_tab1.setGeometry(QtCore.QRect(1130, 10, 340, 500))
        #self.tablefiles_tab1.setObjectName("tableWidget")
        self.tablefiles_tab1.setRowCount(20)
        self.tablefiles_tab1.setColumnCount(2)
        observables = ["Time","Vacuum [10e-5 mbar]", "Current [A]", "Ion source [mA]", "Dee 1 Voltage [kV]", "Dee 2 Voltage [kV]","Flap 1 pos [%]","Flap 2 pos [%]","Fwd Power [kW]","Refl Power [kW]","Extraction position [%]","Balance position [%]", "Foil Number",r"Foil current [uA]", r"Target current [uA]", r"Collimator current l [uA]"
        , r"Collimator current r [uA]", "Collimator current l rel[%]", "Collimator current r rel [%]","Target current rel [%]"]
        self.tablefiles_tab1.setHorizontalHeaderLabels(["Observable","Instant value"])
        for i in range(len(observables)):
          self.tablefiles_tab1.setItem(self.current_row_observables,0, QTableWidgetItem(observables[i]))
          self.current_row_observables += 1
        #self.tablefiles_tab1.setItem(self.current_row_statistics,0, QTableWidgetItem(str(self.df_subsystem_magnet_selected.Time.iloc[self.coordinates_x])))
        #header = self.tablefiles_tab1.horizontalHeader()  
        #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        self.tablefiles_tab1.setColumnWidth(0,180)
        self.tablefiles_tab1.setColumnWidth(1,140)
        widget = QtWidgets.QWidget(self.tab1)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        #self.btni = QPushButton('Get trends using selected files', self.tab1)
        #self.tab1.main_layout.addWidget(self.btn)
        #self.btni.clicked.connect(self.folder_analyze)
        #self.btni.setGeometry(QtCore.QRect(20, 580, 1450, 25))

        self.btn = QPushButton('Cyclotron trends', self.tab1)
        #self.tab1.main_layout.addWidget(self.btn)
        self.btn.setGeometry(QtCore.QRect(20, 740, 1450, 25))
        self.btn.clicked.connect(self.folder_analyze)


        self.tableWidget = QTableWidget(self.tab1)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(30)
        self.tableWidget.setGeometry(QtCore.QRect(20, 580, 1450, 150))
        self.tableWidget.setHorizontalHeaderLabels(["File Name","Cyclotron","Date","Target","Number of Sparks (Dee 1)","Number of Sparks (Dee 2)","Average vacuum [mbar]", "Magnet current [A]", "Ion source [mA]", "Dee 1 Voltage [V]", "Dee 2 Voltage [V]", "Target current [uA]", "Foil current [uA]", "Collimator l current [uA]", "Collimator r current [uA]","Relative Collimators current/Foil [%]", "Relative Target current/Foil [%]","Path"])
        header2 = self.tableWidget.horizontalHeader()  
        header2.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        #self.tab1.main_layout.addWidget(self.tableWidget) 

        self.tableWidget_logfiles = QTableWidget(self.tab1)
        self.tableWidget_logfiles.setRowCount(4)
        self.tableWidget_logfiles.setColumnCount(1500)
        self.tableWidget_logfiles.setGeometry(QtCore.QRect(20, 780, 1450, 140))
        folder_labels = ["Cyclotron","Number of logs"]
        file_numbers = list(range(1,1499))
        for number in file_numbers:
            folder_labels.append(str(number))
        folder_labels.append("Path")
        self.tableWidget_logfiles.setHorizontalHeaderLabels(folder_labels)
        #self.tab1.main_layout.addWidget(self.tableWidget2) 

        selection = self.tableWidget.selectionModel()
        selection.selectionChanged.connect(self.handleSelectionFile)
        self.show()
  
        self.selection_folder = self.tableWidget_logfiles.selectionModel()
        self.selection_folder.selectionChanged.connect(self.handleSelectionFolder)
        self.show()

        # TAB 3

        #self.sc4 = Canvas(width=15, height=24, dpi=100, parent=self.tab3)   
        #self.sc4.setGeometry(QtCore.QRect(20, 10, 1500, 600))
        self.sc4 = Canvas(width=15, height=24, dpi=100, parent=self.tab3)   
        self.sc4.setGeometry(QtCore.QRect(20, 10, 1100, 500))
        self.toolbar_tab3 = NavigationToolbar(self.sc4, self.tab3)
        self.toolbar_tab3.setGeometry(QtCore.QRect(20, 560, 1650, 50))
        #self.tablefiles_tab3 = QtWidgets.QTableWidget(self.tab3)
        #self.tablefiles_tab3.setGeometry(QtCore.QRect(1130, 10, 350, 500))
        #self.tablefiles_tab1.setObjectName("tableWidget")
        #self.tablefiles_tab3.setRowCount(20)
        #self.tablefiles_tab3.setColumnCount(2)
        observables = ["Time","Vacuum [10e-5 mbar]", "Current [A]", "Ion source [mA]", "Dee 1 Voltage [kV]", "Dee 2 Voltage [kV]","Flap 1 pos [%]","Flap 2 pos [%]","Fwd Power [kW]","Refl Power [kW]","Extraction position [%]","Balance position [%]", "Foil Number",r"Foil current [uA]", r"Target current [uA]", r"Collimator current l [uA]"
        , r"Collimator current r [uA]", "Collimator current l rel[%]", "Collimator current r rel [%]","Target current rel [%]"]
        self.tableWidget_tab3 = QTableWidget(self.tab3)
        self.tableWidget_tab3.setRowCount(10)
        self.tableWidget_tab3.setColumnCount(17)
        self.tableWidget_tab3.setGeometry(QtCore.QRect(20, 630, 1750, 150))
        self.tableWidget_tab3.setHorizontalHeaderLabels(observables)
        header_tab3 = self.tableWidget_tab3.horizontalHeader()  
        header_tab3.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 

        measurements_maintenance = ["DATE","CENTRAL REGION (A)","CENTRAL REGION (B)", "CENTRAL REGION (C)","CENTRAL REGION (D)","DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        self.tableWidget_maintenance_tab3 = QTableWidget(self.tab3)
        self.tableWidget_maintenance_tab3.setRowCount(10)
        self.tableWidget_maintenance_tab3.setColumnCount(17)
        self.tableWidget_maintenance_tab3.setGeometry(QtCore.QRect(20, 810, 1750, 150))
        self.tableWidget_maintenance_tab3.setHorizontalHeaderLabels(measurements_maintenance)
        header_tab3_maintenance = self.tableWidget_maintenance_tab3.horizontalHeader()  
        header_tab3_maintenance.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        # for i in range(len(observables)):
        #  self.tableWidget_tab3.setItem(0,self.current_row_observables, QTableWidgetItem(observables[i]))
        #  self.current_row_observables_tab3 += 1
        #self.tab1.main_layout.addWidget(self.tableWidget) 

        # TAB 2

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
        self.tablefiles_tab2.setHorizontalHeaderLabels(["Component","File"])

        self.tablestatistic_tab2 = QtWidgets.QTableWidget(self.tab2) 
        self.tablestatistic_tab2.setGeometry(QtCore.QRect(20, 530, 250, 300))
        self.tablestatistic_tab2.setRowCount(11)
        self.tablestatistic_tab2.setColumnCount(2)
        self.tablestatistic_tab2.setColumnWidth(0, 110)
        self.tablestatistic_tab2.setColumnWidth(1, 115)
        self.tablestatistic_tab2.setHorizontalHeaderLabels(["Information","Summary"])
        #self.tab1.main_layout.addWidget(self.tableView_tab2) 
        self.tablestatistic_tab2.setObjectName("tableView")

        #self.pushButton = QtWidgets.QPushButton('Get statistic values', self.tab2)
        #self.pushButton.setGeometry(QtCore.QRect(20, 820, 1200, 30))
        

        self.selection_component = self.tablefiles_tab2.selectionModel()
        self.selection_component.selectionChanged.connect(self.handleSelectionChanged_variabletoplot)
        self.show()
        self.selection_component_summary = self.tablestatistic_tab2.selectionModel()
        self.selection_component.selectionChanged.connect(self.handleSelectionChanged_variabletoanalyze)
        self.show()
        # Add tabs to widget
        main_layout.addWidget(self.tabs)
        #self.setLayout(self.layout)



        # Add tabs to widget
        main_layout.addWidget(self.tabs)
        #self.setLayout(self.layout)
       
    # FLAG SECTION

    def fileQuit(self):
        self.close()

    def flag_max(self):
        self.max_min_value = 1
        self.handleSelectionChanged_variabletoplot
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
        print ("REMOVING GAPS")
        print (self.flag_no_gap)

    def flag_day_gap(self):
        self.flag_no_gap = 0
        print ("REMOVING GAPS")
        print (self.flag_no_gap)


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


    def remove_row(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.tableWidget.removeRow(index.row())
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.current_row = self.current_row -1
    
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
        print ("NAME")
        print (index.row)
        print(self.fileName)

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
                



    def handleSelectionChanged_variabletoplot(self, selected, deselected):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out","table_summary_transmission.out"]
        summary_file_names_d = ["table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_transmission.out","table_summary_beam.out"]
        labels = ["CURRENT_","VOLTAGE_","RATIO_","SOURCE_PERFORMANCE","PRESSURE_","CURRENT_","RELATIVE_TARGET_CURRENT_","EXTRACTION_LOSSES_","TRANSMISSION"]
        labels_1 = ["DEE1_VOLTAGE_","FORWARD_POWER_","FLAP1_","CAROUSEL_POSITION_","COLL_CURRENT_L_","RELATIVE_COLL_CURRENT_L_","TARGET_CURRENT_"]
        labels_2 = ["DEE2_VOLTAGE_","REFLECTED_POWER_","FLAP2_","BALANCE_POSITION_","COLL_CURRENT_R_","RELATIVE_COLL_CURRENT_R_","FOIL_CURRENT_"]
        ylabel = ["CURRENT [mA]","VOLTAGE [V]",r"RATIO [mA/$\mu A$]",r"RATIO [$\mu A$/mA]",r"PRESSURE [$10^{-5}$mbar]","MAGNET CURRENT [A]",r"RELATIVE CURRENT (FOIL)[%]","LOSSES [%]",r"TRANSMISSION RATE [($\mu A$ Foil/$\mu A$ Probe) %]"]
        ylabel_d = ["AVERAGE VOLTAGE [kV]",r"AVERAGE POWER [kW]",r"AVERAGE POSITION [%]",r"POSITION [%]",r"CURRENT [$\mu A$]",r"RELATIVE CURRENT [%]",r"AVERAGE CURRENT [$\mu$A]"]
        file_name = ["ion_source_evolution.pdf","voltage_evolution.pdf","ratio_evolution.pdf","source_performance.pdf","vacuum_evolution.pdf","magnet_evolution.pdf","relative_currents_foil.pdf","efficiency_target_evolution.pdf","transmission.pdf"]
        file_name_d = ["dee1_dee2_voltage_evolution.pdf","power_evolution.pdf","flap_evolution.pdf","carousel_balance_evolution.pdf","collimator_current_evolution.pdf","absolute_collimator_current_evolution.pdf","target_foil_evolution.pdf"]
        legend = ["T","T","T","T","T","T","T","T","T"]
        legend_1 = ["DEE1 T","FORWARDED T","FLAP 1 T","CAROUSEL T","COLLIMATOR  T","COLLIMATOR  T","TARGET T","COLLIMATOR L T","TARGET T"]
        legend_2 = ["DEE2 T","REFELECTED T","FLAP 2 T","BALANCE T","COLLIMATOR  T","COLLIMATOR  T","FOIL T","COLLIMATOR R T","FOIL T"]
        print ("INDEX")
        print (index.row())
        self.sc3.axes.clear()
        if index.row() in [0,1,2,3,4,5]:
            self.sc3.axes.clear()
            self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names[index.row()]))
            self.sc3.axes.clear()
            tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("1")])
            tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1.reset_index(drop=True, inplace=True)
            tfs_target_4.reset_index(drop=True, inplace=True)
            # Same filter but keeping the previous index
            tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            # filtering: removing duplicates from dataframe
            tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
            tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
            print ("LEN")
            print (len(tfs_unique_target_1))
            if len(tfs_target_1) == 0:
                tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                tfs_target_1.reset_index(drop=True, inplace=True)
                tfs_target_4.reset_index(drop=True, inplace=True)
                # Same filter but keeping the previous index
                tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                # filtering: removing duplicates from dataframe
                tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                print ("THEN YOU ARE HEREE")
                print (tfs_target_1)
                print (tfs_target_4)
            # sorting foil list
            index_foil_list_1 = []
            index_foil_list_4 = []
            index_foil_list_1_position = []
            index_foil_list_4_position = []
            unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
            unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
            for i in range(len(tfs_unique_target_1.FOIL)):
               # get all the positions where a given foil is and convert to a list (TARGET 1)
               index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1 = index_foil_1.tolist()
               # list of positions within the dataframe T1
               index_foil_list_1.append(index_foil_tolist_1)
               index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1_position = index_foil_1_position.tolist()
               # list of positions in the original dataframe
               index_foil_list_1_position.append(index_foil_tolist_1_position)
            for i in range(len(tfs_unique_target_4.FOIL)): 
               # get all the positions where a given foil is and convert to a list (TARGET 4)
               index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4 = index_foil_4.tolist()
               index_foil_list_4.append(index_foil_tolist_4)
               index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4_position = index_foil_4_position.tolist()
               index_foil_list_4_position.append(index_foil_tolist_4_position)
            print ("AND HERE")
            print (index_foil_list_1)
            print (index_foil_list_4)
            index_foil_sorted_1 = np.sort(index_foil_list_1)
            index_foil_sorted_4 = np.sort(index_foil_list_4)
            print ("CHECKING ALSO HERE")
            print (index_foil_sorted_1)
            print (index_foil_sorted_4)
            print (np.array(index_foil_sorted_1))
            print (np.array(index_foil_sorted_4))
            unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
            unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
            index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
            index_foil_sorted_4_position = np.sort(index_foil_list_4_position)     
            if index.row() == 4:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            elif index.row() == 3: 
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            else:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)        
        elif index.row() in [13,14,15]:
            self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-7]))
            self.sc3.axes.clear()
            tfs_target_1 = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1.reset_index(drop=True, inplace=True)
            tfs_target_4.reset_index(drop=True, inplace=True)
            tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
            tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
            if len(tfs_target_1) == 0:
                tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                tfs_target_1.reset_index(drop=True, inplace=True)
                tfs_target_4.reset_index(drop=True, inplace=True)
                # Same filter but keeping the previous index
                tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                # filtering: removing duplicates from dataframe
                tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                print ("THEN YOU ARE HEREE")
                print (tfs_target_1)
                print (tfs_target_4)
            index_foil_list_1 = []
            index_foil_list_4 = []
            index_foil_list_1_position = []
            index_foil_list_4_position = []
            unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
            unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
            for i in range(len(tfs_unique_target_1.FOIL)):
               index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1 = index_foil_1.tolist()
               index_foil_list_1.append(index_foil_tolist_1)
               index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1_position = index_foil_1_position.tolist()
               index_foil_list_1_position.append(index_foil_tolist_1_position)
            for i in range(len(tfs_unique_target_4.FOIL)): 
               index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4 = index_foil_4.tolist()
               index_foil_list_4.append(index_foil_tolist_4)
               index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4_position = index_foil_4_position.tolist()
               index_foil_list_4_position.append(index_foil_tolist_4_position)
            index_foil_sorted_1 = np.sort(index_foil_list_1)
            index_foil_sorted_4 = np.sort(index_foil_list_4)
            unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
            unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
            index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
            index_foil_sorted_4_position = np.sort(index_foil_list_4_position)       
            if index.row() == 15:
                print (self.tfs_input)
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,0) 
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)
                          #self.sc3.draw()
              #self.sc3.show()
              #print (ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5])        
        elif index.row() in [10,11,12]:
                  self.sc3.axes.clear()
                  self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-6]))
                  #self.sc3.axes.clear()
                  print ("FOIL NUMBER")
                  print (self.tfs_input.FOIL)
                  tfs_target_1 = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
                  tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
                  tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
                  tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
                  tfs_target_1.reset_index(drop=True, inplace=True)
                  tfs_target_4.reset_index(drop=True, inplace=True)
                  tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                  tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                  if len(tfs_target_1) == 0:
                      tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                      tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                      tfs_target_1.reset_index(drop=True, inplace=True)
                      tfs_target_4.reset_index(drop=True, inplace=True)
                      # Same filter but keeping the previous index
                      tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                      tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                      # filtering: removing duplicates from dataframe
                      tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                      tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                      print ("THEN YOU ARE HEREE")
                      print (tfs_target_1)
                      print (tfs_target_4)
                  print (tfs_target_1.FOIL)
                  print (tfs_target_4.FOIL)
                  print (tfs_unique_target_1.FOIL)
                  print (tfs_unique_target_4.FOIL)
                  index_foil_list_1 = []
                  index_foil_list_4 = []
                  index_foil_list_1_position = []
                  index_foil_list_4_position = []
                  unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
                  unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
                  for i in range(len(tfs_unique_target_1.FOIL)):
                     index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
                     index_foil_tolist_1 = index_foil_1.tolist()
                     index_foil_list_1.append(index_foil_tolist_1)
                     index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
                     index_foil_tolist_1_position = index_foil_1_position.tolist()
                     index_foil_list_1_position.append(index_foil_tolist_1_position)
                  for i in range(len(tfs_unique_target_4.FOIL)): 
                     print ("TARGET 4 RESULTS")
                     print (tfs_unique_target_4.FOIL.iloc[i])
                     index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
                     print (index_foil_4)
                     index_foil_tolist_4 = index_foil_4.tolist()
                     index_foil_list_4.append(index_foil_tolist_4)
                     index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
                     index_foil_tolist_4_position = index_foil_4_position.tolist()
                     index_foil_list_4_position.append(index_foil_tolist_4_position)
                  print ("INDEX")
                  print (index_foil_1_position)
                  print (index_foil_list_1_position)
                  index_foil_sorted_1 = np.sort(index_foil_list_1)
                  index_foil_sorted_4 = np.sort(index_foil_list_4)
                  unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
                  unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
                  index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
                  index_foil_sorted_4_position = np.sort(index_foil_list_4_position)
                  print ("SORTED")
                  print (unique_index_foil_sorted_1)
                  print (index_foil_sorted_1)
                  print (index_foil_sorted_1_position)
                  if index.row() == 12:
                     #plotting_summary_files_one_target.generic_plot_no_gap_two_quantities(self,tfs_input,labels_1[index.row()-5],labels_2[index.row()-5],ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5],self.output_path) 
                     plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_with_foil(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)
                     #self.sc3.draw()
                  else:
                     print (labels_1[index.row()-6])
                     print (labels_2[index.row()-6])
                     print (ylabel_d[index.row()-6])
                     print (file_name_d[index.row()-6])
                     plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_collimators(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)

        
        else:
              print ("OR HERE")
              print (labels_1[index.row()-5])
              print (labels_2[index.row()-5])
              print (ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5])
              self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-6]))
              print (summary_file_names_d[index.row()-5])
              self.sc3.axes.clear()
              if index.row() == 9:
                   print ("EXTRACTION")
                   print (self.tfs_input)
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_extraction(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.max_min_value,1,self.flag_no_gap)       
              else: 
                   print ("HEREEEE")
                   print (labels_1[index.row()-6])
                   print (labels_2[index.row()-6])
                   print (file_name_d[index.row()-6])
                   print (self.tfs_input)
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)       

              #self.sc3.draw()
              #self.sc3.show()
        self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)
        self.sc3.draw()
        self.sc3.show()


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
         self.tablefiles_tab1.setItem(0,1, QTableWidgetItem(str(self.file_df.Time.iloc[self.coordinates_x])))
         self.tablefiles_tab1.setItem(1,1, QTableWidgetItem(str(self.file_df.Vacuum_P.astype(float).iloc[self.coordinates_x]*1e5)))
         function_names = [self.file_df.Magnet_I,self.file_df.Arc_I,self.file_df.Dee_1_kV,self.file_df.Dee_2_kV,
         self.file_df.Flap1_pos,self.file_df.Flap2_pos,self.file_df.RF_fwd_W,self.file_df.RF_refl_W,
         self.file_df.Extr_pos,self.file_df.Balance,self.file_df.Foil_No,self.file_df.Foil_I,self.file_df.Target_I,self.file_df.Coll_l_I,self.file_df.Coll_r_I]
         for i in range (2,17):
            print (i)
            self.tablefiles_tab1.setItem(i,1, QTableWidgetItem(str(function_names[i-2][self.coordinates_x])))
         #self.tablefiles_tab1.setItem(2,1, QTableWidgetItem(str(self.file_df.Magnet_I[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(3,1, QTableWidgetItem(str(self.file_df.Arc_I[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(4,1, QTableWidgetItem(str(self.file_df.Dee_1_kV[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(5,1, QTableWidgetItem(str(self.file_df.Dee_2_kV[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(6,1, QTableWidgetItem(str(self.file_df.Flap1_pos[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(7,1, QTableWidgetItem(str(self.file_df.Flap2_pos[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(8,1, QTableWidgetItem(str(self.file_df.RF_fwd_W[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(9,1, QTableWidgetItem(str(self.file_df.RF_refl_W[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(10,1, QTableWidgetItem(str(self.file_df.Extr_pos[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(11,1, QTableWidgetItem(str(self.file_df.Balance[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(12,1, QTableWidgetItem(str(self.file_df.Foil_No[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(13,1, QTableWidgetItem(str(self.file_df.Foil_I[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(14,1, QTableWidgetItem(str(self.file_df.Target_I[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(15,1, QTableWidgetItem(str(self.file_df.Coll_l_I[self.coordinates_x])))
         #self.tablefiles_tab1.setItem(16,1, QTableWidgetItem(str(self.file_df.Coll_r_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(17,1, QTableWidgetItem(str(round(df_subsystem_beam.Coll_l_rel[self.coordinates_x],2))))
         self.tablefiles_tab1.setItem(18,1, QTableWidgetItem(str(round(df_subsystem_beam.Coll_r_rel[self.coordinates_x],2))))
         self.tablefiles_tab1.setItem(19,1, QTableWidgetItem(str(round(df_subsystem_beam.Target_rel[self.coordinates_x],2))))
         self.current_row_statistics += 1

    def onpick_trends(self,event):
         print ("GETTING HERE")
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         self.coordinates_x = xdata[ind][0]
         if "TCP" in self.output_path:
            self.name_complete = "TCP"
         elif "DIJ" in self.output_path:
            self.name_complete = "DIJ"
         elif "MRS" in self.output_path:
            self.name_complete = "MRS"
         elif "JNS" in self.output_path:
            self.name_complete = "JNS"
         elif "GLY" in self.output_path:
            self.name_complete = "GLY"
         self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str("CYCLOTRON")))
         self.tablestatistic_tab2.setItem(0,1, QTableWidgetItem(self.name_complete))
         self.tablestatistic_tab2.setItem(1,1, QTableWidgetItem(str(self.tfs_input.DATE.iloc[self.coordinates_x][5:])))
         self.tablestatistic_tab2.setItem(2,1, QTableWidgetItem(str(self.tfs_input.FILE.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(3,1, QTableWidgetItem(str(self.tfs_input.FOIL.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(1,0, QTableWidgetItem(str("DATE")))
         self.tablestatistic_tab2.setItem(2,0, QTableWidgetItem(str("FILE")))
         self.tablestatistic_tab2.setItem(3,0, QTableWidgetItem(str("FOIL")))
         print ("COLUMN INDEX")
         index = ((self.tablefiles_tab2.selectionModel().currentIndex()))
         print (index.row())
         ["PRESSURE_AVE","PRESSURE_STD"]
         COLUMNS_MAGNET = ["CURRENT_AVE","CURRENT_STD"]
         COLUMNS_RF =  ["DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD",
            "FORWARD_POWER_AVE","FORWARD_POWER_STD","REFLECTED_POWER_AVE","REFLECTED_POWER_STD"]
         COLUMNS_BEAM = ["COLL_CURRENT_L_STD","COLL_CURRENT_R_AVE","COLL_CURRENT_R_STD",
            "RELATIVE_COLL_CURRENT_L_AVE","RELATIVE_COLL_CURRENT_L_STD",
            "RELATIVE_COLL_CURRENT_R_AVE","RELATIVE_COLL_CURRENT_R_STD",
             "TARGET_CURRENT_AVE","TARGET_CURRENT_STD",
             "FOIL_CURRENT_AVE","FOIL_CURRENT_STD",
             "EXTRACTION_LOSSES_AVE","EXTRACTION_LOSSES_STD"]
         COLUMNS_EXTRACTION = ["CAROUSEL_POSITION_AVE","CAROUSEL_POSITION_STD","BALANCE_POSITION_AVE","BALANCE_POSITION_STD"]
         if index.row() in [0,1,2]:
            print (self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x])
            print (self.tfs_input.VOLTAGE_AVE.iloc[self.coordinates_x])
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("CURRENT [mA]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("VOLTAGE [V]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("RATIO [mA/uA]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            current_value = str(round(self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CURRENT_STD.iloc[self.coordinates_x],1))
            voltage_value = str(round(self.tfs_input.VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-"+ str(round(self.tfs_input.VOLTAGE_STD.iloc[self.coordinates_x],1))
            ratio_value = str(round(self.tfs_input.RATIO_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RATIO_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(current_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(voltage_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(ratio_value))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 4:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("PRESSURE [10-5 mbar]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            vacuum_value = str(round(self.tfs_input.PRESSURE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.PRESSURE_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(vacuum_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 5:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("MAGNET CURRENT [A]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            current_value = str(round(self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CURRENT_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(current_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [6,7,8]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("DEE1 VOLTAGE [kV]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("DEE2 VOLTAGE [kV]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("FORWARDED POWER [kW]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem(str("REFLECTED POWER [kW]")))
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem(str("FLAP1 POSITION [%]")))
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem(str("FLAP2 POSITION [%]")))
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            dee1_voltage_value = str(round(self.tfs_input.DEE1_VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.DEE1_VOLTAGE_STD.iloc[self.coordinates_x],1))
            dee2_voltage_value = str(round(self.tfs_input.DEE2_VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.DEE2_VOLTAGE_STD.iloc[self.coordinates_x],1))
            for_power_value = str(round(self.tfs_input.FORWARD_POWER_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FORWARD_POWER_STD.iloc[self.coordinates_x],1))
            ref_power_value = str(round(self.tfs_input.REFLECTED_POWER_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.REFLECTED_POWER_STD.iloc[self.coordinates_x],1))
            flap1_pos_value = str(round(self.tfs_input.FLAP1_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FLAP1_STD.iloc[self.coordinates_x],1))
            flap2_pos_value = str(round(self.tfs_input.FLAP2_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FLAP2_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(dee1_voltage_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(dee2_voltage_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(for_power_value))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem(ref_power_value))
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem(flap1_pos_value))
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem(flap2_pos_value))
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 9:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("CAROUSSEL [%]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("BALANCE [%]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            caroussel_value = str(round(self.tfs_input.CAROUSEL_POSITION_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CAROUSEL_POSITION_STD.iloc[self.coordinates_x],1))
            balance_value = str(round(self.tfs_input.BALANCE_POSITION_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.BALANCE_POSITION_STD.iloc[self.coordinates_x],1)) 
            print ("HEREEEEEEEEEE")
            print (caroussel_value)
            print (balance_value)         
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(caroussel_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(balance_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [10,11,12,13]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("COLLIMATORS CURRENT L [uA]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("COLLIMATORS CURRENT R [uA]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("COLLIMATORS [uA]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem(str("COLLIMATORS CURRENT REL L[%]")))
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem(str("COLLIMATORS CURRENT REL R[%]")))
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem(str("COLLIMATORS[%]")))
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem(str("TARGET CURRENT [uA]")))
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem(str("FOIL CURRENT [uA]")))
            coll_current_value_l = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x],1))
            coll_current_value_r = str(round(self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x],1))
            coll_current_rel_value_l = str(round(self.tfs_input.RELATIVE_COLL_CURRENT_L_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_COLL_CURRENT_L_STD.iloc[self.coordinates_x],1))
            coll_current_rel_value_r = str(round(self.tfs_input.RELATIVE_COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_COLL_CURRENT_R_STD.iloc[self.coordinates_x],1))
            coll_current = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1) ) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x] ,1))
            coll_current_rel = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1) ) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x] ,1))
            target_current_value = str(round(self.tfs_input.TARGET_CURRENT_AVE.iloc[self.coordinates_x],1)) + " " + str(round(self.tfs_input.TARGET_CURRENT_STD.iloc[self.coordinates_x],1))
            target_current_rel_value = str(round(self.tfs_input.RELATIVE_TARGET_CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_TARGET_CURRENT_STD.iloc[self.coordinates_x],1))
            foil_current_value = str(round(self.tfs_input.FOIL_CURRENT_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.FOIL_CURRENT_STD.iloc[self.coordinates_x],1))
            extraction_losses_value = str(round(self.tfs_input.EXTRACTION_LOSSES_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.EXTRACTION_LOSSES_STD.iloc[self.coordinates_x],1))
            print ("HEREEEEEE")
            print (coll_current)
            print (coll_current_rel)
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(coll_current_value_l))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(coll_current_value_r))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(coll_current))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem(coll_current_rel_value_l))
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem(coll_current_rel_value_r))
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem(coll_current_rel))
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem(target_current_value))
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem(foil_current_value))
         elif index.row() in [14]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("EXTRACTION LOSSES [%]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            extraction_losses_value = str(round(self.tfs_input.EXTRACTION_LOSSES_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.EXTRACTION_LOSSES_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(extraction_losses_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [15]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("TRANSMISSION")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            transmission = str(round(self.tfs_input.TRANSMISSION.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(transmission))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())


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
