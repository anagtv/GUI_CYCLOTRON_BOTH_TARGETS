import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser
import os
from tkinter import *
from pandas import ExcelWriter
plt.rcParams.update({'font.size': 16})
plt.rcParams["figure.figsize"] = (15,10)
import sys
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python")
sys.path.append("/Users/anagtv/Documents/Beta-Beat.src-master")
#from tfs_files import tfs_pandas
from mpl_interaction import figure_pz
import matplotlib.pyplot as plt
import tfs
import datetime
from datetime import timedelta


COLORS = ['#1E90FF','#FF4500','#32CD32',"#6A5ACD","#20B2AA","#00008B","#A52A2A","#228B22","#FF3300","#3366FF","#FF9933"]

def _parse_args():
    parser = OptionParser()
    parser.add_option("-i", "--input",
                    help="Input measurement path",
                    metavar="INPUT", dest="input_path")
    parser.add_option("-t", "--target",
                    help="Input measurement path (Target 4)",
                    metavar="INPUT", dest="input_path_4")
    parser.add_option("-o", "--output",
                    help="Output measurement path",
                    metavar="OUTPUT", dest="output_path")
    parser.add_option("-c", "--current",
                    help="Target current",
                    metavar="TCURRENT", dest="target_current")
    options, _ = parser.parse_args()
    return options.input_path,options.input_path_4,options.output_path,options.target_current

class Selection_system:
   def __init__(self):
        self.verification = -1
        self.verification_position = 0
        self.counter = []
        self.horizontal_value_plot = []
        self.horizontal_mark_plot = []
        self.horizontal_value_plot_1 = []
        self.horizontal_mark_plot_1 = []
        self.horizontal_value_plot_4 = []
        self.horizontal_mark_plot_4 = []
        self.counter = []
        self.indexi = 0
        self.valuei = 0
        self.counteri = -1
   def check_line(self,line,value,index,line_position):
    #cheking if they are stil 
    if int(line) == int(self.verification + 1) and int(index) == int(self.indexi):
         print ("HEREEE")
         print (line)        
         print (value)
         print (index)
         self.counteri += 1 
    else:
         print ("OR HEREE")
         print (line)
         print (line == (self.verification + 1))
         print (index == self.indexi)
         print (self.verification + 1)
         print (line_position)
         print ("LOCATION")
         print (self.verification_position)
         print (value)
         print (self.valuei)
         print (index)
         print (self.indexi)
         self.horizontal_mark_plot.append(self.verification_position)
         self.horizontal_value_plot.append(self.valuei)
         self.counter.append(self.counteri)
         print (self.counteri)
         self.counteri = 0
         self.verification_position = line_position 
    self.valuei = value
    self.verification = line
    self.indexi = index
    return self.verification 


def plotting_max_min(self,x_target_1,x_target_4,max_value_4,min_value_4,max_value_1,min_value_1,legend1,fmts,target_number_1,target_number_4,flag_min,legend_target):
    #maxmimum values 
    if target_number_4 == 1:
        self.sc3.axes.errorbar(x_target_1,max_value_1,fmt=fmts[1], color=COLORS[9],label= "MAX " + legend1 + legend_target[0], picker=5)
        if flag_min == 1:
            self.sc3.axes.errorbar(x_target_1,min_value_1,fmt=fmts[2], color=COLORS[9],label= "MIN " + legend1 + legend_target[0], picker=5)
    elif target_number_1 == 1:
        self.sc3.axes.errorbar(x_target_4,max_value_4,fmt=fmts[1], color=COLORS[10],label= "MAX " + legend1 + legend_target[1], picker=5)
        if flag_min == 1:
            self.sc3.axes.errorbar(x_target_4,min_value_4,fmt=fmts[2], color=COLORS[10],label= "MIN " + legend1 + legend_target[1], picker=5)
    else: 
        self.sc3.axes.errorbar(x_target_1,max_value_1,fmt=fmts[1], color=COLORS[9],label= "MAX " + legend1 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,max_value_4,fmt=fmts[1], color=COLORS[10],label= "MAX " + legend1 + legend_target[1], picker=5)
        if flag_min == 1:
            self.sc3.axes.errorbar(x_target_1,min_value_1,fmt=fmts[2], color=COLORS[9],label= "MIN " + legend1 + legend_target[0], picker=5)
            self.sc3.axes.errorbar(x_target_4,min_value_4,fmt=fmts[2], color=COLORS[10],label= "MIN " + legend1 + legend_target[1], picker=5)

