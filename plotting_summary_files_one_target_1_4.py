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

def getting_stadistic_values(target_number,label):
    column_name_ave = label + "AVE"
    column_name_max = label + "MAX"
    column_name_std = label + "STD"
    column_name_min = label + "MIN"
    print (target_number.tfs_target)
    ave_value = (getattr(target_number.tfs_target,column_name_ave))
    std_value = (getattr(target_number.tfs_target,column_name_std))
    try:
       max_value = (getattr(target_number.tfs_target,column_name_max))
       min_value = (getattr(target_number.tfs_target,column_name_min))
    except:
        max_value = ave_value*1.3
        min_value = ave_value*0.7
    return (ave_value,std_value,max_value,min_value)

def assigning_statistics(target_number,ave_value,std_value,max_value,min_value):
    target_number.ave_value = ave_value
    target_number.std_value = std_value
    target_number.max_value = max_value
    target_number.min_value = min_value

def setting_plot_for_individual_target(self,target_number):
    self.maximum_value = (np.max(target_number.max_value + target_number.std_value))
    self.minimum_value = (np.min(target_number.min_value - target_number.std_value))
    self.plot_size = self.maximum_value - self.minimum_value

def setting_plot_for_both_targets(self,target_number_1,target_number_2):
    self.maximum_value = (np.max([np.max(target_number_1.max_value + target_number_1.std_value),np.max(target_number_2.max_value + target_number_2.std_value)]))
    self.minimum_value = (np.min([np.max(target_number_1.min_value - target_number_1.std_value),np.min(target_number_2.min_value - target_number_2.std_value)]))
    self.plot_size = self.maximum_value - self.minimum_value
 
def setting_plot_for_both_targets_two_functions(self,target_number_1,target_number_2,target_number_1_extra,target_number_2_extra):
    self.maximum_value_1 = (np.max([np.max(target_number_1.max_value + target_number_1.std_value),np.max(target_number_1_extra.max_value + target_number_1_extra.std_value)]))
    self.minimum_value_1 = (np.min([np.min(target_number_1.min_value - target_number_1.std_value),np.min(target_number_1_extra.min_value - target_number_1_extra.std_value)]))
    self.maximum_value_2 = (np.max([np.max(target_number_2.max_value + target_number_2.std_value),np.max(target_number_2_extra.max_value + target_number_2_extra.std_value)]))
    self.minimum_value_2 = (np.min([np.max(target_number_2.min_value - target_number_2.std_value),np.min(target_number_2_extra.min_value - target_number_2_extra.std_value)]))
    self.maximum_value = np.max([self.maximum_value_1,self.maximum_value_2])
    self.minimum_value = np.min([self.minimum_value_1,self.minimum_value_2])
    self.plot_size = self.maximum_value - self.minimum_value

def setting_minimum_and_maximimum_two_functions(self,target_number_1,target_number_2,target_number_1_extra,target_number_2_extra):
    if self.target_2_value == "1":
       setting_plot_for_both_targets(self,target_number_1,target_number_1_extra)
    elif self.target_1_value == "1":
       setting_plot_for_both_targets(self,target_number_2,target_number_2_extra)
    else:
        setting_plot_for_both_targets_two_functions(self,target_number_1,target_number_2,target_number_1,target_number_2_extra)

def setting_minimum_and_maximimum(self,target_number_1,target_number_2):
    if self.target_2_value == "1":
       setting_plot_for_individual_target(self,target_number_1)
    elif self.target_1_value == "1":
       setting_plot_for_individual_target(self,target_number_2)
    else:
        setting_plot_for_both_targets(self,target_number_1,target_number_2) 

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
    self.fmts = ["o","^","v"]
    fig.tight_layout() 
    locs, labels = plt.yticks()
    self.set_configuration = ((self.maximum_value*upper_value-self.minimum_value*lower_value)/(6*len(locs))+self.maximum_value*upper_value)
    self.set_configuration_min = ((self.maximum_value*upper_value-self.minimum_value*lower_value)/(6*len(locs))+self.minimum_value*lower_value)
    self.sc3.axes.set_ylim([self.minimum_value*lower_value,self.maximum_value*upper_value]) 


def removing_adding_target_1_4_max_min(self,target_information_1,target_information_2,file_name,legend_t1,legend_t2,flag_min,colors,colos_min_mix):
    if self.target_2_value == "1":
        plotting_average_std(self,target_information_1,legend_t1,colors[0],self.target_1)
        if self.max_min_value == "0": 
            plotting_max_min(self,target_information_1,flag_min,colos_min_mix[0],self.target_1)
        self.file_name_current = file_name[:-4] + "_" + str(self.target_1)           
    elif self.target_1_value == "1":
        plotting_average_std(self,target_information_1,legend_t2,colors[1],self.target_2)
        if self.max_min_value == "0": 
            plotting_max_min(self,target_information_1,flag_min,colos_min_mix[1],self.target_2)
        self.file_name_current = file_name[:-4] + "_" + str(self.target_2)
    else:
        self.file_name_current = file_name
        plotting_average_std(self,target_information_1,legend_t1,colors[0],self.target_1)
        plotting_average_std(self,target_information_2,legend_t2,colors[1],self.target_2)
        if self.max_min_value == "0": 
            plotting_max_min(self,target_information_1,flag_min,colos_min_mix[0],self.target_1)
            plotting_max_min(self,target_information_2,flag_min,colos_min_mix[1],self.target_2)

