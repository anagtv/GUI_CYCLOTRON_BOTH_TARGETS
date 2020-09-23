"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import tfs
import pandas as pd 

# Fixing random state for reproducibility
np.random.seed(19680801)

def get_data_tuple(path_file):
    all_parts = []
    logfile = open(path_file,"r")
    print ("path")
    print (path_file)
    for line in logfile:
         parts = line.split()
         all_parts.append(
            parts)
    target_number = (np.array(all_parts[0])[1])
    date_stamp = (np.array(all_parts[0])[8])
    if len(np.array(all_parts[0])) == 10: 
        date_stamp = (np.array(all_parts[0])[8] + "0" + np.array(all_parts[0])[9] )
    real_values = all_parts[4:]
    return real_values,target_number,date_stamp 

def get_data(real_values):
    #print ("real values here")
    #print (real_values[0])
    data_df = pd.DataFrame.from_records(real_values)
    #print (data_df)
    column_names = ["Time","Arc_I","Arc_V","Gas_flow","Dee_1_kV","Dee_2_kV","Magnet_I","Foil_I","Coll_l_I","Target_I","Coll_r_I","Vacuum_P","Target_P","Delta_Dee_kV","Phase_load","Dee_ref_V","Probe_I","He_cool_P","Flap1_pos","Flap2_pos","Step_pos","Extr_pos","Balance","RF_fwd_W","RF_refl_W","Foil_No"]
    column_names_nf = ["Time","Arc_I","Arc_V","Gas_flow","Dee_1_kV","Dee_2_kV","Magnet_I","Foil_I","Coll_l_I","Target_I","Coll_r_I","Vacuum_P","Target_P","Delta_Dee_kV","Phase_load","Dee_ref_V","Probe_I","He_cool_P","Flap1_pos","Flap2_pos","Step_pos","Extr_pos","Balance","RF_fwd_W","RF_refl_W"]
    try:
       data_df = data_df.drop([0,1,2], axis=0)
    except:
       data_df = data_df.drop([0],axis=0)
    try: 
       data_df.columns = column_names
    except:
       data_df.columns = column_names_nf 
    return data_df


def get_plot_foils():
    elements = ('Foil 1 (1)', 'Foil 2 (1)', 'Foil 3 (1)', 'Foil 4 (1)', 'Foil 5 (1)', 'Foil 6 (1)')
    y_pos = np.arange(len(elements))
    performance = np.array(total_foil_relative_1)
    print ("Before")
    print (performance)
    performance_2 = performance.copy()
    performance_3 = performance.copy()
    performance_index = [i for i, x in enumerate(performance > 90) if x]
    performance_index_2 = [i for i, x in enumerate(performance > 70) if x]
    print (performance_index)
    print (performance_index_2)
    print ("LIST 4")
    print (files_list_4)
    for i in performance_index:
        performance_3[i] = 90
    for i in performance_index_2:
    	performance[i] = 70
    ax.barh(y_pos, performance_2,color=red, align='center')
    ax.barh(y_pos, performance_3,color=yellow, align='center')
    ax.barh(y_pos, performance,color=green, align='center')
    print ("Performance 3")
    print (performance_3)
    print ("Performance 2")
    print (performance_2)
    print ("After")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(elements)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Accumulated Charge relative to maximum values [%]')
    plt.savefig("foils_1_after.pdf")


def get_plot_collimators(sum_total_collimators):
    elements = ('Collimator L 1', 'Collimator U 1', 'Collimator L 2', 'Collimator U 2')
    y_pos = np.arange(len(elements))
    cumulative_charge = np.array(sum_total_collimators)
    print ("Before")
    print (cumulative_charge)
    cumulative_charge_warning = cumulative_charge.copy()
    cumulative_charge_error = cumulative_charge.copy()
    cumulative_charge_error_index = [i for i, x in enumerate(cumulative_charge > 90) if x]
    cumulative_charge_warning_index = [i for i, x in enumerate(cumulative_charge > 70) if x]
    print (files_list_4)
    for i in cumulative_charge_error_index:
        cumulative_charge_warning[i] = 90
    for i in cumulative_charge_warning_index:
    	cumulative_charge[i] = 70
    ax.barh(y_pos, cumulative_charge_error,color=green, align='center')
    #ax.barh(y_pos, cumulative_charge_warning,color=yellow, align='center')
    #ax.barh(y_pos, cumulative_charge,color=green, align='center')
    #print ("Performance 3")
    #print (performance_3)
    #print ("Performance 2")
    #print (performance_2)
    #print ("After")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(elements)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Accumulated Charge [$\mu$A]')
    plt.savefig("collimator_current.pdf")

