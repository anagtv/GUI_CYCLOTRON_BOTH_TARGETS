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
import columns_names
import menus
import home_tabs
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
        #frameWidget = UpdateFrame(self)
        self.setWindowTitle("Cyclotron Analysis")
        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowIcon(QIcon('pic.png'))
        #menus.main_menu(self)
        self.mainMenu = self.menuBar()
        self.main_widget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.main_widget)
        self.scrollArea.setWidgetResizable(True)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.lay = QtWidgets.QVBoxLayout(self.main_widget)   
        self.setMinimumSize(1000, 800)
        #


class menus_functions(window):
    def __init__(self):
        super(menus_functions, self).__init__()
        # INIALIZE VARIABLE
        columns_names.flags(self)
        columns_names.initial_df(self)
        # STARTING MENUS
        menus.open_menu(self)
        menus.open_menu_actions(self)
        menus.edit_menu(self)
        menus.plot_menu(self)
        menus.plot_menu_source(self)
        menus.remove_menu(self)
        menus.adding_open_actions(self)
        menus.adding_edit_actions(self)
        menus.adding_plot_actions(self)
        menus.adding_plot_source(self)

     
    def file_open_message(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName_completed, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS","All Files (*);;Python Files (*.py)", options=options)
        managing_files.file_open(self)
        managing_files.file_open_summary(self)
        self.first_row = [self.file_number,self.name,self.date_stamp,self.target_number]
        plotting_data.writing_values(self)

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
            saving_trends.getting_summary(self)
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0      

class editing_table(window):
    def __init__(self):
        super(editing_table, self).__init__()
        columns_names.flags(self)
        columns_names.initial_df(self)
        menus.remove_menu(self)
        menus.main_menu(self)
        #self.setCentralWidget(self.main_widget)
        #self.lay = QtWidgets.QVBoxLayout(self.main_widget)   
        #self.setMinimumSize(1000, 800)
        home_tabs.home(self)
        menus.remove_menu_action(self)

    def remove_row(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.tableWidget.removeRow(index.row())
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.current_row = self.current_row -1

    def writing_values(self):
        beam_summary = [self.df_vacuum.PRESSURE_AVE,self.df_magnet.CURRENT_AVE,self.df_source.CURRENT_AVE,self.df_rf.DEE1_VOLTAGE_AVE,self.df_rf.DEE2_VOLTAGE_AVE,
        self.df_beam.TARGET_CURRENT_AVE,self.df_beam.FOIL_CURRENT_AVE,self.df_beam.COLL_CURRENT_L_AVE,self.df_beam.COLL_CURRENT_R_AVE,self.df_beam.RELATIVE_COLL_CURRENT_AVE,
        self.df_beam.RELATIVE_TARGET_CURRENT_AVE]
        self.tableWidget.setItem(self.current_row,4, QTableWidgetItem(str(len(self.voltage_dee_1))))
        self.tableWidget.setItem(self.current_row,5, QTableWidgetItem(str(len(self.voltage_dee_2))))
        for i in range(4):
             self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(self.first_row[i]))
        for i in range(6,17):
             print (beam_summary[i-6].iloc[self.current_row])
             self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(str(round(beam_summary[i-6].iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(self.fileName_completed))
        self.datos = [self.tableWidget.item(0,0).text()]    
        self.current_row += 1

    def handleSelectionFile(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.fileName = index.sibling(index.row(),18).data()
        self.row_to_plot = index.row()
        managing_files.file_open(self)

    def folder_analyze(self,values):
        #When pressed on Cyclotron trends
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    def handleSelectionFolder(self):
        index=(self.tableWidget_logfiles.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.fileName_folder= index.sibling(index.row(),1499).data()
        self.fileName_completed = os.path.join(self.fileName_folder,self.fileName)
        try:
            managing_files.file_open(self)
            managing_files.file_open_summary(self)
            self.first_row = [self.file_number,self.name,self.date_stamp,self.target_number]
            self.writing_values()
        except:
            # Exception for computing trends
            print ("before the for loop")
            self.fileName_folder = index.sibling(index.row(),1499).data()
            self.fileName_number = self.tableWidget_logfiles.item(index.row(),1).text()
            

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
         #time = saving_files_summary_list_20200420.get_time(self.file_df,current)
         foil_number = saving_files_summary_list_20200420.get_foil_number(self.file_df,current) 
         self.table_summary_log.setItem(0,1, QTableWidgetItem(str(self.file_df.Time.iloc[self.coordinates_x])))
         self.table_summary_log.setItem(1,1, QTableWidgetItem(str(self.file_df.Vacuum_P.astype(float).iloc[self.coordinates_x]*1e5)))
         function_names = [self.file_df.Magnet_I,self.file_df.Arc_I,self.file_df.Dee_1_kV,self.file_df.Dee_2_kV,
         self.file_df.Flap1_pos,self.file_df.Flap2_pos,self.file_df.RF_fwd_W,self.file_df.RF_refl_W,
         self.file_df.Extr_pos,self.file_df.Balance,self.file_df.Foil_No,self.file_df.Foil_I,self.file_df.Target_I,self.file_df.Coll_l_I,self.file_df.Coll_r_I,
         self.df_subsystem_beam.Coll_l_rel,self.df_subsystem_beam.Coll_r_rel,self.df_subsystem_beam.Target_rel]
         for i in range (2,17):
            print (i)
            self.table_summary_log.setItem(i,1, QTableWidgetItem(str(function_names[i-2][self.coordinates_x])))
         for i in range (17,20):
            self.table_summary_log.setItem(17,1, QTableWidgetItem(str(round(function_names[i-2][self.coordinates_x],2))))
         self.current_row_statistics += 1

    def onpick_trends(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         self.coordinates_x = xdata[ind][0]
         self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str("CYCLOTRON")))
         #self.tablestatistic_tab2.setItem(0,1, QTableWidgetItem(self.name))
         self.tablestatistic_tab2.setItem(1,1, QTableWidgetItem(str(self.tfs_input.DATE.iloc[self.coordinates_x][5:])))
         self.tablestatistic_tab2.setItem(2,1, QTableWidgetItem(str(self.tfs_input.FILE.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(3,1, QTableWidgetItem(str(self.tfs_input.FOIL.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(1,0, QTableWidgetItem(str("DATE")))
         self.tablestatistic_tab2.setItem(2,0, QTableWidgetItem(str("FILE")))
         self.tablestatistic_tab2.setItem(3,0, QTableWidgetItem(str("FOIL")))
         index = ((self.tablefiles_tab2.selectionModel().currentIndex()))
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

    def handleSelectionChanged_variabletoanalyze(self):
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out",
        "table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out",
        "table_summary_transmission.out"]
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        #self.fileName=index.sibling(index.row(),index.column()).data()
        print ("FILE OPENING")
        print (index.row())
        print (self.output_path)
        print (os.path.join(self.output_path,summary_file_names[index.row()]))
        self.fileName = os.path.join(self.output_path,summary_file_names[index.row()])



class plotting_data(editing_table,menus_functions):

    def __init__(self):
        super(plotting_data, self).__init__()
        #self.lay = QtWidgets.QVBoxLayout(self.main_widget) 
        menus.plot_source_actions(self)
        #menus.edit_actions(self)
        self.edit_actions()
        self.plot_actions()
 
    def file_plot(self):
        file_plots.file_plot(self)

    def plot_actions(self):
        self.openPlotI.setShortcut('Ctrl+E')
        self.openPlotI.setStatusTip('Plot files')
        self.openPlotI.triggered.connect(self.setting_plot_current)
        self.openPlotIV.triggered.connect(self.setting_plot_vacuum)
        self.openPlotRF.triggered.connect(self.setting_plot_RF)
        self.openPlotRFPower.triggered.connect(self.setting_plot_RF_power)
        self.openPlotM.triggered.connect(self.setting_plot_magnet)      
        self.openPlotEx.triggered.connect(file_plots.file_plot_extraction)
        self.openPlotCol.triggered.connect(file_plots.file_plot_collimation)
        self.openPlotColTarget.triggered.connect(file_plots.file_plot_collimation_target)

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


    def setting_plot_current(self):
        self.x_values = self.file_df.Time
        self.y_values_left = self.file_df.Arc_I.astype(float)
        self.y_values_right = self.file_df.Arc_V.astype(float)
        self.label_left = r"Source Voltage [V]"
        self.label_right = "Source Current [mA]"
        file_plots.file_plot_one_functions(self)

    def setting_plot_vacuum(self):
        self.x_values = self.file_df.Time
        self.y_values_left = self.file_df.Vacuum_P.astype(float)*1e5
        self.y_values_right = self.file_df.Arc_I.astype(float)
        self.label_left = r"Vacuum P [$10^{-5}$ mbar]"
        self.label_right = "Source Current [mA]"
        file_plots.file_plot_one_functions(self)

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


    def setting_plot_magnet(self):
        self.x_values = self.file_df.Time
        self.y_values_left = self.file_df.Magnet_I.astype(float)
        self.df_iso = saving_files_summary_list_20200420.get_isochronism(self.file_df)
        self.y_values_coll = (self.df_iso.Coll_l_I).astype(float) + (self.df_iso.Coll_r_I).astype(float)
        self.y_values_target = self.df_iso.Target_I
        self.y_values_foil = self.df_iso.Foil_I
        self.y_values_magnet = self.df_iso.Magnet_I
        self.label_left = r"Magnet current [A]"
        self.label_right = "Isochronism"
        file_plots.file_plot_iso_one_functions(self)

    def setting_plot_extraction(self):
        ...

    def setting_plot_collimation(self):
        ...

    def setting_plot_collimation_target(self):
        ...
 
 
    #FLAGS

    def flag_max(self):
        print ("HEREEEEEEEEE MAX")
        self.max_min_value = "1"

    def flag_max_reset(self):
        print ("HEREEEEE MAX RESET")
        self.max_min_value = "0"

    def flag_target1(self):
        print ("HEREEEEE TARGET 1")
        self.target_1_value = "1"

    def flag_target1_add(self):
        print ("HEREEEEE TARGET 1 (ADD)")
        self.target_1_value = "0"

    def flag_target4(self):
        print ("HEREEEEE TARGET 4")
        print (self.target_2_value)
        self.target_2_value = "1"
        print (self.target_2_value)
        
    def flag_target4_add(self):
        print ("HEREEEEE TARGET 4 (ADD)")
        self.target_2_value = "0"

    def flag_week(self):
        print ("HEREEEEE WEEK")
        self.week_value = "1"
        self.day_value = "0"

    def flag_day(self):
        print ("HEREEEE DAY")
        self.week_value = "0"
        self.day_value = "1"
        
    def flag_no_day_gap(self):
        print ("HEREEEEEE NO GAP")
        self.flag_no_gap = "1"

    def flag_day_gap(self):
        self.flag_no_gap = "0"

    # FUNCTIONS USING A CONNECT 



    def handleSelectionChanged_variabletoplot(self):
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out",
        "table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out",
        "table_summary_transmission.out"]
        labels = ["CURRENT_","VOLTAGE_","RATIO_","SOURCE_PERFORMANCE_","PRESSURE_","CURRENT_","RELATIVE_TARGET_CURRENT_","EXTRACTION_LOSSES_","TRANSMISSION_"]
        labels_1 = ["DEE1_VOLTAGE_","FORWARD_POWER_","FLAP1_","CAROUSEL_POSITION_","COLL_CURRENT_L_","RELATIVE_COLL_CURRENT_L_","TARGET_CURRENT_"]
        labels_2 = ["DEE2_VOLTAGE_","REFLECTED_POWER_","FLAP2_","BALANCE_POSITION_","COLL_CURRENT_R_","RELATIVE_COLL_CURRENT_R_","FOIL_CURRENT_"]
        ylabel = ["CURRENT [mA]","VOLTAGE [V]",r"RATIO [mA/$\mu A$]",r"RATIO [$\mu A$/mA]",r"PRESSURE [$10^{-5}$mbar]","MAGNET CURRENT [A]",r"RELATIVE CURRENT (FOIL)[%]","LOSSES [%]",r"TRANSMISSION RATE [($\mu A$ Foil/$\mu A$ Probe) %]"]
        ylabel_d = ["AVERAGE VOLTAGE [kV]",r"AVERAGE POWER [kW]",r"AVERAGE POSITION [%]",r"POSITION [%]",r"CURRENT [$\mu A$]",r"RELATIVE CURRENT [%]",r"AVERAGE CURRENT [$\mu$A]"]
        file_name = ["ion_source_evolution.pdf","voltage_evolution.pdf","ratio_evolution.pdf","source_performance.pdf","vacuum_evolution.pdf","magnet_evolution.pdf","relative_currents_foil.pdf","efficiency_target_evolution.pdf","transmission.pdf"]
        file_name_d = ["dee1_dee2_voltage_evolution.pdf","power_evolution.pdf","flap_evolution.pdf","carousel_balance_evolution.pdf","collimator_current_evolution.pdf","absolute_collimator_current_evolution.pdf","target_foil_evolution.pdf"]
        legend = ["T","T","T","T","T","T","T","T","T"]
        legend_1 = ["DEE1","FORWARDED ","FLAP 1 ","CAROUSEL ","COLLIMATOR  L","COLLIMATOR  L","TARGET ","COLLIMATOR L ","TARGET "]
        legend_2 = ["DEE2","REFELECTED ","FLAP 2 ","BALANCE ","COLLIMATOR  R","COLLIMATOR  R","FOIL ","COLLIMATOR R ","FOIL "]
        #
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names[index.row()]))
        self.target_2 = int(np.max(self.tfs_input.TARGET))
        self.target_1 = self.target_2-3 
        self.data_1 = self.tfs_input[self.tfs_input.TARGET == str(self.target_1)]
        self.data_2 = self.tfs_input[self.tfs_input.TARGET == str(self.target_2)]
        self.sc3.axes.clear() 
        # Defining the classes for the two targets 
        target_information_1 = target_information() 
        target_information_2 = target_information()
        target_information_1_extra = target_information() 
        target_information_2_extra = target_information()
        target_information_1.selecting_data_to_plot_reset(self.data_1,self.target_1)
        target_information_2.selecting_data_to_plot_reset(self.data_2,self.target_2)
        target_information_1_extra.selecting_data_to_plot_reset(self.data_1,self.target_1)
        target_information_2_extra.selecting_data_to_plot_reset(self.data_2,self.target_2)
        target_information_1.foil_research()
        target_information_1.sortering_data()       
        target_information_2.foil_research()
        target_information_2.sortering_data()
        target_information_1_extra.foil_research()
        target_information_1_extra.sortering_data()       
        target_information_2_extra.foil_research()
        target_information_2_extra.sortering_data()
        targets_summary = [target_information_1,target_information_2]
        targets_summary_extra = [target_information_1,target_information_2,target_information_1_extra,target_information_2_extra]
        #
        self.flag_max_reset()
        #
        if index.row() in [3,15]:
            self.flag_max()
        if index.row() == 5:
            uppper_limit = 1 
            lower_limit = 1
        else: 
            uppper_limit = 1.1
            lower_limit = 0.9
        if index.row() in [0,1,2,3,4,5]:   
            summary = [labels[index.row()],legend[index.row()],file_name[index.row()],"1"]
            limits = [ylabel[index.row()],uppper_limit,lower_limit]  
            if index.row() == 3:
                self.flag_max() 
                summary = [labels[index.row()],legend[index.row()],file_name[index.row()],"0"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,targets_summary,summary,limits)    
            else:                    
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,targets_summary,summary,limits)
        elif index.row() in [13,14,15]: 
            self.flag_max()
            summary = [labels[index.row()-7],legend[index.row()-7],file_name[index.row()-7],"0"]
            limits = [ylabel[index.row()-7],uppper_limit,lower_limit]     
            if index.row() == 15:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,targets_summary,summary,limits)
            else:
                summary = [labels[index.row()-7],legend[index.row()-7],file_name[index.row()-7],"1"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,targets_summary,summary,limits)           
        else: 
            self.flag_max()           
            summary = [labels_1[index.row()-6],labels_2[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],file_name_d[index.row()-6],"0"]
            limits = [ylabel_d[index.row()-6],uppper_limit,lower_limit]
            if index.row() in [10,11,12]:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,targets_summary_extra,summary,limits)
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,targets_summary_extra,summary,limits)
           
            
        
class target_information(editing_table):
    def __init__(self):
        self.index_foil_list = []
        self.index_foil_list_position = []
        self.unique_index_foil_sorted = []
        self.unique_index_foil = []
        self.index_foil_sorted = []
        self.index_foil_sorted_position = []
        self.ave_value = []
        self.max_value = []
        self.min_value = []
        self.std_value = []
        self.x_values = []
    
    def selecting_data_to_plot_reset(self,data,target):
        self.tfs_target = data
        self.tfs_target.reset_index(drop=True, inplace=True)
        self.tfs_target_no_reset = (data)
        self.tfs_unique_target = (self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))
        self.tfs_unique_target_array = np.array(self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))

  
    def foil_research(self):
            print ("FOIL")
            print (self.tfs_unique_target)
            self.unique_index_foil = np.array(self.tfs_unique_target.FOIL)
            for i in range(len(self.tfs_unique_target.FOIL)):
               # get all the positions where a given foil is and convert to a list (TARGET 1)
               self.getting_position(i)
               # list of positions within the dataframe T1
               self.index_foil_list.append(self.index_foil)
               # list of positions in the original dataframe
               self.index_foil_list_position.append(self.index_foil_position)

    def sortering_data(self):
        self.unique_index_foil_sorted = [self.tfs_unique_target.FOIL for _,self.tfs_unique_target.FOIL in sorted(zip(self.index_foil_list,self.tfs_unique_target.FOIL))]
        self.index_foil_sorted = np.sort(self.index_foil_list)
        self.index_foil_sorted_position = np.sort(self.index_foil_list_position)

    def getting_position(self,i):
        self.index_foil = (((self.tfs_target.FOIL[self.tfs_target["FOIL"] == self.tfs_unique_target.FOIL.iloc[i]].index))).tolist()
        self.index_foil_position = (((self.tfs_target_no_reset.FOIL[self.tfs_target["FOIL"] == self.tfs_unique_target.FOIL.iloc[i]].index))).tolist()






if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        #Gui_tables = menus_functions()
        Gui_tabs = plotting_data()      
        sys.exit(app.exec_())

run()
