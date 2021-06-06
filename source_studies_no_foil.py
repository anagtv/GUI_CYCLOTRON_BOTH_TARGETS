import pandas as pd
import numpy as np
import os
from datetime import datetime
import tfs
from scipy.optimize import curve_fit


class cumulative_charge:
    def __init__(self):
        self.target_current = 0
        self.foil_individual_1 = 0
        self.foil_individual_2 = 0
        self.foil_individual_3 = 0
        self.foil_individual_4 = 0
        self.foil_individual_5 = 0
        self.foil_individual_6 = 0
    def cumluative_charge_calculation(self,previous_value,generic):
        print ("HEREEEE")
        generic = previous_value

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
        self.irradiation_length = []
        self.week = []
        self.file_number = []
        #self.extraction_losses = []
    def selecting_data_to_plot_reset(self,file_df,target,date_stamp_i,week,file_number):
        self.date_stamp.append(date_stamp_i)     
        self.week.append(week)
        self.file_number.append(float(file_number))
        self.foil_individual.append(getattr(file_df,"Foil_I").astype(float).sum()*3/3600)
        self.coll_l_current.append(getattr(file_df,"Coll_l_I").astype(float).sum()*3/3600)
        self.target_current.append(getattr(file_df,"Target_I").astype(float).sum()*3/3600)
        self.coll_r_current.append(getattr(file_df,"Coll_r_I").astype(float).sum()*3/3600)
        self.ion_source_current.append(getattr(file_df,"Arc_I").astype(float).sum()*3/3600)
        #extraction_losses_values = (getattr(file_df,"Foil_I").astype(float)-getattr(file_df,"Coll_l_I").astype(float)+getattr(file_df,"Target_I").astype(float)+getattr(file_df,"Coll_r_I").astype(float))/getattr(file_df,"Foil_I").astype(float)
        #self.extraction_losses.append(extraction_losses_values)
        self.foil_total.append(file_df.Foil_No.iloc[-1])
        self.target_number_list.append(int(target[1]))
        starting = datetime.strptime(file_df.Time.iloc[0], '%H:%M:%S')
        ending = datetime.strptime(file_df.Time.iloc[-1], '%H:%M:%S')
        self.irradiation_length.append((ending-starting).seconds)

class cyclotron:
    def __init__(self):
        self.gas_flow = []
        self.rf = []
        self.rf_power = []
        self.vacuum = []
        self.week = []
        self.vacuum_ave = []
        self.vacuum_std = [] 
        self.date_stamp = []
        self.target_number_list = []
        self.target_current = []
        self.target_volume = []
        self.pressure_initial_all = []
        self.pressure_final_all = []
        self.file_number = []
        self.source_current = []
    def selecting_data(self,file_df,target,date_stamp_i,week,file):
        self.date_stamp.append(date_stamp_i)  
        self.week.append(week)
        self.target_number_list.append(int(target[1]))
        max_current = np.max(file_df.Target_I.astype(float))
        self.target_current.append(np.average(file_df.Target_I[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)))
        self.source_current.append(np.average(file_df.Arc_I[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)))
        print ("VACUUM")
        vacuum = file_df.Vacuum_P[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)
        self.vacuum_ave.append(np.average(vacuum.astype(float)*1e5))
        self.vacuum_std.append(np.std(vacuum.astype(float)*1e5))
        print ("GAS FLOW")
        self.gas_flow.append(np.max(file_df.Gas_flow[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)))
        print ("RF VOLTAGE")
        self.rf.append(np.max(file_df.Dee_1_kV[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)))
        print ("RF POWER")
        self.rf_power.append(np.max(file_df.RF_fwd_W[file_df.Target_I.astype(float) > 0.7*(max_current)].astype(float)))
        pressure_initial = np.min(file_df.Target_P.astype(float)[0:np.min(file_df.Target_P[file_df.Target_P.astype(float) > 400].index)])
        pressure_final = file_df.Target_P.astype(float)[np.min(file_df.Target_P[file_df.Target_P.astype(float) > 400].index)]
        print ("PRESSSURE")
        print (pressure_final)
        print (file_df.Target_P.astype(float).iloc[np.min(file_df.Target_P[file_df.Target_P.astype(float) > 400].index)-5])
        print (pressure_initial)
        print ((pressure_final-pressure_initial)/pressure_final)
        self.pressure_initial_all.append(pressure_initial)
        self.pressure_final_all.append(pressure_final)
        self.target_volume.append((pressure_final-pressure_initial)/pressure_final)
        self.file_number.append(file)

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