plt.rcdefaults()
fig, ax = plt.subplots()

COLORS = ['#1E90FF','#FF4500','#32CD32',"#6A5ACD","#20B2AA","#00008B","#A52A2A","#228B22","#FF3300","#3366FF","#FF9933"]

# Example data


#path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/MRS/Information/2020/2020_no_foil/File_iso"
#path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/DIJ/Last_logs/"
path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Logs_counter_all"
path_logs_tcp = ""
logfile_list = []
logfile_list_names = []
for logfile in os.listdir(path_logs):
    logfile_list.append(int(logfile[:-4]))
logfile_list.sort()
for logfile in logfile_list:
    logfile_list_names.append(str(logfile) + ".log")
# Computing irradiation time
total_time_list = []
total_time_list_1 = []
total_time_list_4 = []
# Computing total current in the collimator 
total_current_collimator_lower_1 = []
total_current_collimator_lower_2 = []
total_current_collimator_upper_1 = []
total_current_collimator_upper_2 = []
# Computing total current in the foils
total_foil_1_1 = []
total_foil_1_2 = []
total_foil_1_3 = []
total_foil_1_4 = []
total_foil_1_5 = []
total_foil_1_6 = []
total_foil_2_1 = []
total_foil_2_2 = []
total_foil_2_3 = []
total_foil_2_4 = []
total_foil_2_5 = []
total_foil_2_6 = []
files_list_1 = []
files_list_4 = []
foil_1_1 = []
foil_2_1 = []
foil_3_1 = []
foil_4_1 = []
foil_5_1 = []
foil_6_1 = []
foil_1_4 = []
foil_2_4 = []
foil_3_4 = []
foil_4_4 = []
foil_5_4 = []
foil_6_4 = []
#source 
total_source_1 = []
total_source_4 = []
total_source_all = []
for file in logfile_list_names:
    [real_values,target_number,date_stamp] = get_data_tuple(os.path.join(path_logs,str(file)))
    data_df = get_data(real_values)
    irradiation_time = list(data_df.Time[data_df.Arc_I.astype(float) > 0])
    #print (irradiation_time)
    initial_time = float(irradiation_time[0][0:2])*3600 + float(irradiation_time[0][3:5])*60 + float(irradiation_time[0][6:8])
    final_time = float(irradiation_time[-1][0:2])*3600 + float(irradiation_time[-1][3:5])*60 + float(irradiation_time[-1][6:8])
    total_time = final_time - initial_time
    total_current_source = data_df.Arc_I[data_df.Arc_I.astype(float) > 0].astype(float).sum()
    total_time_list.append(total_time)
    data_collimator_l = data_df.Coll_l_I[data_df.Arc_I.astype(float) > 0].astype(float).sum()
    data_collimator_r = data_df.Coll_r_I[data_df.Arc_I.astype(float) > 0].astype(float).sum()
    foil_current = data_df.Foil_I[data_df.Arc_I.astype(float) > 0].astype(float).sum()
    average_file_number = list(data_df.Foil_No)[-1]
    total_source_all.append(total_current_source)
    if float(target_number[1]) == 1:
         total_current_collimator_lower_1.append(data_collimator_l)
         total_current_collimator_upper_1.append(data_collimator_r)
         total_time_list_1.append(total_time)
         files_list_1.append(file)
         total_source_1.append(total_current_source)
         if average_file_number == "1":
             total_foil_1_1.append(foil_current)
             foil_1_4.append(file)
         elif average_file_number == "2":
             total_foil_1_2.append(foil_current)
             foil_2_4.append(file)
         elif average_file_number == "3":
             total_foil_1_3.append(foil_current)
             foil_3_4.append(file)
         elif average_file_number == "4":
             total_foil_1_4.append(foil_current)
             foil_4_4.append(file)
         elif average_file_number == "5":
             total_foil_1_5.append(foil_current)
             foil_5_1.append(file)
         elif average_file_number == "6":
             total_foil_1_6.append(foil_current)
             foil_6_4.append(file)
    elif float(target_number[1]) == 4:
         total_current_collimator_lower_2.append(data_collimator_l)
         total_current_collimator_upper_2.append(data_collimator_r)
         total_time_list_4.append(total_time)
         files_list_4.append(file)
         total_source_4.append(total_current_source)
         if average_file_number == "1":
             total_foil_2_1.append(foil_current)
             foil_1_4.append(file)
         elif average_file_number == "2":
             total_foil_2_2.append(foil_current)
             foil_2_4.append(file)
         elif average_file_number == "3":
             total_foil_2_3.append(foil_current)
             foil_3_4.append(file)
         elif average_file_number == "4":
             total_foil_2_4.append(foil_current)
             foil_4_4.append(file)
         elif average_file_number == "5":
             total_foil_2_5.append(foil_current)
             foil_5_4.append(file)
         elif average_file_number == "6":
             total_foil_2_6.append(foil_current)
             foil_6_4.append(file)
