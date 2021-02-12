import pandas as pd
import numpy as np
import saving_files_summary_list_20200420
import columns_names

def get_summary_ion_source(self): 
    source_current = self.df_subsystem_source.Arc_I
    source_voltage = self.df_subsystem_source.Arc_V
    gas_flow = self.df_subsystem_source.Gas_flow
    ratio_current = self.df_subsystem_source.Ratio_current
    foil_number = np.average(self.df_subsystem_source.Foil_No)
    ave_source_current,std_source_current,max_source_current,min_source_current = saving_files_summary_list_20200420.get_statistic_values(source_current)  
    ave_source_voltage,std_source_voltage,max_source_voltage,min_source_voltage = saving_files_summary_list_20200420.get_statistic_values(source_voltage)  
    ave_gas_flow,std_gas_flow,max_gas_flow,min_gas_flow = saving_files_summary_list_20200420.get_statistic_values(gas_flow) 
    ave_ratio_current,std_ratio_current,max_ratio_current,min_ratio_current = saving_files_summary_list_20200420.get_statistic_values(ratio_current)
    df_source_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,
    float(max_source_current),float(min_source_current),float(ave_source_current),float(std_source_current),
    float(max_source_voltage),float(min_source_voltage),float(ave_source_voltage),float(std_source_voltage),
    float(max_gas_flow),
    float(max_ratio_current),float(min_ratio_current),float(ave_ratio_current),float(std_ratio_current),float(self.source_performance)
    ,float(self.source_performance_std)]]
    df_source_i = pd.DataFrame(df_source_values,columns=columns_names.COLUMNS_SOURCE)
    self.df_source = self.df_source.append(df_source_i,ignore_index=True)


def get_summary_vacuum(self):
    print (self.df_subsystem_vacuum)
    vacuum_level = self.df_subsystem_vacuum.Vacuum_P
    foil_number = np.average((self.df_subsystem_vacuum.Foil_No))
    ave_vacuum,std_vacuum,max_vacuum,min_vacuum = saving_files_summary_list_20200420.get_statistic_values(vacuum_level)
    vacuum_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,float(max_vacuum)*1e5,float(min_vacuum)*1e5,float(ave_vacuum)*1e5,float(std_vacuum)*1e5]]
    df_vacuum_i = pd.DataFrame((vacuum_values),columns=columns_names.COLUMNS_VACUUM)
    self.df_vacuum = self.df_vacuum.append(df_vacuum_i,ignore_index=True)


def get_summary_magnet(self):
    print ("MAGNET")
    print (self.df_subsystem_magnet)
    magnet_current = self.df_subsystem_magnet.Magnet_I
    foil_number = np.average((self.df_subsystem_magnet.Foil_No))
    ave_magnet_current,std_magnet_current,max_magnet_current,min_magnet_current = saving_files_summary_list_20200420.get_statistic_values(magnet_current)
    magnet_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,float(max_magnet_current),float(min_magnet_current),float(ave_magnet_current),float(std_magnet_current)]]
    df_magnet_i = pd.DataFrame((magnet_values),columns=columns_names.COLUMNS_MAGNET)
    self.df_magnet = self.df_magnet.append(df_magnet_i,ignore_index=True)
    


def get_summary_rf(self):
    dee1_voltage = self.df_subsystem_rf.Dee_1_kV
    dee2_voltage = self.df_subsystem_rf.Dee_2_kV
    forwarded_power = self.df_subsystem_rf.RF_fwd_W
    reflected_power = self.df_subsystem_rf.RF_refl_W
    phase_load = self.df_subsystem_rf.Phase_load
    flap1_pos = self.df_subsystem_rf.Flap1_pos
    flap2_pos = self.df_subsystem_rf.Flap2_pos
    foil_number = np.average((self.df_subsystem_rf.Foil_No))
    ave_dee1_voltage,std_dee1_voltage,max_dee1_voltage,min_dee1_voltage = saving_files_summary_list_20200420.get_statistic_values(dee1_voltage)   
    ave_dee2_voltage,std_dee2_voltage,max_dee2_voltage,min_dee2_voltage = saving_files_summary_list_20200420.get_statistic_values(dee2_voltage)
    ave_forwarded_power,std_forwarded_power,max_forwarded_power,min_forwarded_power = saving_files_summary_list_20200420.get_statistic_values(forwarded_power)
    ave_reflected_power,std_reflected_power,max_reflected_power,min_reflected_power = saving_files_summary_list_20200420.get_statistic_values(reflected_power)
    ave_flap1_pos,std_flap1_pos,max_flap1_pos,min_flap1_pos = saving_files_summary_list_20200420.get_statistic_values(flap1_pos)
    ave_flap2_pos,std_flap2_pos,max_flap2_pos,min_flap2_pos = saving_files_summary_list_20200420.get_statistic_values(flap2_pos)
    ave_phase_load,std_phase_load,max_phase_load,min_phase_load = saving_files_summary_list_20200420.get_statistic_values(flap2_pos)
    rf_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,max_dee1_voltage,min_dee1_voltage,ave_dee1_voltage,std_dee1_voltage,max_dee2_voltage,min_dee2_voltage,ave_dee2_voltage,std_dee2_voltage,
    max_forwarded_power,min_forwarded_power,ave_forwarded_power,std_forwarded_power,max_reflected_power,min_reflected_power,ave_reflected_power,std_reflected_power,max_phase_load,min_phase_load,ave_phase_load,std_phase_load,max_flap1_pos,min_flap1_pos,ave_flap1_pos,std_flap1_pos,
    max_flap2_pos,min_flap2_pos,ave_flap2_pos,std_flap2_pos]]
    df_rf_i = pd.DataFrame((rf_values),columns=columns_names.COLUMNS_RF)      
    self.df_rf = self.df_rf.append(df_rf_i,ignore_index=True)
 


