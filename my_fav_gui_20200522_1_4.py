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
import saving_files_summary
#import saving_files_summary_list
import plotting_summary_files_one_target_1_4
import saving_files_summary_list_20200420
import numpy as np
import os
import tfs
from matplotlib.widgets import CheckButtons
#import datetime
from datetime import time


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

measurements_maintenance_central_region = ["CYCLOTRON","DATE","CENTRAL_REGION_(A)_BEFORE","CENTRAL_REGION_(B)_BEFORE", "CENTRAL_REGION_(C)_BEFORE","CENTRAL_REGION_(D)_BEFORE","CENTRAL_REGION_(A)_AFTER","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_rf_1 = ["CYCLOTRON","DATE","RF_1_HEIGHT_A_BEFORE","RF_1_HEIGHT_B_BEFORE", "RF_1_HEIGHT_C_BEFORE","RF_1_HEIGHT_D_BEFORE","RF_1_HEIGHT_A_AFTER","RF_1_HEIGHT_B_AFTER", "RF_1_HEIGHT_C_AFTER","RF_1_HEIGHT_D_AFTER",
        "RF_1_THICKNESS_A_BEFORE ","RF_1_THICKNESS_B_BEFORE", "RF_1_THICKNESS_C_BEFORE","RF_1_THICKNESS_D_BEFORE","RF_1_THICKNESS_A_AFTER ","RF_1_THICKNESS_B_AFTER", "RF_1_THICKNESS_C_AFTER","RF_1_THICKNESS_D_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_rf_2 = ["CYCLOTRON","DATE","RF_2_HEIGHT_E_BEFORE","RF_2_HEIGHT_F_BEFORE", "RF_2_HEIGHT_G_BEFORE","RF_2_HEIGHT_H_BEFORE","RF_2_HEIGHT_E_AFTER","RF_2_HEIGHT_F_AFTER", "RF_2_HEIGHT_G_AFTER","RF_2_HEIGHT_H_AFTER",
        "RF_2_THICKNESS_E_BEFORE ","RF_2_THICKNESS_F_BEFORE", "RF_2_THICKNESS_G_BEFORE","RF_2_THICKNESS_H_BEFORE","RF_2_THICKNESS_E_AFTER ","RF_2_THICKNESS_F_AFTER", "RF_2_THICKNESS_G_AFTER","RF_2_THICKNESS_H_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_col = ["CYCLOTRON","DATE","SEPARATION_COL_1_BEFORE","APERTURE_COL_1_BEFORE","SEPARATION_COL_2_BEFORE","APERTURE_COL_2_BEFORE","SEPARATION_COL_1_AFTER","APERTURE_COL_1_AFTER","SEPARATION_COL_2_AFTER","APERTURE_COL_2_AFTER"]
measurements_maintenance_midplane = ["CYCLOTRON","DATE","ACTUAL_A","ACTUAL_B","ACTUAL_C","ACTUAL_D","ACTUAL_E","ACTUAL_F","ACTUAL_G","ACTUAL_H","VARIANCE_A","VARIANCE_B","VARIANCE_C","VARIANCE_D","VARIANCE_E","VARIANCE_F","VARIANCE_G","VARIANCE_H"] 

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
        self.df_central_region = pd.DataFrame(columns=measurements_maintenance_central_region)
        self.df_rf_1 = pd.DataFrame(columns=measurements_maintenance_rf_1)
        self.df_rf_2 = pd.DataFrame(columns=measurements_maintenance_rf_2)
        self.df_col = pd.DataFrame(columns=measurements_maintenance_col)
        self.df_mid_plane = pd.DataFrame(columns=measurements_maintenance_midplane)

        self.df_source = pd.DataFrame(columns=COLUMNS_SOURCE)
        self.df_vacuum = pd.DataFrame(columns=COLUMNS_VACUUM)
        self.df_magnet = pd.DataFrame(columns=COLUMNS_MAGNET)
        self.df_beam = pd.DataFrame(columns=COLUMNS_BEAM )
        self.df_rf = pd.DataFrame(columns=COLUMNS_RF)
        self.df_extraction = pd.DataFrame(columns=COLUMNS_EXTRACTION)

        
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
        openPlotIV.triggered.connect(self.file_plot_vacuum)
        openPlotM.triggered.connect(self.file_plot_magnet)
        openPlotRF.triggered.connect(self.file_plot_rf)
        openPlotRFPower.triggered.connect(self.file_plot_rf_power)
        openPlotEx.triggered.connect(self.file_plot_extraction)
        openPlotCol.triggered.connect(self.file_plot_collimation)
        openPlotColTarget.triggered.connect(self.file_plot_collimation_target)
        loadFileT.triggered.connect(self.file_output_already_computed)

        openPlotI_S = QAction('&Plot Collimators/Ion Source', self)
        openPlotIV_S = QAction('&Plot Vacuum/Magnet vs Ion Source', self)
        openPlotRF_S = QAction('&Plot RF vs Ion Source', self)
        openPlotEx_S = QAction('&Plot Extraction vs Ion Source', self)
        openPlotI.setShortcut('Ctrl+E')
        openPlotI.setStatusTip('Plot files')
        openPlotI_S.triggered.connect(self.file_plot_collimators_source)
        openPlotIV_S.triggered.connect(self.file_plot_vacuum_source)
        openPlotRF_S.triggered.connect(self.file_plot_rf_source)
        openPlotEx_S.triggered.connect(self.file_plot_extraction_source)



        openFile = QAction('Open File', self)
        openFolder = QAction('Open Folder', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
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
        self.tableWidget.setHorizontalHeaderLabels(["File Name","Cyclotron","Date","Target","Number of Sparks (Dee 1)","Number of Sparks (Dee 2)","Average vacuum [mbar]", "Magnet current [A]", "Ion source [mA]", "Dee 1 Voltage [V]", "Dee 2 Voltage [V]", "Target current [uA]", "Foil current [uA]", "Collimator l current [uA]", "Collimator r current [uA]","Relative Collimators current/Foil [%]", "Relative Target current/Foil [%]","Motor Extraction speed [%]","Motor Flap 1 (position) [%]", "Motor Flap 2 (position) [%]","Motor Extraction position[%]","Motor Flap 1 (speed)[%]", "Motor Flap 2 (speed)[%]","Path"])
        header2 = self.tableWidget.horizontalHeader()  
        header2.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents) 
        #self.tab1.main_layout.addWidget(self.tableWidget) 

        self.tableWidget2 = QTableWidget(self.tab1)
        self.tableWidget2.setRowCount(4)
        self.tableWidget2.setColumnCount(1500)
        self.tableWidget2.setGeometry(QtCore.QRect(20, 780, 1450, 140))
        folder_labels = ["Cyclotron","Number of logs"]
        file_numbers = list(range(1,1499))
        for number in file_numbers:
            folder_labels.append(str(number))
        folder_labels.append("Path")
        self.tableWidget2.setHorizontalHeaderLabels(folder_labels)
        #self.tab1.main_layout.addWidget(self.tableWidget2) 

        selection = self.tableWidget.selectionModel()
        selection.selectionChanged.connect(self.handleSelectionFile)
        self.show()
  
        self.selection_folder = self.tableWidget2.selectionModel()
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
       
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    
    def launch_script(self):
        self.panel = saving_files_summary.get_data_tuple()
        self.panel.show()


    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def flag_max(self):
        self.max_min_value = 1
        print ("CHANGIN PLOTTT")
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


    def on_click_load_central(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import central values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_source_file = os.path.join(self.input_path_source,"central_region_values.out")
        self.df_central_region_selected = tfs.read(self.input_path_source_file)
        self.df_central_region_selected = self.df_central_region_selected[(self.df_central_region_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_central_region_selected["DATE"] == self.value_date)]
        print ("HEREEEE")
        print (self.df_central_region_selected)
        try:
           self.textbox_centralregion_a_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].loc[0])
           self.textbox_centralregion_b_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].loc[0])
           self.textbox_centralregion_c_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].loc[0])
           self.textbox_centralregion_d_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].loc[0])
        except:
            try:
               self.textbox_centralregion_a_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].iloc[0])
               self.textbox_centralregion_b_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].iloc[0]) 
               self.textbox_centralregion_c_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].iloc[0])
               self.textbox_centralregion_d_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].iloc[0])
            except:
               self.textbox_centralregion_a_reference.setPlainText("0")
               self.textbox_centralregion_b_reference.setPlainText("0")
               self.textbox_centralregion_c_reference.setPlainText("0")
               self.textbox_centralregion_d_reference.setPlainText("0")

    def on_click_load_rf1(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import RF Dee1 values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_rf = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_file = os.path.join(self.input_path_rf,"rf_dee1_values.out")
        print (self.input_path_rf_file)
        self.df_rf_dee1_selected = tfs.read(self.input_path_rf_file)
        print ()
        self.df_rf_dee1_selected = self.df_rf_dee1_selected[(self.df_rf_dee1_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee1_selected["DATE"] == self.value_date)]
        print ("HEREEEE")
        #print (self.df_central_region_selected)
        print (self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].loc[0])
        try:
        #print ("first step")
          self.textbox_dee1h_a_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].loc[0])
          self.textbox_dee1h_b_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].loc[0])
          self.textbox_dee1h_c_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].loc[0])
          self.textbox_dee1h_d_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].loc[0])
          self.textbox_dee1_a_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].loc[0])
          self.textbox_dee1_b_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].loc[0])
          self.textbox_dee1_c_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].loc[0])
          self.textbox_dee1_d_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].loc[0])
          print ("end of first step")
        except:
            try:
               print ("second step")
               self.textbox_dee1h_a_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].iloc[0])
               self.textbox_dee1h_b_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].iloc[0])
               self.textbox_dee1h_c_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].iloc[0])
               self.textbox_dee1h_d_reference.setPlainText(self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].iloc[0])
               self.textbox_dee1_a_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].iloc[0])
               self.textbox_dee1_b_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].iloc[0])
               self.textbox_dee1_c_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].iloc[0])
               self.textbox_dee1_d_reference.setPlainText(self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].iloc[0] + "/" + self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].iloc[0])
               print ("end of second step")
            except:
               print ("third step")
               self.textbox_dee1h_a_reference.setPlainText("0")
               self.textbox_dee1h_b_reference.setPlainText("0")
               self.textbox_dee1h_c_reference.setPlainText("0")
               self.textbox_dee1h_d_reference.setPlainText("0")
               self.textbox_dee1_a_reference.setPlainText("0")
               self.textbox_dee1_b_reference.setPlainText("0")
               self.textbox_dee1_c_reference.setPlainText("0")
               self.textbox_dee1_d_reference.setPlainText("0")
               print ("end of third step")

    def on_click_load_rf2(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import RF Dee1 values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_rf = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_file = os.path.join(self.input_path_rf,"rf_dee2_values.out")
        self.df_rf_dee2_selected = tfs.read(self.input_path_rf_file)
        self.df_rf_dee2_selected = self.df_rf_dee2_selected[(self.df_rf_dee2_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee2_selected["DATE"] == self.value_date)]
        print ("HEREEEE")
        print (self.input_path_rf_file)
        print (self.df_rf_dee2_selected)
        print (self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"])
        try:
            print ("first step")
            self.textbox_dee2h_e_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].loc[0])
            self.textbox_dee2h_f_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_F_AFTER"].loc[0])
            self.textbox_dee2h_g_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_G_AFTER"].loc[0])
            self.textbox_dee2h_h_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_H_AFTER"].loc[0])
            self.textbox_dee2_e_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_E_AFTER"].loc[0])
            self.textbox_dee2_f_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_F_AFTER"].loc[0])
            self.textbox_dee2_g_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_G_AFTER"].loc[0])
            self.textbox_dee2_h_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_H_AFTER"].loc[0])
        except:
            try:
               print ("second step")
               self.textbox_dee2h_e_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_A_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_HEIGHT_A_AFTER"].iloc[0])
               self.textbox_dee2h_f_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_B_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_HEIGHT_B_AFTER"].iloc[0])
               self.textbox_dee2h_g_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_C_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_HEIGHT_C_AFTER"].iloc[0])
               self.textbox_dee2h_h_reference.setPlainText(self.df_rf_dee2_selected["RF_2_HEIGHT_D_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_HEIGHT_D_AFTER"].iloc[0])
               self.textbox_dee2_e_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_A_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_THICKNESS_A_AFTER"].iloc[0])
               self.textbox_dee2_f_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_B_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_THICKNESS_B_AFTER"].iloc[0])
               self.textbox_dee2_g_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_C_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_THICKNESS_C_AFTER"].iloc[0])
               self.textbox_dee2_h_reference.setPlainText(self.df_rf_dee2_selected["RF_2_THICKNESS_D_AFTER"].iloc[0] + "/" + self.df_rf_dee2_selected["RF_2_THICKNESS_D_AFTER"].iloc[0])
            except:
               print ("third step")
               self.textbox_dee2h_e_reference.setPlainText("0")
               self.textbox_dee2h_f_reference.setPlainText("0")
               self.textbox_dee2h_g_reference.setPlainText("0")
               self.textbox_dee2h_h_reference.setPlainText("0")
               self.textbox_dee2_e_reference.setPlainText("0")
               self.textbox_dee2_f_reference.setPlainText("0")
               self.textbox_dee2_g_reference.setPlainText("0")
               self.textbox_dee2_h_reference.setPlainText("0")
        
    
    def on_click_central(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.value_position_source_a_after = self.textbox_centralregion_a_after.text()
        self.value_position_source_a_before = self.textbox_centralregion_a_before.text()
        self.value_position_source_a_after = self.textbox_centralregion_a_after.text()
        self.value_position_source_b_before = self.textbox_centralregion_b_before.text()
        self.value_position_source_b_after = self.textbox_centralregion_b_after.text()
        self.value_position_source_c_before  = self.textbox_centralregion_c_before.text()
        self.value_position_source_c_after  = self.textbox_centralregion_c_after.text()
        self.value_position_source_d_before = self.textbox_centralregion_d_before.text()
        self.value_position_source_d_after = self.textbox_centralregion_d_after.text()
        #measurements_maintenance = ["CENTRAL_REGION_(A)_BEFORE ","CENTRAL_REGION_(B)_BEFORE", "CENTRAL_REGION_(C)_BEFORE","CENTRAL_REGION_(D)_BEFORE","CENTRAL_REGION_(A)_AFTER ","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER","CENTRAL_REGION_(A)_REFERENCE ","CENTRAL_REGION_(B)_REFERENCE", "CENTRAL_REGION_(C)_REFERENCE","CENTRAL_REGION_(D)_REFERENCE"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        central_values = [[self.value_position_cyclotron,self.value_date,self.value_position_source_a,self.value_position_source_a_after,self.value_position_source_b,self.value_position_source_b_after,self.value_position_source_c,self.value_position_source_c_after,self.value_position_source_d,self.value_position_source_d_after]]
        df_central_region_i = pd.DataFrame((central_values),columns=measurements_maintenance_central_region)
        print (df_central_region_i)
        print ("HEREEE")
        self.df_central_region = self.df_central_region.append(df_central_region_i,ignore_index=True)
        print (self.df_central_region)
        self.question_central =  QMessageBox()
        self.question_central.setText("Select an output folder to import midplane values")
        self.question_central.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_central.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_central = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_central_file = os.path.join(self.output_path_central,"central_region_values.out")
        try: 
            self.df_central_region_all = tfs.read(self.output_path_central_file) 
            self.df_central_region_all.append(self.df_central_region)
            print ("HEREEEEEE ADDING A COLUMN")
            print (df_central_region_all)
            tfs.write(self.output_path_central_file, self.df_central_region_all) 
        except:
            tfs.write(self.output_path_central_file, self.df_central_region) 
        print (df_central_region_all)


    def on_click_rf_dee1(self):
        #thickness
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.value_dee1t_a_before = self.textbox_dee1_a_before.text()
        self.value_dee1t_a_after = self.textbox_dee1_a_after.text()
        self.value_dee1t_b_before = self.textbox_dee1_b_before.text()
        self.value_dee1t_b_after = self.textbox_dee1_b_after.text()
        self.value_dee1t_c_before  = self.textbox_dee1_c_before.text()
        self.value_dee1t_c_after  = self.textbox_dee1_c_after.text()
        self.value_dee1t_d_before = self.textbox_dee1_d_before.text()
        self.value_dee1t_d_after = self.textbox_dee1_d_after.text()
        #height 
        self.value_dee1h_a_before = self.textbox_dee1h_a_before.text()
        self.value_dee1h_a_after = self.textbox_dee1h_a_after.text()
        self.value_dee1h_b_before = self.textbox_dee1h_b_before.text()
        self.value_dee1h_b_after = self.textbox_dee1h_b_after.text()
        self.value_dee1h_c_before  = self.textbox_dee1h_c_before.text()
        self.value_dee1h_c_after  = self.textbox_dee1h_c_after.text()
        self.value_dee1h_d_before = self.textbox_dee1h_d_before.text()
        self.value_dee1h_d_after = self.textbox_dee1h_d_after.text()
        dee1_values = [[self.value_position_cyclotron,self.value_date,self.value_dee1h_a_before,self.value_dee1h_b_before,self.value_dee1h_c_before,self.value_dee1h_d_before,self.value_dee1h_a_after,self.value_dee1h_b_after,self.value_dee1h_c_after,self.value_dee1h_d_after,
        self.value_dee1t_a_before,self.value_dee1t_b_before,self.value_dee1t_c_before,self.value_dee1t_d_before,self.value_dee1t_a_after,self.value_dee1t_b_after,self.value_dee1t_c_after,self.value_dee1t_d_after]]
        df_dee1 = pd.DataFrame((dee1_values),columns=measurements_maintenance_rf_1)
        print (df_dee1)
        print ("HEREEE")
        self.df_rf_1 = self.df_rf_1.append(df_dee1,ignore_index=True)
        self.question_dee1 =  QMessageBox()
        self.question_dee1.setText("Select an output folder to export RF Dee1 values")
        self.question_dee1.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_dee1.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_rf_dee1 = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_rf_dee1_file = os.path.join(self.output_path_rf_dee1,"rf_dee1_values.out")
        try: 
            self.df_rf_dee1_all = tfs.read(self.output_rf_dee1_file) 
            self.df_rf_dee1_all.append(self.df_rf_1)
            #print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_rf_dee1_all)
            tfs.write(self.output_path_rf_dee1_file, self.df_rf_dee1_all) 
        except:
            tfs.write(self.output_path_rf_dee1_file, self.df_rf_1) 
        print (self.df_rf_1)

    def on_click_rf_dee2(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        #thickness
        self.value_dee2t_e_before = self.textbox_dee2_e_before.text()
        self.value_dee2t_e_after = self.textbox_dee2_e_after.text()
        self.value_dee2t_f_before = self.textbox_dee2_f_before.text()
        self.value_dee2t_f_after = self.textbox_dee2_f_after.text()
        self.value_dee2t_g_before  = self.textbox_dee2_g_before.text()
        self.value_dee2t_g_after  = self.textbox_dee2_g_after.text()
        self.value_dee2t_h_before = self.textbox_dee2_h_before.text()
        self.value_dee2t_h_after = self.textbox_dee2_h_after.text()
        #height 
        self.value_dee2h_e_before = self.textbox_dee2h_e_before.text()
        self.value_dee2h_e_after = self.textbox_dee2h_e_after.text()
        self.value_dee2h_f_before = self.textbox_dee2h_f_before.text()
        self.value_dee2h_f_after = self.textbox_dee2h_f_after.text()
        self.value_dee2h_g_before  = self.textbox_dee2h_g_before.text()
        self.value_dee2h_g_after  = self.textbox_dee2h_g_after.text()
        self.value_dee2h_h_before = self.textbox_dee2h_h_before.text()
        self.value_dee2h_h_after = self.textbox_dee2h_h_after.text()
        dee2_values = [[self.value_position_cyclotron,self.value_date,self.value_dee2h_e_before,self.value_dee2h_f_before,self.value_dee2h_g_before,self.value_dee2h_h_before,self.value_dee2h_e_after,self.value_dee2h_f_after,self.value_dee2h_g_after,self.value_dee2h_h_after,
        self.value_dee2t_e_before,self.value_dee2t_f_before,self.value_dee2t_g_before,self.value_dee2t_h_before,self.value_dee2t_e_after,self.value_dee2t_f_after,self.value_dee2t_g_after,self.value_dee2t_h_after]]
        df_dee2 = pd.DataFrame((dee2_values),columns=measurements_maintenance_rf_2)
        print ("DEE 2 VALUES")
        print (dee2_values)
        print (df_dee2)
        print ("HEREEE")
        self.df_rf_2 = self.df_rf_2.append(df_dee2,ignore_index=True)
        print (self.df_rf_2)
        print ("HEREEE")
        self.df_rf_dee2 = self.df_rf_2.append(df_dee2,ignore_index=True)
        self.question_dee2 =  QMessageBox()
        self.question_dee2.setText("Select an output folder to export RF Dee2 values")
        self.question_dee2.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_dee2.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_rf_dee2 = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_rf_dee2_file = os.path.join(self.output_path_rf_dee2,"rf_dee2_values.out")
        try: 
            self.df_rf_dee2_all = tfs.read(self.output_rf_dee2_file) 
            #self.df_rf_dee1_all.append(self.df_rf_dee2)
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_rf_dee2_all)
            tfs.write(self.output_path_rf_dee2_file, self.df_rf_dee2_all) 
        except:
            tfs.write(self.output_path_rf_dee2_file, self.df_rf_2) 
        print (self.df_rf_2)

    def on_click_coll(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.value_coll_1_aperture_before = self.textbox_coll1_aperture_before.text()
        self.value_coll_1_aperture_after = self.textbox_coll1_aperture_after.text()
        self.value_coll_1_aperture_reference = self.textbox_coll1_aperture_reference.text()
        self.value_coll_1_separation_before = self.textbox_coll1_separation_before.text()
        self.value_coll_1_separation_after = self.textbox_coll1_separation_after.text()
        self.value_coll_1_separation_reference = self.textbox_coll1_separation_reference.text()
        self.value_coll_2_aperture_before = self.textbox_coll2_aperture_before.text()
        self.value_coll_2_aperture_after = self.textbox_coll2_aperture_after.text()
        self.value_coll_2_aperture_reference = self.textbox_coll2_aperture_reference.text()
        self.value_coll_2_separation_before = self.textbox_coll2_separation_before.text()
        self.value_coll_2_separation_after = self.textbox_coll2_separation_after.text()
        self.value_coll_2_separation_reference = self.textbox_coll2_separation_reference.text()
        coll_values = [[self.value_position_cyclotron,self.value_date,self.value_coll_1_separation_before,self.value_coll_1_aperture_before,self.value_coll_2_separation_before,self.value_coll_2_aperture_before,self.value_coll_1_separation_after,self.value_coll_1_aperture_after,self.value_coll_2_separation_after,self.value_coll_2_aperture_after]]
        df_col_i = pd.DataFrame((coll_values),columns=measurements_maintenance_col)
        print (df_col_i)
        print ("HEREEE")
        self.df_coll = self.df_col.append(df_col_i,ignore_index=True)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_coll = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_coll_file = os.path.join(self.output_path_rf_dee2,"collimators_values.out")
        try: 
            self.df_coll_all = tfs.read(self.output_path_coll_file) 
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_coll_all)
            tfs.write(self.output_path_coll_file, self.df_coll_all) 
        except:
            tfs.write(self.output_path_coll_file, self.df_coll) 
        print (self.df_col)

    def on_click_midplane(self):
        self.value_position_cyclotron = self.textbox_cyclotron.text()
        self.value_date = self.textbox_date.text()
        self.value_midplane_actual_a = self.textbox_midplane_actual_a.text()
        self.value_midplane_actual_b = self.textbox_midplane_actual_b.text()
        self.value_midplane_actual_c = self.textbox_midplane_actual_c.text()
        self.value_midplane_actual_d = self.textbox_midplane_actual_d.text()
        self.value_midplane_actual_e = self.textbox_midplane_actual_e.text()
        self.value_midplane_actual_f = self.textbox_midplane_actual_f.text()
        self.value_midplane_actual_g = self.textbox_midplane_actual_g.text()
        self.value_midplane_actual_h = self.textbox_midplane_actual_h.text()
        self.value_midplane_variance_a = self.textbox_midplane_variance_a.text()
        self.value_midplane_variance_b = self.textbox_midplane_variance_b.text()
        self.value_midplane_variance_c = self.textbox_midplane_variance_c.text()
        self.value_midplane_variance_d = self.textbox_midplane_variance_d.text()
        self.value_midplane_variance_e = self.textbox_midplane_variance_e.text()
        self.value_midplane_variance_f = self.textbox_midplane_variance_f.text()
        self.value_midplane_variance_g = self.textbox_midplane_variance_g.text()
        self.value_midplane_variance_h = self.textbox_midplane_variance_h.text()
        midplane_values = [[self.value_position_cyclotron,self.value_date,self.value_midplane_actual_a,self.value_midplane_actual_b,self.value_midplane_actual_c,self.value_midplane_actual_d,self.value_midplane_actual_e,self.value_midplane_actual_f,self.value_midplane_actual_g,self.value_midplane_actual_h,
        self.value_midplane_variance_a,self.value_midplane_variance_b,self.value_midplane_variance_c,self.value_midplane_variance_d,self.value_midplane_variance_e,self.value_midplane_variance_f,self.value_midplane_variance_g,self.value_midplane_variance_h]]
        df_mid_plane_i = pd.DataFrame((midplane_values),columns=measurements_maintenance_midplane)
        print (df_mid_plane_i)
        print ("HEREEE")
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import midplane values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_midplane = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_midplane_file = os.path.join(self.output_path_midplane,"mid_plane_values.out")
        self.df_mid_plane = self.df_mid_plane.append(df_mid_plane_i,ignore_index=True)
        try: 
            self.df_mid_plane_all = tfs.read(self.output_path_midplane_file) 
            self.df_mid_plane_all.append(self.df_mid_plane)
            print ("HEREEEEEE ADDING A COLUMN")
            print (df_mid_plane_all)
            tfs.write(self.output_path_midplane_file, self.df_mid_plane_all) 
        except:
            tfs.write(self.output_path_midplane_file, self.df_mid_plane) 
        print (self.df_mid_plane)

    def compute_mid_plane_dee1(self):
        self.midplane_value_a_after = float(self.textbox_dee1h_a_after.text()) + float(self.textbox_dee1_a_after.text())/2
        self.midplane_value_b_after = float(self.textbox_dee1h_b_after.text()) + float(self.textbox_dee1_b_after.text())/2 
        self.midplane_value_c_after = float(self.textbox_dee1h_c_after.text()) + float(self.textbox_dee1_c_after.text())/2 
        self.midplane_value_d_after = float(self.textbox_dee1h_d_after.text()) + float(self.textbox_dee1_d_after.text())/2
        self.textbox_midplane_actual_a.setPlainText(str(self.midplane_value_a_after))
        self.textbox_midplane_actual_b.setPlainText(str(self.midplane_value_b_after))
        self.textbox_midplane_actual_c.setPlainText(str(self.midplane_value_c_after))
        self.textbox_midplane_actual_d.setPlainText(str(self.midplane_value_d_after))

    def compute_mid_plane_dee2(self):
        self.midplane_value_e_after = float(self.textbox_dee2h_e_after.text()) + float(self.textbox_dee2_e_after.text())/2
        self.midplane_value_f_after = float(self.textbox_dee2h_f_after.text()) + float(self.textbox_dee2_f_after.text())/2
        self.midplane_value_g_after = float(self.textbox_dee2h_g_after.text()) + float(self.textbox_dee2_g_after.text())/2
        self.midplane_value_h_after = float(self.textbox_dee2h_h_after.text()) + float(self.textbox_dee2_h_after.text())/2
        self.textbox_midplane_actual_e.setPlainText(str(self.midplane_value_e_after))
        self.textbox_midplane_actual_f.setPlainText(str(self.midplane_value_f_after))
        self.textbox_midplane_actual_g.setPlainText(str(self.midplane_value_g_after))
        self.textbox_midplane_actual_h.setPlainText(str(self.midplane_value_h_after))


    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
    

    def file_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print (self.dir_)
        #Sort the logfiles in a folder 
        self.lis_files = []
        self.lis_files_names = []
        logfile_list = []
        logfile_list_names = []
        for logfile in os.listdir(self.dir_):
            self.lis_files.append(int(logfile[:-4]))
        self.lis_files.sort()
        for logfile in self.lis_files:
            self.lis_files_names.append(str(logfile) + ".log")
        #Shows the cyclotron name 
        #self.tableWidget2.setItem(self.current_row_folder,0, QTableWidgetItem(self.dir_))
        if "TCP" in self.dir_:
            self.name = "TCP"
        elif "DIJ" in self.dir_:
            self.name = "DIJ"
        elif "MRS" in self.dir_:
            self.name = "MRS"
        elif "JNS" in self.dir_:
            self.name = "JNS"
        elif "GLY" in self.dir_:
            self.name = "GLY"
        self.tableWidget2.setItem(self.current_row_folder,0, QTableWidgetItem(self.name))
        self.tableWidget2.setItem(self.current_row_folder,1, QTableWidgetItem(str(len(self.lis_files))))
        for i in range(len(self.lis_files)):
            self.tableWidget2.setItem(self.current_row_folder,i+2, QTableWidgetItem(self.lis_files_names[i]))
        self.tableWidget2.setItem(self.current_row_folder,1499, QTableWidgetItem(self.dir_))
        self.current_row_folder += 1

    def motor_position_difference(self,data_df,steady_current,value_motor):
        df_extraction_position_zero_current_source = data_df[value_motor].astype(float).iloc[0]
        #df_extraction_time_zero_current_source = data_df.Time[data_df['Target_I'].astype(float) == 0]
        df_extraction_position_steady_current_source = data_df[value_motor][data_df['Target_I'].astype(float) > steady_current].astype(float)
        #df_extraction_time_steady_current_source = data_df.Time[data_df['Target_I'].astype(float) > steady_current]
        position_difference = - df_extraction_position_zero_current_source + df_extraction_position_steady_current_source.iloc[0]
        motor_flap = position_difference
        print ("MOTOR POSITION DIFFERENCE")
        print (position_difference)
        print (df_extraction_position_zero_current_source)
        print (df_extraction_position_steady_current_source.iloc[0])
        return motor_flap
        #  
    def motor_speed(self,data_df,steady_current,value_motor):
        df_extraction_position_steady_current_source = data_df[value_motor][data_df['Target_I'].astype(float) > steady_current].astype(float)
        df_extraction_time_steady_current_source = data_df.Time[data_df['Target_I'].astype(float) > steady_current]
        df_extraction_position_steady_current_source_average = np.mean(df_extraction_position_steady_current_source) 
        print (df_extraction_time_steady_current_source)
        hour_i = df_extraction_time_steady_current_source.iloc[0][0:2]
        minute_i = df_extraction_time_steady_current_source.iloc[0][3:5]
        seconds_i = df_extraction_time_steady_current_source.iloc[0][6:8]
        hour_f = df_extraction_time_steady_current_source.iloc[-1][0:2]
        minute_f = df_extraction_time_steady_current_source.iloc[-1][3:5]
        seconds_f = df_extraction_time_steady_current_source.iloc[-1][6:8]
        hour_i_total = int(hour_i)*3600+int(minute_i)*60+int(seconds_i)
        hour_f_total = int(hour_f)*3600+int(minute_f)*60+int(seconds_f)
        position_difference = float(- df_extraction_position_steady_current_source.iloc[0] + df_extraction_position_steady_current_source.iloc[-1])
        time_difference = float(hour_f_total - hour_i_total)
        motor_flap = position_difference/time_difference*60
        return motor_flap

        #print (df_extraction_time_ze
 

    def file_open(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName_completed, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        [real_values,target_number,date_stamp] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName_completed))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        max_source_current = saving_files_summary_list_20200420.get_source_parameters_limit(data_df)
        target_current = data_df.Target_I.astype(float)
        steady_current = current 
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        #
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_vacuum = saving_files_summary_list_20200420.get_subsystems_dataframe_vacuum(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_magnet = saving_files_summary_list_20200420.get_subsystems_dataframe_magnet(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_rf = saving_files_summary_list_20200420.get_subsystems_dataframe_rf(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_rf_sparks = saving_files_summary_list_20200420.get_subsystems_dataframe_rf_sparks(data_df,max_source_current,target_number,target_current,time,foil_number)
        df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_pressure = saving_files_summary_list_20200420.get_subsystems_dataframe_pressure(data_df,current,target_number,target_current,time,foil_number)    
        self.df_subsystem_source_all.append(df_subsystem_source)
        self.df_subsystem_vacuum_all.append(df_subsystem_vacuum)
        self.df_subsystem_magnet_all.append(df_subsystem_magnet)
        self.df_subsystem_rf_all.append(df_subsystem_rf)
        self.df_subsystem_extraction_all.append(df_subsystem_extraction)
        self.df_subsystem_beam_all.append(df_subsystem_beam)
        self.df_subsystem_pressure_all.append(df_subsystem_pressure)
        #
        self.df_source = saving_files_summary_list_20200420.get_summary_ion_source(df_subsystem_source,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_source)
        self.df_vacuum = saving_files_summary_list_20200420.get_summary_vacuum(df_subsystem_vacuum,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_vacuum)
        self.df_magnet = saving_files_summary_list_20200420.get_summary_magnet(df_subsystem_magnet,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_magnet)
        self.df_rf = saving_files_summary_list_20200420.get_summary_rf(df_subsystem_rf,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_rf)
        self.df_extraction = saving_files_summary_list_20200420.get_summary_extraction(df_subsystem_extraction,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_extraction)
        self.df_beam = saving_files_summary_list_20200420.get_summary_beam(df_subsystem_beam,str(self.fileName_completed.split("/")[-1]),target_number[1],date_stamp,self.df_beam)
        #print (self.df_source)
        #print (self.df_source.CURRENT_AVE.iloc[0])
        #print (self.df_source)
        # 
        # ["File Name","Target","Average vacuum [mbar]", "Magnet current [A]", "Ion source [mA]", "Dee 1 Voltage [V]", "Dee 2 Voltage [V]", "Target current [muA]", "Average Collimator current [%]"]
        # self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
        motor_extraction = float(self.motor_speed(data_df,steady_current,"Extr_pos"))*60
        motor_flap_1 = float(self.motor_speed(data_df,steady_current,"Flap1_pos"))*60
        motor_flap_2 = float(self.motor_speed(data_df,steady_current,"Flap2_pos"))*60
        motor_extraction_pos = float(self.motor_position_difference(data_df,steady_current,"Extr_pos"))
        motor_flap_1_pos = float(self.motor_position_difference(data_df,steady_current,"Flap1_pos"))
        motor_flap_2_pos = float(self.motor_position_difference(data_df,steady_current,"Flap2_pos"))
        print (float(motor_flap_1))
        #self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName_completed))
        self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
        #self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(self.fileName_completed.split("/")[-2]))
        if "TCP" in self.fileName_completed:
            self.name_complete = "TCP"
        elif "DIJ" in self.fileName_completed:
            self.name_complete = "DIJ"
        elif "MRS" in self.fileName_completed:
            self.name_complete = "MRS"
        elif "JNS" in self.fileName_completed:
            self.name_complete = "JNS"
        elif "GLY" in self.fileName_completed:
            self.name_complete = "GLY"
        self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(self.name_complete))
        print (self.fileName_completed.split("/")[-2])
        print ("AVERAGE VALUES")
        print (str(round(self.df_magnet.CURRENT_AVE.iloc[self.current_row],2)))
        print (str(round(self.df_source.CURRENT_AVE.iloc[self.current_row],2)))
        self.tableWidget.setItem(self.current_row,2, QTableWidgetItem(date_stamp))
        self.tableWidget.setItem(self.current_row,3, QTableWidgetItem(str(target_number)))
        self.tableWidget.setItem(self.current_row,6, QTableWidgetItem(str(round(self.df_vacuum.PRESSURE_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,7, QTableWidgetItem(str(round(self.df_magnet.CURRENT_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,8, QTableWidgetItem(str(round(self.df_source.CURRENT_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,9, QTableWidgetItem(str(round(self.df_rf.DEE1_VOLTAGE_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,10, QTableWidgetItem(str(round(self.df_rf.DEE2_VOLTAGE_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,11, QTableWidgetItem(str(round(self.df_beam.TARGET_CURRENT_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,12, QTableWidgetItem(str(round(self.df_beam.FOIL_CURRENT_AVE.iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,13, QTableWidgetItem(str(round((self.df_beam.COLL_CURRENT_L_AVE.iloc[self.current_row]),2))))
        self.tableWidget.setItem(self.current_row,14, QTableWidgetItem(str(round((self.df_beam.COLL_CURRENT_R_AVE.iloc[self.current_row]),2))))
        self.tableWidget.setItem(self.current_row,15, QTableWidgetItem(str(round((self.df_beam.RELATIVE_COLL_CURRENT_L_AVE.iloc[self.current_row]+self.df_beam.RELATIVE_COLL_CURRENT_R_AVE.iloc[self.current_row]),2))))
        self.tableWidget.setItem(self.current_row,16, QTableWidgetItem(str(round((self.df_beam.RELATIVE_TARGET_CURRENT_AVE.iloc[self.current_row]),2))))
        self.tableWidget.setItem(self.current_row,23, QTableWidgetItem(self.fileName_completed))
        self.datos = [self.tableWidget.item(0,0).text()]
        #target_current = excel_data_df.Target_I[excel_data_df['Target_I'].astype(float) > float(max_current)].astype(float)       
        #print (self.df_rf.DEE1_VOLTAGE_AVE.iloc[self.current_row])
        #print (df_subsystem_rf.Dee_1_kV)
        voltage_limit = (0.8*(self.df_rf.DEE1_VOLTAGE_AVE))       
        voltage_dee_1 = df_subsystem_rf_sparks.Dee_1_kV[df_subsystem_rf_sparks.Dee_1_kV < float(voltage_limit.iloc[self.current_row])]
        voltage_dee_2 = df_subsystem_rf_sparks.Dee_2_kV[df_subsystem_rf_sparks.Dee_2_kV < float(voltage_limit.iloc[self.current_row])]
        self.tableWidget.setItem(self.current_row,4, QTableWidgetItem(str(len(voltage_dee_1))))
        self.tableWidget.setItem(self.current_row,5, QTableWidgetItem(str(len(voltage_dee_2))))
        self.tableWidget.setItem(self.current_row,17, QTableWidgetItem(str(round(motor_flap_1,3))))
        self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(str(round(motor_flap_2,3))))
        self.tableWidget.setItem(self.current_row,19, QTableWidgetItem(str(round(motor_extraction,3))))
        self.tableWidget.setItem(self.current_row,20, QTableWidgetItem(str(round(motor_flap_1_pos,3))))
        self.tableWidget.setItem(self.current_row,21, QTableWidgetItem(str(round(motor_flap_2_pos,3))))
        self.tableWidget.setItem(self.current_row,22, QTableWidgetItem(str(round(motor_extraction_pos,3))))
        self.current_row += 1
        #[target_number,vacuum_average,magnet_average] = saving_files_summary.getting_average_values(str(self.fileName))
        #self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
        #self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(str(target_number)))
        #self.tableWidget.setItem(self.current_row,2, QTableWidgetItem(str(vacuum_average)))
        #self.tableWidget.setItem(self.current_row,3, QTableWidgetItem(str(magnet_average)))
        #self.current_row += 1
        #self.datos = [self.tableWidget.item(0,0).text()]

    def file_output(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        print ("FILEEEEE")
        print (self.fileName_folder)
        saving_files_summary_list_20200420.main(self.fileName_individual,self.output_path,0)
        components = ["Source","Vacuum","Magnet","RF","Extraction","Beam"]
        file_components = [["table_summary_source.out"],["table_summary_vacuum.out"],["table_summary_magnet.out"],["table_summary_rf.out"],["table_summary_extraction.out"],["table_summary_beam.out"]]
        file_components_columns = [["Current","Voltage","Ratio","Source Performance"],["Pressure"],["Magnet Current"],["Dee Voltage","Power","Flap"],["Caroussel"],["Absolute Collimator","Relative Collimator","Absolute Target","Relative Target","Extraction losses","Transmission"]]
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0

    def file_output_already_computed(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        #saving_files_summary_list_20200420.main(self.fileName_individual,self.output_path,0)
        components = ["Source","Vacuum","Magnet","RF","Extraction","Beam"]
        file_components = [["table_summary_source.out"],["table_summary_vacuum.out"],["table_summary_magnet.out"],["table_summary_rf.out"],["table_summary_extraction.out"],["table_summary_beam.out"]]
        file_components_columns = [["Current","Voltage","Ratio","Source Performance"],["Pressure"],["Magnet Current"],["Dee Voltage","Power","Flap"],["Caroussel"],["Absolute Collimator","Relative Collimator","Target","Relative Current Foil","Extraction losses","Transmission"]]
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0

    def folder_analyze(self,values):
        print (self.lis_files_names)
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    def remove_row(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.tableWidget.removeRow(index.row())
        print ("INDEX")
        print (index.row())
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.current_row = self.current_row -1


    def handleSelectionChanged_variabletoanalyze(self):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        # foil being used 
        # percentage of target being used
        # number of preirradiations
        #time 
 
    def handleSelectionChanged_variabletoplot(self, selected, deselected):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        print ("ENTERING HEREE!!!!!")
        print(index.row())
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


    def file_plot(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        #[target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Arc_V.astype(float),data_df.Time,self.fileName[-8:-4],"Source Voltage [V]",1)
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Arc_I.astype(float),data_df.Time,self.fileName[-8:-4],"Source Current [mA]",0)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
        self.sc1.draw()
        self.sc1.show()

    def file_plot_vacuum(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Vacuum_P.astype(float)*1e5,data_df.Time,self.fileName[-8:-4],r"Vacuum P [$10^{-5}$ mbar]",1)
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Arc_I.astype(float),data_df.Time,self.fileName[-8:-4],"Source Current [mA]",0)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)

        self.sc1.draw()
        self.sc1.show()

    def file_plot_collimators_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        #saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),df_subsystem_beam.Target_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]","Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Target_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]",1)
        self.sc4.draw()
        self.sc4.show()

    def file_plot_vacuum_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_vacuum = saving_files_summary_list_20200420.get_subsystems_dataframe_vacuum(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_magnet = saving_files_summary_list_20200420.get_subsystems_dataframe_magnet(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_vacuum.Vacuum_P.astype(float)*1e5,df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Vacuum P [$10^{5}$ mbar]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_magnet.Magnet_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Magnet Current [A]",1)
        self.sc4.draw()
        self.sc4.show()

    
    def file_plot_rf_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_rf = saving_files_summary_list_20200420.get_subsystems_dataframe_rf(data_df,current,target_number,target_current,time,foil_number)
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_1_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 1)[V]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_2_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 2) [V]",1)
        self.sc4.draw()
        self.sc4.show()
    


    def file_plot_extraction_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current)
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Extr_pos.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Extraction Position [%]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Balance.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Balance Position [%]",1)
        self.sc4.draw()
        self.sc4.show()


    def onpick(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         points = tuple(zip(xdata[ind], ydata[ind]))
         self.coordinates_x = xdata[ind][0]
         [real_values,target_number,date_stamp] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
         print ("PLOTTING MAGNETIC FIELD")
         print (self.fileName)
         data_df = saving_files_summary_list_20200420.get_data(real_values)
         [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
         max_source_current = saving_files_summary_list_20200420.get_source_parameters_limit(data_df)
         target_current = data_df.Target_I.astype(float)
         steady_current = current 
         current = 0
         time = saving_files_summary_list_20200420.get_time(data_df,current)
         foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
         df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
         self.df_subsystem_source_selected = self.df_subsystem_source_all[self.row_to_plot]
         self.df_subsystem_rf_selected = self.df_subsystem_rf_all[self.row_to_plot]
         self.df_subsystem_extraction_selected = self.df_subsystem_extraction_all[self.row_to_plot]
         self.df_subsystem_beam_selected = self.df_subsystem_beam_all[self.row_to_plot]
         self.df_subsystem_vacuum_selected = self.df_subsystem_vacuum_all[self.row_to_plot]
         self.df_subsystem_magnet_selected = self.df_subsystem_magnet_all[self.row_to_plot]
         print('onpick points:', points) 
         print (self.coordinates_x)
         value_magnet = (self.df_subsystem_magnet_selected.Magnet_I.tolist()[0])
         print (value_magnet)

         self.tablefiles_tab1.setItem(0,1, QTableWidgetItem(str(data_df.Time.iloc[self.coordinates_x])))
         self.tablefiles_tab1.setItem(1,1, QTableWidgetItem(str(data_df.Vacuum_P.astype(float).iloc[self.coordinates_x]*1e5)))
         self.tablefiles_tab1.setItem(2,1, QTableWidgetItem(str(data_df.Magnet_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(3,1, QTableWidgetItem(str(data_df.Arc_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(4,1, QTableWidgetItem(str(data_df.Dee_1_kV[self.coordinates_x])))
         self.tablefiles_tab1.setItem(5,1, QTableWidgetItem(str(data_df.Dee_2_kV[self.coordinates_x])))
         self.tablefiles_tab1.setItem(6,1, QTableWidgetItem(str(data_df.Flap1_pos[self.coordinates_x])))
         self.tablefiles_tab1.setItem(7,1, QTableWidgetItem(str(data_df.Flap2_pos[self.coordinates_x])))
         self.tablefiles_tab1.setItem(8,1, QTableWidgetItem(str(data_df.RF_fwd_W[self.coordinates_x])))
         self.tablefiles_tab1.setItem(9,1, QTableWidgetItem(str(data_df.RF_refl_W[self.coordinates_x])))
         self.tablefiles_tab1.setItem(10,1, QTableWidgetItem(str(data_df.Extr_pos[self.coordinates_x])))
         self.tablefiles_tab1.setItem(11,1, QTableWidgetItem(str(data_df.Balance[self.coordinates_x])))
         self.tablefiles_tab1.setItem(12,1, QTableWidgetItem(str(data_df.Foil_No[self.coordinates_x])))
         self.tablefiles_tab1.setItem(13,1, QTableWidgetItem(str(data_df.Foil_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(14,1, QTableWidgetItem(str(data_df.Target_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(15,1, QTableWidgetItem(str(data_df.Coll_l_I[self.coordinates_x])))
         self.tablefiles_tab1.setItem(16,1, QTableWidgetItem(str(data_df.Coll_r_I[self.coordinates_x])))
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


    def file_plot_rf(self):
        self.coordinates_x = 0
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        self.df_subsystem_rf_selected = self.df_subsystem_rf_all[self.row_to_plot]
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Dee_1_kV.astype(float),data_df.Dee_2_kV.astype(float),data_df.Time,"Dee1","Dee2","Voltage [kV]",0)
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Flap1_pos.astype(float),data_df.Flap2_pos.astype(float),data_df.Time,"Flap1","Flap2","Position [%]",1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)      
        self.sc1.draw()
        self.sc1.show()

    def file_plot_rf_power(self):
        self.coordinates_x = 0
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.RF_fwd_W.astype(float),data_df.RF_refl_W.astype(float),data_df.Time,"Forwared","Reflected","Power [kW]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Phase_load.astype(float),data_df.Time,self.fileName[-8:-4],"Phase load",1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
        print ("HEREEEEE")
        print (self.coordinates_x)       
        self.sc1.draw()
        self.sc1.show()

    def file_plot_extraction(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Extr_pos.astype(float),data_df.Balance.astype(float),data_df.Time,"Extr_pos","Balance","Position [%]",0)
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Coll_l_I.astype(float),data_df.Coll_r_I.astype(float),data_df.Time,"Coll l ","Coll r",r"Current [$\mu$A]",1)   
        self.sc1.draw()
        self.sc1.show()



    def file_plot_collimation(self):
        #["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Extraction_losses"]
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        self.df_subsystem_beam_selected = df_subsystem_beam
        self.df_subsystem_beam_selected = self.df_subsystem_beam_all[self.row_to_plot]
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Foil_I.astype(float),data_df.Target_I.astype(float),data_df.Time,"Foil I","Target I",r"Current [$\mu$A]",1)
        #saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Coll_l_rel,self.df_subsystem_beam_selected.Coll_r_rel,time,"Coll l rel","Coll r rel",r"Current [%]",1)
        saving_files_summary_list_20200420.get_plots_three_functions_area(self,self.df_subsystem_beam_selected,data_df.Time,r"Current [$\mu$A]",0)
        self.sc1.draw()
        self.sc1.show()

    def file_plot_collimation_target(self):
        #["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Extraction_losses"]
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        self.df_subsystem_extraction_selected = df_subsystem_extraction
        self.df_subsystem_beam_selected = df_subsystem_beam
        print ("HEREEE")
        print (self.df_subsystem_extraction_selected)
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Target_rel,self.df_subsystem_beam_selected.Coll_r_rel.astype(float) + self.df_subsystem_beam_selected.Coll_l_rel.astype(float),data_df.Time,"Target I/Foil I","Collimators I/Foil I","Current [%]",1)
        #saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Coll_l_rel,self.df_subsystem_beam_selected.Coll_r_rel,time,"Coll l rel","Coll r rel",r"Current [%]",1)
        saving_files_summary_list_20200420.get_plots_three_functions_area(self,self.df_subsystem_beam_selected,data_df.Time,r"Current [$\mu$A]",0)
        self.sc1.draw()
        self.sc1.show()

    def file_plot_magnet(self):
        [real_values,target_number,date_stamp] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        print ("PLOTTING MAGNETIC FIELD")
        print (self.fileName)
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()  
        self.df_subsystem_magnet_selected = self.df_subsystem_magnet_all[self.row_to_plot]    
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Magnet_I.astype(float),data_df.Time,self.fileName[-8:-4],"Magnet Current [A]",0)
        df_iso = saving_files_summary_list_20200420.get_isochronism(data_df)
        print ("HEREEEE ISO")
        print (df_iso)
        print ((df_iso.Coll_l_I).astype(float) + (df_iso.Coll_r_I).astype(float))
        saving_files_summary_list_20200420.get_plots_tunning(self,(df_iso.Coll_l_I).astype(float) + (df_iso.Coll_r_I).astype(float),df_iso.Target_I,df_iso.Foil_I,df_iso.Magnet_I,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
        self.sc1.draw()
        self.sc1.show()


    #self.df_subsystem_source_selected = self.df_subsystem_source_all[self.row_to_plot]
    #self.df_subsystem_vacuum_selected = self.df_subsystem_vacuum_all[self.row_to_plot]
    #

    def handleSelectionFile(self, selected, deselected):
        index=(self.tableWidget.selectionModel().currentIndex())
        #self.fileName=index.sibling(index.row(),index.column()).data()
        self.fileName=index.sibling(index.row(),23).data()
        #self.fileName=os.path.join(self.dir_,self.fileName)
        self.row_to_plot = index.row()
        print(self.fileName)

    def handleSelectionFolder(self, selected, deselected):
        index=(self.tableWidget2.selectionModel().currentIndex())
        index2 = self.tableWidget2.selectionModel().selectedRows()
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.fileName_folder= index.sibling(index.row(),1499).data()
        #self.fileName_folder= index.sibling(index.row(),0).data()
        try:
           self.fileName_completed = os.path.join(self.fileName_folder,self.fileName)
           #self.fileName_completed = os.path.join(self.dir_,self.fileName)
        except: 
           self.fileName_completed = ""
        #self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName_completed))
        #[real_values,target_number,date_stamp ] = saving_files_summary.get_data_tuple(str(self.fileName))
        try:
             [real_values,target_number,date_stamp] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName_completed))
             data_df = saving_files_summary_list_20200420.get_data(real_values)
             [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
             target_current = data_df.Target_I.astype(float)
             steady_current = current
             motor_extraction = float(self.motor_speed(data_df,steady_current,"Extr_pos"))*60
             motor_flap_1 = float(self.motor_speed(data_df,steady_current,"Flap1_pos"))*60
             motor_flap_2 = float(self.motor_speed(data_df,steady_current,"Flap2_pos"))*60
             motor_extraction_pos = float(self.motor_position_difference(data_df,steady_current,"Extr_pos"))
             motor_flap_1_pos = float(self.motor_position_difference(data_df,steady_current,"Flap1_pos"))
             motor_flap_2_pos = float(self.motor_position_difference(data_df,steady_current,"Flap2_pos"))
             current = 0
             max_source_current = saving_files_summary_list_20200420.get_source_parameters_limit(data_df)
             time = saving_files_summary_list_20200420.get_time(data_df,current)
             foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        #
             df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_vacuum = saving_files_summary_list_20200420.get_subsystems_dataframe_vacuum(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_magnet = saving_files_summary_list_20200420.get_subsystems_dataframe_magnet(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_rf = saving_files_summary_list_20200420.get_subsystems_dataframe_rf(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_rf_sparks = saving_files_summary_list_20200420.get_subsystems_dataframe_rf_sparks(data_df,max_source_current,target_number,target_current,time,foil_number)
             df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
             df_subsystem_pressure = saving_files_summary_list_20200420.get_subsystems_dataframe_pressure(data_df,current,target_number,target_current,time,foil_number)   
             [probe_current,ion_source_current,source_performance] = saving_files_summary_list_20200420.get_ion_source_performance(data_df) 
             self.df_subsystem_source_all.append(df_subsystem_source)
             self.df_subsystem_vacuum_all.append(df_subsystem_vacuum)
             self.df_subsystem_magnet_all.append(df_subsystem_magnet)
             self.df_subsystem_rf_all.append(df_subsystem_rf)
             self.df_subsystem_extraction_all.append(df_subsystem_extraction)
             self.df_subsystem_beam_all.append(df_subsystem_beam)
             self.df_subsystem_pressure_all.append(df_subsystem_pressure)
             #  
             self.df_source = saving_files_summary_list_20200420.get_summary_ion_source(df_subsystem_source,source_performance,str(self.fileName),target_number[1],date_stamp,self.df_source)
             self.df_vacuum = saving_files_summary_list_20200420.get_summary_vacuum(df_subsystem_vacuum,str(self.fileName),target_number[1],date_stamp,self.df_vacuum)
             self.df_magnet = saving_files_summary_list_20200420.get_summary_magnet(df_subsystem_magnet,str(self.fileName),target_number[1],date_stamp,self.df_magnet)
             self.df_rf = saving_files_summary_list_20200420.get_summary_rf(df_subsystem_rf,str(self.fileName),target_number[1],date_stamp,self.df_rf)
             self.df_extraction = saving_files_summary_list_20200420.get_summary_extraction(df_subsystem_extraction,str(self.fileName),target_number[1],date_stamp,self.df_extraction)
             self.df_beam = saving_files_summary_list_20200420.get_summary_beam(df_subsystem_beam,str(self.fileName),target_number[1],date_stamp,self.df_beam)
             #print (self.df_source)
             #print (self.df_source.CURRENT_AVE.iloc[0])
             #print (self.df_source)
             # 
             # ["File Name","Target","Average vacuum [mbar]", "Magnet current [A]", "Ion source [mA]", "Dee 1 Voltage [V]", "Dee 2 Voltage [V]", "Target current [muA]", "Average Collimator current [%]"]
             # self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
             print ("INFORMATION")
             print (str(round(self.df_vacuum.PRESSURE_AVE.iloc[self.current_row],2)))
             print (str(round(self.df_magnet.CURRENT_AVE.iloc[self.current_row],2)))
             print (str(round(self.df_source.CURRENT_AVE.iloc[self.current_row],2)))
             if "TCP" in self.fileName_completed:
                 self.name_complete = "TCP"
             elif "DIJ" in self.fileName_completed:
                 self.name_complete = "DIJ"
             elif "MRS" in self.fileName_completed:
                 self.name_complete = "MRS"
             elif "JNS" in self.fileName_completed:
                 self.name_complete = "JNS"
             elif "GLY" in self.fileName_completed:
                 self.name_complete = "GLY"
             self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(self.name_complete))
             #self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName_completed))
             #self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(self.fileName_completed.split("/")[-2]))
             self.tableWidget.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
             #self.tableWidget.setItem(self.current_row,1, QTableWidgetItem(self.name))
             self.tableWidget.setItem(self.current_row,2, QTableWidgetItem(date_stamp))
             self.tableWidget.setItem(self.current_row,3, QTableWidgetItem(str(target_number)))
             self.tableWidget.setItem(self.current_row,6, QTableWidgetItem(str(round(self.df_vacuum.PRESSURE_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,7, QTableWidgetItem(str(round(self.df_magnet.CURRENT_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,8, QTableWidgetItem(str(round(self.df_source.CURRENT_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,9, QTableWidgetItem(str(round(self.df_rf.DEE1_VOLTAGE_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,10, QTableWidgetItem(str(round(self.df_rf.DEE2_VOLTAGE_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,11, QTableWidgetItem(str(round(self.df_beam.TARGET_CURRENT_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,12, QTableWidgetItem(str(round(self.df_beam.FOIL_CURRENT_AVE.iloc[self.current_row],2))))
             self.tableWidget.setItem(self.current_row,13, QTableWidgetItem(str(round((self.df_beam.COLL_CURRENT_L_AVE.iloc[self.current_row]),2))))
             self.tableWidget.setItem(self.current_row,14, QTableWidgetItem(str(round((self.df_beam.COLL_CURRENT_R_AVE.iloc[self.current_row]),2))))
             self.tableWidget.setItem(self.current_row,15, QTableWidgetItem(str(round((self.df_beam.RELATIVE_COLL_CURRENT_L_AVE.iloc[self.current_row]+self.df_beam.RELATIVE_COLL_CURRENT_R_AVE.iloc[self.current_row]),2))))
             self.tableWidget.setItem(self.current_row,16, QTableWidgetItem(str(round((self.df_beam.RELATIVE_TARGET_CURRENT_AVE.iloc[self.current_row]),2))))
             self.tableWidget.setItem(self.current_row,23, QTableWidgetItem(self.fileName_completed))
             self.datos = [self.tableWidget.item(0,0).text()]
             #target_current = excel_data_df.Target_I[excel_data_df['Target_I'].astype(float) > float(max_current)].astype(float)
             #print (self.df_rf.DEE1_VOLTAGE_AVE.iloc[self.current_row])
             #print (df_subsystem_rf.Dee_1_kV)
             voltage_limit = (0.8*(self.df_rf.DEE1_VOLTAGE_AVE))
             voltage_dee_1 = df_subsystem_rf_sparks.Dee_1_kV[df_subsystem_rf_sparks.Dee_1_kV < float(voltage_limit.iloc[self.current_row])]
             voltage_dee_2 = df_subsystem_rf_sparks.Dee_2_kV[df_subsystem_rf_sparks.Dee_2_kV < float(voltage_limit.iloc[self.current_row])]
             self.tableWidget.setItem(self.current_row,4, QTableWidgetItem(str(len(voltage_dee_1))))
             self.tableWidget.setItem(self.current_row,5, QTableWidgetItem(str(len(voltage_dee_2))))
             self.tableWidget.setItem(self.current_row,17, QTableWidgetItem(str(round(motor_flap_1,3))))
             self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(str(round(motor_flap_2,3))))
             self.tableWidget.setItem(self.current_row,19, QTableWidgetItem(str(round(motor_extraction,3))))
             self.tableWidget.setItem(self.current_row,20, QTableWidgetItem(str(round(motor_flap_1_pos,3))))
             self.tableWidget.setItem(self.current_row,21, QTableWidgetItem(str(round(motor_flap_2_pos,3))))
             self.tableWidget.setItem(self.current_row,22, QTableWidgetItem(str(round(motor_extraction_pos,3))))
             self.current_row += 1
        except:
            print ("before the for loop")
            for index3 in self.tableWidget2.selectionModel().selectedRows():
                 print (index3)
                 print('Row %d is selected' % index3.row())
                 #self.fileName_folder = self.tableWidget2.item(index3.row(),0).text()
                 self.fileName_folder = index.sibling(index.row(),1499).data()
                 self.fileName_number = self.tableWidget2.item(index3.row(),1).text()
                 self.fileName_individual = []
                 self.fileName_individual.append(self.fileName_folder)
                 print ("NUMBER OF FILES")
                 print (self.fileName_number)
                 for i in range(int(self.fileName_number)):
                    self.fileName_individual.append(self.tableWidget2.item(index3.row(),i+2).text())
                 #self.fileName_individual = self.fileName_individual[1:]
                 print (self.fileName_individual)
               
        ##for index in self.tableWidget.selectionModel().selectedRows():
        ##    print (index)
        #    print('Row %d is selected' % index.row())
        #    self.fileName = self.tableWidget.item(0,0).text()
        #    print (self.fileName)



    def Clear(self):
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.draw()
        self.axes_1.clear()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.ax.clear()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.ax.clear()
        self.ui.widget_4.canvas.draw()


    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50 , 500, 300)


    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass




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
