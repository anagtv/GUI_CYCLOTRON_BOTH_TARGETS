import sys
sys.path.append("/Users/anagtv/Desktop/GUI_CYCLOTRON_T1T4")
import saving_files_summary_list_20200420
import os
import pandas as pd
import numpy as np
import tfs 
import matplotlib.pyplot as plt

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


def get_start_isochronism(df_isochronism):
    isochronism_initial = list(df_isochronism.Magnet_I)[0]
    return isochronism_initial

def get_end_isochronism(df_isochronism):
    isochronism_final = list(df_isochronism.Magnet_I)[-1]
    return isochronism_final

def get_number_of_steps(df_isochronism):
    number_of_steps = float(len(list(df_isochronism.Magnet_I)))
    return number_of_steps

def get_step_size(df_isochronism):
    step_value = float(list(df_isochronism.Magnet_I)[1]) - float(list(df_isochronism.Magnet_I)[0])
    return step_value 

def main(): 
    COLUMNS_SUMMARY = ["FILE","DATE","INITIAL","FINAL","LENGTH","STEP"]
    COLUMNS_INCREMENT = ["DATE","RELATIVE_INCREMENT","RELATIVE_INCREMENT_FINAL"]
    df_isochronism_summary = pd.DataFrame(columns=COLUMNS_SUMMARY)
    df_isochronism_increase = pd.DataFrame(columns=COLUMNS_INCREMENT)
    #path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/MRS/Information/2020/2020_no_foil/File_iso"
    path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/DIJ/Last_logs/"
    #path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/DIJ/Logs_20200914/Logs/"
    #path_logs = "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Logs_mayo_julio/"
    path_logs_tcp = ""
    logfile_list = []
    logfile_list_names = []
    for logfile in os.listdir(path_logs):
        logfile_list.append(int(logfile[:-4]))
    logfile_list.sort()
    for logfile in logfile_list:
       logfile_list_names.append(str(logfile) + ".log")
    for file in logfile_list_names:
        try: 
            [real_values,target_number,date_stamp] = get_data_tuple(os.path.join(path_logs,str(file)))
            data_df = get_data(real_values)
            df_isochronism = saving_files_summary_list_20200420.get_isochronism(data_df)
            isochronism_initial = get_start_isochronism(df_isochronism)
            isochronism_final = get_end_isochronism(df_isochronism)
            number_of_steps = get_number_of_steps(df_isochronism)
            step_value  = get_step_size(df_isochronism)  
            print (date_stamp)   
            isochronism_summary_list = [[file,date_stamp,isochronism_initial,isochronism_final,number_of_steps,step_value]] 
            df_isochronism_summary_i = pd.DataFrame((isochronism_summary_list),columns=COLUMNS_SUMMARY) 
            df_isochronism_summary = df_isochronism_summary.append(df_isochronism_summary_i,ignore_index=True)
        except:
             print (file)
    dates_unique = (df_isochronism_summary.drop_duplicates(subset='DATE'))
    print (dates_unique)
    print (dates_unique.DATE)
    delta_magnet_all = []
    for date_unique in dates_unique.DATE:
         df_isochronism_summary_initial = list(df_isochronism_summary.INITIAL[df_isochronism_summary.DATE == date_unique])
         df_isochronism_summary_final = list(df_isochronism_summary.FINAL[df_isochronism_summary.DATE == date_unique])
         magnet_current_day =  (df_isochronism_summary_initial)
         magnet_current_day_initial =  (df_isochronism_summary_initial[0])
         magnet_current_day_final =  (df_isochronism_summary_initial[-1])
         delta_magnet = (magnet_current_day_final - magnet_current_day_initial)/len(magnet_current_day)
         delta_magnet_final = (df_isochronism_summary_final[-1]-df_isochronism_summary_final[0])/len(magnet_current_day)
         isochronism_increase_list = [[date_unique,delta_magnet,delta_magnet_final]] 
         df_isochronism_increase_i = pd.DataFrame((isochronism_increase_list),columns=COLUMNS_INCREMENT) 
         df_isochronism_increase = df_isochronism_increase.append(df_isochronism_increase_i,ignore_index=True)
         delta_magnet_all.append(delta_magnet)
    print (delta_magnet_all)
    print (df_isochronism_increase)
    df_isochronism_increase_tcp = tfs.read("magnet_increment_TCP.out")
    df_isochronism_increase_mrs = tfs.read("magnet_increment_MRS.out")
    #df_isochronism_summary.agg(['min', 'max', 'mean', 'std']).round(decimals=2)
    #fig, ax = plt.subplots()
    #df_isochronism_summary.INITIAL.plot.kde(ax=ax, legend=False, title='Histogram: A vs. B')
    #df_isochronism_increase_tcp.RELATIVE_INCREMENT.plot.hist(bins=20,density=1,rwidth=0.9,ax=ax,label="TCP")
    #df_isochronism_increase_mrs.RELATIVE_INCREMENT.plot.hist(bins=20,density=1,rwidth=0.9,ax=ax,label="MRS")
    #df_isochronism_increase.RELATIVE_INCREMENT.plot.hist(bins=20,density=1,rwidth=0.9, ax=ax,label="DIJ")
    #ax.legend(loc=1)
    #ax.set_ylabel('Probability')
    #ax.grid(axis='y')
    tfs.write("magnet_test_DIJ_2.out", df_isochronism_summary)
    tfs.write("magnet_increment_DIJ_2.out",df_isochronism_increase)
    #fig.savefig("histogram_DIJ.pdf")

    

if __name__ == "__main__":
    main()