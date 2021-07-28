import pandas as pd
import numpy as np
import os
from datetime import datetime
import tfs
from scipy.optimize import curve_fit
import saving_files_summary_list_20200420
import computing_charge_df
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

def func(X, a):
     x,y,z = X
     return a*(x+y) 
def func_2(X, a,b):
     x,y,z = X
     return a*(x+y) + b*z
def main():
	#folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/2021"
	folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/LOGS/2021/Last_maintenance"
	jns = [5476.0,5477.0,5478.0,5482.0,5527.0,5550.0,5563.0,5588.0]
	jns = [5476.0,5477.0,5478.0,5482.0,5527.0]
	tcp = [5671.0,5617.0,5695.0,5712.0,5605.0,5719.0,5638.0,5602.0]
	#folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/JNS/LOGS/2021/Last_maintenance"
	filename_completed = []
	for file in os.listdir(folder):
	    filename_completed.append(os.path.join(folder,file))
	x_list = []
	x_list_sigma = []
	file_values = []
	z_list = []
	z_list_sigma = []
	vacuum_average_relative = []
	vacuum_average_absolute = []
	vacuum_std_relative = []
	vacuum_std_absolute = []
	ion_source_average = []
	ion_source_std = []
	average_collimators = []
	std_collimators = []
	average_target = []
	std_target = []
	date_stamp_all = []
	for file in filename_completed:
		[target_number,date_stamp,name,file_number] = saving_files_summary_list_20200420.get_headers(file)
		real_values = saving_files_summary_list_20200420.get_irradiation_information(file)
		data_df = saving_files_summary_list_20200420.get_data(real_values)
		if np.max(data_df.Target_I.astype(float))> 80:
			y_value_to_fit = data_df.Arc_I[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float)
			x_value_target = data_df.Target_I[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float)
			x_value_foil = data_df.Foil_I[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float)
			time = data_df.Time[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))]
			time_dt = pd.to_datetime(time, format='%H:%M:%S')
			# relative value
			#x_value_vacuum = (data_df.Vacuum_P[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float) - np.min(data_df.Vacuum_P[data_df.Arc_I.astype(float) == 0].astype(float)))
			# absolute value 
			x_value_vacuum = (data_df.Vacuum_P[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float))
			x_value_collimators = data_df.Coll_l_I[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float) + data_df.Coll_r_I[data_df.Target_I.astype(float) > 0.7*np.max(data_df.Target_I.astype(float))].astype(float)
			df_summary = pd.DataFrame(list(zip(y_value_to_fit.astype(float),x_value_target.astype(float),x_value_collimators.astype(float),x_value_vacuum.astype(float),x_value_foil.astype(float))),columns=["I_SOURCE","I_TARGET","I_COLLIMATOR","VACUUM","I_FOIL"])
			if float(file_number) in tcp:
				print ("CORRELATION!!!!!")
				print (df_summary.corr())
				f, ax = plt.subplots(figsize =(9, 8))
				sns.heatmap(df_summary.corr(), ax = ax, cmap ="YlGnBu", annot=True, linewidths = 0.1,cbar_kws={"shrink": .5})
				plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/not_normal_correlation_"+str(int(file_number))+".pdf")
				fig, ax = plt.subplots()
				#X = pd.DataFrame(np.c_[df_summary['I_TARGET'].astype(float), df_summary['I_COLLIMATOR'].astype(float),(df_summary['VACUUM'].astype(float)-np.min(df_summary['VACUUM'].astype(float)))*1e5], columns=['I_TARGET','I_COLLIMATOR','VACUUM'])
				X = pd.DataFrame(np.c_[df_summary['I_TARGET'].astype(float), df_summary['I_COLLIMATOR'].astype(float),(df_summary['VACUUM'].astype(float)-np.min(df_summary['VACUUM'].astype(float)))*1e5], columns=['I_TARGET','I_COLLIMATOR','VACUUM'])
				Y = df_summary.I_SOURCE
				X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=9)
				ax.scatter(X.I_TARGET, Y,label="Measured")
				popt, pcov = curve_fit(func_2, (X_train.I_TARGET,X_train.I_COLLIMATOR,X_train.VACUUM*1e5),y_train)
				ax.scatter(X_test.I_TARGET,func_2((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1]),label="Estimated")
				plt.legend(loc='best')
				plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/target_source_evolution_"+str(int(file_number)))
				fig2, ax2 = plt.subplots()
				ax2.scatter(X_test.I_COLLIMATOR,y_test,label="Measured")
				ax2.scatter(X_test.I_COLLIMATOR,func_2((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1]),label="Estimated")
				plt.legend(loc='best')
				plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/collimator_source_evolution_"+str(int(file_number)))
				fig5, ax5 = plt.subplots()
				ax5.scatter(range(len(time_dt)),Y,label="Measured")
				ax5.scatter(range(len(time_dt)),func_2((X.I_TARGET,X.I_COLLIMATOR,X.VACUUM*1e5),popt[0],popt[1]),label="Estimated")
				plt.legend(loc='best')
				plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/time_source_evolution_"+str(int(file_number)))
				print ("PARAMETERS")
				print (file_number)
				print (popt)
				print (np.diag(pcov)**0.5)
				print (np.array(np.diag(pcov)**0.5/np.array(popt)*100))
				fig3, ax3 = plt.subplots()
				ax3.scatter(X_test.VACUUM,y_test,label="Measured")
				ax3.scatter(X_test.VACUUM,func_2((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1]),label="Estimated")
				plt.legend(loc='best')
				plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/vacuum_source_evolution_"+str(int(file_number)))
			X = pd.DataFrame(np.c_[df_summary['I_TARGET'].astype(float), df_summary['I_COLLIMATOR'].astype(float),df_summary['VACUUM'].astype(float)-np.min(df_summary['VACUUM'].astype(float))], columns=['I_TARGET','I_COLLIMATOR','VACUUM'])
			Y = df_summary.I_SOURCE
			X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=9)
			popt, pcov = curve_fit(func, (X_train.I_TARGET,X_train.I_COLLIMATOR,X_train.VACUUM),y_train)
			if float(file_number) in tcp:
			     fig3, ax3 = plt.subplots()
			     ax3.scatter(range(len(time_dt)),Y,label="Measured")
			     ax3.scatter(range(len(time_dt)),func((X.I_TARGET,X.I_COLLIMATOR,X.VACUUM*1e5),popt[0]),label="Estimated")
			     plt.legend(loc='best')
			     plt.savefig("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/PLOTS_2/time_source_evolution_alternative_"+str(int(file_number)))
			print ("ALTERNATIVE METHOD")
			print (popt)
			print (np.diag(pcov)**0.5)
			print (np.array(np.diag(pcov)**0.5/np.array(popt)*100))
			average_collimators.append(np.average(x_value_collimators))
			std_collimators.append(np.std(x_value_collimators))
			average_target.append(np.average(x_value_target))
			std_target.append(np.std(x_value_target))
			ion_source_average.append(np.average(Y))
			ion_source_std.append(np.std(Y))
			vacuum_average_relative.append(np.average(x_value_vacuum)*1e5)
			vacuum_average_absolute.append(np.average((data_df.Vacuum_P[data_df.Target_I.astype(float) > 0.9*np.max(data_df.Target_I.astype(float))].astype(float)))*1e5)
			vacuum_std_relative.append(np.std(x_value_vacuum)*1e5)
			vacuum_std_absolute.append(np.std((data_df.Vacuum_P[data_df.Target_I.astype(float) > 0.9*np.max(data_df.Target_I.astype(float))].astype(float)))*1e5)		
			T_2 = np.average((df_summary.I_TARGET + df_summary.I_COLLIMATOR)/df_summary.I_FOIL)
			sigma_T_2 = np.std((df_summary.I_TARGET + df_summary.I_COLLIMATOR)/df_summary.I_FOIL)
			df_isochronism = saving_files_summary_list_20200420.get_isochronism(data_df)
			source_current_probe = getattr(data_df,"Arc_I").astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]
			probe_current = getattr(data_df,"Probe_I").astype(float)[(data_df.Probe_I.astype(float) > 14) & (data_df.Probe_I.astype(float) < 16)]
			T_1 = np.average(np.max(df_isochronism.Foil_I)/probe_current)
			a = popt[0]
			x = a*T_1*T_2
			x_list.append(x)
			sigma_T_1 = np.std(np.max(df_isochronism.Foil_I)/probe_current)
			sigma_a = (np.diag(pcov)**0.5)[0]
			sigma_x = ((T_1*T_2*sigma_a)**2+(a*T_2*sigma_T_1)**2+(a*T_1*sigma_T_2))**0.5
			file_values.append(float(file_number))
			x_list_sigma.append(sigma_x)
			date_stamp_all.append(date_stamp)
	print ("HEREE")
	print (pd.DataFrame(list(zip(date_stamp_all,file_values,x_list,x_list_sigma)),columns=["DATE","FILE","PERFORMANCE","PERFORMANCE_STD"]))
	summary = pd.DataFrame(list(zip(date_stamp_all,file_values,x_list,x_list_sigma)),columns=["DATE","FILE","PERFORMANCE","PERFORMANCE_STD"])
	#print (summary.loc[227])
	print (summary.dropna())
	tfs.write("source_summary_values_JNS.out",summary.dropna())


if __name__ == "__main__":
    main()