def generic_plot_gap_one_quantitie(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,output_path,flag_value,target_number_1,target_number_4,index_week,flag_min):
    df_sorted_combined = df_sorted_combined.sort_values(by=['FILE'])
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    legend_target = [" 1", " 4"]
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
        legend_target = [" 2", " 5"]
    #columns_rf_dee_voltage =  ["FILE","DATE","TARGET","DEE1_VOLTAGE_MAX","DEE1_VOLTAGE_MIN","DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_MAX","DEE2_VOLTAGE_MIN","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD"]
    column_name_ave_1 = label_1 + "AVE"
    column_name_max_1 = label_1 + "MAX"
    column_name_std_1 = label_1 + "STD"
    column_name_min_1 = label_1 + "MIN"
    #df_date_unique = pd.DataFrame(columns=columns_rf_dee_voltage)
    date_format = "%d-%m-%Y"
    ave_value_1 = []
    std_value_1 = []
    max_value_1 = []
    min_value_1 = []
    target_number = []
    date_stamp = []
    date_stamp_individual = []
    file_number = []
    ave_value_1 = (getattr(df_sorted_target_1,column_name_ave_1))
    std_value_1 = (getattr(df_sorted_target_1,column_name_std_1))
    ave_value_4 = (getattr(df_sorted_target_4,column_name_ave_1))
    std_value_4 = (getattr(df_sorted_target_4,column_name_std_1))
    #maxmimum values 
    max_value_4 = (getattr(df_sorted_target_4,column_name_max_1))
    min_value_4 = (getattr(df_sorted_target_4,column_name_min_1))
    max_value_1 = (getattr(df_sorted_target_1,column_name_max_1))
    min_value_1 = (getattr(df_sorted_target_1,column_name_min_1))
    if target_number_4 == 1:
       maximum_value = (np.max(ave_value_1 + std_value_1))
       minimum_value = (np.max(ave_value_1 - std_value_1))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.09*plot_size+maximum_value
    elif target_number_1 == 1:
       maximum_value = (np.max(ave_value_4 + std_value_4))
       minimum_value = (np.min(ave_value_4 - std_value_4))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    else:
       maximum_value = (np.max([np.max(ave_value_1 + std_value_1),np.max(ave_value_4 + std_value_4)]))
       minimum_value = (np.min([np.max(ave_value_1 - std_value_1),np.min(ave_value_4 - std_value_4)]))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    #plot_size = maximum_value - minimum_value
    print ("MAXIMUMM")
    print ("TARGETS")
    print (df_sorted_combined)
    print (df_sorted_target_1)
    print ("VALUES")
    print (maximum_value)
    print (minimum_value)
    print (plot_size)
    print (set_configuration)
    target_number = (df_sorted_combined.TARGET)
    file_number_all = (df_sorted_combined.FILE)
    fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE',fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name,fontsize=14)
    x_target_1 = (df_sorted_target_1.FILE.astype(float))
    x_target_4 = (df_sorted_target_4.FILE.astype(float))
    index_week_list = []  
    week_number = []
    x_values = []
    fmts = ["o","^","v"]
    if target_number_4 == 1: 
        file_name_current = file_name[:-4] + "_target_1.pdf"
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=std_value_1,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + legend_target[0], picker=5)
    elif target_number_1 == 1: 
        file_name_current = file_name[:-4] + "_target_4.pdf"
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=std_value_4,fmt=fmts[0], color=COLORS[8],label= "AVE " + legend1 + legend_target[1], picker=5)
    else: 
        file_name_current = file_name
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=std_value_1,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=std_value_4,fmt=fmts[0], color=COLORS[8],label= "AVE " + legend1 + legend_target[1], picker=5)
    if flag_value == 0:
        if target_number_4 == 1:
            file_name_current = file_name[:-4] + "_target_1.pdf"
            maximum_value = (np.max(max_value_1))
            minimum_value = (np.min(min_value_1))
        elif target_number_1 == 1:
            file_name_current = file_name[:-4] + "_target_4.pdf"
            maximum_value = (np.max(max_value_4))
            minimum_value = (np.min(min_value_4))
        else:
            file_name_current = file_name
            maximum_value = (np.max([np.max(max_value_1),np.max(max_value_4)]))
            minimum_value = (np.min([np.min(min_value_1),np.min(min_value_4)]))
        plotting_max_min(self,x_target_1,x_target_4,max_value_4,min_value_4,max_value_1,min_value_1,legend1,fmts,target_number_1,target_number_4,flag_min,legend_target)
        plot_size = maximum_value - minimum_value
        set_configuration = 0.08*plot_size+maximum_value
    #self.sc3.axes.set_xticks(range(len(file_number_all)))
    for i in range(0,len(df_sorted_combined.DATE),10):
       x = i
       x_values.append(i)
       print ("CHECKIN POSITION")
       print (set_configuration)
       self.sc3.axes.text(x-0.3, set_configuration,df_sorted_combined.DATE.iloc[i][5:], fontsize=12,rotation=90)
    
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name)
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if index_week == 1:
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                print ("HEREEEEE")
                self.sc3.axes.text(index_week_list[i]-0.3,  set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else:
        for i in range(0,len(file_number_all),1):
           date_to_week = datetime.datetime.strptime(df_sorted_combined.DATE.iloc[i],"%Y-%m-%d")
           week_number.append(date_to_week.isocalendar()[1])
    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14) 
    print (list(x_target_1))
    print (np.min(list(x_target_1)))
    print (np.min(list(x_target_4)))
    min_x = np.min([np.min(list(x_target_1)),np.min(list(x_target_4))])
    max_x = np.max([np.max(list(x_target_1)),np.max(list(x_target_4))])
    self.sc3.axes.set_xlim([min_x-2,max_x+2]) 
    fig.tight_layout()  
    time_list = (list(range(len(df_sorted_combined.FILE))))
    #try:
    ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)]   
    ticks_to_use_list = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)] 
    print ("TICKS")
    print (df_sorted_combined.FILE)
    print (ticks_to_use)
    print (ticks_to_use_list)
    self.sc3.axes.set_xticks(ticks_to_use.astype(float))
    self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)
    #except:
    #   print ("also here")
    #   #ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/2)]   
       #ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/2)] 
    #   self.sc3.axes.set_xticks(df_sorted_combined.FILE.astype(float))
       #self.sc3.axes.set_xticklabels(ticks_to_use)
    print ("SAVING FILE")
    self.sc3.savefig(file_name_current)
    return (maximum_value,minimum_value,plot_size)
    # otherwise the right y-label is slightly clipped  
    #dee1dee2file = os.path.join(output_path, file_name)
    #fig.savefig(dee1dee2file) 

def generic_plot_no_gap_one_quantitie_no_std(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,output_path,flag_value,target_number_1,target_number_4,index_week,flag_min,flag_no_gap,color_code):
    df_sorted_combined = df_sorted_combined.sort_values(by=['FILE'])
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
    #columns_rf_dee_voltage =  ["FILE","DATE","TARGET","DEE1_VOLTAGE_MAX","DEE1_VOLTAGE_MIN","DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_MAX","DEE2_VOLTAGE_MIN","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD"]
    column_name_ave_1 = label_1 
    #df_date_unique = pd.DataFrame(columns=columns_rf_dee_voltage)
    date_format = "%d-%m-%Y"
    ave_value_1 = []
    std_value_1 = []
    max_value_1 = []
    min_value_1 = []
    target_number = []
    date_stamp = []
    date_stamp_individual = []
    file_number = []
    ave_value_1 = (getattr(df_sorted_target_1,column_name_ave_1))
    ave_value_4 = (getattr(df_sorted_target_4,column_name_ave_1))
    if target_number_4 == 1:
       maximum_value = (np.max(ave_value_1))
       minimum_value = (np.min(ave_value_1))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.09*plot_size+maximum_value
    elif target_number_1 == 1:
       maximum_value = (np.max(ave_value_4))
       minimum_value = (np.min(ave_value_4))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    else:
       maximum_value = (np.max([np.max(ave_value_1),np.max(ave_value_4)]))
       minimum_value = (np.min([np.max(ave_value_1),np.min(ave_value_4)]))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    #plot_size = maximum_value - minimum_value
    target_number = (df_sorted_combined.TARGET)
    file_number_all = (df_sorted_combined.FILE)
    fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE',fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name,fontsize=14)
    if flag_no_gap == 1:
        x_target_1 = (df_sorted_target_1.index)
        x_target_4 = (df_sorted_target_4.index)
    else:
        x_target_1 = (df_sorted_target_1.FILE.astype(float))
        x_target_4 = (df_sorted_target_4.FILE.astype(float))
    index_week_list = []  
    week_number = []
    x_values = []
    fmts = ["o","^","v"]
    if target_number_4 == 1:
        file_name_current = file_name[:-4] + "_target_1.pdf"
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=0,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + " 1", picker=5)
    elif target_number_1 == 1:
        file_name_current = file_name[:-4] + "_target_4.pdf"
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=0,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + " 4", picker=5)
    else:
        file_name_current = file_name
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=0,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + " 1", picker=5)
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=0,fmt=fmts[0], color=COLORS[4],label= "AVE " + legend1 + " 4", picker=5)
    for i in range(0,len(df_sorted_combined.DATE),10):
       x = i
       x_values.append(i)
       self.sc3.axes.text(x-0.3, set_configuration,df_sorted_combined.DATE.iloc[i][5:], fontsize=12,rotation=90)
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name)
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if index_week == 1:
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                print ("HEREEEEE")
                self.sc3.axes.text(index_week_list[i]-0.3,  set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else:
        for i in range(0,len(file_number_all),1):
           date_to_week = datetime.datetime.strptime(df_sorted_combined.DATE.iloc[i],"%Y-%m-%d")
           week_number.append(date_to_week.isocalendar()[1])
    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    #self.sc3.axes.legend(loc='best',ncol=3,fontsize=14) 
    min_x = np.min([np.min(list(x_target_1)),np.min(list(x_target_4))])
    max_x = np.max([np.max(list(x_target_1)),np.max(list(x_target_4))])
    self.sc3.axes.set_xlim([min_x-2,max_x+2]) 
    fig.tight_layout()  
    time_list = (list(range(len(df_sorted_combined.FILE))))
    if flag_no_gap == 1:
        try:
           ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/10)]   
           ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/10)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
        except:
           ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/2)]   
           ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/2)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
    else: 
        ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)]   
        ticks_to_use_list = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)] 
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)
    print ("SAVING FILE")
    self.sc3.fig.savefig((os.path.join(output_path,file_name_current)))
    return (maximum_value,minimum_value,plot_size)
    # otherwise the right y-label is slightly clipped  
    #dee1dee2file = os.path.join(output_path, file_name)
     