def selecting_data(file):
    [target_number,date_stamp,name,file_number] = get_headers(file)
    real_values = get_irradiation_information(file)
    data_df = get_data(real_values) 
    return target_number,date_stamp,name,file_number,data_df

def cumulative_charge_individual(df_information,target,atributes,columns_write):  
    for i in range(len(columns_write)):
        print (atributes[i])
        print (getattr(target,atributes[i]))
        df_information[columns_write[i]] = getattr(target,atributes[i])
    return df_information


def cumulative_charge_folder(target):
    #week_period = [[0, 52]]
    columns_write = ["DATE","WEEK","CURRENT_SOURCE","TARGET_CURRENT","IRRADIATION"]
    df_information = pd.DataFrame(columns=columns_write)
    atributes = ['date_stamp', 'week','ion_source_current','target_current',"irradiation_length"]
    total_ion_source_current= []
    total_target_current = []
    number_files = []
    total_irradiation = []
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    week_list = []
    df_information_maintenance_filter = df_information.drop_duplicates(subset="WEEK", keep='first', inplace=False).sort_values(by="WEEK")
    for week_i in df_information_maintenance_filter.WEEK:
        df_information_month = df_information[(df_information['WEEK'] == week_i)]
        week_list.append(float(df_information_month.WEEK.iloc[1]))
        total_ion_source_current.append(float(df_information_month.CURRENT_SOURCE.sum()))
        total_irradiation.append(float(df_information_month.IRRADIATION[df_information_month.TARGET_CURRENT.astype(float)>65.0].sum()))
        number_files.append(float(len(df_information_month)))
        #max_current_target.append(np.max(df_information_target.TARGET_I))
    df = pd.DataFrame(list(zip(number_files,week_list,total_ion_source_current,total_irradiation)),columns=["NUMBER","WEEK","SOURCE","IRRADIATION"])
    return (df)

