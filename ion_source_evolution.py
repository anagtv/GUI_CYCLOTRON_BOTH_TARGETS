from datetime import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tfs
import os
import pandas as pd
from scipy.optimize import curve_fit

###

def get_logfile_lines(path_file):
    lines = []
    logfile = open(path_file,"r")
    for line in logfile:
         parts = line.split()
         lines.append(
            parts)
    return lines

def get_headers(path_file):
    headers_lines = get_logfile_lines(path_file)
    target_number = (np.array(headers_lines[0])[1])
    date_stamp = (np.array(headers_lines[0])[8])
    site_name = (np.array(headers_lines[1])[2])
    file_number = (np.array(headers_lines[0])[6])
    if len(np.array(headers_lines[0])) == 10: 
        date_stamp = (np.array(headers_lines[0])[8] + "0" + np.array(headers_lines[0])[9] )
    return target_number,date_stamp,site_name,file_number

def get_irradiation_information(path_file):
    irradiation_information = get_logfile_lines(path_file)    
    irradiation_information = irradiation_information[4:]
    return irradiation_information  


def get_data(real_values):
    data_df = pd.DataFrame.from_records(real_values)
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

def get_collimator_parameters(excel_data_df,current):
    collimator_r = excel_data_df.Coll_r_I[excel_data_df['Target_I'].astype(float) > float(current)].astype(float)
    collimator_l = excel_data_df.Coll_l_I[excel_data_df['Target_I'].astype(float) > float(current)].astype(float)
    return collimator_r,collimator_l

def get_source_parameters(excel_data_df,current):
    source_voltage = excel_data_df.Arc_V[excel_data_df['Target_I'].astype(float) > float(current)].astype(float)
    gas_flow = excel_data_df.Gas_flow[excel_data_df['Target_I'].astype(float) > float(current)].astype(float)
    source_current = excel_data_df.Arc_I[excel_data_df['Target_I'].astype(float) > float(current)].astype(float)
    return source_voltage,source_current,gas_flow

def get_subsystems_dataframe_beam(file_df):
    df_column_names_beam = ["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Target_rel","Extraction_losses"]
    collimator_r,collimator_l = get_collimator_parameters(file_df,0) 
    extraction_current = get_extraction_parameters(file_df,0)
    collimator_r_rel = collimator_r/extraction_current*100
    collimator_l_rel = collimator_l/extraction_current*100
    target_rel = (self.target_current)/extraction_current*100
    extraction_losses = (1-(self.target_current+collimator_l+collimator_r)/extraction_current)*100
    df_subsystem_values_beam = [self.time,self.foil_number,extraction_current,collimator_l,self.target_current,collimator_r,collimator_l_rel,collimator_r_rel,target_rel,extraction_losses]
    df_subsystem_beam = pd.concat(df_subsystem_values_beam,axis=1,keys=df_column_names_beam)
    return df_subsystem_beam

def selecting_data(file):
    [target_number,date_stamp,name,file_number] = get_headers(file)
    real_values = get_irradiation_information(file)
    data_df = get_data(real_values) 
    return target_number,date_stamp,name,file_number,data_df

###




def get_transmission(df_isochronism,probe_current):
    foil_current_max_isochronism = np.max(df_isochronism.Foil_I)/probe_current
    transmission = foil_current_max_isochronism
    return transmission


def get_isochronism(data_df):
    maximum_value = float(max(data_df.Magnet_I))
    minimum_value = float(min(data_df.Magnet_I))
    maximum_value_str = str(maximum_value)
    minimum_value_str = str(minimum_value)
    intial_values = data_df.Magnet_I[data_df.Magnet_I == minimum_value_str]
    final_values = data_df.Magnet_I[data_df.Magnet_I == maximum_value_str]
    if len(final_values) == 0: 
        maximum_value = int(max(data_df.Magnet_I))
        maximum_value_str = str(maximum_value)     
    if len(intial_values) == 0:
        minimum_value = int(max(data_df.Magnet_I))
        minimum_value_str = str(minimum_value)
    final_index = data_df.Magnet_I[data_df.Magnet_I == maximum_value_str].index[0]
    intial_index = data_df.Magnet_I[data_df.Magnet_I == minimum_value_str].index[0]
    magnet_current = data_df.Magnet_I.loc[intial_index:final_index].astype(float)
    coll_current_l = data_df.Coll_l_I.loc[intial_index:final_index].astype(float)
    coll_current_r = data_df.Coll_r_I.loc[intial_index:final_index].astype(float)
    target_current = data_df.Target_I.loc[intial_index:final_index].astype(float)
    foil_current = data_df.Foil_I.loc[intial_index:final_index].astype(float)
    df_column_isochronism = ["Magnet_I","Foil_I","Coll_l_I","Target_I","Coll_r_I"]
    df_subsystem_values_beam = [magnet_current,foil_current,coll_current_l,target_current,coll_current_r]
    df_isochronism = pd.concat(df_subsystem_values_beam,axis=1,keys=df_column_isochronism)
    return df_isochronism

folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2019"
#folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2018"
folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2020_borrador/2020_all"
filename_completed = []
for file in os.listdir(folder):
    filename_completed.append(os.path.join(folder,file))

week_list = []
ranges_current = [[24.0,26.0],[49.0,52.0],[79.0,82.0]]
name_list = []
data_stamp_list = []
df_total_information = pd.DataFrame(columns=["SOURCE","FOIL","TARGET","PROBE","DATE","TARGET_FOIL","TRANSMISSION"])
information_complete = []
filename_completed_current = []
for file in filename_completed:
    print (file)
    [target_number,date_stamp,name,file_number,data_df] = selecting_data(file)
    if (np.average(data_df.Target_I.astype(float)) > 10.0):
        filename_completed_current.append(file)
        
transmission_all = []
for file in filename_completed_current:
    [target_number,date_stamp,name,file_number,data_df] = selecting_data(file)
    df_isochronism = get_isochronism(data_df)
    if len(df_isochronism) == 0: 
    	continue
    #probe_current_transmission = data_df.Probe_I.astype(float)[(data_df.Probe_I.astype(float)[data_df.Probe_I.astype(float) > 10].index[-1])]
    probe_current_transmission = np.average((data_df.Probe_I.astype(float)[data_df.Probe_I.astype(float) > 14]))
    transmission = get_transmission(df_isochronism,probe_current_transmission)
    transmission_all.append(transmission)
    date_stamp_format = datetime.strptime(date_stamp, '%Y-%m-%d')
    week_list.append(date_stamp_format.isocalendar()[1])  
    date_format = []
    transmission_all_values = []
    target_current = []
    foil_current = []
    probe_current = []
    source_current = []
    week_list_number = []
    target_to_foil_ratio = []
    for current in ranges_current:
    	transmission_all_values.append(transmission)
    	date_format.append(date_stamp)
    	week_list_number.append(date_stamp_format.isocalendar()[1])
    	target_current.append(np.average(data_df.Target_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
    	foil_current.append(np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
    	target_to_foil_ratio.append(np.average(data_df.Target_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
    	probe_current.append(np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/transmission)
    	if np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/transmission > 500:
    		files_wrong.append(file)
    	source_current.append(np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
    information = {"SOURCE":source_current,"FOIL":foil_current,"TARGET":target_current,"PROBE":probe_current,"TRANSMISSION":transmission_all_values,"DATE":date_format,"WEEK":week_list_number,"TARGET_FOIL":target_to_foil_ratio}
    df_information = pd.DataFrame(information)
    print ("DF INFORMATION")
    print (df_information)
    df_information.dropna()
    if len(df_information)> 2:
        df_total_information = df_total_information.append(df_information.dropna(),ignore_index=False)
        name_list.append(name)
        data_stamp_list.append(date_stamp)
        information_complete.append(information)



ranges_current = [[24.0,26.0],[49.0,52.0],[79.0,82.0]]
#######
df_total_information_all = [df_total_information_2018,df_total_information_2019,df_total_information_2020]
df_total_information_all = [df_total_information]
weeks_2018 = [list(range(28,34,1)),list(range(35,45,1)),list(range(45,48,1))]
weeks_2019 = [list(range(5,14,1)),list(range(14,22,1)),list(range(22,30,1)),list(range(30,38,1)),list(range(38,48,1))]
weeks_2020 = [list(range(6,11,1)),list(range(12,19,1)),list(range(20,27,1)),list(range(28,35,1)),list(range(36,41,1)),list(range(42,49,1))]
files_names_probe = ["probe_performance_2020_1","probe_performance_2020_2","probe_performance_2020_3","probe_performance_2020_4","probe_performance_2020_5","probe_performance_2020_6"]
files_names_source = ["source_performance_2020_1","source_performance_2020_2","source_performance_2020_3","source_performance_2020_4","source_performance_2020_5","source_performance_2020_6"]
for i in range(len(weeks_2020)):
     for df_total_information in df_total_information_all:
         probe_values = {}
         source_values = {}
         for j in range(len(ranges_current)):
             value = "I_"+str(j)
             value_std = "I_"+str(j) + "_STD"
             probe_values[value] = []
             probe_values[value_std] = []
             probe_values["WEEK"] = []
             source_values[value] = []
             source_values[value_std] = []
             source_values["WEEK"] = []
             for week in weeks_2020[i]:
                  if len(df_total_information.PROBE[(df_total_information.WEEK.astype(float) == week) & (df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1]))]) == 0:
                      continue
                  selected_current_probe = (df_total_information.PROBE[(df_total_information.WEEK.astype(float) == week) & (df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1]))])
                  selected_current_source = (df_total_information.SOURCE[(df_total_information.WEEK.astype(float) == week) & (df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1]))])
                  source_values["WEEK"].append(float(week))
                  source_values[value].append(np.average(selected_current_source))
                  source_values[value_std].append(np.std(selected_current_source))
                  probe_values["WEEK"].append(float(week))
                  probe_values[value].append(np.average(selected_current_probe))
                  probe_values[value_std].append(np.std(selected_current_probe))
     dataframe_probe_values = pd.DataFrame(probe_values)
     dataframe_source_values = pd.DataFrame(source_values)
     tfs.write(files_names_probe[i],dataframe_probe_values)
     tfs.write(files_names_source[i],dataframe_source_values)

