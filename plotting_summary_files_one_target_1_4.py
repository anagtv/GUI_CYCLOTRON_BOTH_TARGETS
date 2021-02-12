import pandas as pd
import numpy as np
import os
import sys
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
plt.rcParams["figure.figsize"] = (15,10)
import tfs
import datetime
from datetime import timedelta
import menus

COLORS = ['#1E90FF','#FF4500','#32CD32',"#6A5ACD","#20B2AA","#00008B","#A52A2A","#228B22","#FF3300","#3366FF","#FF9933"]


def setting_plot_for_individual_target(self,target_number):
    self.maximum_value = (np.max(target_number.max_value + target_number.std_value))
    self.minimum_value = (np.min(target_number.min_value - target_number.std_value))
    print ("MAXIMUM AND MINIMUM VALUES")
    print (self.maximum_value,self.minimum_value)

def setting_plot_for_both_targets(self,targets_summary):
    maximum_value = []
    minimum_value = []
    for i in range(len(self.total_targets)):
        maximum_value.append(np.max(self.total_targets[i].max_value + self.total_targets[i].std_value))
        minimum_value.append(np.min(self.total_targets[i].min_value - self.total_targets[i].std_value))
    self.maximum_value = np.max([maximum_value])
    self.minimum_value = np.min([minimum_value])


def setting_minimum_and_maximimum_two_functions(self):
    if self.target_2_value == "1":
       targets_summary = [self.total_targets[0],self.total_targets[2]]
       setting_plot_for_both_targets(self,targets_summary)
    elif self.target_1_value == "1":
       targets_summary = [self.total_targets[1],self.total_targets[3]]
       setting_plot_for_both_targets(self,targets_summary)
    else:
        setting_plot_for_both_targets(self,self.total_targets)

def setting_minimum_and_maximimum(self):
    if self.target_2_value == "1":
       setting_plot_for_individual_target(self,self.total_targets[0])
    elif self.target_1_value == "1":
       setting_plot_for_individual_target(self,self.total_targets[1])
    else:
        setting_plot_for_both_targets(self,self.total_targets) 

def setting_configuration(self):
    locs, labels = plt.yticks()
    distance_plot = (self.maximum_value*self.limits[0]-self.minimum_value*self.limits[1])/(6*len(locs))
    self.set_configuration = distance_plot+self.maximum_value*self.limits[0]
    self.set_configuration_min = distance_plot+self.minimum_value*self.limits[1]

def plot_configuration(self):
    fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE',fontsize=14)
    self.sc3.axes.set_ylabel(self.ylabel,fontsize=14)
    self.sc3.axes.set_xlabel('FILE')
    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14) 
    fig.tight_layout() 
    setting_configuration(self)
    self.sc3.axes.set_ylim([self.minimum_value*self.limits[1],self.maximum_value*self.limits[0]]) 


def setting_minimum_maximum_x(self):
    self.min_x = np.min([np.min(list(self.targets_summary_selected[0].x_values)),np.min(list(self.targets_summary_selected[1].x_values))])
    self.max_x = np.max([np.max(list(self.targets_summary_selected[0].x_values)),np.max(list(self.targets_summary_selected[1].x_values))])
    
def getting_stadistic_values(target_number,label):
    column_name_ave = label + "AVE"
    column_name_max = label + "MAX"
    column_name_std = label + "STD"
    column_name_min = label + "MIN"
    print (target_number)
    ave_value = (getattr(target_number.tfs_target,column_name_ave))
    std_value = (getattr(target_number.tfs_target,column_name_std))
    try:
       max_value = (getattr(target_number.tfs_target,column_name_max))
       min_value = (getattr(target_number.tfs_target,column_name_min))
    except:
        max_value = ave_value*1.3
        min_value = ave_value*0.7
    target_number.ave_value = ave_value
    target_number.std_value = std_value
    target_number.max_value = max_value
    target_number.min_value = min_value

def selecting_first_foils(self):
    if self.foils_flag == "1":
        for j in self.indexes:
                for i in range(len(self.targets_summary[0][j].foil_values)): 
                    self.sc3.axes.text(np.array(self.targets_summary[0][j].foil_values.index[i]),self.set_configuration_min,"F " + (str(self.targets_summary[0][j].foil_values.iloc[i])), fontsize=10,rotation=90)   
        self.sc3.draw()
        self.sc3.show()

def generic_plot_no_gap_one_quantitie_with_foil(self):  
    if self.target_1_value == "1":
        self.indexes = [1]
        self.foils_flag = "1"
    elif self.target_2_value == "1":
        self.indexes = [0] 
        self.foils_flag = "1"
    else:
        self.indexes = [0,1]
        self.foils_flag = "0"
    generic_plot_no_gap_one_quantitie(self)
    selecting_first_foils(self)

    
