import pandas as pd
import numpy as np
import os
from datetime import datetime
import tfs


class target_information:
    def __init__(self):
        self.foil_individual = []
        self.foil_total = []
        self.target_number_list = []
        self.coll_l_current = []
        self.target_current = []
        self.coll_r_current = []
        self.ion_source_current = []
        self.date_stamp = []
        self.vacuum_ave = []
        self.vacuum_std = [] 
        self.irradiation_length = []
    def selecting_data_to_plot_reset(self,file_df,target,date_stamp_i):
        self.date_stamp.append(date_stamp_i)     
        self.foil_individual.append(getattr(file_df,"Foil_I").astype(float).sum()*3/3600)
        self.coll_l_current.append(getattr(file_df,"Coll_l_I").astype(float).sum()*3/3600)
        self.target_current.append(getattr(file_df,"Target_I").astype(float).sum()*3/3600)
        self.coll_r_current.append(getattr(file_df,"Coll_r_I").astype(float).sum()*3/3600)
        self.ion_source_current.append(getattr(file_df,"Arc_I").astype(float).sum()*3/3600)
        self.foil_total.append(file_df.Foil_No.iloc[-1])
        self.target_number_list.append(int(target[1]))
        self.vacuum_ave.append(np.average(getattr(file_df,"Vacuum_P").astype(float)*1e5))
        self.vacuum_std.append(np.std(getattr(file_df,"Vacuum_P").astype(float)*1e5))
        starting = datetime.strptime(file_df.Time.iloc[0], '%H:%M:%S')
        ending = datetime.strptime(file_df.Time.iloc[-1], '%H:%M:%S')
        self.irradiation_length.append((ending-starting).seconds)


class rf_information:
    def __init__(self):
        self.rf_voltage_dee1 = []
        self.rf_voltage_dee2 = []
        self.rf_power_fwd = []
        self.rf_power_reflected = []
        self.date_stamp = []
        self.target_number_list = []
    def selecting_data(self,file_df,target,date_stamp_i):
        self.date_stamp.append(date_stamp_i)
        self.target_number_list.append(int(target[1]))
        self.rf_voltage_dee1.append(np.average(getattr(file_df,"Dee_1_kV").astype(float)))
        self.rf_voltage_dee2.append(np.average(getattr(file_df,"Dee_2_kV").astype(float)))
        self.rf_power_fwd.append(np.average(getattr(file_df,"RF_fwd_W").astype(float)))
        self.rf_power_reflected.append(np.average(getattr(file_df,"RF_refl_W").astype(float)))

class ion_source_vacuum_transmission:
    def __init__(self):
        self.gas_flow = []
        self.current_value = []
        self.source_performance = []
        self.transmission = []
        self.date_stamp = []
        self.target_number_list = []
        self.target_current_inst = []
        self.probe_current_inst = []
    def selecting_data(self,file_df,target,date_stamp_i):
        transmission_ave = file_df.Target_I.astype(float)[(file_df.Probe_I.astype(float)[file_df.Probe_I.astype(float) > 10].index[-1])+ 1]/file_df.Probe_I.astype(float)[(file_df.Probe_I.astype(float)[file_df.Probe_I.astype(float) > 10].index[-1])]
        self.target_current_inst.append(np.average(file_df.Target_I.astype(float)))
        self.probe_current_inst.append(np.average(file_df.Target_I.astype(float))/transmission_ave)
        self.target_number_list.append(int(target[1]))
        self.date_stamp.append(date_stamp_i)
        self.gas_flow.append(np.average(file_df.Gas_flow.astype(float)))
        self.current_value.append(np.average(file_df.Arc_I.astype(float)))
        self.source_performance.append(np.average(file_df.Arc_I[(file_df.Probe_I.astype(float) > 10) & (file_df.Probe_I.astype(float) < 20)].astype(float)/file_df.Probe_I[(file_df.Probe_I.astype(float) > 10) & (file_df.Probe_I.astype(float) < 20)].astype(float)))
        self.transmission.append(transmission_ave)

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

def cumulative_charge_individual(df_information,target,atributes,columns_write):  
    for i in range(len(columns_write)):
        df_information[columns_write[i]] = getattr(target,atributes[i])
    return df_information