def generic_plot_no_gap_one_quantitie(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,output_path,flag_value,target_number_1,target_number_4,index_week,flag_min,flag_no_gap,color_code):
    df_sorted_combined = df_sorted_combined.sort_values(by=['FILE'])
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    legend_target = [" 1"," 4"]
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
        legend_target = [" 2"," 5"]
    #columns_rf_dee_voltage =  ["FILE","DATE","TARGET","DEE1_VOLTAGE_MAX","DEE1_VOLTAGE_MIN","DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_MAX","DEE2_VOLTAGE_MIN","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD"]
    column_name_ave_1 = label_1 + "AVE"
    column_name_max_1 = label_1 + "MAX"
    column_name_std_1 = label_1 + "STD"
    column_name_min_1 = label_1 + "MIN"
    #df_date_unique = pd.DataFrame(columns=columns_rf_dee_voltage)
    date_format = "%d-%m-%Y"
    ave_value_1 = []
    std_value_1 = []
    max_value_1 = []
    min_value_1 = []
    target_number = []
    date_stamp = []
    date_stamp_individual = []
    file_number = []
    ave_value_1 = (getattr(df_sorted_target_1,column_name_ave_1))
    ave_value_4 = (getattr(df_sorted_target_4,column_name_ave_1))
    std_value_1 = (getattr(df_sorted_target_1,column_name_std_1))
    std_value_4 = (getattr(df_sorted_target_4,column_name_std_1))
    #maxmimum values 
    max_value_4 = (getattr(df_sorted_target_4,column_name_max_1))
    min_value_4 = (getattr(df_sorted_target_4,column_name_min_1))
    max_value_1 = (getattr(df_sorted_target_1,column_name_max_1))
    min_value_1 = (getattr(df_sorted_target_1,column_name_min_1))
    if color_code == 1:
         selected_color = [COLORS[4],COLORS[8]]
    else: 
        selected_color = [COLORS[4],COLORS[4]]
    if target_number_4 == 1:
       maximum_value = (np.max(ave_value_1 + std_value_1))
       minimum_value = (np.max(ave_value_1 - std_value_1))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.09*plot_size+maximum_value
    elif target_number_1 == 1:
       maximum_value = (np.max(ave_value_4 + std_value_4))
       minimum_value = (np.min(ave_value_4 - std_value_4))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    else:
       maximum_value = (np.max([np.max(ave_value_1 + std_value_1),np.max(ave_value_4 + std_value_4)]))
       minimum_value = (np.min([np.max(ave_value_1 - std_value_1),np.min(ave_value_4 - std_value_4)]))
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    #plot_size = maximum_value - minimum_value
    target_number = (df_sorted_combined.TARGET)
    file_number_all = (df_sorted_combined.FILE)
    fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE',fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name,fontsize=14)
    if flag_no_gap == 1:
        x_target_1 = (df_sorted_target_1.index)
        x_target_4 = (df_sorted_target_4.index)
    else:
        x_target_1 = (df_sorted_target_1.FILE.astype(float))
        x_target_4 = (df_sorted_target_4.FILE.astype(float))
    index_week_list = []  
    week_number = []
    x_values = []
    fmts = ["o","^","v"]
    if target_number_4 == 1:
        file_name_current = file_name[:-4] + "_target_1.pdf"
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=std_value_1,fmt=fmts[0], color=selected_color[0],label= "AVE " + legend1 + legend_target[0], picker=5)
    elif target_number_1 == 1:
        file_name_current = file_name[:-4] + "_target_4.pdf"
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=std_value_4,fmt=fmts[0], color=selected_color[1],label= "AVE " + legend1 + legend_target[1], picker=5)
    else:
        file_name_current = file_name
        self.sc3.axes.errorbar(x_target_1,ave_value_1,yerr=std_value_1,fmt=fmts[0], color=selected_color[0],label= "AVE " + legend1 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,ave_value_4,yerr=std_value_4,fmt=fmts[0], color=selected_color[1],label= "AVE " + legend1 + legend_target[1], picker=5)
    if flag_value == 0:
        if target_number_4 == 1:
            maximum_value = (np.max(max_value_1))
            minimum_value = (np.min(min_value_1))
        elif target_number_1 == 1:
            maximum_value = (np.max(max_value_4))
            minimum_value = (np.min(min_value_4))
        else:
            maximum_value = (np.max([np.max(max_value_1),np.max(max_value_4)]))
            minimum_value = (np.min([np.min(min_value_1),np.min(min_value_4)]))
        plotting_max_min(self,x_target_1,x_target_4,max_value_4,min_value_4,max_value_1,min_value_1,legend1,fmts,target_number_1,target_number_4,flag_min,legend_target)
        plot_size = maximum_value - minimum_value
        set_configuration = 0.08*plot_size+maximum_value
    #self.sc3.axes.set_xticks(range(len(file_number_all)))
    for i in range(0,len(df_sorted_combined.DATE),10):
       x = i
       x_values.append(i)
       print ("CHECKING POSITION")
       print (set_configuration)
       self.sc3.axes.text(x-0.3, set_configuration,df_sorted_combined.DATE.iloc[i][5:], fontsize=12,rotation=90)
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name)
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if index_week == 1:
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                print ("HEREEEEE")
                self.sc3.axes.text(index_week_list[i]-0.3,  set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else:
        for i in range(0,len(file_number_all),1):
           date_to_week = datetime.datetime.strptime(df_sorted_combined.DATE.iloc[i],"%Y-%m-%d")
           week_number.append(date_to_week.isocalendar()[1])
    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    self.sc3.axes.legend(loc='best',ncol=3,fontsize=14) 
    print (list(x_target_1))
    print (np.min(list(x_target_1)))
    print (np.min(list(x_target_4)))
    min_x = np.min([np.min(list(x_target_1)),np.min(list(x_target_4))])
    max_x = np.max([np.max(list(x_target_1)),np.max(list(x_target_4))])
    self.sc3.axes.set_xlim([min_x-2,max_x+2]) 
    fig.tight_layout()  
    time_list = (list(range(len(df_sorted_combined.FILE))))
    if flag_no_gap == 1:
        try:
           ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/10)]   
           ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/10)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
        except:
           ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/2)]   
           ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/2)] 
           self.sc3.axes.set_xticks(ticks_to_use_list)
           self.sc3.axes.set_xticklabels(ticks_to_use)
    else: 
        ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)]   
        ticks_to_use_list = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)] 
        print ("TICKS")
        print (df_sorted_combined.FILE)
        print (ticks_to_use)
        print (ticks_to_use_list)
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)
    print ("SAVING FILE")
    self.sc3.fig.savefig((os.path.join(output_path,file_name_current)))
    return (maximum_value,minimum_value,plot_size)
    # otherwise the right y-label is slightly clipped  
    #dee1dee2file = os.path.join(output_path, file_name)
     


