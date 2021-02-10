



#### PAST

def getting_average_values(file_name):
    [real_values,target_number,date_stamp ] = get_data_tuple(file_name)
    data_df = get_data(real_values)
    vacuum = get_vacuum_parameters(data_df,0)
    vacuum_average = round(np.average(vacuum)*1e5,2)
    magnet_current = get_magnet_parameters(data_df,0)
    magnet_average = np.average(magnet_current)
    return target_number,vacuum_average,magnet_average

def get_raw_parameters(excel_data_df):
    [target_current,current] = get_target_parameters(excel_data_df)
    time = get_time(excel_data_df,current)
    foil_number = get_time(excel_data_df,current)
    return target_current,current,time,foil_number