 # TAB PARAMETERES
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
from PyQt5 import QtCore, QtWidgets
import file_plots
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import selecting_trends
def home(self):
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
        widget.setLayout(self.lay)
        self.setCentralWidget(widget)
        # TAB 1
        tab1_layout(self)
        tab1_selection(self)
        tab1_data(self)
        # TAB 2
        tab2_layout(self)
        tab2_selection(self)
        tab2_data(self)
        # TAB 3
        tab3_layout(self)
        tab3_data(self)
        # Add tabs to widget
        self.lay.addWidget(self.tabs)
        # Add tabs to widget
        self.lay.addWidget(self.tabs)
        #self.setLayout(self.layout)

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
        print ("HEREEEEEE 2")
        selection.selectionChanged.connect(self.handleSelectionFile)
        self.show()
        self.selection_folder = self.tableWidget_logfiles.selectionModel()
        self.selection_folder.selectionChanged.connect(self.handleSelectionFolder)
        print ("ENDINND")
        #self.show()
    
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
        self.selection_component.selectionChanged.connect(self.handleSelectionChanged_variabletoplot)
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
