import saving_files_summary_list_20200420
import getting_subsystems 
import numpy as np
import pandas as pd
def setting_plot(self):
    self.sc1.axes[0].clear()
    self.sc1.axes[1].clear()

def compute_max_min_function(self):
    max_function = (float(np.max(self.y_values)))
    min_function = (float(np.min(self.y_values)))
    max_function2 = (float(np.max(self.y_values_right_2)))
    min_function2 = (float(np.min(self.y_values_right_2)))
    max_value = np.max([max_function1,max_function2])
    min_value = np.max([min_function1,min_function2])
    ticks_to_use = self.x_values[::int(len(self.x_values)/6)]   
    ticks_to_use_list = self.x_values[::int(len(self.x_values)/6)] 
    self.sc1.axes[pn].set_xticks(ticks_to_use_list)
    self.sc1.axes[pn].set_xticklabels(ticks_to_use)



def get_plots_tunning(self,current_col,current_target,current_foil,magnet_current,pn):
    self.sc1.axes[pn].plot(magnet_current,current_col,'o',label="Collimators",picker=5)
    self.sc1.axes[pn].plot(magnet_current,current_target,'o',label="Target",picker=5)
    self.sc1.axes[pn].plot(magnet_current,current_foil,'o',label="Foil",picker=5)
    #self.sc1.axes[pn].plot(time,function2,label=file_names[1])
    self.sc1.axes[pn].legend(loc='best',ncol=5,fontsize=10)
    self.sc1.axes[pn].set_xlabel("Magnet Current [A]",fontsize=10)
    self.sc1.axes[pn].set_ylabel(str(r"Current [$\mu$A]"),fontsize=10)
    print ("HEREEEEEEE")
    ##print (ticks_to_use_list)
    print (magnet_current)
    self.sc1.axes[pn].tick_params(labelsize=10)


# SOURCE 
def get_plots_two_functions_all(self,pn):
    self.sc1.axes[pn].plot(self.x_values,self.y_values_1,label=self.legend_1,picker=5)
    self.sc1.axes[pn].plot(self.x_values,self.y_values_2,label=self.legend_2,picker=5)
    self.sc1.axes[pn].legend(loc='best',ncol=5,fontsize=10)
    self.sc1.axes[pn].set_xlabel("Time [s]",fontsize=10)
    self.sc1.axes[pn].set_ylabel(str(self.ylabel),fontsize=10)
    max_function1 = (float(np.max(self.y_values_1)))
    min_function1 = (float(np.min(self.y_values_1)))
    max_function2 = (float(np.max(self.y_values_2)))
    min_function2 = (float(np.min(self.y_values_2)))
    max_value = np.max([max_function1,max_function2])
    min_value = np.max([min_function1,min_function2])
    ticks_to_use = self.x_values[::int(len(self.x_values)/6)]   
    ticks_to_use_list = self.x_values[::int(len(self.x_values)/6)] 
    self.sc1.axes[pn].set_xticks(ticks_to_use_list)
    self.sc1.axes[pn].set_xticklabels(ticks_to_use)
    self.sc1.axes[pn].tick_params(labelsize=10)

def get_plots_one_functions_all(self,pn):
    self.sc1.axes[pn].plot(self.x_values,self.y_values,label=self.legend,picker=5)
    self.sc1.axes[pn].legend(loc='best',ncol=5,fontsize=10)
    self.sc1.axes[pn].set_xlabel("Time [s]",fontsize=10)
    self.sc1.axes[pn].set_ylabel(str(self.ylabel),fontsize=10)
    max_value = (float(np.max(self.y_values)))
    min_value = (float(np.min(self.y_values)))
    ticks_to_use = self.x_values[::int(len(self.x_values)/6)]   
    ticks_to_use_list = self.x_values[::int(len(self.x_values)/6)] 
    yticks_to_use = self.y_values.index[::int(len(self.y_values)/6)]
    diference = max(self.y_values)+2 - min(self.y_values)
    self.sc1.axes[pn].set_xticks(ticks_to_use_list)
    self.sc1.axes[pn].set_xticklabels(ticks_to_use)
    self.sc1.axes[pn].tick_params(labelsize=10)


def file_plot_collimators_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = getting_subsystems.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        df_subsystem_beam = getting_subsystems.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        #saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),df_subsystem_beam.Target_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]","Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Coll_l_I.astype(float) + df_subsystem_beam.Coll_r_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Collimator Current [$\mu$A]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_beam.Target_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Target Current [$\mu$A]",1)
        self.sc4.draw()
        self.sc4.show()

def file_plot_vacuum_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = getting_subsystems.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_vacuum = getting_subsystems.get_subsystems_dataframe_vacuum(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_magnet = getting_subsystems.get_subsystems_dataframe_magnet(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_vacuum.Vacuum_P.astype(float)*1e5,df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Vacuum P [$10^{5}$ mbar]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_magnet.Magnet_I.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Magnet Current [A]",1)
        self.sc4.draw()
        self.sc4.show()

    
def file_plot_rf_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current) 
        df_subsystem_source = getting_subsystems.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_rf = getting_subsystems.get_subsystems_dataframe_rf(data_df,current,target_number,target_current,time,foil_number)
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_1_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 1)[V]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_rf.Dee_2_kV.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Voltage (Dee 2) [V]",1)
        self.sc4.draw()
        self.sc4.show()
    


