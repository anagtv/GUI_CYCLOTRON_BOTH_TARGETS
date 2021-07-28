#Functions: open the files and get key parameters and summaries 
import getting_subsystems_data
import getting_subsystems 
import getting_summaries
import pandas as pd
def file_open(self):
        # Opening input file
        [self.target_number,self.date_stamp,self.name,self.file_number] = getting_subsystems_data.get_headers(str(self.fileName))
        self.irradiation_values = getting_subsystems_data.get_irradiation_information(str(self.fileName))
        self.file_df = getting_subsystems_data.get_data(self.irradiation_values)
        # get_target_paramenteres filters the current smaller than 90% the maximum (target_current) and returns the maximum current value
        [self.target_current,self.max_current] = getting_subsystems_data.get_target_parameters(self.file_df)
        # sets a lower ion source limit for finding RF sparks 
        self.low_source_current = getting_subsystems_data.get_source_parameters_limit(self.file_df)
        # get irradiation hours
        self.time = getting_subsystems_data.get_time(self.file_df,self.max_current)
        self.foil_number = getting_subsystems_data.get_foil_number(self.file_df,self.max_current) 
        # creating dataframes for all the different susbystems with time evolution 
        self.df_subsystem_source = getting_subsystems.get_subsystems_dataframe_source(self)
        self.df_subsystem_vacuum = getting_subsystems.get_subsystems_dataframe_vacuum(self)
        self.df_subsystem_magnet = getting_subsystems.get_subsystems_dataframe_magnet(self)
        self.df_subsystem_rf = getting_subsystems.get_subsystems_dataframe_rf(self)
        self.df_subsystem_rf_sparks = getting_subsystems.get_subsystems_dataframe_rf_sparks(self)
        self.df_subsystem_extraction = getting_subsystems.get_subsystems_dataframe_extraction(self)
        self.df_subsystem_beam = getting_subsystems.get_subsystems_dataframe_beam(self)
        self.df_subsystem_pressure = getting_subsystems.get_subsystems_dataframe_pressure(self) 
        self.df_subsystem_pressure_irradiation = getting_subsystems.get_subsystems_dataframe_pressure_irradiation(self) 
        self.df_isochronism = getting_subsystems_data.get_isochronism(self.file_df)
        [self.probe_current,self.ion_source_current,self.source_performance,self.source_performance_std] = getting_subsystems_data.get_ion_source_performance(self.file_df) #  
        # Adds dataframe to previous dataframes in case it has been already oppened,

def file_open_summary(self):
        getting_summaries.get_summary_ion_source(self)
        getting_summaries.get_summary_vacuum(self)
        getting_summaries.get_summary_magnet(self)
        getting_summaries.get_summary_rf(self)
        getting_summaries.get_summary_extraction(self)
        getting_summaries.get_summary_beam(self)
        getting_summaries.get_summary_volume(self)
        getting_subsystems_data.get_transmission(self)
        getting_subsystems_data.get_pressure_fluctuations(self,0)
        getting_subsystems_data.get_filling_volume(self,0) 
        self.voltage_limit = (0.8*(self.df_rf.DEE1_VOLTAGE_AVE))  
        self.voltage_values = ["Dee_1_kV","Dee_2_kV"]     
        self.voltage_dee_1 = getting_sparks(self,self.voltage_values[0])
        self.voltage_dee_2 = getting_sparks(self,self.voltage_values[1])

def getting_sparks(self,voltage_value):
        voltage_dee = self.df_subsystem_rf_sparks.Dee_1_kV[getattr(self.df_subsystem_rf_sparks,voltage_value) < float(self.voltage_limit.iloc[self.current_row])]
        return (voltage_dee)