print ("TARGET 1")
print (total_current_collimator_lower_1)
print (total_current_collimator_upper_1)
print ("COLIMATOR SUM")
print (sum(total_current_collimator_lower_1))
print (sum(total_current_collimator_upper_1))
print ("FOIL")
total_foils_1 = np.array([sum(total_foil_1_1)*3/3600,sum(total_foil_1_2)*3/3600,sum(total_foil_1_3)*3/3600,sum(total_foil_1_4)*3/3600,sum(total_foil_1_5)*3/3600,sum(total_foil_1_6)*3/3600])
total_foils_4 = np.array([sum(total_foil_2_1)*3/3600,sum(total_foil_2_2)*3/3600,sum(total_foil_2_3)*3/3600,sum(total_foil_2_4)*3/3600,sum(total_foil_2_5)*3/3600,sum(total_foil_2_6)*3/3600])
total_foil_relative_1 = total_foils_1/2500
total_foil_relative_4 = total_foils_4/2500
print (total_foils_1)
print (total_foils_4)
#print (sum(total_foil_1_2_1)/2500)
print (total_time_list_1)
print (sum(total_current_collimator_lower_1)*4/3600)
print (sum(total_current_collimator_upper_1)*4/3600)
print (sum(total_time_list_1))
print ("TARGET 1")
print (total_foils_1)
print (total_foils_4)
print (total_time_list_4)
print ("TARGET 4")
print (total_current_collimator_lower_2)
print (total_current_collimator_upper_2)
print (total_time_list_4)
print ("COLIMATOR SUM")
print (sum(total_current_collimator_lower_2))
print (sum(total_current_collimator_upper_2))
print ("FOIL 1")
print (sum(total_foil_1_1))
print ("SOURCE")
print (total_source_all)
print (sum(total_source_all))
print ("SOURCE TOTAL")
print (sum(total_source_all)*3/3600*1/1000)
print (sum(total_source_all)*3/3600*1/1000*1/108.9)
print ("TARGET 1")
print (total_source_1)
print (sum(total_source_1))
print ("TARGET 1 TOTAL")
print (sum(total_source_1)*3/3600*1/1000)
print (sum(total_source_1)*3/3600*1/1000*1/50)
print ("TARGET 4")
print (total_source_4)
print (sum(total_source_4))
print ("TARGET 4 TOTAL")
print (sum(total_source_4)*3/3600*1/1000*1/50)
print (sum(total_source_4)*3/3600*1/1000*1/50)
green = "#329932"
yellow = "#FFDA36"
red = "#FC0202"
sum_total_collimators = [sum(total_current_collimator_lower_1)*3/3600,sum(total_current_collimator_upper_1)*3/3600,sum(total_current_collimator_lower_2)*3/3600,sum(total_current_collimator_upper_2)*3/3600]
get_plot_collimators(sum_total_collimators)

#ax.set_title('')

plt.show()
