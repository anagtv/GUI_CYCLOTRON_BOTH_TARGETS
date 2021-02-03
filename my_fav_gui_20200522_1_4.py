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
        #
        menus.edit_menu(self)
        #
        menus.plot_menu(self)
        #
        menus.plot_menu_source(self)
        #
        menus.remove_menu(self)
        #
        menus.adding_open_actions(self)
        menus.adding_edit_actions(self)
        menus.adding_plot_actions(self)
        menus.adding_plot_source(self)
        #

     
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
        print ("FILENAME")
        print (self.fileName)
        self.row_to_plot = index.row()
        managing_files.file_open(self)
        print ("dataframe")
        print (self.file_df)

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
         time = saving_files_summary_list_20200420.get_time(self.file_df,current)
         foil_number = saving_files_summary_list_20200420.get_foil_number(self.file_df,current) 
         #df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(self.file_df,current,self.target_number,target_current,time,foil_number)
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
         #self.table_summary_log.setItem(18,1, QTableWidgetItem(str(round(self.df_subsystem_beam.Coll_r_rel[self.coordinates_x],2))))
         #self.table_summary_log.setItem(19,1, QTableWidgetItem(str(round(self.df_subsystem_beam.Target_rel[self.coordinates_x],2))))
         self.current_row_statistics += 1

    def handleSelectionChanged_variabletoanalyze(self):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()


    def selecting_data_to_plot_reset(self):
        self.tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == self.target_1])
        self.tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == self.target_2])
        self.tfs_target_1_no_reset = (self.tfs_input[self.tfs_input.TARGET == self.target_1])
        self.tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == self.target_2])
        self.tfs_unique_target_1 = (self.tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
        self.tfs_unique_target_4 = (self.tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
        self.tfs_target_1.reset_index(drop=True, inplace=True)
        self.tfs_target_4.reset_index(drop=True, inplace=True)

    def getting_position(tfs_target,tfs_unique_target):
        index_foil = (((tfs_target.FOIL[tfs_target["FOIL"] == tfs_unique_target.FOIL.iloc[i]].index))).tolist()
        return index_foil

    def foil_research(self,tfs_target,tfs_target_no_reset,tfs_unique_target):
        index_foil_list = []
        index_foil_list_position = []
        unique_index_foil = np.array(tfs_unique_target.FOIL)
        for i in range(len(tfs_unique_target.FOIL)):
           # get all the positions where a given foil is and convert to a list (TARGET 1)
           positions = tfs_target.FOIL[tfs_target["FOIL"] == tfs_unique_target.FOIL.iloc[i]]
           index_foil = getting_position(tfs_target,tfs_unique_target)
           index_foil_position = getting_position(tfs_target_no_reset,tfs_unique_target)
           # list of positions within the dataframe T1
           index_foil_list.append(index_foil_tolist)
           # list of positions in the original dataframe
           index_foil_list_position.append(index_foil_position_tolist)
        return index_foil_list,index_foil_list_position,unique_index_foil

    def handleSelectionChanged_variabletoplot(self):
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out",
        "table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out",
        "table_summary_transmission.out"]
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
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names[index.row()]))
        print (self.tfs_input)
        self.target_2 = int(np.max(self.tfs_input.TARGET))-3
        self.target_1 = self.target_2-3
        self.sc3.axes.clear()  
        self.selecting_data_to_plot_reset()    
        index_foil_list_1,index_foil_list_1_position,unique_index_foil_1 = self.foil_research(self.tfs_target_1,self.tfs_target_1_no_reset,self.tfs_unique_target_1)
        index_foil_list_4,index_foil_list_4_position,unique_index_foil_4 = self.foil_research(self.tfs_target_1,self.tfs_target_1_no_reset,self.tfs_unique_target_1)
        unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
        unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
        index_foil_sorted_1 = np.sort(index_foil_list_1)
        index_foil_sorted_4 = np.sort(index_foil_list_4)
        index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
        index_foil_sorted_4_position = np.sort(index_foil_list_4_position)     
        if index.row() in range(6):    
            if index.row() == 4:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            elif index.row() == 3: 
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            else:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)        
        elif index.row() in [13,14,15]:      
            if index.row() == 15:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,0) 
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)     
        elif index.row() in [10,11,12]:
            if index.row() == 12:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_with_foil(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_collimators(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)       
        else:
              if index.row() == 9:
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_extraction(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.max_min_value,1,self.flag_no_gap)       
              else: 
                   print (self.tfs_input)
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)       
        self.sc3.fig.canvas.mpl_connect('pick_event', selecting_trends.onpick_trends)
        self.sc3.draw()
        self.sc3.show()

class plotting_data(editing_table,menus_functions):

    def __init__(self):
        super(plotting_data, self).__init__()
        #self.lay = QtWidgets.QVBoxLayout(self.main_widget) 
        menus.plot_source_actions(self)
        menus.edit_actions(self)
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

    def flag_day_gap(self):
        self.flag_no_gap = 0

    # FUNCTIONS USING A CONNECT 
        


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        #Gui_tables = menus_functions()
        Gui_tabs = plotting_data()      
        sys.exit(app.exec_())

run()
