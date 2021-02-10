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

class Selection_system:
   def __init__(self):
        self.verification = -1
        self.verification_position = 0
        self.counter = []
        self.horizontal_value_plot = []
        self.horizontal_mark_plot = []
        self.counter = []
        self.indexi = 0
        self.valuei = 0
        self.counteri = -1
   def check_line(self,line,value,index,line_position):
    #cheking if they are stil 
    if int(line) == int(self.verification + 1) and int(index) == int(self.indexi):
         self.counteri += 1 
    else:
         self.horizontal_mark_plot.append(self.verification_position)
         self.horizontal_value_plot.append(self.valuei)
         self.counter.append(self.counteri)
         self.counteri = 0
         self.verification_position = line_position 
    self.valuei = value
    self.verification = line
    self.indexi = index
    return self.verification 


def setting_plot_for_individual_target(self,target_number):
    self.maximum_value = (np.max(target_number.max_value + target_number.std_value))
    self.minimum_value = (np.min(target_number.min_value - target_number.std_value))

def setting_plot_for_both_targets(self,targets_summary):
    maximum_value = []
    minimum_value = []
    for i in range(len(targets_summary)):
        maximum_value.append(np.max(targets_summary[i].max_value + targets_summary[i].std_value))
        minimum_value.append(np.min(targets_summary[i].min_value - targets_summary[i].std_value))
    self.maximum_value = np.max([maximum_value])
    self.minimum_value = np.min([minimum_value])


def setting_minimum_and_maximimum_two_functions(self,targets_summary):
    if self.target_2_value == "1":
       setting_plot_for_both_targets(self,targets_summary[0:2])
    elif self.target_1_value == "1":
       setting_plot_for_both_targets(self,targets_summary[2:4])
    else:
        setting_plot_for_both_targets(self,targets_summary)

def setting_minimum_and_maximimum(self,targets_summary):
    if self.target_2_value == "1":
       setting_plot_for_individual_target(self,targets_summary[0])
    elif self.target_1_value == "1":
       setting_plot_for_individual_target(self,targets_summary[1])
    else:
        setting_plot_for_both_targets(self,targets_summary) 

def setting_configuration(self,upper_value,lower_value):
    locs, labels = plt.yticks()
    distance_plot = (self.maximum_value*upper_value-self.minimum_value*lower_value)/(6*len(locs))
    self.set_configuration = distance_plot+self.maximum_value*upper_value
    self.set_configuration_min = distance_plot+self.minimum_value

def plot_configuration(self,ylabel_name,upper_value,lower_value):
    fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE',fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name,fontsize=14)
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name)
    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14) 
    fig.tight_layout() 
    setting_configuration(self,upper_value,lower_value)
    self.sc3.axes.set_ylim([self.minimum_value*lower_value,self.maximum_value*upper_value]) 


def setting_minimum_maximum_x(self,targets_summary):
    self.min_x = np.min([np.min(list(targets_summary[0].x_values)),np.min(list(targets_summary[1].x_values))])
    self.max_x = np.max([np.max(list(targets_summary[0].x_values)),np.max(list(targets_summary[1].x_values))])
    
def getting_stadistic_values(target_number,label):
    column_name_ave = label + "AVE"
    column_name_max = label + "MAX"
    column_name_std = label + "STD"
    column_name_min = label + "MIN"
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

def generic_plot_no_gap_one_quantitie_with_foil(self,targets_summary,labels,limits):  
    if self.target_1_value == "1":
        indexes = [0]
    elif self.target_2_value == "1":
        indexes = [1]  
    else:
        indexes = [0,1]
    generic_plot_no_gap_one_quantitie(self,targets_summary,labels,limits)
    sel_system = Selection_system()
    for j in indexes:
        selecting_foils(sel_system,targets_summary[0][j])
    for i in range(len(sel_system.horizontal_mark_plot)): 
            print ("FOILSSSSSSS")
            print (sel_system.horizontal_mark_plot)  
            print (self.set_configuration_min)
            self.sc3.axes.text(sel_system.horizontal_mark_plot,self.set_configuration_min,"F " + str(sel_system.horizontal_value_plot), fontsize=10,rotation=90)

def plotting_trends(self,targets_summary,labels):
    self.final_legend = []
    self.fmts = ["o","^","v"]
    for i in range(len(targets_summary)):
        getting_stadistic_values(targets_summary[i],self.column[i])
        targets_summary[i].x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == self.targets[i]].index)
        self.final_legend.append("AVE " + labels[1] + self.targets[i])
    self.final_legend.append(labels[2])
    self.final_legend.append(labels[3])
         
def removing_adding_target_1_4_max_min(self,targets_summary,legend,colors_plot):
    for j in (self.rango):
        plotting_average_std(self,targets_summary[j],legend[j],colors_plot[0][j])
        if self.max_min_value == "0": 
            plotting_max_min(self,targets_summary[j],"1",colors_plot[1][j])  