def get_summary_extraction(self):
    carousel_position = self.df_subsystem_extraction.Extr_pos
    balance_position = self.df_subsystem_extraction.Balance
    foil_number = np.average((self.df_subsystem_extraction.Foil_No))
    ave_carousel_position,std_carousel_position, max_carousel_position, min_carousel_position = saving_files_summary_list_20200420.get_statistic_values(carousel_position)
    ave_balance_position,std_balance_position, max_balance_position, min_balance_position = saving_files_summary_list_20200420.get_statistic_values(balance_position)
    extraction_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,max_carousel_position,min_carousel_position,ave_carousel_position,std_carousel_position,max_balance_position,min_balance_position,ave_balance_position,std_balance_position]]
    df_extraction_i = pd.DataFrame((extraction_values),columns=columns_names.COLUMNS_EXTRACTION)      
    self.df_extraction = self.df_extraction.append(df_extraction_i,ignore_index=True)



def get_summary_beam(self):
    target_current = self.df_subsystem_beam.Target_I
    extraction_current = self.df_subsystem_beam.Foil_I 
    collimator_r = self.df_subsystem_beam.Coll_r_I   
    collimator_l = self.df_subsystem_beam.Coll_l_I  
    collimator_r_rel = self.df_subsystem_beam.Coll_r_rel 
    collimator_l_rel = self.df_subsystem_beam.Coll_l_rel
    target_rel = self.df_subsystem_beam.Target_rel
    extraction_losses = self.df_subsystem_beam.Extraction_losses
    foil_number = np.average((self.df_subsystem_beam.Foil_No))
    collimator_total_rel = collimator_r_rel + collimator_l_rel
    ave_extraction_current,std_extraction_current,max_extraction_current,min_extraction_current = saving_files_summary_list_20200420.get_statistic_values(extraction_current)
    ave_target_current,std_target_current,max_target_current,min_target_current = saving_files_summary_list_20200420.get_statistic_values(target_current)
    ave_collimator_r,std_collimator_r, max_collimator_r, min_collimator_r = saving_files_summary_list_20200420.get_statistic_values(collimator_r)
    ave_collimator_l,std_collimator_l, max_collimator_l, min_collimator_l = saving_files_summary_list_20200420.get_statistic_values(collimator_l)
    ave_collimator_r_rel,std_collimator_r_rel, max_collimator_r_rel, min_collimator_r_rel = saving_files_summary_list_20200420.get_statistic_values(collimator_r_rel)
    ave_collimator_l_rel,std_collimator_l_rel, max_collimator_l_rel, min_collimator_l_rel = saving_files_summary_list_20200420.get_statistic_values(collimator_l_rel)
    ave_collimator_total_rel,std_collimator_total_rel, max_collimator_total_rel, min_collimator_total_rel = saving_files_summary_list_20200420.get_statistic_values(collimator_total_rel)
    ave_target_rel,std_target_rel,max_target_rel,min_target_rel = saving_files_summary_list_20200420.get_statistic_values(target_rel)
    ave_extraction_losses,std_extraction_losses,max_extraction_losses,min_extraction_losses = saving_files_summary_list_20200420.get_statistic_values(extraction_losses)
    beam_values = [[str(int(self.file_number)),self.date_stamp,self.target_number[1],foil_number,
    max_collimator_l,min_collimator_l, ave_collimator_l, std_collimator_l,
    max_collimator_r,min_collimator_r, ave_collimator_r, std_collimator_r,
    max_collimator_l_rel,min_collimator_l_rel, ave_collimator_l_rel, std_collimator_l_rel,
    max_collimator_r_rel,min_collimator_r_rel, ave_collimator_r_rel, std_collimator_r_rel,
    max_target_current,min_target_current,ave_target_current,std_target_current,
    max_extraction_current,min_extraction_current,ave_extraction_current,std_extraction_current,
    max_target_rel,min_target_rel,ave_target_rel,std_target_rel,
    max_extraction_losses,min_extraction_losses,ave_extraction_losses,std_extraction_losses, 
    max_collimator_total_rel,min_collimator_total_rel, ave_collimator_total_rel, std_collimator_total_rel,]]
    df_beam_i = pd.DataFrame((beam_values),columns=columns_names.COLUMNS_BEAM )      
    self.df_beam = self.df_beam.append(df_beam_i,ignore_index=True)
