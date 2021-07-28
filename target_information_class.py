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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
import matplotlib.pyplot as plt
import numpy as np
import os
import tfs
from matplotlib.widgets import CheckButtons
import flag_selection
import file_plots
from datetime import time
import saving_trends
import managing_files
import columns_names
import menus
import home_tabs
from editing_table_class import window,editing_table

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
    
    def selecting_data_to_plot_reset(self,target,total):    
        self.foil_values = total[total.TARGET == str(target)].drop_duplicates(subset="FOIL",keep = "first").FOIL
        self.tfs_target = total[total.TARGET == str(target)]