def file_plot_extraction_source(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
        data_df = saving_files_summary_list_20200420.get_data(real_values)
        [target_current,current] = saving_files_summary_list_20200420.get_target_parameters(data_df)
        time = saving_files_summary_list_20200420.get_time(data_df,current)
        foil_number = saving_files_summary_list_20200420.get_foil_number(data_df,current)
        df_subsystem_source = getting_subsystems.get_subsystems_dataframe_source(data_df,current,target_number,target_current,time,foil_number)
        df_subsystem_extraction = getting_subsystems.get_subsystems_dataframe_extraction(data_df,current,target_number,target_current,time,foil_number)
        self.sc4.axes[0].clear()
        self.sc4.axes[1].clear()
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Extr_pos.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Extraction Position [%]",0)
        saving_files_summary_list_20200420.get_plots_one_functions_source(self,df_subsystem_extraction.Balance.astype(float),df_subsystem_source.Arc_I.astype(float),"Source Current [mA]",r"Balance Position [%]",1)
        self.sc4.draw()
        self.sc4.show()



def file_plot_extraction(self):
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
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
        [real_values,target_number,date_stamp ] = saving_files_summary_list_20200420.get_data_tuple(str(self.self.fileName))
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
        df_subsystem_beam = getting_subsystems.get_subsystems_dataframe_beam(data_df,current,target_number,target_current,time,foil_number)
        self.df_subsystem_beam_selected = df_subsystem_beam
        self.df_subsystem_beam_selected = self.df_subsystem_beam_all[self.row_to_plot]
        saving_files_summary_list_20200420.get_plots_two_functions_all(self,data_df.Foil_I.astype(float),data_df.Target_I.astype(float),data_df.Time,"Foil I","Target I",r"Current [$\mu$A]",1)
        #saving_files_summary_list_20200420.get_plots_two_functions_all(self,self.df_subsystem_beam_selected.Coll_l_rel,self.df_subsystem_beam_selected.Coll_r_rel,time,"Coll l rel","Coll r rel",r"Current [%]",1)
        saving_files_summary_list_20200420.get_plots_three_functions_area(self,self.df_subsystem_beam_selected,data_df.Time,r"Current [$\mu$A]",0)
        self.sc1.draw()
        self.sc1.show()


def get_plots_two_functions_source(self,function_horizontal,function1_vertical,function2_vertical,label1,label2,ylabel,xlabel,pn):
    function_horizontal_list = (list(range(len(function_horizontal))))
    #print ("HEREEEEEE")
    #print (function_horizontal)
    #print (np.max(function_horizontal))
    #print (function1_vertical)
    #print (function2_vertical)
    self.sc4.axes[pn].errorbar(function_horizontal,function1_vertical,label=label1,picker=5,fmt="o")
    self.sc4.axes[pn+1].errorbar(function_horizontal,function2_vertical,label=label2,picker=5,fmt="o")
    self.sc4.axes[pn].legend(loc='best',ncol=5,fontsize=10)
    self.sc4.axes[pn+1].legend(loc='best',ncol=5,fontsize=10)
    self.sc4.axes[pn].set_xlabel(str(xlabel),fontsize=10)
    self.sc4.axes[pn].set_xlim([0,10])
    self.sc4.axes[pn].set_ylabel(str(ylabel),fontsize=10)
    self.sc4.axes[pn+1].set_xlabel(str(xlabel),fontsize=10)
    self.sc4.axes[pn+1].set_xlim([0,10])
    self.sc4.axes[pn+1].set_ylabel(str(ylabel),fontsize=10)
    max_function1 = (float(np.max(function1_vertical)))
    min_function1 = (float(np.min(function1_vertical)))
    max_function2 = (float(np.max(function2_vertical)))
    min_function2 = (float(np.min(function2_vertical)))
    max_value = np.max([max_function1,max_function2])
    min_value = np.max([min_function1,min_function2])
    #ticks_to_use = function_horizontal[::int(len(function_horizontal)/6)]   
    #ticks_to_use_list = function_horizontal[::int(len(function_horizontal)/6)] 
    #self.sc4.axes[pn].set_xticks(ticks_to_use_list)
    #self.sc4.axes[pn].set_xticklabels(ticks_to_use)
    #self.sc1.axes[pn].set_yticks(np.arange(min_value,max_value*1.1, step=5))
    #self.sc4.axes[pn].tick_params(labelsize=10)

def get_plots_one_functions_source(self,function_horizontal,function1_vertical,ylabel,xlabel,pn):
    function_horizontal_list = (list(range(len(function_horizontal))))
    self.sc4.axes[pn].errorbar(function_horizontal,function1_vertical,fmt="o",picker=5)
    self.sc4.axes[pn].set_ylabel(str(ylabel),fontsize=10)
    self.sc4.axes[pn].set_xlabel(str(xlabel),fontsize=10)
    max_value = (float(np.max(function1_vertical)))
    min_value = (float(np.min(function1_vertical)))
    self.sc4.axes[pn].set_xlim([0.95*min(function_horizontal),1.01*max(function_horizontal)])
    self.sc4.axes[pn].tick_params(labelsize=10)