def cumulative_charge_target_collimators(target):
    columns_write = ["FILE","DATE","WEEK","TARGET_NO","FOIL_NO","FOIL_CURRENT","CURRENT_COLL_L","TARGET","CURRENT_COLL_R","IRRADIATION"]
    df_information = pd.DataFrame(columns=columns_write)
    atributes = ['file_number','date_stamp', 'week','target_number_list','foil_total','foil_individual','coll_l_current', 'target_current' ,'coll_r_current',"irradiation_length"]    
    total_collimator_l = []
    total_collimator_r = []
    total_target_current = []
    week_list = []
    target_number_list = []
    number_files = []
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
    total_current_week_target_list = []
    total_current_week_collimator_l_list = []
    total_current_week_collimator_r_list = [] 
    total_current_weel_total_collimator_list = []   
    foil_number_list = []
    total_foil = []
    foil_list = []
    total_foil_list = []
    date_list = []
    for target_number in targets_numbers:
        total_current_week_target = 0      
        print ("DF INFORMATION")  
        df_information_target = df_information[(df_information['TARGET_NO'] == target_number)].sort_values(by="FILE").reset_index(drop=True)
        print (df_information_target)
        position = []
        datos_selected = []
        datos = np.array(df_information_target.FOIL_NO.reset_index(drop=True))
        for i in range(len(datos)-1):
            if (float(datos[i]) == float(datos[i+1])-1) or (float(datos[i]) == float(datos[i+1]) or (float(datos[i]) == float(datos[i+1])+1)):
               print ("OK")
            else:
               print ("NOT OK")
               print (datos[i+1])
               datos_selected.append(datos[i+1])
               position.append(i+1)
        information = pd.DataFrame(list(zip(datos_selected,position)),columns=["DATOS","POSITION"])
        if len(information[information.DATOS == "1"]) == 0: 
            week_maintenace = df_information_target.WEEK.loc[0]-1
            print ("NO RESTART")
        else:
            print ("RESTART")
            week_index = np.array(information.POSITION[information.DATOS == "1"])
            print (week_index)
            week_maintenace = np.array(df_information_target.WEEK.loc[week_index])
            print (week_maintenace)
        df_information_maintenance_filter_foil = df_information_target.drop_duplicates(subset="FOIL_NO", keep='first', inplace=False)       
        print ("WEEK MAINTENANCE")
        print (week_maintenace)
        print ("FOILL")
        print (df_information_maintenance_filter_foil.FOIL_NO)
        total_current_week_collimator_l = 0
        total_current_week_collimator_r = 0
        for foil_i in df_information_maintenance_filter_foil.FOIL_NO:
            print ("FOIL!!!!")
            print (foil_i)
            df_information_target_foil = df_information_target[(df_information_target['FOIL_NO'] == foil_i)]
            print ("RESULT")
            print (df_information_target)
            df_information_maintenance_filter = df_information_target_foil.drop_duplicates(subset="DATE", keep='first', inplace=False).sort_values(by="DATE")
            total_foil_week = 0
            for date_i in df_information_maintenance_filter.DATE:
                foil_list.append(foil_i)
                target_number_list.append(float(target_number))
                foil_number_list.append(float(foil_i))
                print ("DATEEEEEE")
                df_information_month_target = df_information_target_foil[(df_information_target_foil['DATE'] == date_i)]
                print (df_information_month_target)
                week_list.append(np.array(df_information_month_target.WEEK)[0])
                date_list.append(str(date_i))
                print ("WEEEEEEK")
                print (df_information_month_target.WEEK.iloc[0])
                print (df_information_month_target.WEEK.iloc[0] == week_maintenace)
                if (df_information_month_target.WEEK.iloc[0] == week_maintenace): 
                    total_current_week_target = 0
                    total_current_week_collimator_l = 0
                    total_current_week_collimator_r = 0
                    total_foil_week = 0
                total_current_week_target += float(df_information_month_target.TARGET.sum())
                total_current_week_collimator_l += float(df_information_month_target.CURRENT_COLL_L.sum())
                total_current_week_collimator_r += float(df_information_month_target.CURRENT_COLL_R.sum())
                total_foil_week += float(df_information_month_target.FOIL_CURRENT.sum()) 
                total_foil_list.append(total_foil_week) 
                total_current_week_target_list.append(total_current_week_target)   
                total_current_week_collimator_l_list.append(total_current_week_collimator_l)
                total_current_week_collimator_r_list.append(total_current_week_collimator_r)
                total_current_weel_total_collimator_list.append(total_current_week_collimator_r+total_current_week_collimator_l)
    print ("SUMMARY")
    print (target_number_list)
    print (foil_list)
    print (total_collimator_r)
    print (total_collimator_l)
    print (total_current_week_target_list)
    print (total_current_week_collimator_l_list)
    file_list = df_information_target.FILE
    df = pd.DataFrame(list(zip(file_list,week_list,target_number_list,foil_list,total_current_week_target_list,total_current_week_collimator_l_list,total_current_week_collimator_r_list,total_current_weel_total_collimator_list,total_foil_list)),columns=["FILE","WEEK","TARGET_NUMBER","FOIL","TARGET_TOTAL","COLLIMATOR_R_TOTAL","COLLIMATOR_L_TOTAL","COLLIMATORS","FOIL_TOTAL"])
    print ("HEREEE")
    print (df)
    return (df)

