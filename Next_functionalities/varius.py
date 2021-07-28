
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


fig, ax = plt.subplots()
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_SOURCE,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_TARGET,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_COLL_L,fmt="o")
ax.errorbar(df_sorted.CHARGE_FOIL,df_sorted.CHARGE_COLL_R,fmt="o")

irradiation_time = list(file_df.Time[file_df.Arc_I.astype(float) > 0])
initial_time = float(irradiation_time[0][0:2])*3600 + float(irradiation_time[0][3:5])*60 + float(irradiation_time[0][6:8])
final_time = float(irradiation_time[-1][0:2])*3600 + float(irradiation_time[-1][3:5])*60 + float(irradiation_time[-1][6:8])