def cumulative_charge_folder(target):
    #time_period = [['2016-01-01','2016-04-31'],['2016-05-01','2016-08-31'],['2016-09-01','2016-12-31'],['2017-01-01','2017-04-31'],['2017-05-01','2017-08-31'],['2017-09-01','2017-12-31'],['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31']]
    #time_period_names = ['2016_1','2016_2','2016_3','2017_1','2017_2','2017_3','2018_1','2018_2','2018_3']
    time_period = [['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31'],['2019-01-01','2019-04-31'],['2019-05-01','2019-08-31'],['2019-09-01','2019-12-31'],['2020-01-01','2020-04-31'],['2020-09-01','2020-12-31'],['2021-01-01','2021-04-31']]
    time_period_names = ['2018_1','2018_2','2018_3','2019_1','2019_2','2019_3','2020_1','2020_3','2021_1']
    df_information = pd.DataFrame(columns=["DATE","FOIL","TARGET","CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R","VACUUM","IRRADIATION"])
    atributes = ['date_stamp','foil_individual','target_number_list', 'ion_source_current','foil_total', 'coll_l_current', 'coll_r_current','target_current','vacuum_ave','vacuum_std',"irradiation_length"]
    columns_write = ["DATE","FOIL","TARGET","CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R","VACUUM","VACUUM_STD","IRRADIATION"] 
    total_ion_source_current= []
    total_target_current = []
    target_list = []
    total_names = []
    number_files = []
    total_vacuum = []
    total_vacuum_std = []
    total_irradiation = []
    max_current_target = []
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
    for i in range(len(time_period)):
        df_information_month = df_information[(df_information['DATE'] > time_period[i][0]) & (df_information['DATE'] < time_period[i][1])]
        for target_number in targets_numbers:
            df_information_target = df_information_month[df_information_month.TARGET  == target_number]
            total_ion_source_current.append(df_information_target.CURRENT_SOURCE.sum())
            total_target_current.append(df_information_target.CURRENT_TARGET.sum())
            total_irradiation.append(df_information_target.IRRADIATION.sum())
            target_list.append(target_number)
            total_names.append(time_period_names[i])
            number_files.append(len(df_information_target))
            total_vacuum.append(np.average(df_information_target.VACUUM))
            total_vacuum_std.append(np.std(df_information_target.VACUUM_STD))
            #max_current_target.append(np.max(df_information_target.TARGET_I))
    df = pd.DataFrame(list(zip(target_list,number_files,total_target_current,total_ion_source_current,total_names,total_vacuum,total_vacuum_std,total_irradiation)),columns=["TARGET","NUMBER","TARGET_TOTAL","SOURCE","TIME_INT","VACUUM","VACUUM_STD","IRRADIATION"])
    df_sorted_target_1 = df[df.TARGET == 2].sort_values(by=['TIME_INT'])
    df_sorted_target_4 = df[df.TARGET == 5].sort_values(by=['TIME_INT'])
    return (df,df_sorted_target_1,df_sorted_target_1)