def generic_plot_no_gap_two_quantities_collimators(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend,index_foil_1,unique_index_foil_1,index_foil_4,unique_index_foil_4,index_foil_sorted_1_position,index_foil_sorted_4_position,output_path,target_number_1,target_number_4,index_week,flag_no_gap):
    df_sorted_combined = df_sorted_combined.sort_values(by=['FILE'])
    column_name_ave_1 = label_1 + "AVE"
    column_name_ave_2 = label_2 + "AVE"
    column_name_std_1 = label_1 + "STD"
    column_name_std_2 = label_2 + "STD"
    date_format = "%Y-%m-%d"
    file_number=(df_sorted_combined.FILE)
    file_number_all = (np.sort(file_number))
    target_number = (df_sorted_combined.TARGET)
    # COMPUTING STATISTIC VALUES   
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    legend_target = [" 1"," 4"]
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
        legend_target = [" 2"," 5"]
    ave_value_1_t1 = (getattr(df_sorted_target_1,column_name_ave_1))
    std_value_1_t1 = (getattr(df_sorted_target_1,column_name_std_1))
    ave_value_2_t1 = (getattr(df_sorted_target_1,column_name_ave_2))
    std_value_2_t1 = (getattr(df_sorted_target_1,column_name_std_2))
    ave_value_total_t1 = ave_value_1_t1 + ave_value_2_t1
    std_value_total_t1 = (std_value_1_t1**2+std_value_2_t1**2)**0.5
    ave_value_1_t4 = (getattr(df_sorted_target_4,column_name_ave_1))
    std_value_1_t4 = (getattr(df_sorted_target_4,column_name_std_1))
    ave_value_2_t4 = (getattr(df_sorted_target_4,column_name_ave_2))
    std_value_2_t4 = (getattr(df_sorted_target_4,column_name_std_2))
    ave_value_total_t4 = ave_value_1_t4 + ave_value_2_t4
    std_value_total_t4 = (std_value_1_t4**2+std_value_2_t4**2)**0.5
    #herreeee
    ave_value_1 = (getattr(df_sorted_combined,column_name_ave_1))
    ave_value_2 = (getattr(df_sorted_combined,column_name_ave_2))
    std_value_1 = (getattr(df_sorted_combined,column_name_std_1))
    std_value_2 = (getattr(df_sorted_combined,column_name_std_2))
    ave_value_total = ave_value_1 + ave_value_2
    std_value_total = (std_value_1+std_value_2)**0.5
    #fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name) 
    #maximum_value = (np.max([np.max(ave_value_1+std_value_1),np.max(ave_value_2+std_value_2)]))
    #minimum_value = (np.min([np.min(ave_value_1+std_value_1),np.min(ave_value_2+std_value_2)]))
    #plot_size = maximum_value - minimum_value
    #preparing weeks
    index_week_list = []  
    week_number = []
    x_values = []
    if flag_no_gap == 1:
        x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("1")].index)
        x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("4")].index)
        if len(x_target_1) == 0:
            x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("2")].index)
            x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("5")].index)
    else:
        x_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")].FILE.astype(float))
        x_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")].FILE.astype(float))       
        if len(x_target_1) == 0:
            x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("2")].index)
            x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("5")].index)           
    fmts = ["o","s"]
    if target_number_4 == 1:
       maximum_value = np.max([np.max(ave_value_total_t1 + std_value_total_t1)])
       minimum_value = np.min([np.min(ave_value_total_t1 + std_value_total_t1)])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
       #set_configuration_l = 0.75*maximum_value
    elif target_number_1 == 1:
       maximum_value = np.max([np.max(ave_value_total_t4 + std_value_total_t4)])
       minimum_value = np.min([np.min(ave_value_total_t4 + std_value_total_t4)])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    else:
       maximum_value = np.max([np.max(ave_value_total + std_value_total)])
       minimum_value = np.min([np.min(ave_value_total + std_value_total)])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value   
    if target_number_4 == 1:
        self.sc3.axes.errorbar(x_target_1,(ave_value_total_t1),yerr=(std_value_total_t1),fmt=fmts[0], color=COLORS[4],label= legend + legend_target[0], picker=5)
        file_name_current = file_name[:-4] + "_target_1.pdf"
        #self.sc3.axes.errorbar(x_target_1,np.array(ave_value_2_t1),yerr=np.array(std_value_2_t1),fmt=fmts[0], color=COLORS[9],label= legend2 + ", picker=5)       
    elif target_number_1 == 1:
        self.sc3.axes.errorbar(x_target_4,(ave_value_total_t4),yerr=(std_value_total_t4),fmt=fmts[0], color=COLORS[10],label= legend  + legend_target[1], picker=5)
        file_name_current = file_name[:-4] + "_target_4.pdf"
        #self.sc3.axes.errorbar(x_target_4,np.array(ave_value_2_t4),yerr=np.array(std_value_2_t4),fmt=fmts[0], color=COLORS[8],label= legend2 + " 4", picker=5)
    else:
        self.sc3.axes.errorbar(x_target_1,(ave_value_total_t1),yerr=(std_value_total_t1),fmt=fmts[0], color=COLORS[4],label= legend + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,(ave_value_total_t4),yerr=(std_value_total_t4),fmt=fmts[0], color=COLORS[10],label= legend + legend_target[1], picker=5)
        file_name_current = file_name
    for i in range(0,len(file_number_all),1):
        date_to_week = datetime.datetime.strptime(df_sorted_combined.DATE.iloc[i],"%Y-%m-%d")
        week_number.append(date_to_week.isocalendar()[1])
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if index_week == 1:
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                self.sc3.axes.text(index_week_list[i]-0.3,  set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else: 
        for i in range(0,len(file_number_all),10):
            x_values.append(i)
            self.sc3.axes.text(i, set_configuration ,df_sorted_combined.DATE.iloc[i][5:], fontsize=12,rotation=90)
    self.sc3.axes.set_xlabel('FILE', fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name, fontsize=14)
    time_list = (list(range(len(df_sorted_combined.FILE))))
    if flag_no_gap == 1:
        try:
            ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/5)] 
            ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/5)]   
        except:
            ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/2)]
            ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/2)] 
        self.sc3.axes.set_xticks(ticks_to_use_list)
        self.sc3.axes.set_xticklabels(ticks_to_use)
    else:
        ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)]   
        ticks_to_use_list = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)] 
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)
    sel_system_1 = Selection_system()
    sel_system_4 = Selection_system()
    for i in range(len(index_foil_1)):
        checking_value = (index_foil_1[i] == list(range(min(index_foil_1[i]), max(index_foil_1[i])+1)))
        if checking_value == True:
            sel_system_1.horizontal_mark_plot.append(index_foil_sorted_1_position[i][0])
            sel_system_1.horizontal_value_plot.append(unique_index_foil_1[i])
        else: 
           for j in range(len(index_foil_1[i])):
                sel_system_1.check_line(index_foil_1[i][j],unique_index_foil_1[i],i,index_foil_sorted_1_position[i][j])
           sel_system_1.horizontal_mark_plot.append(sel_system_1.verification_position)
           sel_system_1.horizontal_value_plot.append(sel_system_1.valuei)
           sel_system_1.counter.append(sel_system_1.counteri)
    for i in range(len(index_foil_4)):
        checking_value = (index_foil_4[i] == list(range(min(index_foil_4[i]), max(index_foil_4[i])+1)))
        if len(index_foil_4) == 1:
           checking_value =  checking_value[0]
        if checking_value == True:
            print ("IM HEREEEEEE")
            sel_system_4.horizontal_mark_plot.append(index_foil_sorted_4_position[i][0])
            sel_system_4.horizontal_value_plot.append(unique_index_foil_4[i])
        else: 
           for j in range(len(index_foil_4[i])):
                sel_system_4.check_line(index_foil_4[i][j],unique_index_foil_4[i],i,index_foil_sorted_4_position[i][j])
           sel_system_4.horizontal_mark_plot.append(sel_system_4.verification_position)
           sel_system_4.horizontal_value_plot.append(sel_system_4.valuei)
           sel_system_4.counter.append(sel_system_4.counteri) 
    if target_number_1 == 1:    
        for i in range(len(sel_system_4.horizontal_mark_plot)):   
            self.sc3.axes.text(sel_system_4.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_4.horizontal_value_plot[i]), fontsize=12,rotation=90) 
    elif target_number_4 == 1:
        for i in range(len(sel_system_1.horizontal_mark_plot)):
            self.sc3.axes.text(sel_system_1.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_1.horizontal_value_plot[i]), fontsize=12,rotation=90)
    self.sc3.axes.legend(loc='best',ncol=2,fontsize=14) 
    self.sc3.fig.savefig((os.path.join(output_path,file_name_current))) 
    return (maximum_value,minimum_value,plot_size)
    
    #self.sc3.axes.clear()

