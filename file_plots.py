import saving_files_summary_list_20200420
def file_plot(self):
    #[real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        self.irradiation_values = saving_files_summary_list_20200420.get_irradiation_information(str(self.fileName_completed))
        data_df = saving_files_summary_list_20200420.get_data(self.irradiation_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Arc_V.astype(float),data_df.Time,self.fileName_completed[-8:-4],"Source Voltage [V]",1)
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Arc_I.astype(float),data_df.Time,self.fileName_completed[-8:-4],"Source Current [mA]",0)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
        self.sc1.draw()
        self.sc1.show()


def setting_plot(self):
    self.sc1.axes[0].clear()
    self.sc1.axes[1].clear()

def file_plot_vacuum(self):
    setting_plot(self)
    saving_files_summary_list_20200420.get_plots_one_functions_all(self,self.y_values_right,self.x_values,self.fileName[-8:-4],self.label_right,1)
    saving_files_summary_list_20200420.get_plots_one_functions_all(self,self.y_values_left,self.x_values,self.fileName[-8:-4],self.label_left,0)
    self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
    self.sc1.draw()
    self.sc1.show()


def file_plot_two_functions(self):
    setting_plot(self)
    saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.y_values_left_1,self.y_values_left_1,self.x_values,self.legend_left_1,self.legend_left_2,self.label_left,0)
    saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.y_values_right_1,self.y_values_right_2,self.x_values,self.legend_right_1,self.legend_right_2,self.label_right,1) 
    self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)      
    self.sc1.draw()
    self.sc1.show()

def file_plot_two_one_functions(self):
    setting_plot(self)
    saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.y_values_left_1,self.y_values_left_1,self.x_values,self.legend_left_1,self.legend_left_2,self.label_left,0)
    saving_files_summary_list_20200420.get_plots_one_functions_all(self,self.y_values_right,self.x_values,self.fileName[-8:-4],self.label_right,1)
    self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)      
    self.sc1.draw()
    self.sc1.show()

# SOURCE 


def file_plot_collimators_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        #saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),df_subsystem_beam.Target_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]","Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Target_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]",1)
        self.sc4.draw()
        self.sc4.show()

def file_plot_vacuum_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_vacuum = saving_files_summary_list_20200420.get_subsystems_dataframe_vacuum(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_magnet = saving_files_summary_list_20200420.get_subsystems_dataframe_magnet(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_vacuum.Vacuum_P.astype(float)*1e5,df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Vacuum P [$10^{5}$ mbar]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_magnet.Magnet_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Magnet Current [A]",1)
        self.sc4.draw()
        self.sc4.show()

    
def file_plot_rf_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_rf = saving_files_summary_list_20200420.get_subsystems_dataframe_rf(data_df,current,target_number,target_current,time,foil_number)
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_1_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 1)[V]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_2_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 2) [V]",1)
        self.sc4.draw()
        self.sc4.show()
    


def file_plot_extraction_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current)
        df_subsystem_source = saving_files_summary_list_20200420.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Extr_pos.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Extraction Position [%]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Balance.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Balance Position [%]",1)
        self.sc4.draw()
        self.sc4.show()



def file_plot_extraction(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Extr_pos.astype(float),data_df.Balance.astype(float),data_df.Time,"Extr_pos","Balance","Position [%]",0)
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Coll_l_I.astype(float),data_df.Coll_r_I.astype(float),data_df.Time,"Coll l ","Coll r",r"Current [$\mu$A]",1)   
        self.sc1.draw()
        self.sc1.show()

def file_plot_collimation(self):
        #["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Extraction_losses"]
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        self.df_subsystem_beam_selected = df_subsystem_beam
        self.df_subsystem_beam_selected = self.df_subsystem_beam_all[self.row_to_plot]
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Foil_I.astype(float),data_df.Target_I.astype(float),data_df.Time,"Foil I","Target I",r"Current [$\mu$A]",1)
        #saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Coll_l_rel,self.df_subsystem_beam_selected.Coll_r_rel,time,"Coll l rel","Coll r rel",r"Current [%]",1)
        saving_files_summary_list_20200420.get_plots_three_functions_area(self,self.df_subsystem_beam_selected,data_df.Time,r"Current [$\mu$A]",0)
        self.sc1.draw()
        self.sc1.show()

def file_plot_collimation_target(self):
        #["Time","Foil_No","Foil_I","Coll_l_I","Target_I","Coll_r_I","Coll_l_rel","Coll_r_rel","Extraction_losses"]
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_extraction = saving_files_summary_list_20200420.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_beam = saving_files_summary_list_20200420.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        self.df_subsystem_extraction_selected = df_subsystem_extraction
        self.df_subsystem_beam_selected = df_subsystem_beam
        print ("HEREEE")
        print (self.df_subsystem_extraction_selected)
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Target_rel,self.df_subsystem_beam_selected.Coll_r_rel.astype(float) + self.df_subsystem_beam_selected.Coll_l_rel.astype(float),data_df.Time,"Target I/Foil I","Collimators I/Foil I","Current [%]",1)
        #saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Coll_l_rel,self.df_subsystem_beam_selected.Coll_r_rel,time,"Coll l rel","Coll r rel",r"Current [%]",1)
        saving_files_summary_list_20200420.get_plots_three_functions_area(self,self.df_subsystem_beam_selected,data_df.Time,r"Current [$\mu$A]",0)
        self.sc1.draw()
        self.sc1.show()

def file_plot_magnet(self):
        [real_values,target_number,date_stamp] = saving_files_summary_list_20200420.get_data_tuple(str(self.fileName))
        print ("PLOTTING MAGNETIC FIELD")
        print (self.fileName)
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        target_current = data_df.Target_I.astype(float)
        current = 0
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        self.sc1.axes[0].clear()
        self.sc1.axes[1].clear()  
        self.df_subsystem_magnet_selected = self.df_subsystem_magnet_all[self.row_to_plot]    
        saving_files_summary_list_20200420.get_plots_one_functions_all(self,data_df.Magnet_I.astype(float),data_df.Time,self.fileName[-8:-4],"Magnet Current [A]",0)
        df_iso = saving_files_summary_list_20200420.get_isochronism(data_df)
        print ("HEREEEE ISO")
        print (df_iso)
        print ((df_iso.Coll_l_I).astype(float) + (df_iso.Coll_r_I).astype(float))
        saving_files_summary_list_20200420.get_plots_tunning(self,(df_iso.Coll_l_I).astype(float) + (df_iso.Coll_r_I).astype(float),df_iso.Target_I,df_iso.Foil_I,df_iso.Magnet_I,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)
        self.sc1.draw()
        self.sc1.show()