def average_rf_folder(target):
    #time_period = [['2016-01-01','2016-04-31'],['2016-05-01','2016-08-31'],['2016-09-01','2016-12-31'],['2017-01-01','2017-04-31'],['2017-05-01','2017-08-31'],['2017-09-01','2017-12-31'],['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31']]
    #time_period_names = ['2016_1','2016_2','2016_3','2017_1','2017_2','2017_3','2018_1','2018_2','2018_3']
    time_period = [['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31'],['2019-01-01','2019-04-31'],['2019-05-01','2019-08-31'],['2019-09-01','2019-12-31'],['2020-01-01','2020-04-31'],['2020-09-01','2020-12-31'],['2021-01-01','2021-04-31']]
    time_period_names = ['2018_1','2018_2','2018_3','2019_1','2019_2','2019_3','2020_1','2020_3','2021_1']
    average_rf_voltage_dee_1 = []
    average_rf_voltage_dee_2 = []
    average_rf_power_fwd = []
    average_rf_power_reflected = []
    total_names = []
    number_files = []
    target_list = []
    df_information = pd.DataFrame(columns=["DATE","TARGET","DEE_1","DEE_2","RF_FWD","RF_RFL"] )
    columns_write = ["DATE","TARGET","DEE_1","DEE_2","RF_FWD","RF_RFL"] 
    atributes = ['date_stamp','target_number_list','rf_voltage_dee1','rf_voltage_dee2','rf_power_fwd','rf_power_reflected']
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    print ("DF INFORMATION")
    print (df_information)
    targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
    for i in range(len(time_period)):
        df_information_month = df_information[(df_information['DATE'] > time_period[i][0]) & (df_information['DATE'] < time_period[i][1])]
        for target_number in targets_numbers:
            df_information_target = df_information_month[df_information_month.TARGET  == target_number]
            target_list.append(target_number)
            total_names.append(time_period_names[i])
            number_files.append(len(df_information_target))
            average_rf_voltage_dee_1.append(np.average(df_information_target.DEE_1))
            average_rf_voltage_dee_2.append(np.average(df_information_target.DEE_2))
            average_rf_power_fwd.append(np.average(df_information_target.RF_FWD))
            average_rf_power_reflected.append(np.average(df_information_target.RF_RFL))
    df = pd.DataFrame(list(zip(target_list,number_files,total_names,average_rf_voltage_dee_1,average_rf_voltage_dee_2,average_rf_power_fwd,average_rf_power_reflected)),columns=["TARGET","NUMBER","TIME_INT","DEE_1","DEE_2","RF_FWD","RF_RFL"])
    df_sorted_target_1 = df[df.TARGET == 1].sort_values(by=['TIME_INT'])
    df_sorted_target_4 = df[df.TARGET == 4].sort_values(by=['TIME_INT'])
    return (df,df_sorted_target_1,df_sorted_target_1)

def average_ion_source_folder(target):
    #time_period = [['2016-01-01','2016-04-31'],['2016-05-01','2016-08-31'],['2016-09-01','2016-12-31'],['2017-01-01','2017-04-31'],['2017-05-01','2017-08-31'],['2017-09-01','2017-12-31'],['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31']]
    #time_period_names = ['2016_1','2016_2','2016_3','2017_1','2017_2','2017_3','2018_1','2018_2','2018_3']
    time_period = [['2018-01-01','2018-04-31'],['2018-05-01','2018-08-31'],['2018-09-01','2018-12-31'],['2019-01-01','2019-04-31'],['2019-05-01','2019-08-31'],['2019-09-01','2019-12-31'],['2020-01-01','2020-04-31'],['2020-09-01','2020-12-31'],['2021-01-01','2021-04-31']]
    time_period_names = ['2018_1','2018_2','2018_3','2019_1','2019_2','2019_3','2020_1','2020_3','2021_1']
    average_gas_flow = [] 
    average_current_value = []
    average_transmission = []
    average_current_target = []
    average_current_probe = []
    total_names = []
    number_files = []
    target_list = []
    average_source_performance = []
    df_information = pd.DataFrame(columns=["DATE","TARGET","GAS_FLOW","CURRENT_SOURCE_AVE","CURRENT_TARGET_AVE","SOURCE_PERFORMANCE","TRANSMISSION","PROBE"])
    columns_write = ["DATE","TARGET","GAS_FLOW","CURRENT_SOURCE_AVE","CURRENT_TARGET_AVE","SOURCE_PERFORMANCE","TRANSMISSION","PROBE"] 
    atributes = ['date_stamp','target_number_list','gas_flow','current_value','target_current_inst','source_performance','transmission','probe_current_inst']
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    print ("DF INFORMATION")
    print (df_information)
    targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
    for i in range(len(time_period)):
        df_information_month = df_information[(df_information['DATE'] > time_period[i][0]) & (df_information['DATE'] < time_period[i][1])]
        print ("DF MONTH")
        print (df_information_month)
        for target_number in targets_numbers:
            df_information_target = df_information_month[df_information_month.TARGET  == target_number]
            print (np.array(df_information_target.PROBE))
            print (np.average(df_information_target.PROBE[df_information_target.PROBE.astype(float) < 500]))
            target_list.append(target_number)
            total_names.append(time_period_names[i])
            number_files.append(len(df_information_target))
            average_gas_flow.append(np.average(df_information_target.GAS_FLOW))
            average_current_value.append(np.average(df_information_target.CURRENT_SOURCE_AVE))
            average_current_target.append(np.average(df_information_target.CURRENT_TARGET_AVE))
            average_source_performance.append(np.average(df_information_target.SOURCE_PERFORMANCE))
            average_transmission.append(np.average(df_information_target.TRANSMISSION))
            average_current_probe.append(np.average(np.average(df_information_target.PROBE[df_information_target.PROBE.astype(float) < 500])))
    df = pd.DataFrame(list(zip(target_list,number_files,total_names,average_gas_flow,average_current_value,average_current_target,average_transmission,average_source_performance,average_current_probe)),columns=["TARGET","NUMBER","TIME_INT","GAS_FLOW","CURRENT_SOURCE_AVE","CURRENT_TARGET_AVE","TRANSMISSION_AVE","SOURCE_PERFORMANCE","CURRENT_PROBE_AVE"])
    df_sorted_target_1 = df[df.TARGET == 2].sort_values(by=['TIME_INT'])
    df_sorted_target_4 = df[df.TARGET == 5].sort_values(by=['TIME_INT'])
    return (df,df_sorted_target_1,df_sorted_target_1)

