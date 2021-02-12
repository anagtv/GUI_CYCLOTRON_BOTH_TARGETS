import my_fav_gui_20200522_1_4
import numpy as np
import pandas as pd
class plotting_data(editing_table,menus_functions):
    def __init__(self):
        super(plotting_data, self).__init__()
        menus.plot_source_actions(self)
        self.edit_actions()
        self.plot_actions()
 
    def file_plot(self):
        file_plots.file_plot(self)

    def plot_actions(self):
        self.openPlotI.setShortcut('Ctrl+E')
        self.openPlotI.setStatusTip('Plot files')
        self.openPlotI.triggered.connect(self.setting_plot_current)
        self.openPlotIV.triggered.connect(self.setting_plot_vacuum)
        self.openPlotRF.triggered.connect(self.setting_plot_RF)
        self.openPlotRFPower.triggered.connect(self.setting_plot_RF_power)
        self.openPlotM.triggered.connect(self.setting_plot_magnet)      
        self.openPlotEx.triggered.connect(self.setting_plot_extraction)
        self.openPlotColTarget.triggered.connect(self.setting_target_collimator)


    def edit_actions(self):      
        self.editplotmax.triggered.connect(self.flag_max)
        self.resetplotmax.triggered.connect(self.flag_max_reset)
        self.editplottarget1.triggered.connect(self.flag_target1)
        self.editplottarget4.triggered.connect(self.flag_target4)
        self.editplottarget1_add.triggered.connect(self.flag_target1_add)
        self.editplottarget4_add.triggered.connect(self.flag_target4_add)
        self.editplotweek.triggered.connect(self.flag_week)
        self.editplotday.triggered.connect(self.flag_day)
        self.editplottime.triggered.connect(self.flag_day_gap)
        self.editplottime_remove.triggered.connect(self.flag_no_day_gap)


    def setting_plot_current(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Arc_I.astype(float)
        self.ylabel = "Current [mA]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.y_values = self.file_df.Arc_V.astype(float)
        self.ylabel = r"Voltage [V]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()    

    def setting_plot_vacuum(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Arc_I.astype(float)
        self.ylabel = "Current [mA]"
        self.legend = "Source Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.y_values = self.file_df.Vacuum_P.astype(float)*1e5
        self.ylabel = r"[$10^{-5}$ mbar]"  
        self.legend = "Vacuum P"  
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_RF(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time 
        self.y_values_1 = self.file_df.Dee_1_kV.astype(float)
        self.y_values_2 = self.file_df.Dee_2_kV.astype(float)
        self.legend_1 = "Dee1"
        self.legend_2 = "Dee2"
        self.ylabel = "Voltage [kV]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values_1 = self.file_df.Flap1_pos.astype(float)
        self.y_values_2 = self.file_df.Flap2_pos.astype(float)
        self.legend_1 = "Flap1"
        self.legend_2 = "Flap2"
        self.ylabel = "Position [%]"
        file_plots.get_plots_two_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_RF_power(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values_1 = self.file_df.RF_fwd_W.astype(float)
        self.y_values_2 = self.file_df.RF_refl_W.astype(float)
        self.legend_1 = "Forwared"
        self.legend_2 = "Reflected"
        self.label_left = "Power [kW]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values = self.file_df.Phase_load.astype(float)
        self.legend = "Phase load"
        self.label = "Phase load"   
        file_plots.get_plots_one_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()

    def setting_plot_extraction(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values_1 = self.file_df.Extr_pos.astype(float)
        self.y_values_2 = self.file_df.Balance.astype(float)
        self.legend_1 = "Extr_pos"
        self.legend_2 = "Balance"
        self.ylabel = "Position [%]"
        file_plots.get_plots_two_functions_all(self,0)
        self.y_values_1 = self.file_df.Coll_l_I.astype(float)
        self.y_values_2 = self.file_df.Coll_r_I.astype(float)
        self.legend_1 = "Coll l "
        self.legend_2 = "Coll r"
        self.ylabel = "Current [$\mu$A]"
        file_plots.get_plots_two_functions_all(self,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()


    def setting_target_collimator(self):
        file_plots.setting_plot(self)
        self.x_values = self.df_subsystem_beam.Time
        self.y_values_1 = self.df_subsystem_beam.Target_rel.astype(float)
        self.y_values_2 = self.df_subsystem_beam.Coll_r_rel.astype(float) + self.df_subsystem_beam.Coll_l_rel.astype(float)
        self.legend_1 = "Target I/Foil I"
        self.legend_2 = "Collimators I/Foil I"
        self.ylabel = "Current [%]"
        file_plots.get_plots_two_functions_all(self,1)
        y_values_right = [self.file_df.Foil_I.astype(float),self.file_df.Target_I.astype(float),self.file_df.Coll_l_I.astype(float) + self.file_df.Coll_l_I.astype(float)]
        y_values_legend = ["Foil","Target","Collimators"]  
        self.ylabel = "Current [uA]" 
        self.x_values = self.file_df.Time
        for i in range(len(y_values_right)):
            self.y_values = y_values_right[i]
            self.y_legend = y_values_legend[i]
            self.get_plots_three_functions_area(0)


    def get_plots_three_functions_area(self,pn):
        self.sc1.axes[pn].fill_between(self.x_values,0,self.y_values,label= self.y_legend)
        self.sc1.axes[pn].legend(loc='best',ncol=1,fontsize=10)
        self.sc1.axes[pn].set_xlabel("Time [s]",fontsize=10)
        self.sc1.axes[pn].set_ylabel(str(self.ylabel),fontsize=10)
        ticks_to_use = self.x_values[::int(len(self.x_values)/6)]   
        ticks_to_use_list = self.x_values[::int(len(self.x_values)/6)] 
        self.sc1.axes[pn].set_xticks(ticks_to_use_list)
        self.sc1.axes[pn].set_xticklabels(ticks_to_use)
        #self.sc1.axes[pn].set_yticks(np.arange(min_value,max_value*1.1, step=5))
        self.sc1.axes[pn].tick_params(labelsize=10)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.axes[pn].tick_params(labelsize=10)
        self.sc1.draw()
        self.sc1.show()


    def setting_plot_magnet(self):
        file_plots.setting_plot(self)
        self.x_values = self.file_df.Time
        self.y_values = self.file_df.Magnet_I.astype(float)
        self.ylabel = "Current [A]"
        self.legend = "Magnet Current"
        file_plots.get_plots_one_functions_all(self,0)
        self.df_iso = saving_files_summary_list_20200420.get_isochronism(self.file_df)
        self.x_values = self.df_subsystem_beam.Time
        self.y_values_coll = (self.df_iso.Coll_l_I).astype(float) + (self.df_iso.Coll_r_I).astype(float)
        self.y_values_target = self.df_iso.Target_I
        self.y_values_foil = self.df_iso.Foil_I
        self.y_values_magnet = self.df_iso.Magnet_I
        self.label_left = r"Magnet current [A]"
        self.label_right = "Isochronism"
        file_plots.get_plots_tunning(self,self.y_values_coll,self.y_values_target,self.y_values_foil,self.y_values_magnet,1)
        self.sc1.fig.canvas.mpl_connect('pick_event', self.onpick)             
        self.sc1.draw()
        self.sc1.show()
        #file_plots.file_plot_iso_one_functions(self)
 

    #FLAGS

    def flag_max(self):
        print ("HEREEEEEEEEE MAX")
        self.max_min_value = "1"

    def flag_max_reset(self):
        print ("HEREEEEE MAX RESET")
        self.max_min_value = "0"

    def flag_target1(self):
        print ("HEREEEEE TARGET 1")
        self.target_1_value = "1"

    def flag_target1_add(self):
        print ("HEREEEEE TARGET 1 (ADD)")
        self.target_1_value = "0"

    def flag_target4(self):
        print ("HEREEEEE TARGET 4")
        print (self.target_2_value)
        self.target_2_value = "1"
        print (self.target_2_value)
        
    def flag_target4_add(self):
        print ("HEREEEEE TARGET 4 (ADD)")
        self.target_2_value = "0"

    def flag_week(self):
        print ("HEREEEEE WEEK")
        self.week_value = "1"
        self.day_value = "0"

    def flag_day(self):
        print ("HEREEEE DAY")
        self.week_value = "0"
        self.day_value = "1"
        
    def flag_no_day_gap(self):
        print ("HEREEEEEE NO GAP")
        self.flag_no_gap = "1"

    def flag_day_gap(self):
        self.flag_no_gap = "0"

    # FUNCTIONS USING A CONNECT 



    def handleSelectionChanged_variabletoplot(self):
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out",
        "table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out",
        "table_summary_transmission.out"]
        labels = ["CURRENT_","VOLTAGE_","RATIO_","SOURCE_PERFORMANCE_","PRESSURE_","CURRENT_","RELATIVE_TARGET_CURRENT_","EXTRACTION_LOSSES_","TRANSMISSION_"]
        labels_1 = ["DEE1_VOLTAGE_","FORWARD_POWER_","FLAP1_","CAROUSEL_POSITION_","COLL_CURRENT_L_","RELATIVE_COLL_CURRENT_L_","TARGET_CURRENT_"]
        labels_2 = ["DEE2_VOLTAGE_","REFLECTED_POWER_","FLAP2_","BALANCE_POSITION_","COLL_CURRENT_R_","RELATIVE_COLL_CURRENT_R_","FOIL_CURRENT_"]
        ylabel = ["CURRENT [mA]","VOLTAGE [V]",r"RATIO [mA/$\mu A$]",r"RATIO [$\mu A$/mA]",r"PRESSURE [$10^{-5}$mbar]","MAGNET CURRENT [A]",r"RELATIVE CURRENT (FOIL)[%]","LOSSES [%]",r"TRANSMISSION RATE [($\mu A$ Foil/$\mu A$ Probe) %]"]
        ylabel_d = ["AVERAGE VOLTAGE [kV]",r"AVERAGE POWER [kW]",r"AVERAGE POSITION [%]",r"POSITION [%]",r"CURRENT [$\mu A$]",r"RELATIVE CURRENT [%]",r"AVERAGE CURRENT [$\mu$A]"]
        file_name = ["ion_source_evolution.pdf","voltage_evolution.pdf","ratio_evolution.pdf","source_performance.pdf","vacuum_evolution.pdf","magnet_evolution.pdf","relative_currents_foil.pdf","efficiency_target_evolution.pdf","transmission.pdf"]
        file_name_d = ["dee1_dee2_voltage_evolution.pdf","power_evolution.pdf","flap_evolution.pdf","carousel_balance_evolution.pdf","collimator_current_evolution.pdf","absolute_collimator_current_evolution.pdf","target_foil_evolution.pdf"]
        legend = ["T","T","T","T","T","T","T","T","T"]
        legend_1 = ["DEE1","FORWARDED ","FLAP 1 ","CAROUSEL ","COLLIMATOR  L","COLLIMATOR  L","TARGET ","COLLIMATOR L ","TARGET "]
        legend_2 = ["DEE2","REFELECTED ","FLAP 2 ","BALANCE ","COLLIMATOR  R","COLLIMATOR  R","FOIL ","COLLIMATOR R ","FOIL "]
        #
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names[index.row()]))
        self.target_2 = int(np.max(self.tfs_input.drop_duplicates(subset="TARGET",keep = "first").TARGET))
        self.target_1 = int(np.min(self.tfs_input.drop_duplicates(subset="TARGET",keep = "first").TARGET))
        self.targets = [self.target_1,self.target_2]
        target_information_1 = target_information() 
        target_information_2 = target_information()
        target_information_1_extra = target_information() 
        target_information_2_extra = target_information()
        self.target_information_summary = [target_information_1,target_information_2]
        self.target_information_summary_extra = [target_information_1_extra,target_information_2_extra]
        self.sc3.axes.clear() 
        # Defining the classes for the two targets 
        for i in range(len(self.targets)):
            self.target_information_summary[i].selecting_data_to_plot_reset(self.targets[i],self.tfs_input)
            self.target_information_summary_extra[i].selecting_data_to_plot_reset(self.targets[i],self.tfs_input)       
        self.targets_summary = [self.target_information_summary]
        self.targets_summary_extra = [self.target_information_summary,self.target_information_summary_extra]
        #
        self.flag_max_reset()
        #
        if index.row() in [3,15]:
            self.flag_max()
        if index.row() == 5:
            uppper_limit = 1 
            lower_limit = 1
        else: 
            uppper_limit = 1.1
            lower_limit = 0.95
        if index.row() in [0,1,2,3,4,5]:   
            summary = [labels[index.row()],legend[index.row()],file_name[index.row()],"1"]
            limits = [ylabel[index.row()],uppper_limit,lower_limit]  
            if index.row() == 3:
                self.flag_max() 
                summary = [labels[index.row()],legend[index.row()],file_name[index.row()],"0"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)   
            else:                    
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)
        elif index.row() in [13,14,15]: 
            self.flag_max()
            summary = [labels[index.row()-7],legend[index.row()-7],file_name[index.row()-7],"0"]
            limits = [ylabel[index.row()-7],uppper_limit,lower_limit]     
            if index.row() == 15:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)
            else:
                summary = [labels[index.row()-7],legend[index.row()-7],file_name[index.row()-7],"1"]
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,summary,limits)           
        else: 
            self.flag_max()           
            summary = [labels_1[index.row()-6],labels_2[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],file_name_d[index.row()-6],"0"]
            limits = [ylabel_d[index.row()-6],uppper_limit,lower_limit]
            if index.row() in [10,11,12]:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,summary,limits)
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,summary,limits)
        self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)    
           
        
class target_information(editing_table):
    def __init__(self):
        self.index_foil_list = []
        self.index_foil_list_position = []
        self.unique_index_foil_sorted = []
        self.unique_index_foil = []
        self.index_foil_sorted = []
        self.index_foil_sorted_position = []
        self.ave_value = []
        self.max_value = []
        self.min_value = []
        self.std_value = []
        self.x_values = []
    
    def selecting_data_to_plot_reset(self,target,total):
        #self.foil_position = total[total.TARGET == str(target)].drop_duplicates(subset="FOIL",keep = "first").index
        self.foil_values = total[total.TARGET == str(target)].drop_duplicates(subset="FOIL",keep = "first").FOIL
        self.tfs_target = total[total.TARGET == str(target)]
        #self.tfs_target.reset_index(drop=True, inplace=True)
        #self.tfs_target_no_reset = (data)
        #self.tfs_unique_target = (self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))
        #self.tfs_unique_target_array = np.array(self.tfs_target.drop_duplicates(subset="FOIL",keep = "first"))
        