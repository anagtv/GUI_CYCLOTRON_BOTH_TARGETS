import saving_files_summary_list_20200420
def get_subsystems_dataframe_source(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_source = ["Time","Foil_No","Arc_I","Arc_V","Gas_flow","Ratio_current"]
    source_voltage,source_current,gas_flow = saving_files_summary_list_20200420.get_source_parameters(excel_data_df,current)
    ratio_current = source_current/(target_current)
    df_subsystem_values_source = [time,foil_number,source_current,source_voltage,gas_flow,ratio_current]  
    df_subsystem_source = pd.concat(df_subsystem_values_source, axis=1, keys=df_column_names_source)
    return df_subsystem_source

def get_subsystems_dataframe_vacuum(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_vacuum = ["Time","Foil_No","Vacuum_P"]
    vacuum_level = saving_files_summary_list_20200420.get_vacuum_parameters(excel_data_df,current)
    magnet_current = saving_files_summary_list_20200420.get_magnet_parameters(excel_data_df,current)
    df_subsystem_values_vacuum = [time,foil_number,vacuum_level]
    df_subsystem_vacuum = pd.concat(df_subsystem_values_vacuum,axis=1,keys=df_column_names_vacuum)
    return df_subsystem_vacuum

import pandas as pd
import numpy as np
def get_subsystems_dataframe_magnet(excel_data_df,current,target_number,target_current,time,foil_number):    
    df_column_names_magnet = ["Time","Foil_No","Magnet_I"]
    magnet_current = saving_files_summary_list_20200420.get_magnet_parameters(excel_data_df,current)
    df_subsystem_valuesmagnet = [time,foil_number,magnet_current]
    df_subsystem_magnet = pd.concat(df_subsystem_valuesmagnet,axis=1,keys=df_column_names_magnet)
    return df_subsystem_magnet

def get_subsystems_dataframe_rf(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_rf = ["Time","Foil_No","Dee_1_kV","Dee_2_kV","RF_fwd_W","RF_refl_W","Phase_load","Flap1_pos","Flap2_pos"]
    dee1_voltage,dee2_voltage = saving_files_summary_list_20200420.get_rf_parameters(excel_data_df,current) 
    forwarded_power,reflected_power,phase_load = saving_files_summary_list_20200420.get_rf_parameters_power(excel_data_df,current)
    flap1_pos,flap2_pos = saving_files_summary_list_20200420.get_rf_parameters_flaps(excel_data_df,current)
    df_subsystem_values_rf = [time,foil_number,dee1_voltage,dee2_voltage,forwarded_power,reflected_power,phase_load,flap1_pos,flap2_pos]
    df_subsystem_rf = pd.concat(df_subsystem_values_rf,axis=1,keys=df_column_names_rf)
    return df_subsystem_rf

def get_subsystems_dataframe_rf_sparks(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_rf = ["Dee_1_kV","Dee_2_kV","RF_fwd_W","RF_refl_W","Phase_load","Flap1_pos","Flap2_pos"]
    dee1_voltage,dee2_voltage = saving_files_summary_list_20200420.get_rf_parameters_sparks(excel_data_df,current) 
    forwarded_power,reflected_power,phase_load = saving_files_summary_list_20200420.get_rf_parameters_power_sparks(excel_data_df,current)
    flap1_pos,flap2_pos = saving_files_summary_list_20200420.get_rf_parameters_flaps_sparks(excel_data_df,current)
    df_subsystem_values_rf = [dee1_voltage,dee2_voltage,forwarded_power,reflected_power,phase_load,flap1_pos,flap2_pos]
    df_subsystem_rf = pd.concat(df_subsystem_values_rf,axis=1,keys=df_column_names_rf)
    return df_subsystem_rf

def get_subsystems_dataframe_extraction(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_extraction = ["Time","Foil_No","Extr_pos","Balance"]
    carousel_position,balance_position = saving_files_summary_list_20200420.get_extraction_parameters_position(excel_data_df,current)
    df_subsystem_values_extraction = [time,foil_number,carousel_position,balance_position]
    df_subsystem_extraction = pd.concat(df_subsystem_values_extraction,axis=1,keys=df_column_names_extraction)
    return df_subsystem_extraction

def get_subsystems_dataframe_beam(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_beam = ["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Target_rel","Extraction_losses"]
    collimator_r,collimator_l = saving_files_summary_list_20200420.get_collimator_parameters(excel_data_df,current) 
    extraction_current = saving_files_summary_list_20200420.get_extraction_parameters(excel_data_df,current)
    collimator_r_rel = collimator_r/extraction_current*100
    collimator_l_rel = collimator_l/extraction_current*100
    target_rel = (target_current)/extraction_current*100
    extraction_losses = (1-(target_current+collimator_l+collimator_r)/extraction_current)*100
    df_subsystem_values_beam = [time,foil_number,extraction_current,collimator_l,target_current,collimator_r,collimator_l_rel,collimator_r_rel,target_rel,extraction_losses]
    df_subsystem_beam = pd.concat(df_subsystem_values_beam,axis=1,keys=df_column_names_beam)
    return df_subsystem_beam

def get_subsystems_dataframe_pressure(excel_data_df,current,target_number,target_current,time,foil_number):
    df_column_names_pressure = ["Time","Foil_No","Target_P"]
    target_pressure = saving_files_summary_list_20200420.get_target_pressure(excel_data_df,current)
    df_subsystem_values_pressure = [time,foil_number,target_pressure]
    df_subsystem_pressure = pd.concat(df_subsystem_values_pressure,axis=1,keys=df_column_names_pressure)
    return df_subsystem_pressure