def get_correlation(corr_df_total,data_df,file,vacuum_fault_files):
    data_df_not_zero = data_df[data_df.Arc_I != "0"]
    data_test = pd.DataFrame(list(zip(data_df_not_zero.Vacuum_P.astype(float)*1e5,data_df_not_zero.Arc_I.astype(float),data_df_not_zero.Target_I.astype(float),data_df_not_zero.Magnet_I.astype(float),
    data_df_not_zero.Coll_l_I.astype(float),data_df_not_zero.Coll_r_I.astype(float))),columns=["VACUUM","CURRENT","TARGET","MAGNET","COLLL","COLLR"])  
    if np.max(data_test.VACUUM) > 2.5:
       print (file)
       print ("SUMMARY VACUUM")
       print (np.average(data_test.VACUUM))
       print (np.max(data_test.VACUUM))
       print (np.std(data_test.VACUUM))
       vacuum_fault_files.append(file[106:])
    corr_df_total.append(data_test.corr())
    return vacuum_fault_files

def get_rf_parameters_sparks(data_df,source_current):
    data_df_sparks = data_df[data_df.Arc_I.astype(float) > float(source_current)]
    return data_df_sparks

def getting_sparks(data_df,voltage_limit):
    voltage_dee = data_df.Dee_1_kV[data_df.Dee_1_kV.astype(float) < float(voltage_limit)]
    voltage_dee_len = len(voltage_dee)
    return (voltage_dee,voltage_dee_len)