def cyclotron_information(target):
    columns_write = ["FILE","DATE","WEEK","TARGET","VACUUM","SOURCE_CURRENT","TARGET_CURRENT","RF","RF_POWER","GAS_FLOW","TARGET_VOLUME","PRESSURE_INITIAL","PRESSURE_FINAL"]
    df_information = pd.DataFrame(columns= columns_write)
    atributes = ['file_number','date_stamp','week','target_number_list','vacuum_ave','source_current','target_current','rf','rf_power','gas_flow','target_volume','pressure_initial_all',"pressure_final_all"]
    total_vacuum = []
    total_gas_flow = []
    total_rf = []
    total_rf_power = []
    max_current_target = []
    df_information = cumulative_charge_individual(df_information,target,atributes,columns_write)
    targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
    week_list = []
    target_number_list = []
    number_files = []
    target_current = []
    target_volume = []
    pressure_final = []
    pressure_initial = []
    print ("DF INFORMATION")
    print (df_information[df_information.TARGET == np.min(df_information.TARGET.astype(float))])
    print (df_information[df_information.TARGET == np.max(df_information.TARGET.astype(float))])
    #df_information_maintenance_filter = df_information.drop_duplicates(subset="DATE", keep='first', inplace=False).sort_values(by="WEEK")
    return (df_information)


def get_correlation(corr_df_total,data_df,file,vacuum_fault_files):
    data_df_not_zero = data_df[data_df.Arc_I != "0"]
    data_test = pd.DataFrame(list(zip(data_df_not_zero.Vacuum_P.astype(float)*1e5,data_df_not_zero.Arc_I.astype(float),data_df_not_zero.Target_I.astype(float),data_df_not_zero.Magnet_I.astype(float),
    data_df_not_zero.Coll_l_I.astype(float),data_df_not_zero.Coll_r_I.astype(float))),columns=["VACUUM","CURRENT","TARGET","MAGNET","COLLL","COLLR"])  
    if np.max(data_test.VACUUM) > 2.5:
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

def get_transmission(df_isochronism,probe_current):
    foil_current_max_isochronism = np.max(df_isochronism.Foil_I)/probe_current
    transmission = foil_current_max_isochronism
    return transmission


def get_isochronism(data_df):
    print ("ISOCHRONISM")
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

def func(x, a):
     return a  * x 

def func_2(x, a,b):
     return a  * x +b

