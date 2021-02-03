import saving_files_summary_list_20200420
def file_open(self):
        # Opening input file
        [self.target_number,self.date_stamp,self.name,self.file_number] = saving_files_summary_list_20200420.get_headers(str(self.fileName_completed))
        self.irradiation_values = saving_files_summary_list_20200420.get_irradiation_information(str(self.fileName_completed))
        self.file_df = saving_files_summary_list_20200420.get_data(self.irradiation_values)
        # get_target_paramenteres filters the current smaller than 90% the maximum (target_current) and returns the maximum current value
        [self.target_current,self.max_current] = saving_files_summary_list_20200420.get_target_parameters(self.file_df)
        # sets a lower ion source limit for finding RF sparks 
        self.low_source_current = saving_files_summary_list_20200420.get_source_parameters_limit(self.file_df)
        # get irradiation hours
        self.time = saving_files_summary_list_20200420.get_time(self.file_df,self.max_current)
        self.foil_number = saving_files_summary_list_20200420.get_foil_number(self.file_df,self.max_current) 
        # creating dataframes for all the different susbystems with time evolution 
        self.df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_vacuum = saving_files_summary_list_20200420.get_subsystems_dataframe_vacuum(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_magnet = saving_files_summary_list_20200420.get_subsystems_dataframe_magnet(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_rf = saving_files_summary_list_20200420.get_subsystems_dataframe_rf(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_rf_sparks = saving_files_summary_list_20200420.get_subsystems_dataframe_rf_sparks(self.file_df,self.low_source_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)
        self.df_subsystem_pressure = saving_files_summary_list_20200420.get_subsystems_dataframe_pressure(self.file_df,self.max_current,self.target_number,self.target_current,self.time,self.foil_number)  
        self.df_isochronism = saving_files_summary_list_20200420.get_isochronism(self.file_df)
        [self.probe_current,self.ion_source_current,self.source_performance] = saving_files_summary_list_20200420.get_ion_source_performance(self.file_df) #  
        print ("FINALLY HERE")
        print (self.probe_current)     
        print (self.df_subsystem_source)
        # Adds dataframe to previous dataframes in case it has been already oppened,

def file_open_summary(self):
        self.df_source = saving_files_summary_list_20200420.get_summary_ion_source(self.df_subsystem_source,self.source_performance,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_source)
        self.df_vacuum = saving_files_summary_list_20200420.get_summary_vacuum(self.df_subsystem_vacuum,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_vacuum)
        self.df_magnet = saving_files_summary_list_20200420.get_summary_magnet(self.df_subsystem_magnet,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_magnet)
        self.df_rf = saving_files_summary_list_20200420.get_summary_rf(self.df_subsystem_rf,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_rf)
        self.df_extraction = saving_files_summary_list_20200420.get_summary_extraction(self.df_subsystem_extraction,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_extraction)
        self.df_beam = saving_files_summary_list_20200420.get_summary_beam(self.df_subsystem_beam,str(self.fileName_completed.split("/")[-1]),self.target_number[1],self.date_stamp,self.df_beam)
        self.df_transmission = saving_files_summary_list_20200420.get_transmission(self.df_isochronism,self.probe_current,self.df_subsystem_source,str(self.file_number),self.target_number[1],self.date_stamp,self.df_transmission)
        self.df_pressure_fluctuations = saving_files_summary_list_20200420.get_pressure_fluctuations(self.file_df,self.target_number[1],0,str(self.file_number),self.date_stamp,self.df_pressure_fluctuations)
        self.df_filling_volume = saving_files_summary_list_20200420.get_filling_volume(self.file_df,self.target_number[1],0,str(self.file_number),self.date_stamp,self.df_filling_volume) 
        self.voltage_limit = (0.8*(self.df_rf.DEE1_VOLTAGE_AVE))       
        self.voltage_dee_1 = self.df_subsystem_rf_sparks.Dee_1_kV[self.df_subsystem_rf_sparks.Dee_1_kV < float(self.voltage_limit.iloc[self.current_row])]
        self.voltage_dee_2 = self.df_subsystem_rf_sparks.Dee_2_kV[self.df_subsystem_rf_sparks.Dee_2_kV < float(self.voltage_limit.iloc[self.current_row])]