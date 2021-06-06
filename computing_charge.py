import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_SOURCE,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_TARGET,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_COLL_L,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_COLL_R,fmt="o")

irradiation_time = list(file_df.Time[file_df.Arc_I.astype(float) > 0])
initial_time = float(irradiation_time[0][0:2])*3600 + float(irradiation_time[0][3:5])*60 + float(irradiation_time[0][6:8])
final_time = float(irradiation_time[-1][0:2])*3600 + float(irradiation_time[-1][3:5])*60 + float(irradiation_time[-1][6:8])

folder_files = "Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/Max_performance"
folder_analysis = "Desktop/Test_for_GUI/test_tcp_max_2020/"
file_source = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_source.out"
file_rf = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_rf.out"
file_vacuum = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_vacuum.out"
file_beam = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_beam.out"
file_transmission = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_transmission.out"
file_extraction = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_extraction.out"
file_magnet = "Desktop/Test_for_GUI/test_tcp_2020/table_summary_magnet.out"
data_df_source = tfs.read(file_source)
data_df_rf = tfs.read(file_rf)
data_df_vacuum = tfs.read(file_vacuum)
data_df_beam = tfs.read(file_beam)
data_df_extraction = tfs.read(file_extraction)
data_df_transmission = tfs.read(file_transmission)
data_df_magnet = tfs.read(file_magnet)
source_performance = data_df_source.SOURCE_PERFORMANCE_AVE
rf_voltage_1 = data_df_rf.DEE1_VOLTAGE_AVE
rf_voltage_2 = data_df_rf.DEE2_VOLTAGE_AVE

source_performance_rf = pd.concat([data_df_rf.DEE1_VOLTAGE_AVE,data_df_rf.DEE2_VOLTAGE_AVE,data_df_source.SOURCE_PERFORMANCE_AVE],axis=1)
source_performance_vacuum = pd.concat([data_df_vacuum.PRESSURE_AVE,data_df_source.SOURCE_PERFORMANCE_AVE,data_df_source.CURRENT_AVE],axis=1)
source_performance_beam = pd.concat([data_df_beam.RELATIVE_COLL_CURRENT_L_AVE,data_df_beam.RELATIVE_COLL_CURRENT_R_AVE,data_df_source.SOURCE_PERFORMANCE_AVE],axis=1)
source_performance_extraction = pd.concat([data_df_extraction.CAROUSEL_POSITION_AVE[data_df_extraction.TARGET == "1"],data_df_extraction.BALANCE_POSITION_AVE[data_df_extraction.TARGET == "1"],
	data_df_source.CURRENT_AVE[data_df_source.TARGET == "1"]],axis=1)
corrMatrix_source_rf = source_performance_rf.corr()
sn.heatmap(corrMatrix_source_rf, annot=True)

source_information = pd.concat([data_df_source.CURRENT_AVE,data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,data_df_source.SOURCE_PERFORMANCE_AVE,data_df_vacuum.PRESSURE_AVE,
	data_df_transmission.TRANSMISSION_AVE],axis=1)
source_information_medium_correlation = source_information.corr()[(abs(source_information.corr().CURRENT_AVE) > 0.3) & (abs(source_information.corr().CURRENT_AVE) < 0.49)]
source_information_high_correlation = source_information.corr()[abs(source_information.corr().CURRENT_AVE) > 0.5]
source_information.columns = ["SOURCE","COLLIMATORS","PERFORMANCE","PRESSURE","TRANSMISSION"]

# VARIABLE CORRELATION 

def func(x, a, c):
    return a * x + c