def plotting_average_std(self,target_information,legend,colors,target_number):
    self.sc3.axes.errorbar(target_information.x_values,target_information.ave_value,yerr=target_information.std_value,fmt=self.fmts[0], color=colors,label= legend, picker=5)  
    self.sc3.axes.set_xlim([self.min_x-2,self.max_x+2]) 

def plotting_max_min(self,target_information,flag_min,colors,target_number):
    #maxmimum values 
    self.sc3.axes.errorbar(target_information.x_values,target_information.max_value,fmt=self.fmts[1], color=colors,label= "MAX T" + str(target_number), picker=5)
    if flag_min == "1":
        self.sc3.axes.errorbar(target_information.x_values,target_information.min_value,fmt=self.fmts[2], color=colors,label= "MIN T " + str(target_number), picker=5)

def removing_days_adding_weeks(self):
    index_week_list = []  
    week_number = []
    x_values = []
    # WEEK_DAYS 
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if self.week_value == "1":
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                self.sc3.axes.text(index_week_list[i]-0.3,  self.set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else:
        for i in range(0,len(self.tfs_input.DATE),10):
            x = i
            x_values.append(i)
            self.sc3.axes.text(x-0.3, self.set_configuration,self.tfs_input.DATE.iloc[i][5:], fontsize=12,rotation=90)
        for i in range(0,len(self.tfs_input),1):
           date_to_week = datetime.datetime.strptime(self.tfs_input.DATE.iloc[i],"%Y-%m-%d")
           week_number.append(date_to_week.isocalendar()[1])
    #

def removing_adding_gap(self):
    time_list = (list(range(len(self.tfs_input.FILE))))
    if self.flag_no_gap == "1":
        try:
           ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/10)]   
           ticks_to_use_list = time_list[::int(len(self.tfs_input.FILE)/10)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
        except:
           ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/2)]   
           ticks_to_use_list = time_list[::int(len(self.tfs_input.FILE)/2)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
    else: 
        ticks_to_use = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/15)]   
        ticks_to_use_list = self.tfs_input.FILE[::int(len(self.tfs_input.FILE)/15)] 
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)

def getting_foil_change_position(sel_system,index_foil,index_foil_sorted,unique_index_foil):
    for i in range(len(index_foil)):
        checking_value = (index_foil[i] == list(range(min(index_foil[i]), max(index_foil[i])+1)))
        if len(index_foil) == 1:
           checking_value =  checking_value[0]
        if checking_value == True:
            sel_system.horizontal_mark_plot.append(index_foil_sorted_position[i][0])
            sel_system.horizontal_value_plot.append(unique_index_foil_1[i])
        else: 
           for j in range(len(index_foil_1[i])):
                sel_system.check_line(index_foil_1[i][j],unique_index_foil_1[i],i,index_foil_sorted_1_position[i][j])
           sel_system.horizontal_mark_plot.append(sel_system_1.verification_position)
           sel_system.horizontal_value_plot.append(sel_system_1.valuei)
           sel_system.counter.append(sel_system_1.counteri)

def generic_plot_no_gap_one_quantitie(self,target_number_1,target_number_2,label,ylabel_name,file_name,legend,flag_min,uppper_limit,lower_limit):
    #date_format = "%d-%m-%Y"
    (ave_value_t1,std_value_t1,max_value_t1,min_value_t1) = getting_stadistic_values(target_number_1,label)
    (ave_value_t2,std_value_t2,max_value_t2,min_value_t2) = getting_stadistic_values(target_number_2,label)
    assigning_statistics(target_number_1,ave_value_t1,std_value_t1,max_value_t1,min_value_t1)
    assigning_statistics(target_number_2,ave_value_t2,std_value_t2,max_value_t2,min_value_t2)
    self.selected_color = [COLORS[4],COLORS[8]]
    colors = [COLORS[4],COLORS[8]]
    colors_min = [COLORS[9],COLORS[10]]
    target_number_1.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_1)].index)
    target_number_2.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_2)].index) 
    if flag_min == "1":
        self.flag_max_reset()     
    setting_minimum_and_maximimum(self,target_number_1,target_number_2)
    self.min_x = np.min([np.min(list(target_number_1.x_values)),np.min(list(target_number_2.x_values))])
    self.max_x = np.max([np.max(list(target_number_1.x_values)),np.max(list(target_number_2.x_values))])
    plot_configuration(self,ylabel_name,uppper_limit,lower_limit)
    legend_t1 = "AVE " + legend + str(self.target_1)
    legend_t2 = "AVE " + legend + str(self.target_2)
    flag_min = "1"
    removing_adding_target_1_4_max_min(self,target_number_1,target_number_2,file_name,legend_t1,legend_t2,flag_min,colors,colors_min)  
    removing_days_adding_weeks(self)
    removing_adding_gap(self)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14)
    self.sc3.fig.savefig((os.path.join(self.output_path,self.file_name_current)))
    self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)
    self.sc3.draw()
    self.sc3.show()