def generic_plot_no_gap_two_quantities_extraction(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend1,legend2,output_path,target_number_1,target_number_4,index_week,flag_value,flag_min,flag_no_gap):
    generic_plot_no_gap_two_quantities(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend1,legend2,output_path,target_number_1,target_number_4,index_week,flag_no_gap)
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])    
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
    column_name_max_1 = label_1 + "MAX"
    column_name_min_1 = label_1 + "MIN"
    #column_name_max_2 = label_2 + "AVE"
    #column_name_min_2 = label_2 + "AVE"
    fmts = ["o","^","v"]
    max_value_4 = (getattr(df_sorted_target_4,column_name_max_1))
    min_value_4 = (getattr(df_sorted_target_4,column_name_min_1))
    max_value_1 = (getattr(df_sorted_target_1,column_name_max_1))
    min_value_1 = (getattr(df_sorted_target_1,column_name_min_1))
    x_target_1 = (df_sorted_target_1.index)
    x_target_4 = (df_sorted_target_4.index)
    if flag_value == 0:
        if target_number_4 == 1:
            maximum_value = (np.max(max_value_1))
            minimum_value = (np.min(min_value_1))
        elif target_number_1 == 1:
            maximum_value = (np.max(max_value_4))
            minimum_value = (np.min(min_value_4))
        else:
            maximum_value = (np.max([np.max(max_value_1),np.max(max_value_4)]))
            minimum_value = (np.min([np.min(min_value_1),np.min(min_value_4)]))
        #plotting_max_min(self,x_target_1,x_target_4,max_value_4,min_value_4,max_value_1,min_value_1,legend1,fmts,target_number_1,target_number_4,flag_min)
        plot_size = maximum_value - minimum_value
        set_configuration = 0.08*plot_size+maximum_value
    #self.sc3.axes.set_xticks(range(len(file_number_all)))