#popt_values_all = []
#pcov_values_all = []
#for j in range(len(probe_all_values_all)):
popt_values_all = []
pcov_values_all = []
popt_values = []
pcov_values = []
week_values = []
fig, ax = plt.subplots(figsize=(7, 4))
current_names = ["I_0","I_1","I_2"]
current_names_std = ["I_0_STD","I_1_STD","I_2_STD"]
df_cumulative_charge = tfs.read("summary_df_2020_6")
for week in dataframe_probe_values.WEEK:
    source_current_values = []
    source_current_values_std = []
    probe_current_values = []
    probe_current_values_std = []
    week_values.append(week)
    for i in range(len(current_names)):
         source_current_values.append(np.array(getattr(dataframe_source_values,current_names[i])[dataframe_source_values.WEEK == week])[0])
         source_current_values_std.append(np.array(getattr(dataframe_source_values,current_names_std[i])[dataframe_source_values.WEEK == week])[0])
         probe_current_values.append(np.array(getattr(dataframe_probe_values,current_names[i])[dataframe_probe_values.WEEK == week])[0])
         probe_current_values_std.append(np.array(getattr(dataframe_probe_values,current_names_std[i])[dataframe_probe_values.WEEK == week])[0])
    ax.errorbar(source_current_values, probe_current_values, xerr=source_current_values_std, yerr=probe_current_values_std,fmt="o",label=str(i))
    popt, pcov = curve_fit(func, np.array(source_current_values), np.array(probe_current_values), sigma=1./(np.array(probe_current_values_std)*np.array(probe_current_values_std)))
    popt_values.append(popt[0])
    pcov_values.append(pcov[0][0]**0.5)
fit_values = {"WEEK":list(df_cumulative_charge.WEEK),"FIT":popt_values,"FIT_ERROR":pcov_values,"CUMULATIVE_TOTAL":list(df_cumulative_charge.CUMULATIVE_TOTAL)}
dataframe_fit_values = pd.DataFrame(fit_values).reset_index(drop=True)

	#plt.plot(source_all_values[i], func(np.array(source_all_values[i]), *po}

#plt.scatter(weeks,popt_values)
fig, ax = plt.subplots(figsize=(7, 4))
labels = ["2018","2019","2020"]
for i in range(len(popt_values_all)):
      ax.errorbar(range(len(popt_values_all[i])), popt_values_all[i], xerr=0, yerr=pcov_values_all[i],fmt="o",label=labels[i])
plt.legend(loc='best')
plt.show()



