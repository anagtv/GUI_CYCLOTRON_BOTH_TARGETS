import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
import matplotlib.pyplot as plt
import getting_subsystems_data
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
import columns_names
import menus
import home_tabs
#import editing_table_class
#stheclass = TheClass()
#import plotting_data_class
#matplotlib.use('Qt5Agg')


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Cyclotron Analysis")
        self.setGeometry(50, 50, 1500, 1000)
        menus.main_menu(self)
        self.mainMenu = self.menuBar()
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.lay = QtWidgets.QVBoxLayout(self.main_widget)   
        self.setMinimumSize(1000, 800)
        #

class editing_table(window):
    def __init__(self):
        super(editing_table, self).__init__()
        columns_names.flags(self)
        columns_names.initial_df(self)
        menus.remove_menu(self)
        menus.main_menu(self)
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
             self.tableWidget.setItem(self.current_row,i, QTableWidgetItem(str(round(beam_summary[i-6].iloc[self.current_row],2))))
        self.tableWidget.setItem(self.current_row,18, QTableWidgetItem(self.fileName))
        self.datos = [self.tableWidget.item(0,0).text()]    
        self.current_row += 1

    def handleSelectionFile(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        self.fileName = index.sibling(index.row(),18).data()
        self.row_to_plot = index.row()
        managing_files.file_open(self)
        managing_files.file_open_summary(self)

    def handleSelectionFolder(self):
        index=(self.tableWidget_logfiles.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.fileName_folder= index.sibling(index.row(),1499).data()
        self.fileName = os.path.join(self.fileName_folder,self.fileName)
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
            

    def folder_analyze(self,values):
        #When pressed on Cyclotron trends
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    
    def onpick(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         points = tuple(zip(xdata[ind], ydata[ind]))
         self.coordinates_x = xdata[ind][0]
         [target_current,current] = getting_subsystems_data.get_target_parameters(self.file_df)
         foil_number = getting_subsystems_data.get_foil_number(self.file_df,current) 
         self.table_summary_log.setItem(0,1, QTableWidgetItem(str(self.file_df.Time.iloc[ind[0]])))
         self.table_summary_log.setItem(1,1, QTableWidgetItem(str(self.file_df.Vacuum_P.astype(float).iloc[ind[0]]*1e5)))
         function_names = [self.file_df.Magnet_I,self.file_df.Arc_I,self.file_df.Dee_1_kV,self.file_df.Dee_2_kV,
         self.file_df.Flap1_pos,self.file_df.Flap2_pos,self.file_df.RF_fwd_W,self.file_df.RF_refl_W,
         self.file_df.Extr_pos,self.file_df.Balance,self.file_df.Foil_No,self.file_df.Foil_I,self.file_df.Target_I,self.file_df.Coll_l_I,self.file_df.Coll_r_I,
         self.df_subsystem_beam.Coll_l_rel,self.df_subsystem_beam.Coll_r_rel,self.df_subsystem_beam.Target_rel]
         for i in range (2,17):
            print (i)
            self.table_summary_log.setItem(i,1, QTableWidgetItem(str(function_names[i-2][ind[0]])))
         for i in range (17,20):
            self.table_summary_log.setItem(17,1, QTableWidgetItem(str(round(function_names[i-2][ind[0]],2))))
         self.current_row_statistics += 1


    def onpick_trends(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         self.coordinates_x = xdata[ind][0]
         COLUMNS_GENERAL = ["CYCLOTRON","DATE","FILE","FOIL"]
         self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str("CYCLOTRON")))
         self.tablestatistic_tab2.setItem(0,1, QTableWidgetItem(str(getattr(self.tfs_input_cyclotron,"CYCLOTRON").iloc[self.coordinates_x])))
         for i in range(1,4,1): 
              self.tablestatistic_tab2.setItem(i,0, QTableWidgetItem(COLUMNS_GENERAL[i]))
              self.tablestatistic_tab2.setItem(i,1,QTableWidgetItem(str(getattr(self.tfs_input,COLUMNS_GENERAL[i]).iloc[self.coordinates_x])))
         index = ((self.tablefiles_tab2.selectionModel().currentIndex()))
         if index.row() in [0,1,2,3]:
            column = columns_names.COLUMN_ION_SOURCE
            column_ave = columns_names.COLUMNS_ION_SOURCE_AVE
            colum_std = columns_names.COLUMNS_ION_SOURCE_STD
         elif index.row() == 4:
            column = columns_names.COLUMN_VACUUM
            column_ave = columns_names.COLUMNS_VACUUM_AVE
            colum_std = columns_names.COLUMNS_VACUUM_STD
         elif index.row() == 5:
            column = columns_names.COLUMN_MAGNET
            column_ave = columns_names.COLUMNS_MAGNET_AVE
            colum_std = columns_names.COLUMNS_MAGNET_STD
         elif index.row() in [6,7,8]:
            column = columns_names.COLUMN_RF
            column_ave = columns_names.COLUMNS_RF_AVE
            colum_std = columns_names.COLUMNS_RF_STD
         elif index.row() == 9:
            column = columns_names.COLUMN_EXTRACTION
            column_ave = columns_names.COLUMNS_EXTRACTION_AVE
            colum_std = columns_names.COLUMNS_EXTRACTION_STD
         elif index.row() in [10,11,12,13]:
            column = columns_names.COLUMN_BEAM
            column_ave = columns_names.COLUMNS_BEAM_AVE
            colum_std = columns_names.COLUMNS_BEAM_STD
         elif index.row() == 14:
            column = columns_names.COLUMN_LOSSES
            column_ave =columns_names.COLUMNS_LOSSES_AVE
            colum_std = columns_names.COLUMNS_LOSSES_STD
         elif index.row() in [15]:
            column = columns_names.COLUMN_TRANSMISSION
            column_ave =columns_names.COLUMNS_TRANSMISSION_AVE
            colum_std = columns_names.COLUMNS_TRANSMISSION_STD
         for i in range(len(column)):
                self.tablestatistic_tab2.setItem(i+4,0, QTableWidgetItem(str(column[i])))
                value = str(round(getattr(self.tfs_input,column_ave[i]).iloc[self.coordinates_x],1)) + "+-" + str(round(getattr(self.tfs_input,colum_std[i]).iloc[self.coordinates_x],1))
                self.tablestatistic_tab2.setItem(i+4,1, QTableWidgetItem(value))
                for i in range(len(column),8,1):
                    self.tablestatistic_tab2.setItem(i+4,0, QTableWidgetItem(""))
                    self.tablestatistic_tab2.setItem(i+4,1, QTableWidgetItem(""))
                
    def handleSelectionChanged_variabletoanalyze(self):
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out",
        "table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out",
        "table_summary_transmission.out"]
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName = os.path.join(self.output_path,summary_file_names[index.row()])