def generic_plot_no_gap_two_quantities(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend1,legend2,output_path,target_number_1,target_number_4,index_week,flag_no_gap):
    df_sorted_combined = df_sorted_combined.sort_values(by=['FILE'])
    column_name_ave_1 = label_1 + "AVE"
    column_name_ave_2 = label_2 + "AVE"
    column_name_std_1 = label_1 + "STD"
    column_name_std_2 = label_2 + "STD"
    date_format = "%Y-%m-%d"
    file_number=(df_sorted_combined.FILE)
    file_number_all = (np.sort(file_number))
    target_number = (df_sorted_combined.TARGET)
    # COMPUTING STATISTIC VALUES   
    df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")])
    df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")])
    legend_target = [" 1"," 4"]
    if len(df_sorted_target_1) == 0:
        df_sorted_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("2")])
        df_sorted_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("5")])
        legend_target = [" 2"," 5"]
    ave_value_1_t1 = (getattr(df_sorted_target_1,column_name_ave_1))
    std_value_1_t1 = (getattr(df_sorted_target_1,column_name_std_1))
    ave_value_2_t1 = (getattr(df_sorted_target_1,column_name_ave_2))
    std_value_2_t1 = (getattr(df_sorted_target_1,column_name_std_2))
    ave_value_1_t4 = (getattr(df_sorted_target_4,column_name_ave_1))
    std_value_1_t4 = (getattr(df_sorted_target_4,column_name_std_1))
    ave_value_2_t4 = (getattr(df_sorted_target_4,column_name_ave_2))
    std_value_2_t4 = (getattr(df_sorted_target_4,column_name_std_2))
    #herreeee
    ave_value_1 = (getattr(df_sorted_combined,column_name_ave_1))
    ave_value_2 = (getattr(df_sorted_combined,column_name_ave_2))
    std_value_1 = (getattr(df_sorted_combined,column_name_std_1))
    std_value_2 = (getattr(df_sorted_combined,column_name_std_2))
    #fig, ax1 = plt.subplots()
    self.sc3.axes.ticklabel_format(axis="y",style="sci")
    self.sc3.axes.set_xlabel('FILE')
    self.sc3.axes.set_ylabel(ylabel_name) 
    #maximum_value = (np.max([np.max(ave_value_1+std_value_1),np.max(ave_value_2+std_value_2)]))
    #minimum_value = (np.min([np.min(ave_value_1+std_value_1),np.min(ave_value_2+std_value_2)]))
    #plot_size = maximum_value - minimum_value
    #preparing weeks
    index_week_list = []  
    week_number = []
    x_values = []
    if flag_no_gap == 1:
        print ("HEREEEEEEEE")
        x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("1")].index)
        x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("4")].index)
        print ("first attemp")
        print (x_target_1)
        print (len(x_target_1))
        print (len(x_target_1 == 0))
        if len(x_target_1) == 0:
            x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("2")].index)
            x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("5")].index)
            print ("second attemp")
            print (x_target_4)
    else:
        x_target_1 = (df_sorted_combined[df_sorted_combined.TARGET == ("1")].FILE.astype(float))
        x_target_4 = (df_sorted_combined[df_sorted_combined.TARGET == ("4")].FILE.astype(float))
        if len(x_target_1) == 0:
            x_target_1 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("2")].index)
            x_target_4 = np.array(df_sorted_combined[df_sorted_combined.TARGET == ("5")].index)
    fmts = ["o","s"]
    if target_number_4 == 1:
       file_name_current = file_name[:-4] + "_target_1.pdf"
       maximum_value = np.max([np.max(ave_value_1_t1 + std_value_1_t1),np.max(np.max(ave_value_2_t1 + std_value_2_t1))])
       minimum_value = np.min([np.min(ave_value_1_t1 + std_value_1_t1),np.min(np.min(ave_value_2_t1 + std_value_2_t1))])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
       #set_configuration_l = 0.75*maximum_value
    elif target_number_1 == 1:
       file_name_current = file_name[:-4] + "_target_4.pdf"
       maximum_value = np.max([np.max(ave_value_1_t4 + std_value_1_t4),np.max(np.max(ave_value_2_t4 + std_value_2_t4))])
       minimum_value = np.min([np.min(ave_value_1_t4 + std_value_1_t4),np.min(np.min(ave_value_2_t4 + std_value_2_t4))])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value
    else:
       file_name_current = file_name
       maximum_value = np.max([np.max(ave_value_1 + std_value_1),np.max(np.max(ave_value_2 + std_value_2))])
       minimum_value = np.min([np.min(ave_value_1 + std_value_1),np.min(np.min(ave_value_2 + std_value_2))])
       plot_size = maximum_value - minimum_value
       set_configuration = 0.08*plot_size+maximum_value   
    if target_number_4 == 1:
        self.sc3.axes.errorbar(x_target_1,(ave_value_1_t1),yerr=(std_value_1_t1),fmt=fmts[0], color=COLORS[4],label= legend1 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_1,np.array(ave_value_2_t1),yerr=np.array(std_value_2_t1),fmt=fmts[0], color=COLORS[9],label= legend2 + legend_target[0], picker=5)       
    elif target_number_1 == 1:
        self.sc3.axes.errorbar(x_target_4,(ave_value_1_t4),yerr=(std_value_1_t4),fmt=fmts[0], color=COLORS[10],label= legend1 + legend_target[1], picker=5)
        self.sc3.axes.errorbar(x_target_4,np.array(ave_value_2_t4),yerr=np.array(std_value_2_t4),fmt=fmts[0], color=COLORS[8],label= legend2 + legend_target[1], picker=5)
    else:
        print ("JUST BEFORE PLOTTING")
        print (len(x_target_1),len(ave_value_1_t1),len(std_value_1_t1))
        print (x_target_1)
        print (ave_value_1_t1)
        print (std_value_1_t1)
        self.sc3.axes.errorbar(x_target_1,(ave_value_1_t1),yerr=(std_value_1_t1),fmt=fmts[0], color=COLORS[4],label= legend1 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,(ave_value_1_t4),yerr=(std_value_1_t4),fmt=fmts[0], color=COLORS[10],label= legend1 + legend_target[1], picker=5)
        self.sc3.axes.errorbar(x_target_1,np.array(ave_value_2_t1),yerr=np.array(std_value_2_t1),fmt=fmts[0], color=COLORS[9],label= legend2 + legend_target[0], picker=5)
        self.sc3.axes.errorbar(x_target_4,np.array(ave_value_2_t4),yerr=np.array(std_value_2_t4),fmt=fmts[0], color=COLORS[8],label= legend2 + legend_target[1], picker=5)
    for i in range(0,len(file_number_all),1):
        date_to_week = datetime.datetime.strptime(df_sorted_combined.DATE.iloc[i],"%Y-%m-%d")
        week_number.append(date_to_week.isocalendar()[1])
    df_week = pd.DataFrame(week_number,columns =['WEEK'])
    df_week_first = df_week.drop_duplicates(subset="WEEK",keep = "last")
    df_week_first_index = df_week_first.index
    if index_week == 1:
        for i in range(len(df_week_first.WEEK)):
            index_week = (((df_week[df_week["WEEK"] == df_week_first.WEEK.iloc[i]].index)))
            index_week_tolist = index_week.tolist()
            index_week_tolist_average = np.average(index_week_tolist)
            index_week_list.append(index_week_tolist_average)  
            if index_week_list[i] not in x_values: 
                self.sc3.axes.text(index_week_list[i]-0.3,  set_configuration ,"W " + str(df_week_first.WEEK.iloc[i]),color='r', fontsize=12,rotation=90)
    else: 
        for i in range(0,len(file_number_all),10):
            x_values.append(i)
            self.sc3.axes.text(i, set_configuration ,df_sorted_combined.DATE.iloc[i][5:], fontsize=12,rotation=90)
    self.sc3.axes.set_xlabel('FILE', fontsize=14)
    self.sc3.axes.set_ylabel(ylabel_name, fontsize=14)
    time_list = (list(range(len(df_sorted_combined.FILE))))
    if flag_no_gap == 1:
        try:
            ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/5)] 
            ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/5)]   
        except:
            ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/2)]
            ticks_to_use_list = time_list[::int(len(df_sorted_combined.FILE)/2)] 
        self.sc3.axes.set_xticks(ticks_to_use_list)
        self.sc3.axes.set_xticklabels(ticks_to_use)
    else:
        ticks_to_use = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)]   
        ticks_to_use_list = df_sorted_combined.FILE[::int(len(df_sorted_combined.FILE)/15)] 
        print ("TICKS")
        print (df_sorted_combined.FILE)
        print (ticks_to_use)
        print (ticks_to_use_list)
        self.sc3.axes.set_xticks(ticks_to_use.astype(float))
        self.sc3.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=90)

    plt.xticks(rotation=90,fontsize=16)
    plt.yticks(fontsize=16)
    self.sc3.axes.legend(loc='best',ncol=2,fontsize=14)  
    print ("SAVING FILE")
    self.sc3.fig.savefig(os.path.join(output_path,file_name_current))
    return (maximum_value,minimum_value,plot_size)
     
    #self.sc3.axes.clear()


def generic_plot_no_gap_two_quantities_with_foil(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend1,legend2,index_foil_1,unique_index_foil_1,index_foil_4,unique_index_foil_4,index_foil_sorted_1_position,index_foil_sorted_4_position,output_path,target_number_1,target_number_4,index_week,flag_no_gap):
    [maximum_value,minimum_value,plot_size] = generic_plot_no_gap_two_quantities(self,df_sorted_combined,label_1,label_2,ylabel_name,file_name,legend1,legend2,output_path,target_number_1,target_number_4,index_week,flag_no_gap)
    #self.sc3.axes.clear()
    sel_system_1 = Selection_system()
    sel_system_4 = Selection_system()
    #self.sc3.axes.clear()
    print ("INFORMATION")
    print (index_foil_1)
    print (index_foil_sorted_1_position)
    print (unique_index_foil_1)
    print (index_foil_4)
    print (index_foil_sorted_4_position)
    print (unique_index_foil_4)
    for i in range(len(index_foil_1)):
        checking_value = (index_foil_1[i] == list(range(min(index_foil_1[i]), max(index_foil_1[i])+1)))
        if checking_value == True:
            sel_system_1.horizontal_mark_plot.append(index_foil_sorted_1_position[i][0])
            sel_system_1.horizontal_value_plot.append(unique_index_foil_1[i])
        else: 
           for j in range(len(index_foil_1[i])):
                sel_system_1.check_line(index_foil_1[i][j],unique_index_foil_1[i],i,index_foil_sorted_1_position[i][j])
           sel_system_1.horizontal_mark_plot.append(sel_system_1.verification_position)
           sel_system_1.horizontal_value_plot.append(sel_system_1.valuei)
           sel_system_1.counter.append(sel_system_1.counteri)
    print ("HEREEEE")
    print (sel_system_1)
    print (index_foil_4)
    print (sel_system_1.horizontal_mark_plot)
    print (sel_system_1.horizontal_value_plot)
    for i in range(len(index_foil_4)):
        print ("HEEREEEEEEEHDSJJSN")
        print (index_foil_4[i])
        print (list(range(min(index_foil_4[i]), max(index_foil_4[i])+1)))
        checking_value = (index_foil_4[i] == list(range(min(index_foil_4[i]), max(index_foil_4[i])+1)))
        if len(index_foil_4) == 1:
           checking_value =  checking_value[0]
        if checking_value == True:
            print ("IM HEREEEEEE")
            sel_system_4.horizontal_mark_plot.append(index_foil_sorted_4_position[i][0])
            sel_system_4.horizontal_value_plot.append(unique_index_foil_4[i])
        else: 
           for j in range(len(index_foil_4[i])):
                sel_system_4.check_line(index_foil_4[i][j],unique_index_foil_4[i],i,index_foil_sorted_4_position[i][j])
           sel_system_4.horizontal_mark_plot.append(sel_system_4.verification_position)
           sel_system_4.horizontal_value_plot.append(sel_system_4.valuei)
           sel_system_4.counter.append(sel_system_4.counteri) 
    print (sel_system_4.horizontal_mark_plot)
    print (sel_system_4.horizontal_value_plot) 
    if target_number_1 == 1:
        for i in range(len(sel_system_4.horizontal_mark_plot)):   
            self.sc3.axes.text(sel_system_4.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_4.horizontal_value_plot[i]), fontsize=10,rotation=90) 
    elif target_number_4 == 1:  
        for i in range(len(sel_system_1.horizontal_mark_plot)):
            self.sc3.axes.text(sel_system_1.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_1.horizontal_value_plot[i]), fontsize=10,rotation=90)