def main():
    #folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/2016_2017_2018"
    folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2018_2019_2020_2021"
    #folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2021"
    filename_completed = []
    for file in os.listdir(folder):
         filename_completed.append(os.path.join(folder,file))
    #time_period_names = ['2016_1','2016_2','2016_3','2017_1','2017_2','2017_3','2018_1','2018_2','2018_3']
    time_period_names = ['2018_1','2018_2','2018_3','2019_1','2019_2','2019_3','2020_1','2020_2','2020_3']
    pre_irradiations = []
    empty_irradiations = []
    target = target_information()
    target_pre = target_information()
    target_empty = target_information()
    rf_summary = rf_information()
    ion_source_summary = ion_source_vacuum_transmission()
    corr_df_total = []
    vacuum_fault_files = []
    sparks_fault_files = []
    ion_source_fault_files = []
    collimator_fault_files = []
    vacuum_high_files = []
    sparks_high_files = []
    ion_source_high_files = []
    collimator_high_files = []
    day_irradiations = []
    total_files = []
    possible_test = []
    week_list = []
    irradiation_length = []
    for file in filename_completed:
        print ("file")
        print (file)
        [target_number,date_stamp,name,file_number,data_df] = selecting_data(file)
        if (np.average(data_df.Target_I.astype(float)) < 50.0):
            if (np.max(data_df.Target_I.astype(float)) == 0.0):
                empty_irradiations.append(file) 
                target_empty.selecting_data_to_plot_reset(data_df,target_number,date_stamp)
                if np.max(data_df.Vacuum_P.astype(float)) > 2.5:
                    print ("HIGH VACUUM")
                    print (file)
            else: 
                pre_irradiations.append(file)
                if np.max(data_df.Vacuum_P.astype(float)) > 2.5:
                    print ("HIGH VACUUM")
                    print (file)
                target_pre.selecting_data_to_plot_reset(data_df,target_number,date_stamp)
        else: 
            starting = datetime.strptime(data_df.Time.iloc[0], '%H:%M:%S')
            ending = datetime.strptime(data_df.Time.iloc[1], '%H:%M:%S')
            if (starting > datetime.strptime("11:00:00", '%H:%M:%S') and starting < datetime.strptime("20:00:00", '%H:%M:%S')): 
                possible_test.append(file[106:])
            else:
                date_stamp_format = datetime.strptime(date_stamp, '%Y-%m-%d')
                week_list.append(date_stamp_format.isocalendar()[1])
                vacuum_fault_files = get_correlation(corr_df_total,data_df,file,vacuum_fault_files)
                target.selecting_data_to_plot_reset(data_df,target_number,date_stamp)
                rf_summary.selecting_data(data_df,target_number,date_stamp)
                ion_source_summary.selecting_data(data_df,target_number,date_stamp)
                # maximum 
                max_source_current = np.max(data_df.Arc_I.astype(float))
                max_source_current_len = len(data_df[data_df.Arc_I.astype(float) > 700])/len(data_df)
                max_current_collimator_l = np.max(data_df.Coll_l_I.astype(float))
                max_current_collimator_r = np.max(data_df.Coll_r_I.astype(float))
                source_current = 0.75*max_source_current
                voltage_limit = 0.8*np.average(data_df.Dee_1_kV.astype(float))
                data_df_sparks = get_rf_parameters_sparks(data_df,source_current)
                [voltage_dee,voltage_dee_len] = getting_sparks(data_df_sparks,voltage_limit)
                if voltage_dee_len >= 1:
                    sparks_fault_files.append(file[106:])
                if (max_source_current > 700.0):
                    ave_target_current = np.average(data_df.Target_I[data_df.Arc_I.astype(float) > 700].astype(float))
                    if (ave_target_current < 0.8*np.max(data_df.Target_I.astype(float))):
                        ion_source_fault_files.append(file[106:])
                    else: 
                        ion_source_high_files.append(file[106:])
                if (max_current_collimator_r > 15.0 or max_current_collimator_l > 15.0):
                    ave_target_current = np.average(data_df.Target_I[(data_df.Coll_r_I.astype(float) > 15.0)].astype(float))
                    if (ave_target_current < 0.8*np.max(data_df.Target_I.astype(float))):
                        collimator_fault_files.append(file[106:])
                    else: 
                        collimator_high_files.append(file[106:])
    print (ion_source_summary.target_number_list)
    print (ion_source_summary.gas_flow)
    [df_ion_source,df_sorted_target_1_ion_source,df_sorted_target_4_ion_source] = average_ion_source_folder(ion_source_summary)
    [df,df_sorted_target_1,df_sorted_target_4] = cumulative_charge_folder(target)
    [df_rf,df_sorted_target_1_rf,df_sorted_target_4_rf] = average_rf_folder(rf_summary)
    print ("DATA ########################")
    print (df)
    print (df_rf)
    print (df_ion_source)
    tfs.write("test_df_ion_source", df_ion_source)
    [df_pre,df_sorted_target_1_pre,df_sorted_target_4_pre] = cumulative_charge_folder(target_pre)
    print (df_pre)
    [df_empty,df_sorted_target_1_empty,df_sorted_target_4_empty] = cumulative_charge_folder(target_empty)
    print (df_empty)
    print ("FAULTS")
    print (vacuum_fault_files)
    print (sparks_fault_files)
    print (ion_source_fault_files)
    print (ion_source_high_files)
    print (collimator_fault_files)
    print (collimator_high_files)
    print ("TESTS")
    print (possible_test)
    print ("WEEKS")
    print (week_list)
    print ("NUMBER OF IRRADIATIONS")
    print (len(week_list))
    print ("NUMBER OF FAULTS")
    print (len(vacuum_fault_files))
    print (len(sparks_fault_files))
    print (len(ion_source_fault_files))
    print (len(collimator_fault_files))

if __name__ == "__main__":
    main()