def plotting_max_min(self,target_information,flag_min,colors):
    self.sc3.axes.errorbar(target_information.x_values,target_information.max_value,fmt=self.fmts[1], color=colors, picker=5)
    if flag_min == "1":
        self.sc3.axes.errorbar(target_information.x_values,target_information.min_value,fmt=self.fmts[2], color=colors, picker=5)

def plotting_average_std(self,target_information,legend_i,colors):
    self.sc3.axes.errorbar(target_information.x_values,target_information.ave_value,yerr=target_information.std_value,fmt=self.fmts[0], color=colors,label= legend_i, picker=5)  
    self.sc3.axes.set_xlim([self.min_x-2,self.max_x+2]) 


def generic_plot_no_gap_one_quantitie(self,targets_summary,labels,limits):
    columns = [[labels[0],labels[0]]]
    self.targets = [str(self.target_1),str(self.target_2)]
    self.fmts = ["o","^","v"]
    colors = [COLORS[4],COLORS[8]]
    colors_min = [COLORS[9],COLORS[10]]
    colors_plot = [[colors,colors_min]]
    legend1_1 = "AVE " + labels[1] + str(self.target_1)
    legend1_2 = "AVE " + labels[1] + str(self.target_2)
    total_legend = [[legend1_1,legend1_2]]
    total_targets = [targets_summary[0][0],targets_summary[0][1]]
    plotting(self,targets_summary,labels,total_legend,colors_plot,columns,total_targets,limits,"1")


def generic_plot_no_gap_two_quantities(self,targets_summary,labels,limits):
    self.targets = [str(self.target_1),str(self.target_2),str(self.target_1),str(self.target_2)]
    columns = [[labels[0],labels[0]],[labels[1],labels[1]]]
    self.flag_max()
    colors = [COLORS[4],COLORS[4]]
    colors_2 = [COLORS[8],COLORS[8]]
    colors_min = [COLORS[4],COLORS[9]]
    colors_plot = [[colors,colors_min],[colors_2,colors_min]]
    legend1_1 = "AVE " + labels[2]
    legend2_1 = '_nolegend_'
    legend1_2 = "AVE " + labels[3]
    legend2_2 ='_nolegend_'  
    total_legend = [[legend1_1,legend2_1],[legend1_2,legend2_2]]
    total_targets = [targets_summary[0][0],targets_summary[0][1],targets_summary[1][0],targets_summary[1][1]]
    plotting(self,targets_summary,labels,total_legend,colors_plot,columns,total_targets,limits,"0")
    
def plotting(self,targets_summary,labels,total_legend,colors_plot,columns,total_targets,limits,value):
    self.fmts = ["o","^","v"]
    if self.target_2_value == "1":
        self.rango = [0]
        self.file_name_current = labels[2][:-4] + "_" + str(self.target_1)
    elif self.target_1_value == "1":
        self.rango = [1] 
        self.file_name_current = labels[2][:-4] + "_" + str(self.target_2)
    else:
        self.rango = [0,1]
        self.file_name_current = labels[2][:-4] 
    for i in range(len(targets_summary)):
        self.column = columns[i]
        plotting_trends(self,targets_summary[i],labels)
        setting_minimum_maximum_x(self,targets_summary[i]) 
        removing_adding_target_1_4_max_min(self,targets_summary[i],total_legend[i],colors_plot[i]) 
    if value == "0":
        setting_minimum_and_maximimum_two_functions(self,total_targets)
    else: 
        setting_minimum_and_maximimum(self,total_targets)
    plot_configuration(self,limits[0],limits[1],limits[2])      
    menus.removing_days_adding_weeks(self)
    menus.removing_adding_gap(self)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14)
    self.sc3.fig.savefig((os.path.join(self.output_path,self.file_name_current)))
   
def selecting_foils(sel_system,target_information):
    for i in range(len(target_information.index_foil_sorted)):
        checking_value = (target_information.index_foil_sorted[i] == list(range(min(target_information.index_foil_sorted[i]), max(target_information.index_foil_sorted[i])+1)))
        if len(target_information.index_foil_sorted) == 1:
           checking_value =  checking_value[0]
        if checking_value == True:
            print (target_information.index_foil_sorted_position)
            sel_system.horizontal_mark_plot.append(target_information.index_foil_sorted_position[i][0])
            sel_system.horizontal_value_plot.append(target_information.unique_index_foil[i])
        else: 
           for j in range(len(target_information.index_foil_sorted[i])):
                sel_system.check_line(target_information.index_foil_sorted[i][j],target_information.unique_index_foil[i],i,target_information.index_foil_sorted_position[i][j])
           sel_system.horizontal_mark_plot.append(sel_system.verification_position)
           sel_system.horizontal_value_plot.append(sel_system.valuei)
           sel_system.counter.append(sel_system.counteri)