def information_summary(data_df,date_stamp,ranges_current,df_total_information,df_isochronism):
    print ("INFORMATION")
    probe_current_transmission = np.average((data_df.Probe_I.astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]))
    transmission = get_transmission(df_isochronism,probe_current_transmission)
    date_stamp_format = datetime.strptime(date_stamp, '%Y-%m-%d')
    date_format = []
    transmission_all_values = []
    target_current = []
    foil_current = []
    probe_current = []
    source_current = []
    week_list_number = []
    target_to_foil_ratio = []
    vacuum = []
    probe_current_transmission_all = []
    source_current_transmission = []
    for current in ranges_current:
        print ("CURRENT")
        print (current)
        print (date_stamp_format.isocalendar()[1])
        transmission_all_values.append(transmission)
        date_format.append(date_stamp)
        week_list_number.append(date_stamp_format.isocalendar()[1])
        target_current.append(np.average(data_df.Target_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
        foil_current.append(np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
        target_to_foil_ratio.append(np.average(data_df.Target_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
        probe_current.append(np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/transmission)
        vacuum.append(np.average(data_df.Vacuum_P[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)*1e5))
        probe_current_transmission_all.append(probe_current_transmission)
        if np.average(data_df.Foil_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float))/transmission > 500:
            files_wrong.append(file)
        source_current.append(np.average(data_df.Arc_I[(data_df.Target_I.astype(float) > current[0]) & (data_df.Target_I.astype(float) < current[1])].astype(float)))
        source_current_transmission.append(np.average(data_df.Arc_I[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)].astype(float)))
    information = {"SOURCE":source_current,"FOIL":foil_current,"TARGET":target_current,"PROBE":probe_current,"TRANSMISSION":transmission_all_values,"DATE":date_format,"WEEK":week_list_number,"TARGET_FOIL":target_to_foil_ratio,"VACUUM":vacuum,"PROBE_MEASURED":probe_current_transmission_all,"SOURCE_PROBE":source_current_transmission}
    df_information = pd.DataFrame(information)
    df_information.dropna()
    print ("MORE INFORMATION")
    print (df_information)
    #if len(df_information)> 2:
    df_total_information = df_total_information.append(df_information.dropna(),ignore_index=False)
    return df_total_information

def source_performance_calculation(df_total_information):
    ranges_current = [[24.0,26.0],[49.0,52.0],[79.0,102.0]]
    probe_values = pd.DataFrame()
    source_values = pd.DataFrame()
    probe_values_measured = pd.DataFrame()
    source_values_measured = pd.DataFrame()
    vacuum_values = pd.DataFrame()
    df_total_information_probe = df_total_information.reset_index(drop=True).drop_duplicates()
    probe_values["DATE"] = df_total_information_probe.DATE
    probe_values["WEEK"] = df_total_information_probe.WEEK
    probe_values["I_S"] = df_total_information_probe.SOURCE_PROBE.astype(float)
    probe_values["I_P"] =  df_total_information_probe.PROBE_MEASURED.astype(float)
    print ("PROBE_VALUES")
    print (probe_values)
    print (probe_values.drop_duplicates())
    tfs.write("info_probe.out",probe_values.drop_duplicates())
    names = ["infor_25.out","infor_50.out","infor_100.out"]
    for j in range(len(ranges_current)):
        probe_values = pd.DataFrame()
        value = "I"
        value_source = "I_S"
        value_vacumm = "I_V"
        probe_values["DATE"] = df_total_information.DATE[((df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1])))].reset_index(drop=True)
        probe_values["WEEK"] = df_total_information.WEEK[((df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1])))].reset_index(drop=True).astype(float)
        probe_values[value_source] = df_total_information.SOURCE[((df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1])))].reset_index(drop=True).astype(float)
        print ("SOURCE")
        print (probe_values[value_source])
        probe_values[value] = (df_total_information.PROBE[((df_total_information.TARGET.astype(float) >ranges_current[j][0]) & ((df_total_information.TARGET.astype(float)<ranges_current[j][1])))]).reset_index(drop=True).astype(float)
        print ("PROBE")
        print (probe_values)
        tfs.write(names[j],probe_values.reset_index(drop=True))
    dataframe_probe_values = (probe_values).dropna()
    dataframe_source_values = (source_values).dropna()
    dataframe_vacuum_values = (vacuum_values).dropna()
    return dataframe_probe_values,dataframe_source_values,dataframe_vacuum_values