def generic_plot_no_gap_one_quantitie_with_foil(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,index_foil_1,unique_index_foil_1,index_foil_4,unique_index_foil_4,index_foil_sorted_1_position,index_foil_sorted_4_position,output_path,flag_max_min,target_number_1,target_number_4,index_week,flag_min,flag_no_gap,color_code):
    if color_code == 1:
        [maximum_value,minimum_value,plot_size] = generic_plot_no_gap_one_quantitie(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,output_path,flag_max_min,target_number_1,target_number_4,index_week,flag_min,flag_no_gap,color_code)
    else: 
        [maximum_value,minimum_value,plot_size] = generic_plot_no_gap_one_quantitie(self,df_sorted_combined,label_1,ylabel_name,file_name,legend1,output_path,flag_max_min,target_number_1,target_number_4,index_week,flag_min,flag_no_gap,color_code)
    #self.sc3.axes.clear()
    sel_system_1 = Selection_system()
    sel_system_4 = Selection_system()
    #self.sc3.axes.clear()
    for i in range(len(index_foil_1)):
        print ("INDEX FOIL 1")
        print (index_foil_1)
        print (len(index_foil_1))
        print (index_foil_1[i])
        checking_value = (index_foil_1[i] == list(range(min(index_foil_1[i]), max(index_foil_1[i])+1)))
        print (checking_value)
        if checking_value == True:
            sel_system_1.horizontal_mark_plot.append(index_foil_sorted_1_position[i][0])
            sel_system_1.horizontal_value_plot.append(unique_index_foil_1[i])
        else: 
           for j in range(len(index_foil_1[i])):
                sel_system_1.check_line(index_foil_1[i][j],unique_index_foil_1[i],i,index_foil_sorted_1_position[i][j])
           sel_system_1.horizontal_mark_plot.append(sel_system_1.verification_position)
           sel_system_1.horizontal_value_plot.append(sel_system_1.valuei)
           sel_system_1.counter.append(sel_system_1.counteri)
    for i in range(len(index_foil_4)):
        print ("INDEX FOIL 4")
        print (index_foil_4)
        print (len(index_foil_4))
        print (index_foil_4[i])
        print (index_foil_4[0][i] == list(range(min(index_foil_4[i]), max(index_foil_4[i])+1)))
        checking_value = (index_foil_4[i] == list(range(min(index_foil_4[i]), max(index_foil_4[i])+1)))
        print (np.array(checking_value))
        if len(index_foil_4) == 1:
           index_foil_4 = np.array(index_foil_4[0])
           print ("HEREEE!!!!!!!!!!!!!!!!")
           print (index_foil_4)
           print (index_foil_4)
           print (np.max(index_foil_4))
           print (np.min(index_foil_4))
           print ((index_foil_4 == list(range(min(index_foil_4), max(index_foil_4)+1))))
           checking_value = (index_foil_4 == list(range(min(index_foil_4), max(index_foil_4)+1)))
           checking_value =  checking_value[0]
        print (checking_value)
        if checking_value == True:
            sel_system_4.horizontal_mark_plot.append(index_foil_sorted_4_position[i][0])
            sel_system_4.horizontal_value_plot.append(unique_index_foil_4[i])
        else: 
           for j in range(len(index_foil_4[i])):
                sel_system_4.check_line(index_foil_4[i][j],unique_index_foil_4[i],i,index_foil_sorted_4_position[i][j])
           sel_system_4.horizontal_mark_plot.append(sel_system_4.verification_position)
           sel_system_4.horizontal_value_plot.append(sel_system_4.valuei)
           sel_system_4.counter.append(sel_system_4.counteri) 
    if target_number_1 == 1:
        for i in range(len(sel_system_4.horizontal_mark_plot)):   
            self.sc3.axes.text(sel_system_4.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_4.horizontal_value_plot[i]), fontsize=10,rotation=90) 
    elif target_number_4 == 1:  
        for i in range(len(sel_system_1.horizontal_mark_plot)):
            self.sc3.axes.text(sel_system_1.horizontal_mark_plot[i],minimum_value,"F " + str(sel_system_1.horizontal_value_plot[i]), fontsize=10,rotation=90)
   
    
    #print (x_target_1)
    
    


