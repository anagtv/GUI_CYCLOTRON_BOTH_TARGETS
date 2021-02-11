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


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Cyclotron Analysis")
        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowIcon(QIcon('pic.png'))
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
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS","All Files (*);;Python Files (*.py)", options=options)
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
        #self.fileName_folder 
        if (os.path.isfile(source_summary_path) == False): 
            saving_trends.getting_summary(self)
        for i in range(len(components)):
          self.tablefiles_tab2.setItem(self.current_row_analysis,0, QTableWidgetItem(components[i]))
          for j in range(len(file_components_columns[i])):          
              self.tablefiles_tab2.setItem(self.current_row_analysis,1, QTableWidgetItem(str(file_components_columns[i][j])))
              self.current_row_analysis += 1
        self.current_row_analysis = 0      

# Another class for tables and actions to buttons
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
        print ("FILE TO PLOT")
        print (self.fileName)
        self.row_to_plot = index.row()
        managing_files.file_open(self)
        managing_files.file_open_summary(self)

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
            

    def onpick(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         points = tuple(zip(xdata[ind], ydata[ind]))
         self.coordinates_x = xdata[ind][0]
         [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(self.file_df)
         foil_number = saving_files_summary_list_20200420.get_foil_number(self.file_df,current) 
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
         #self.tablestatistic_tab2.setItem(0,1, QTableWidgetItem(self.name))
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
                print ("PRINTING TABLE")
                print (i)
                print (8-len(column))
                self.tablestatistic_tab2.setItem(i+4,0, QTableWidgetItem(str(column[i])))
                value = str(round(getattr(self.tfs_input,column_ave[i]).iloc[self.coordinates_x],1)) + "+-" + str(round(getattr(self.tfs_input,colum_std[i]).iloc[self.coordinates_x],1))
                print (value)
                self.tablestatistic_tab2.setItem(i+4,1, QTableWidgetItem(value))
                for i in range(len(column),8,1):
                    self.tablestatistic_tab2.setItem(i+4,0, QTableWidgetItem(""))
                    self.tablestatistic_tab2.setItem(i+4,1, QTableWidgetItem(""))
                
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
        menus.plot_source_actions(self)
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
        self.openPlotEx.triggered.connect(self.setting_plot_extraction)
        self.openPlotColTarget.triggered.connect(self.setting_target_collimator)


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
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Arc_I.astype(float)
        self.ylabel = "Current [mA]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.y_values = self.file_df.Arc_V.astype(float)
        self.ylabel = r"Voltage [V]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()    

    def setting_plot_vacuum(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Arc_I.astype(float)
        self.ylabel = "Current [mA]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.y_values = self.file_df.Vacuum_P.astype(float)*1e5
        self.ylabel = r"[$10^{-5}$ mbar]"  
        self.legend = "Vacuum P"  
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_RF(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time 
        self.y_values_1 = self.file_df.Dee_1_kV.astype(float)
        self.y_values_2 = self.file_df.Dee_2_kV.astype(float)
        self.legend_1 = "Dee1"
        self.legend_2 = "Dee2"
        self.ylabel = "Voltage [kV]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values_1 = self.file_df.Flap1_pos.astype(float)
        self.y_values_2 = self.file_df.Flap2_pos.astype(float)
        self.legend_1 = "Flap1"
        self.legend_2 = "Flap2"
        self.ylabel = "Position [%]"
        file_plots.get_plots_two_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_RF_power(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values_1 = self.file_df.RF_fwd_W.astype(float)
        self.y_values_2 = self.file_df.RF_refl_W.astype(float)
        self.legend_1 = "Forwared"
        self.legend_2 = "Reflected"
        self.label_left = "Power [kW]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values = self.file_df.Phase_load.astype(float)
        self.legend = "Phase load"
        self.label = "Phase load"   
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_extraction(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values_1 = self.file_df.Extr_pos.astype(float)
        self.y_values_2 = self.file_df.Balance.astype(float)
        self.legend_1 = "Extr_pos"
        self.legend_2 = "Balance"
        self.ylabel = "Position [%]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values_1 = self.file_df.Coll_l_I.astype(float)
        self.y_values_2 = self.file_df.Coll_r_I.astype(float)
        self.legend_1 = "Coll l "
        self.legend_2 = "Coll r"
        self.ylabel = "Current [$\mu$A]"
        file_plots.get_plots_two_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()


    def setting_target_collimator(self):
        file_plots.setting_plot(self)
        self.x_values = self.df_subsystem_beam.Time
        self.y_values_1 = self.df_subsystem_beam.Target_rel.astype(float)
        self.y_values_2 = self.df_subsystem_beam.Coll_r_rel.astype(float) + self.df_subsystem_beam.Coll_l_rel.astype(float)
        self.legend_1 = "Target I/Foil I"
        self.legend_2 = "Collimators I/Foil I"
        self.ylabel = "Current [%]"
        file_plots.get_plots_two_functions_all(self,1)
        y_values_right = [self.file_df.Foil_I.astype(float),self.file_df.Target_I.astype(float),self.file_df.Coll_l_I.astype(float) + self.file_df.Coll_l_I.astype(float)]
        y_values_legend = ["Foil","Target","Collimators"]  
        self.ylabel = "Current [uA]" 
        self.x_values = self.file_df.Time
        for i in range(len(y_values_right)):
            self.y_values = y_values_right[i]
            self.y_legend = y_values_legend[i]
            self.get_plots_three_functions_area(0)


    def get_plots_three_functions_area(self,pn):
        self.sc1.axes[pn].fill_between(self.x_values,0,self.y_values,label= self.y_legend)
        self.sc1.axes[pn].legend(loc='best',ncol=1,fontsize=10)
        self.sc1.axes[pn].set_xlabel("Time [s]",fontsize=10)
        self.sc1.axes[pn].set_ylabel(str(self.ylabel),fontsize=10)
        ticks_to_use = self.x_values[::int(len(self.x_values)/6)]   
        ticks_to_use_list = self.x_values[::int(len(self.x_values)/6)] 
        self.sc1.axes[pn].set_xticks(ticks_to_use_list)
        self.sc1.axes[pn].set_xticklabels(ticks_to_use)
        #self.sc1.axes[pn].set_yticks(np.arange(min_value,max_value*1.1, step=5))
        self.sc1.axes[pn].tick_params(labelsize=10)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.axes[pn].tick_params(labelsize=10)
        self.sc1.draw()
        self.sc1.show()


    def setting_plot_magnet(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Magnet_I.astype(float)
        self.ylabel = "Current [A]"
        self.legend = "Magnet Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.df_iso = saving_files_summary_list_20200420.get_isochronism(self.file_df)
        self.x_values = self.df_subsystem_beam.Time
        self.y_values_coll = (self.df_iso.Coll_l_I).astype(float) + (self.df_iso.Coll_r_I).astype(float)
        self.y_values_target = self.df_iso.Target_I
        self.y_values_foil = self.df_iso.Foil_I
        self.y_values_magnet = self.df_iso.Magnet_I
        self.label_left = r"Magnet current [A]"
        self.label_right = "Isochronism"
        file_plots.get_plots_tunning(self,self.y_values_coll,self.y_values_target,self.y_values_foil,self.y_values_magnet,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()
        #file_plots.file_plot_iso_one_functions(self)
 

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
        target_information_1.selecting_data_to_plot_reset(self.data_1,self.target_1,self.tfs_input)
        target_information_2.selecting_data_to_plot_reset(self.data_2,self.target_2,self.tfs_input)
        target_information_1_extra.selecting_data_to_plot_reset(self.data_1,self.target_1,self.tfs_input)
        target_information_2_extra.selecting_data_to_plot_reset(self.data_2,self.target_2,self.tfs_input)
        targets_summary = [[target_information_1,target_information_2]]
        targets_summary_extra = [[target_information_1,target_information_2],[target_information_1_extra,target_information_2_extra]]
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
            lower_limit = 0.95
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
        self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)    
           
        
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
    
    def selecting_data_to_plot_reset(self,data,target,total):
        self.foil_position = total[total.TARGET == str(target)].drop_duplicates(subset="FOIL",keep = "first").index
        self.foil_values = total[total.TARGET == str(target)].drop_duplicates(subset="FOIL",keep = "first").FOIL
        self.tfs_target = (data)
        self.tfs_target.reset_index(drop=True, inplace=True)
        self.tfs_target_no_reset = (data)
        self.tfs_unique_target = (self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))
        self.tfs_unique_target_array = np.array(self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))
        
 


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        #Gui_tables = menus_functions()
        Gui_tabs = plotting_data()      
        sys.exit(app.exec_())

run()