def main():
    #folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2018"
    folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/2021"
    filename_completed = []
    for file in os.listdir(folder):
         filename_completed.append(os.path.join(folder,file))
    ranges_current = [[24.0,26.0],[49.0,52.0],[79.0,82.0]]
    #ranges_current = [[80.0,100.0]]
    df_total_information = pd.DataFrame(columns=["SOURCE","FOIL","TARGET","PROBE","DATE","TARGET_FOIL","TRANSMISSION","VACUUM"])
    target = target_information()
    cyclotron_parameters = cyclotron()
    corr_df_total = []
    week_list = []
    filename_completed_current = []
    transmission_all = []
    vacuum_transmission = []
    probe_current_all = []
    probe_current_std_all = []
    for file in filename_completed:
        [target_number,date_stamp,name,file_number,data_df] = selecting_data(file)
        if (np.average(data_df.Target_I.astype(float)) > 10.0):
            filename_completed_current.append(file)
            date_stamp_format = datetime.strptime(date_stamp, '%Y-%m-%d')
            week_list.append(date_stamp_format.isocalendar()[1])
            target.selecting_data_to_plot_reset(data_df,target_number,datetime.strptime(date_stamp, '%Y-%m-%d'),datetime.strptime(date_stamp, '%Y-%m-%d').isocalendar()[1],file[-8:])
            cyclotron_parameters.selecting_data(data_df,target_number,datetime.strptime(date_stamp, '%Y-%m-%d'),datetime.strptime(date_stamp, '%Y-%m-%d').isocalendar()[1],file[-8:])
            df_isochronism = get_isochronism(data_df)
            probe_current_transmission = np.average((data_df.Probe_I.astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]))
            probe_current_transmission_std = np.std((data_df.Probe_I.astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]))
            probe_vacuum_transmission = np.average((data_df.Vacuum_P.astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]))
            transmission = get_transmission(df_isochronism,probe_current_transmission)
            vacuum_transmission.append(probe_vacuum_transmission*1e5)
            probe_current_all.append(probe_current_transmission)
            probe_current_std_all.append(probe_current_transmission_std)
            transmission_all.append(transmission)
            if len(df_isochronism) == 0: 
                continue
            df_total_information = information_summary(data_df,date_stamp,ranges_current,df_total_information,df_isochronism)
    print ("FILES")
    print (filename_completed)
    df = cumulative_charge_folder(target)
    df_collimators = cumulative_charge_target_collimators(target)
    print ("CUMULATIVE")
    print (df_collimators)
    df_cyclotron = cyclotron_information(cyclotron_parameters)
    #tfs.write("summary_df_2020_6",df_2)
    print ("df_total_information")
    print (df_total_information)
    #print (df)
    print (df_collimators.dropna)
    df_transmission = pd.DataFrame({"TRANSMISSION":transmission_all,"VACUUM_T":vacuum_transmission,"PROBE_CURRENT":probe_current_all,"PROBE_CURRENT_STD":probe_current_std_all})
    df_collimators = df_collimators.dropna()
    #df_cyclotron = df_cyclotron.join(df_transmission).dropna()
    print ("DF CYCLOTRON")
    print (df_cyclotron)
    tfs.write("charge_collimators_target_2021.out",df_collimators)
    tfs.write("cyclotron_configuration_2021.out",df_cyclotron)
    print (df_cyclotron)
    print (df_cyclotron.dropna())
    print (df_cyclotron.join(df_transmission).dropna())
    #df_total_information = df_total_information.join(df_transmission)
    print ("NEW DF")
    print (df_total_information)
    [dataframe_probe_values_all,dataframe_source_values_all,dataframe_vacuum_values_all] = source_performance_calculation(df_total_information)
    #print (dataframe_probe_values_all)
    print ("HEREEEE")
    print (dataframe_source_values_all)
    #dataframe_fit_values = source_performance_fitting(dataframe_source_values_all,dataframe_probe_values_all,df)
    #print (dataframe_fit_values)
    #tfs.write("all_data.out",df_total_information.reset_index(drop=True))
    #tfs.write("probe_values_2020_tcp.out",dataframe_probe_values_all.reset_index(drop=True))
    #tfs.write("source_values_2020_tcp.out",dataframe_source_values_all.reset_index(drop=True))
    #tfs.write("vacuum_values_2020_tcp.out",dataframe_vacuum_values_all.reset_index(drop=True))
    print ("VALUES FINAL")
    #print (dataframe_fit_values)
    #tfs.write("slopes_values_2020_tcp.out",dataframe_fit_values)
    tfs.write("charge_source_2021_tcp.out",df)
     

   
    
    



if __name__ == "__main__":
    main()