def generic_plot_no_gap_one_quantitie_with_foil(self,target_number_1,target_number_2,label,ylabel_name,file_name,legend,flag_min,uppper_limit,lower_limit):
    generic_plot_no_gap_one_quantitie(self,target_number_1,target_number_2,label,ylabel_name,file_name,legend,flag_min,uppper_limit,lower_limit)
    sel_system_1 = Selection_system()
    sel_system_4 = Selection_system()
    selecting_foils(sel_system_1,target_number_1)
    selecting_foils(sel_system_4,target_number_2)
    if self.target_1_value == "1":
        for i in range(len(sel_system_4.horizontal_mark_plot)):   
            self.sc3.axes.text(sel_system_4.horizontal_mark_plot[i],self.set_configuration_min,"F " + str(sel_system_4.horizontal_value_plot[i]), fontsize=10,rotation=90) 
    elif self.target_2_value == "1":  
        for i in range(len(sel_system_1.horizontal_mark_plot)):
            self.sc3.axes.text(sel_system_1.horizontal_mark_plot[i],self.set_configuration_min,"F " + str(sel_system_1.horizontal_value_plot[i]), fontsize=10,rotation=90)

def generic_plot_no_gap_two_quantities(self,target_number_1,target_number_2,target_number_1_extra,target_number_2_extra,labels1,labels2,ylabel_name,legend1,legend2,file_name,legend,flag_min,uppper_limit,lower_limit):
    (ave_value_t1,std_value_t1,max_value_t1,min_value_t1) = getting_stadistic_values(target_number_1,labels1)
    (ave_value_t2,std_value_t2,max_value_t2,min_value_t2) = getting_stadistic_values(target_number_2,labels1)
    assigning_statistics(target_number_1,ave_value_t1,std_value_t1,max_value_t1,min_value_t1)
    assigning_statistics(target_number_2,ave_value_t2,std_value_t2,max_value_t2,min_value_t2)
    (ave_value_t1,std_value_t1,max_value_t1,min_value_t1) = getting_stadistic_values(target_number_1_extra,labels2)
    (ave_value_t2,std_value_t2,max_value_t2,min_value_t2) = getting_stadistic_values(target_number_2_extra,labels2)
    assigning_statistics(target_number_1_extra,ave_value_t1,std_value_t1,max_value_t1,min_value_t1)
    assigning_statistics(target_number_2_extra,ave_value_t2,std_value_t2,max_value_t2,min_value_t2)
    colors = [COLORS[4],COLORS[4]]
    colors_2 = [COLORS[8],COLORS[8]]
    colors_min = [COLORS[4],COLORS[9]]
    self.selected_color = [COLORS[4],COLORS[8]]
    target_number_1.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_1)].index)
    target_number_2.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_2)].index)
    target_number_1_extra.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_1)].index)
    target_number_2_extra.x_values = (self.tfs_input.TARGET[self.tfs_input.TARGET == str(self.target_2)].index)
    setting_minimum_and_maximimum_two_functions(self,target_number_1,target_number_2,target_number_1_extra,target_number_2_extra)
    self.min_x = np.min([np.min(list(target_number_1.x_values)),np.min(list(target_number_2.x_values))])
    self.max_x = np.max([np.max(list(target_number_1.x_values)),np.max(list(target_number_2.x_values))])
    plot_configuration(self,ylabel_name,uppper_limit,lower_limit)
    self.flag_max()
    legend1_1 = "AVE " + legend1
    legend2_1 = '_nolegend_'
    legend2_2 ='_nolegend_'
    legend1_2 = "AVE " + legend2
    removing_adding_target_1_4_max_min(self,target_number_1,target_number_2,file_name,legend1_1,legend2_1,flag_min,colors,colors_min)
    removing_adding_target_1_4_max_min(self,target_number_1_extra,target_number_2_extra,file_name,legend1_2,legend2_2,flag_min,colors_2,colors_min)   
    removing_days_adding_weeks(self)
    removing_adding_gap(self)
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
           for j in range(len(index_foil_sorted[i])):
                sel_system_1.check_line(target_information.index_foil_sorted[i][j],target_information.unique_index_foil[i],i,target_information.index_foil_sorted_position[i][j])
           sel_system.horizontal_mark_plot.append(sel_system.verification_position)
           sel_system.horizontal_value_plot.append(sel_system.valuei)
           sel_system.counter.append(sel_system.counteri)