fig, ax = plt.subplots(figsize=(7, 4))
ax.errorbar(dataframe_fit_values.CUMULATIVE_TOTAL, dataframe_fit_values.FIT, xerr=0, yerr=dataframe_fit_values.FIT_ERROR,fmt="o")
popt_final, pcov_final = curve_fit(func_2, dataframe_fit_values.CUMULATIVE_TOTAL, dataframe_fit_values.FIT, sigma=1./(dataframe_fit_values.FIT_ERROR*dataframe_fit_values.FIT_ERROR))
plt.plot(dataframe_fit_values.CUMULATIVE_TOTAL, func_2(np.array(dataframe_fit_values.CUMULATIVE_TOTAL), *popt_final))
plt.legend(loc='best')
plt.show()
popt_exp, pcov_exp = curve_fit(func_exp, weeks, popt_values_all[0])



total_irradiation_list_2020 = []
total_irradiation_2020 = 0
for i in range(len(summary_irradiation_2020_second.WEEK)):
     total_irradiation_2020 = total_irradiation + summary_irradiation.IRRADIATION.iloc[i]
     total_irradiation_list_2020.append(total_irradiation_2020) 
total_source_list_2020 = []
source_value_2020 = 0
for source_i in summary_irradiation_2020_second.SOURCE:
    source_value_2020 += source_i
    total_source_list_2020.append(source_value_2020)


def func_exp(x, a, b):
    return a * x**2 + b

def func_exp(x, a, b, c):
    return a * np.exp(-b * x) + c
    
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7, 4))
ax.errorbar(source_ave, probe_ave, xerr=probe_std, yerr=source_std,fmt="^",label="Before")
ax.errorbar(source_ave_after, probe_ave_after, xerr=probe_std_after, yerr=source_std_after,fmt="o",label="After")
popt, pcov = curve_fit(func, source_ave, probe_ave)
popt_after, pcov_after = curve_fit(func, source_ave_after, probe_ave_after)
plt.plot(source_ave_after, func(np.array(source_ave_after), *popt_after),label="After fit")
plt.plot(source_ave, func(np.array(source_ave), *popt),label="Before fit")
plt.legend(loc='best',ncol=2)
plt.show()

def func(x, a):
     return a  * x 

def func_2(x, a,b):
     return a  * x +b

plt.scatter(df_total_information.SOURCE[df_total_information.WEEK.astype(float) == 28.0],df_total_information.PROBE[df_total_information.WEEK.astype(float) == 28.0],label="after")  
  df_source_performance = pd.DataFrame()
transmission = data_df.Target_I.astype(float)[(data_df.Probe_I.astype(float)[data_df.Probe_I.astype(float) > 10].index[-1])+ 1]/data_df.Probe_I.astype(float)[(data_df.Probe_I.astype(float)[data_df.Probe_I.astype(float) > 10].index[-1])]


target_25 = np.average(data_df.Target_I[(data_df.Target_I.astype(float) > 24.0) & (data_df.Target_I.astype(float) < 26.0)].astype(float))
foil_25 = np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > 24.0) & (data_df.Target_I.astype(float) < 26.0)].astype(float))
probe_25 = foil_25/transmission
source_25 = np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > 24.0) & (data_df.Target_I.astype(float) < 26.0)].astype(float))

target_50 = np.average(data_df.Target_I[(data_df.Target_I.astype(float) > 49.0) & (data_df.Target_I.astype(float) < 52.0)].astype(float))
foil_50 = np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > 49.0) & (data_df.Target_I.astype(float) < 52.0)].astype(float))
probe_50 = foil_50/transmission
source_50 = np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > 49.0) & (data_df.Target_I.astype(float) < 52.0)].astype(float))

target_80 = np.average(data_df.Target_I[(data_df.Target_I.astype(float) > 79.0) & (data_df.Target_I.astype(float) < 82.0)].astype(float))
foil_80 = np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > 79.0) & (data_df.Target_I.astype(float) < 82.0)].astype(float))
probe_80 = foil_80/transmission
source_80 = np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > 79.0) & (data_df.Target_I.astype(float) < 82.0)].astype(float))


target_100 = np.average(data_df.Target_I[(data_df.Target_I.astype(float) > 99.0) & (data_df.Target_I.astype(float) < 102.0)].astype(float))

source_100 = np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > 99.0) & (data_df.Target_I.astype(float) < 102.0)].astype(float))
source = [source_25,source_50,source_80,source_100]
target = [foil_25,foil_50,foil_80,target_100]
information = {"SOURCE":source,"FOIL":target}
df_information = pd.DataFrame(information)
df_information.dropna()
if len(df_information.dropna > 2)