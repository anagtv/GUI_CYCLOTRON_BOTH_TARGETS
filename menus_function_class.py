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
import columns_names
import menus
import home_tabs
from editing_table_class import window,editing_table
#from editing_table_class import edting_table
#import my_fav_gui_20200522_1_4 

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
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS","All Files (*);;Python Files (*.py)", options=options)
        managing_files.file_open(self)
        managing_files.file_open_summary(self)
        self.first_row = [self.file_number,self.name,self.date_stamp,self.target_number]
        editing_table.writing_values(self)

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
        #self.fileName_folder 
        if (os.path.isfile(source_summary_path) == False): 
            saving_trends.getting_summary(self)
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0      

