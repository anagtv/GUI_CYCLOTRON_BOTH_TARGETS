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
#import editing_table_class
from editing_table_class import window
from editing_table_class import editing_table
from menus_function_class import menus_functions
from target_information_class import target_information
#stheclass = TheClass()
#import plotting_data_class
#matplotlib.use('Qt5Agg')

class plotting_data(editing_table,menus_functions):
    def __init__(self):
        super(plotting_data, self).__init__()
        menus.plot_source_actions(self)
        self.edit_actions()
        self.plot_actions()
 
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
        #self.editplotweek.triggered.connect(self.flag_week)
        #self.editplotday.triggered.connect(self.flag_day)
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
            file_plots.get_plots_three_functions_area(self,0)


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

        
    def flag_no_day_gap(self):
        self.flag_no_gap = "1"

    def flag_day_gap(self):
        self.flag_no_gap = "0"

    # FUNCTIONS USING A CONNECT 

    def handleSelectionChanged_variabletoplot(self):
        #
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.tfs_input = tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[index.row()]))
        self.target_2 = int(np.max(self.tfs_input.drop_duplicates(subset="TARGET",keep = "first").TARGET))
        self.target_1 = int(np.min(self.tfs_input.drop_duplicates(subset="TARGET",keep = "first").TARGET))
        self.targets = [self.target_1,self.target_2]
        target_information_1 = target_information() 
        target_information_2 = target_information()
        target_information_1_extra = target_information() 
        target_information_2_extra = target_information()
        self.target_information_summary = [target_information_1,target_information_2]
        self.target_information_summary_extra = [target_information_1_extra,target_information_2_extra]
        self.sc3.axes.clear() 
        # Defining the classes for the two targets 
        for i in range(len(self.targets)):
            self.target_information_summary[i].selecting_data_to_plot_reset(self.targets[i],self.tfs_input)
            self.target_information_summary_extra[i].selecting_data_to_plot_reset(self.targets[i],self.tfs_input)       
        self.targets_summary = [self.target_information_summary]
        self.targets_summary_extra = [self.target_information_summary,self.target_information_summary_extra]
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
            summary = [columns_names.LABELS[index.row()],columns_names.LEGEND[index.row()],columns_names.FILE_NAME[index.row()],"1"]
            limits = [columns_names.YLABEL[index.row()],uppper_limit,lower_limit]  
            if index.row() == 3:
                self.flag_max() 
                summary = [columns_names.LABELS[index.row()],columns_names.LEGEND[index.row()],columns_names.FILE_NAME[index.row()],"0"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)   
            else:                    
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)
        elif index.row() in [13,14,15]: 
            self.flag_max()
            summary = [columns_names.LABELS[index.row()-7],columns_names.LEGEND[index.row()-7],columns_names.FILE_NAME[index.row()-7],"0"]
            limits = [columns_names.YLABEL[index.row()-7],uppper_limit,lower_limit]     
            if index.row() == 15:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)
            else:
                summary = [columns_names.LABELS[index.row()-7],columns_names.LEGEND[index.row()-7],columns_names.FILE_NAME[index.row()-7],"1"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)           
        else: 
            self.flag_max()           
            summary = [columns_names.LABELS_1[index.row()-6],columns_names.LABELS_2[index.row()-6],columns_names.LEGEND_1[index.row()-6],columns_names.LEGEND_2[index.row()-6],columns_names.FILE_NAME_D[index.row()-6],"0"]
            limits = [columns_names.YLABEL_D[index.row()-6],uppper_limit,lower_limit]
            if index.row() in [10,11,12]:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,summary,limits)
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,summary,limits)
        self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)    
           


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        #Gui_tables = menus_functions()
        Gui_tabs = plotting_data()      
        sys.exit(app.exec_())

run()