def plotting_trends(self):
    self.final_legend = []
    self.fmts = ["o","^","v"]
    for i in range(len(self.targets_summary_selected)):
        getting_stadistic_values(self.targets_summary_selected[i],self.column[i])
        self.targets_summary_selected[i].x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == self.targets[i]].index)

         
def removing_adding_target_1_4_max_min(self):
    for j in (self.rango):
        plotting_average_std(self,self.targets_summary_selected[j],self.total_legend_selected[j],self.colors_plot_selected[0][j])
        if self.max_min_value == "0": 
            plotting_max_min(self,self.targets_summary_selected[j],"1",self.colors_plot_selected[1][j])  

def plotting_max_min(self,target_information,flag_min,colors):
    self.sc3.axes.errorbar(target_information.x_values,target_information.max_value,fmt=self.fmts[1], color=colors, picker=5)
    if flag_min == "1":
        self.sc3.axes.errorbar(target_information.x_values,target_information.min_value,fmt=self.fmts[2], color=colors, picker=5)

def plotting_average_std(self,target_information,legend_i,colors):
    self.sc3.axes.errorbar(target_information.x_values,target_information.ave_value,yerr=target_information.std_value,fmt=self.fmts[0], color=colors,label= legend_i, picker=5)  
    self.sc3.axes.set_xlim([self.min_x-2,self.max_x+2]) 


def generic_plot_no_gap_one_quantitie(self):
    self.columns = [[self.labels[0],self.labels[0]]]
    self.targets = [str(self.targets[0]),str(self.targets[1])]
    self.fmts = ["o","^","v"]
    colors = [COLORS[4],COLORS[8]]
    colors_min = [COLORS[9],COLORS[10]]
    self.colors_plot = [[colors,colors_min]]
    legend1_1 = "AVE " + self.legend[0] + str(self.targets[0])
    legend1_2 = "AVE " + self.legend[0] + str(self.targets[1])
    self.total_legend = [[legend1_1,legend1_2]]
    self.total_targets = [self.targets_summary[0][0],self.targets_summary[0][1]]
    self.targets_summary = self.targets_summary
    plotting(self,"1")


def generic_plot_no_gap_two_quantities(self):
    self.columns = [[self.labels[0],self.labels[0]],[self.labels[1],self.labels[1]]]
    self.targets = [str(self.targets[0]),str(self.targets[1]),str(self.targets[0]),str(self.targets[1])]
    self.flag_max()
    colors = [COLORS[4],COLORS[4]]
    colors_2 = [COLORS[8],COLORS[8]]
    colors_min = [COLORS[4],COLORS[9]]
    self.colors_plot = [[colors,colors_min],[colors_2,colors_min]]
    legend1_1 = "AVE " + self.legend[0]
    legend2_1 = '_nolegend_'
    legend1_2 = "AVE " + self.legend[1]
    legend2_2 ='_nolegend_'  
    self.total_legend = [[legend1_1,legend2_1],[legend1_2,legend2_2]]
    self.targets_summary = self.targets_summary_extra
    self.total_targets = [self.targets_summary_extra[0][0],self.targets_summary_extra[0][1],self.targets_summary_extra[1][0],self.targets_summary_extra[1][1]]
    plotting(self,"0")
    
def plotting(self,value):
    self.fmts = ["o","^","v"]
    if self.target_2_value == "1":
        self.rango = [0]
        self.file_name_current = self.file_name[:-4] + "_" + str(self.targets[0])
    elif self.target_1_value == "1":
        self.rango = [1] 
        self.file_name_current = self.file_name[:-4] + "_" + str(self.targets[1])
    else:
        self.rango = [0,1]
        self.file_name_current = self.file_name[:-4] 
    for i in range(len(self.targets_summary)):
        self.column = self.columns[i]
        self.targets_summary_selected = self.targets_summary[i]
        self.colors_plot_selected = self.colors_plot[i]
        self.total_legend_selected = self.total_legend[i]
        plotting_trends(self)
        setting_minimum_maximum_x(self) 
        removing_adding_target_1_4_max_min(self) 
    if value == "0":
        setting_minimum_and_maximimum_two_functions(self)
    else: 
        setting_minimum_and_maximimum(self)
    plot_configuration(self)      
    menus.removing_days_adding_weeks(self)
    menus.removing_adding_gap(self)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14)
    self.sc3.fig.savefig((os.path.join(self.output_path,self.file_name_current)))
   