popt_coll, pcov_coll = curve_fit(func,data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,func(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_coll = np.sqrt(np.diag(pcov_coll))

popt_source, pcov_source = curve_fit(func,data_df_source.SOURCE_PERFORMANCE_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_source.SOURCE_PERFORMANCE_AVE, data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_source.SOURCE_PERFORMANCE_AVE, func(data_df_source.SOURCE_PERFORMANCE_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_source = np.sqrt(np.diag(pcov_source))

popt_magnet, pcov_magnet = curve_fit(func,data_df_magnet.CURRENT_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_magnet.CURRENT_AVE, data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_magnet.CURRENT_AVE, func(data_df_magnet.CURRENT_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_magnet = np.sqrt(np.diag(pcov_magnet))

fig, ax = plt.subplots()
ax.errorbar(data_df_source.CURRENT_AVE,data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE)
ax.errorbar(source_performance_vacuum.PRESSURE_AVE,source_performance_vacuum.CURRENT_AVE,fmt="o")

corrMatrix_source_vacuum = source_performance_vacuum.corr()
sn.heatmap(corrMatrix_source_vacuum, annot=True)

corrMatrix_source_beam = source_performance_beam.corr()
sn.heatmap(corrMatrix_source_beam, annot=True)

corrMatrix_source_extraction = source_performance_extraction.corr()
sn.heatmap(corrMatrix_source_extraction, annot=True)


#folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2020_2"
folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2021"
#folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/Anciens logs/2018"
filename_completed = []
for file in os.listdir(folder):
    filename_completed.append(os.path.join(folder,file))
target = target_information2()
corr_df_total = []
for file in filename_completed:
    print (file)
    [target_number,date_stamp,name,file_number] = get_headers(file)
    real_values = get_irradiation_information(file)
    data_df = get_data(real_values)
    print ("FOIL")
    print (np.average(data_df.Foil_No.astype(float)))
    data_df_not_zero = data_df[data_df.Arc_I != "0"]
    data_test = pd.DataFrame(list(zip(data_df_not_zero.Vacuum_P.astype(float)*1e5,data_df_not_zero.Arc_I.astype(float),data_df_not_zero.Target_I.astype(float),data_df_not_zero.Magnet_I.astype(float),
    data_df_not_zero.Coll_l_I.astype(float),data_df_not_zero.Coll_r_I.astype(float)))
    ,columns=["VACUUM","CURRENT","TARGET","MAGNET","COLLL","COLLR"])
    corr_df_total.append(data_test.corr())
    target.selecting_data_to_plot_reset(data_df,target_number,date_stamp)

# COMPUTING CHARGE

df_information = pd.DataFrame(columns=["DATE","FOIL","TARGET","CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R","VACUUM"])
df_information["DATE"] = target.date_stamp 
df_information["FOIL"] = target.foil_total
df_information["TARGET"] = target.target_number_list
df_information["CURRENT_SOURCE"] = target.ion_source_current
df_information["CURRENT_FOIL"] = target.foil_individual
df_information["CURRENT_COLL_L"] = target.coll_l_current
df_information["CURRENT_TARGET"] = target.target_current
df_information["CURRENT_COLL_R"] = target.coll_r_current
#df_information["VACUUM"] = target.vacuum_level
total_current_per_foil = []
total_current_collimator_l = []
total_current_collimator_r = []
total_current_target = []
total_ion_source_current = []
foil_list = []
target_list = []
vacuum_level_list = []
targets_numbers = [np.min(target.target_number_list),np.max(target.target_number_list)]
#time_period = [['2020-10-01','2020-10-31'],['2020-11-01','2020-11-31'],['2020-12-01','2020-12-31']]
#time_period = [['2016-10-01','2016-10-31'],['2016-11-01','2016-11-31'],['2016-12-01','2016-12-31']]
time_period = [['2021-01-01','2021-01-31'],['2021-02-01','2021-02-31'],['2021-03-01','2021-03-31']]
time_period_labels = ["january","february","march"]
#time_period_labels = ["october","november","december"]
target_month = []
number_of_irradiations_per_foil = []
for i in range(len(time_period)):
    df_information_month = df_information[(df_information['DATE'] > time_period[i][0]) & (df_information['DATE'] < time_period[i][1])]
    for target_number in targets_numbers:
        df_information_target = df_information_month[df_information_month.TARGET  == target_number]
        total_current_foil =  df_information_target.drop_duplicates(subset="FOIL",keep = "first").FOIL
        print (total_current_foil)
        for foil in total_current_foil: 
            foil_list.append(foil)
            target_list.append(target_number)
            target_month.append(time_period_labels[i])
            number_of_irradiations_per_foil.append(len(df_information_target.CURRENT_FOIL[df_information_target.FOIL  == foil]))
            total_current_per_foil.append(df_information_target.CURRENT_FOIL[df_information_target.FOIL  == foil].sum())
            total_current_collimator_l.append(df_information_target.CURRENT_COLL_L[df_information_target.FOIL  == foil].sum())
            total_current_collimator_r.append(df_information_target.CURRENT_COLL_R[df_information_target.FOIL  == foil].sum())
            total_current_target.append(df_information_target.CURRENT_TARGET[df_information_target.FOIL  == foil].sum())
            total_ion_source_current.append(df_information_target.CURRENT_SOURCE[df_information_target.FOIL  == foil].sum())
        #vacuum_level_list.append(np.average(df_information_target.VACUUM[df_information_target.FOIL  == foil]))
df = pd.DataFrame(list(zip(target_list,foil_list,total_ion_source_current,total_current_per_foil,total_current_collimator_l,total_current_target,total_current_collimator_r,target_month,number_of_irradiations_per_foil)),columns=["TARGET","FOIL","CHARGE_SOURCE","CHARGE_FOIL","CHARGE_COLL_L","CHARGE_TARGET","CHARGE_COLL_R","DATE","NUMBER"])
df_sorted = df.sort_values(by=['TARGET','FOIL'])


fig, ax = plt.subplots()
ax.errorbar(data_df_not_zero.Vacuum_P.astype(float)*1e5,data_df_not_zero.Arc_I.astype(float),fmt="o")

current_foil_sorted = [target.foil_individual for _,target.foil_individual in sorted(zip(target.target_number_list,target.foil_individual))]
foil_number_sorted = [target.foil_total for _,target.foil_total in sorted(zip(target.target_number_list,target.foil_total))]

class target_information2:
    def __init__(self):
        self.foil_individual = []
        self.foil_total = []
        self.target_number_list = []
        self.coll_l_current = []
        self.target_current = []
        self.coll_r_current = []
        self.ion_source_current = []
        self.date_stamp = []
    def selecting_data_to_plot_reset(self,file_df,target,date_stamp_i):
        self.date_stamp.append(date_stamp_i)     
        self.foil_individual.append(getattr(file_df,"Foil_I").astype(float).sum()*3/3600)
        self.coll_l_current.append(getattr(file_df,"Coll_l_I").astype(float).sum()*3/3600)
        self.target_current.append(getattr(file_df,"Target_I").astype(float).sum()*3/3600)
        self.coll_r_current.append(getattr(file_df,"Coll_r_I").astype(float).sum()*3/3600)
        self.ion_source_current.append(getattr(file_df,"Arc_I").astype(float).sum()*3/3600)
        self.foil_total.append(file_df.Foil_No.iloc[-1])
        self.target_number_list.append(int(target[1]))
        

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