def main(input_path_target_1,input_path_target_4,output_path,target_current):

    tfs_input_source_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_source.out"))
    tfs_input_source_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_source.out"))
    tfs_input_vacuum_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_vacuum.out"))
    tfs_input_vacuum_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_vacuum.out"))
    tfs_input_magnet_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_magnet.out"))
    tfs_input_magnet_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_magnet.out"))
    tfs_input_collimators_relative_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_collimators_relative.out"))
    tfs_input_collimators_relative_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_collimators_relative.out"))
    tfs_input_collimators_absolute_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_collimators_absolute.out"))
    tfs_input_collimators_absolute_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_collimators_absolute.out"))    
    tfs_input_target_foil_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_target_foil.out"))
    tfs_input_target_foil_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_target_foil.out"))    
    tfs_input_losses_all_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_losses_all.out"))
    tfs_input_losses_all_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_losses_all.out"))    
    tfs_input_carousel_foil_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_foil_target.out"))
    tfs_input_carousel_foil_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_foil_target.out"))    
    #tfs_input_balance_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_balance.out"))
    #tfs_input_balance_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_balance.out"))    
    tfs_input_dee_voltage_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_dee_voltage.out"))
    tfs_input_dee_voltage_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_dee_voltage.out"))    
    tfs_input_power_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_rf_power.out"))
    tfs_input_power_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_rf_power.out"))    
    tfs_input_flaps_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_flaps.out"))
    tfs_input_flaps_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_flaps.out"))
    tfs_input_ratio_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_ratio.out"))    
    tfs_input_ratio_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_ratio.out")) 
    tfs_input_extraction_balance_1 = tfs.read(os.path.join(input_path_target_1,"table_summary_carousel_balance.out"))    
    tfs_input_extraction_balance_4 = tfs.read(os.path.join(input_path_target_4,"table_summary_carousel_balance.out")) 

   #columns_extraction_absolute_l = ["FILE","DATE","TARGET","COLLIMATOR_CURRENT_L_MAX","COLLIMATOR_CURRENT_L_MIN","COLLIMATOR_CURRENT_L_AVE","COLLIMATOR_CURRENT_L_STD","COLLIMATOR_CURRENT_R_MAX","COLLIMATOR_CURRENT_R_MIN","COLLIMATOR_CURRENT_R_AVE","COLLIMATOR_CURRENT_R_STD"]
    #columns_extraction_relative_l = ["FILE","DATE","TARGET","RELATIVE_COLLIMATOR_CURRENT_L_MAX","RELATIVE_COLLIMATOR_CURRENT_L_MIN","RELATIVE_COLLIMATOR_CURRENT_L_AVE","RELATIVE_COLLIMATOR_CURRENT_L_STD","RELATIVE_COLLIMATOR_CURRENT_R_MAX","RELATIVE_COLLIMATOR_CURRENT_R_MIN","RELATIVE_COLLIMATOR_CURRENT_R_AVE","RELATIVE_COLLIMATOR_CURRENT_R_STD"]

    columns = ["FILE","DATE","TARGET","CURRENT_MAX", "CURRENT_MIN","CURRENT_AVE","CURRENT_STD","VOLTAGE_MAX","VOLTAGE_MIN","VOLTAGE_AVERAGE","VOLTAGE_STD","HFLOW"] 
    units_columns = ["-","-","-","mA","mA","mA","mA","V","V","V","V","sccm"]
    columns_ratio = ["FILE","DATE","TARGET","RATIO_MAX", "RATIO_MIN","RATIO_AVE","RATIO_STD"] 
    columns_extraction_losses = ["FILE","DATE","TARGET","EXTRACTION_LOSSES_MAX","EXTRACTION_LOSSES_MIN","EXTRACTION_LOSSES_AVE","EXTRACTION_LOSSES_STD"]
    #columns_extraction_carousel_position = ["FILE","DATE","TARGET","CAROUSEL_POSITION_MAX","CAROUSEL_POSITION_MIN","CAROUSEL_POSITION_AVE","CAROUSEL_POSITION_STD"]
    #columns_extraction_balance_position = ["FILE","DATE","TARGET","BALANCE_POSITION_MAX","BALANCE_POSITION_MIN","BALANCE_POSITION_AVE","BALANCE_POSITION_STD"]
    columns_vacuum = ["FILE","DATE","TARGET","PRESSURE_MAX","PRESSURE_MIN","PRESSURE_AVE","PRESSURE_STD"]
    columns_magnet = ["FILE","DATE","TARGET","CURRENT_MAX","CURRENT_MIN","CURRENT_AVE","CURRENT_STD"]

    generic_plot_no_gap_two_quantities(tfs_input_dee_voltage_1,"DEE1_VOLTAGE_","DEE2_VOLTAGE_","AVERAGE VOLTAGE [kV]","dee1_dee2_voltage_evolution.pdf","DEE1 T","DEE2 T",1.017,output_path)
    generic_plot_no_gap_two_quantities(tfs_input_carousel_foil_1,"TARGET_CURRENT_","FOIL_CURRENT_",r"AVERAGE CURRENT [$\mu$A]","target_foil_evolution.pdf","TARGET T","FOIL T",1.047,output_path)
    generic_plot_no_gap_two_quantities(tfs_input_power_1,"FORWARD_POWER_","REFLECTED_POWER_",r"AVERAGE POWER [kW]","power_evolution.pdf","TARGET T","FOIL T",1.085,output_path)
    generic_plot_no_gap_two_quantities(tfs_input_flaps_1,"FLAP1_","FLAP2_",r"AVERAGE POSITION [%]","flap_evolution.pdf","FLAP 1","FLAP 2",1.045,output_path)
    generic_plot_no_gap_two_quantities_collimators(tfs_input_collimators_relative_1,"RELATIVE_COLLIMATOR_CURRENT_L_","RELATIVE_COLLIMATOR_CURRENT_R_",r"RELATIVE CURRENT [%]","collimator_current_evolution.pdf","COLLIMATOR L T","COLLIMATOR R T",1.16,output_path)
    generic_plot_no_gap_two_quantities(tfs_input_collimators_absolute_1,"COLLIMATOR_CURRENT_L_","COLLIMATOR_CURRENT_R_",r"CURRENT [$\mu A$]","absolute_collimator_current_evolution.pdf","COLLIMATOR L T","COLLIMATOR R T",1.14,output_path)
    generic_plot_no_gap_two_quantities(tfs_input_extraction_balance_1,"CAROUSEL_POSITION_","BALANCE_POSITION_",r"POSITION [%]","carousel_balance_evolution.pdf","CAROUSEL T","BALANCE R T",1.04,output_path)

    generic_plot_no_gap_one_quantitie(tfs_input_source_1,tfs_input_source_4,"CURRENT_","CURRENT [mA]","ion_source_evolution.pdf","T",1.05,output_path,flag_value,target_number_1,target_number_4)
    generic_plot_no_gap_one_quantitie(tfs_input_ratio_1,tfs_input_ratio_4,"RATIO_",r"RATIO [mA/$\mu A$]","ratio_evolution.pdf","T",1.05,output_path,flag_value,target_number_1,target_number_4)
    generic_plot_no_gap_one_quantitie(tfs_input_vacuum_1,tfs_input_vacuum_4,"PRESSURE_",r"PRESSURE [$10^{-5}$mbar]","vacuum_evolution.pdf","T",1.018,output_path,flag_value,target_number_1,target_number_4)
    generic_plot_no_gap_one_quantitie(tfs_input_magnet_1,tfs_input_magnet_4,"CURRENT_","MAGNET CURRENT [A]","magnet_evolution.pdf","T",1.0008,output_path,flag_value,target_number_1,target_number_4)
    generic_plot_no_gap_one_quantitie(tfs_input_losses_all_1,tfs_input_losses_all_4,"EXTRACTION_LOSSES_","EFFICIENCY [%]","efficiency_target_evolution.pdf","T",1.005,output_path,flag_value,target_number_1,target_number_4)
    #get_plots_extraction(df_extraction_relative_all_l,df_extraction_relative_all_r,output_path,file_number)
    #get_plots_extraction_efficiency(df_extraction_losses_all,output_path,file_number)
    #get_plots_target_foil_efficiency(df_extraction_target_foil_all,output_path,file_number)
    #get_plots_extraction_efficiency(df_extraction_losses_all,output_path,file_number)
    #get_plots_target_foil_efficiency(df_extraction_target_foil_all,output_path,file_number)
    #get_plots_extraction_absolute(df_extraction_absolute_all_l,df_extraction_absolute_all_r,output_path,file_number)
    #get_plots_carousel_balance(df_extraction_carousel_position_all,df_extraction_balance_position_all,output_path,file_number)
    #power
    #get_plots_rf_dee(df_rf_dee_voltage_all,output_path,file_number)
    #get_plots_rf_flaps(df_rf_flaps_all,output_path,file_number,target_number)
    #get_plots_rf_power(df_rf_power_all,output_path,file_number)
    # source, magnet, vacuum
    #get_plots_vacuum(df_vacuum_all,output_path)
    #get_plots_magnet(df_magnet_all,output_path)
    #get_plots_source(df_source_all,output_path)
    #get_plots_ratio(df_ratio_current_all,output_path,target_number)
    #  

if __name__ == "__main__":
    _input_path,_input_path_4,_output_path,target_current = _parse_args()
    main(_input_path,_input_path_4,_output_path,target_current)
