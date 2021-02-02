def handleSelectionChanged_variabletoplot(self, selected, deselected):
        index=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        print ("ENTERING HEREE!!!!!")
        print(index.row())
        summary_file_names = ["table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_source.out","table_summary_vacuum.out","table_summary_magnet.out","table_summary_transmission.out"]
        summary_file_names_d = ["table_summary_rf.out","table_summary_rf.out","table_summary_rf.out","table_summary_extraction.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_beam.out","table_summary_transmission.out","table_summary_beam.out"]
        labels = ["CURRENT_","VOLTAGE_","RATIO_","SOURCE_PERFORMANCE","PRESSURE_","CURRENT_","RELATIVE_TARGET_CURRENT_","EXTRACTION_LOSSES_","TRANSMISSION"]
        labels_1 = ["DEE1_VOLTAGE_","FORWARD_POWER_","FLAP1_","CAROUSEL_POSITION_","COLL_CURRENT_L_","RELATIVE_COLL_CURRENT_L_","TARGET_CURRENT_"]
        labels_2 = ["DEE2_VOLTAGE_","REFLECTED_POWER_","FLAP2_","BALANCE_POSITION_","COLL_CURRENT_R_","RELATIVE_COLL_CURRENT_R_","FOIL_CURRENT_"]
        ylabel = ["CURRENT [mA]","VOLTAGE [V]",r"RATIO [mA/$\mu A$]",r"RATIO [$\mu A$/mA]",r"PRESSURE [$10^{-5}$mbar]","MAGNET CURRENT [A]",r"RELATIVE CURRENT (FOIL)[%]","LOSSES [%]",r"TRANSMISSION RATE [($\mu A$ Foil/$\mu A$ Probe) %]"]
        ylabel_d = ["AVERAGE VOLTAGE [kV]",r"AVERAGE POWER [kW]",r"AVERAGE POSITION [%]",r"POSITION [%]",r"CURRENT [$\mu A$]",r"RELATIVE CURRENT [%]",r"AVERAGE CURRENT [$\mu$A]"]
        file_name = ["ion_source_evolution.pdf","voltage_evolution.pdf","ratio_evolution.pdf","source_performance.pdf","vacuum_evolution.pdf","magnet_evolution.pdf","relative_currents_foil.pdf","efficiency_target_evolution.pdf","transmission.pdf"]
        file_name_d = ["dee1_dee2_voltage_evolution.pdf","power_evolution.pdf","flap_evolution.pdf","carousel_balance_evolution.pdf","collimator_current_evolution.pdf","absolute_collimator_current_evolution.pdf","target_foil_evolution.pdf"]
        legend = ["T","T","T","T","T","T","T","T","T"]
        legend_1 = ["DEE1 T","FORWARDED T","FLAP 1 T","CAROUSEL T","COLLIMATOR  T","COLLIMATOR  T","TARGET T","COLLIMATOR L T","TARGET T"]
        legend_2 = ["DEE2 T","REFELECTED T","FLAP 2 T","BALANCE T","COLLIMATOR  T","COLLIMATOR  T","FOIL T","COLLIMATOR R T","FOIL T"]
        print ("INDEX")
        print (index.row())
        self.sc3.axes.clear()
        if index.row() in [0,1,2,3,4,5]:
            self.sc3.axes.clear()
            self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names[index.row()]))
            self.sc3.axes.clear()
            tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("1")])
            tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1.reset_index(drop=True, inplace=True)
            tfs_target_4.reset_index(drop=True, inplace=True)
            # Same filter but keeping the previous index
            tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            # filtering: removing duplicates from dataframe
            tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
            tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
            print ("LEN")
            print (len(tfs_unique_target_1))
            if len(tfs_target_1) == 0:
                tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                tfs_target_1.reset_index(drop=True, inplace=True)
                tfs_target_4.reset_index(drop=True, inplace=True)
                # Same filter but keeping the previous index
                tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                # filtering: removing duplicates from dataframe
                tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                print ("THEN YOU ARE HEREE")
                print (tfs_target_1)
                print (tfs_target_4)
            # sorting foil list
            index_foil_list_1 = []
            index_foil_list_4 = []
            index_foil_list_1_position = []
            index_foil_list_4_position = []
            unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
            unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
            for i in range(len(tfs_unique_target_1.FOIL)):
               # get all the positions where a given foil is and convert to a list (TARGET 1)
               index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1 = index_foil_1.tolist()
               # list of positions within the dataframe T1
               index_foil_list_1.append(index_foil_tolist_1)
               index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1_position = index_foil_1_position.tolist()
               # list of positions in the original dataframe
               index_foil_list_1_position.append(index_foil_tolist_1_position)
            for i in range(len(tfs_unique_target_4.FOIL)): 
               # get all the positions where a given foil is and convert to a list (TARGET 4)
               index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4 = index_foil_4.tolist()
               index_foil_list_4.append(index_foil_tolist_4)
               index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4_position = index_foil_4_position.tolist()
               index_foil_list_4_position.append(index_foil_tolist_4_position)
            print ("AND HERE")
            print (index_foil_list_1)
            print (index_foil_list_4)
            index_foil_sorted_1 = np.sort(index_foil_list_1)
            index_foil_sorted_4 = np.sort(index_foil_list_4)
            print ("CHECKING ALSO HERE")
            print (index_foil_sorted_1)
            print (index_foil_sorted_4)
            print (np.array(index_foil_sorted_1))
            print (np.array(index_foil_sorted_4))
            unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
            unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
            index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
            index_foil_sorted_4_position = np.sort(index_foil_list_4_position)     
            if index.row() == 4:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            elif index.row() == 3: 
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,0,self.flag_no_gap,1)
            else:
                  plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()],ylabel[index.row()],file_name[index.row()],legend[index.row()],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)        
        elif index.row() in [13,14,15]:
            self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-7]))
            self.sc3.axes.clear()
            tfs_target_1 = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
            tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
            tfs_target_1.reset_index(drop=True, inplace=True)
            tfs_target_4.reset_index(drop=True, inplace=True)
            tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
            tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
            if len(tfs_target_1) == 0:
                tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                tfs_target_1.reset_index(drop=True, inplace=True)
                tfs_target_4.reset_index(drop=True, inplace=True)
                # Same filter but keeping the previous index
                tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                # filtering: removing duplicates from dataframe
                tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                print ("THEN YOU ARE HEREE")
                print (tfs_target_1)
                print (tfs_target_4)
            index_foil_list_1 = []
            index_foil_list_4 = []
            index_foil_list_1_position = []
            index_foil_list_4_position = []
            unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
            unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
            for i in range(len(tfs_unique_target_1.FOIL)):
               index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1 = index_foil_1.tolist()
               index_foil_list_1.append(index_foil_tolist_1)
               index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
               index_foil_tolist_1_position = index_foil_1_position.tolist()
               index_foil_list_1_position.append(index_foil_tolist_1_position)
            for i in range(len(tfs_unique_target_4.FOIL)): 
               index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4 = index_foil_4.tolist()
               index_foil_list_4.append(index_foil_tolist_4)
               index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
               index_foil_tolist_4_position = index_foil_4_position.tolist()
               index_foil_list_4_position.append(index_foil_tolist_4_position)
            index_foil_sorted_1 = np.sort(index_foil_list_1)
            index_foil_sorted_4 = np.sort(index_foil_list_4)
            unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
            unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
            index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
            index_foil_sorted_4_position = np.sort(index_foil_list_4_position)       
            if index.row() == 15:
                print (self.tfs_input)
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_no_std(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,0) 
            else:
                plotting_summary_files_one_target_1_4.generic_plot_no_gap_one_quantitie_with_foil(self,self.tfs_input,labels[index.row()-7],ylabel[index.row()-7],file_name[index.row()-7],legend[index.row()-7],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.max_min_value,self.target_1_value,self.target_4_value,self.week_value,1,self.flag_no_gap,1)
                          #self.sc3.draw()
              #self.sc3.show()
              #print (ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5])        
        elif index.row() in [10,11,12]:
                  self.sc3.axes.clear()
                  self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-6]))
                  #self.sc3.axes.clear()
                  print ("FOIL NUMBER")
                  print (self.tfs_input.FOIL)
                  tfs_target_1 = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
                  tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("4")])
                  tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("1")]))
                  tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("4")])
                  tfs_target_1.reset_index(drop=True, inplace=True)
                  tfs_target_4.reset_index(drop=True, inplace=True)
                  tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                  tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                  if len(tfs_target_1) == 0:
                      tfs_target_1 = (self.tfs_input[self.tfs_input.TARGET == ("2")])
                      tfs_target_4 = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                      tfs_target_1.reset_index(drop=True, inplace=True)
                      tfs_target_4.reset_index(drop=True, inplace=True)
                      # Same filter but keeping the previous index
                      tfs_target_1_no_reset = ((self.tfs_input[self.tfs_input.TARGET == ("2")]))
                      tfs_target_4_no_reset = (self.tfs_input[self.tfs_input.TARGET == ("5")])
                      # filtering: removing duplicates from dataframe
                      tfs_unique_target_1 = (tfs_target_1.drop_duplicates(subset="FOIL",keep = "first"))
                      tfs_unique_target_4 = (tfs_target_4.drop_duplicates(subset="FOIL",keep = "first"))
                      print ("THEN YOU ARE HEREE")
                      print (tfs_target_1)
                      print (tfs_target_4)
                  print (tfs_target_1.FOIL)
                  print (tfs_target_4.FOIL)
                  print (tfs_unique_target_1.FOIL)
                  print (tfs_unique_target_4.FOIL)
                  index_foil_list_1 = []
                  index_foil_list_4 = []
                  index_foil_list_1_position = []
                  index_foil_list_4_position = []
                  unique_index_foil_1 = np.array(tfs_unique_target_1.FOIL)
                  unique_index_foil_4 = np.array(tfs_unique_target_4.FOIL)
                  for i in range(len(tfs_unique_target_1.FOIL)):
                     index_foil_1 = (((tfs_target_1.FOIL[tfs_target_1["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
                     index_foil_tolist_1 = index_foil_1.tolist()
                     index_foil_list_1.append(index_foil_tolist_1)
                     index_foil_1_position = (((tfs_target_1_no_reset.FOIL[tfs_target_1_no_reset["FOIL"] == tfs_unique_target_1.FOIL.iloc[i]].index)))
                     index_foil_tolist_1_position = index_foil_1_position.tolist()
                     index_foil_list_1_position.append(index_foil_tolist_1_position)
                  for i in range(len(tfs_unique_target_4.FOIL)): 
                     print ("TARGET 4 RESULTS")
                     print (tfs_unique_target_4.FOIL.iloc[i])
                     index_foil_4 = (((tfs_target_4.FOIL[tfs_target_4["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
                     print (index_foil_4)
                     index_foil_tolist_4 = index_foil_4.tolist()
                     index_foil_list_4.append(index_foil_tolist_4)
                     index_foil_4_position = (((tfs_target_4_no_reset.FOIL[tfs_target_4_no_reset["FOIL"] == tfs_unique_target_4.FOIL.iloc[i]].index)))
                     index_foil_tolist_4_position = index_foil_4_position.tolist()
                     index_foil_list_4_position.append(index_foil_tolist_4_position)
                  print ("INDEX")
                  print (index_foil_1_position)
                  print (index_foil_list_1_position)
                  index_foil_sorted_1 = np.sort(index_foil_list_1)
                  index_foil_sorted_4 = np.sort(index_foil_list_4)
                  unique_index_foil_sorted_1 = [unique_index_foil_1 for _,unique_index_foil_1 in sorted(zip(index_foil_list_1,unique_index_foil_1))]
                  unique_index_foil_sorted_4 = [unique_index_foil_4 for _,unique_index_foil_4 in sorted(zip(index_foil_list_4,unique_index_foil_4))]
                  index_foil_sorted_1_position = np.sort(index_foil_list_1_position)
                  index_foil_sorted_4_position = np.sort(index_foil_list_4_position)
                  print ("SORTED")
                  print (unique_index_foil_sorted_1)
                  print (index_foil_sorted_1)
                  print (index_foil_sorted_1_position)
                  if index.row() == 12:
                     #plotting_summary_files_one_target.generic_plot_no_gap_two_quantities(self,tfs_input,labels_1[index.row()-5],labels_2[index.row()-5],ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5],self.output_path) 
                     plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_with_foil(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)
                     #self.sc3.draw()
                  else:
                     print (labels_1[index.row()-6])
                     print (labels_2[index.row()-6])
                     print (ylabel_d[index.row()-6])
                     print (file_name_d[index.row()-6])
                     plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_collimators(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],index_foil_sorted_1,unique_index_foil_sorted_1,index_foil_sorted_4,unique_index_foil_sorted_4,index_foil_sorted_1_position,index_foil_sorted_4_position,self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)

        
        else:
              print ("OR HERE")
              print (labels_1[index.row()-5])
              print (labels_2[index.row()-5])
              print (ylabel_d[index.row()-5],file_name_d[index.row()-5],legend_1[index.row()-5],legend_2[index.row()-5])
              self.tfs_input = tfs.read(os.path.join(self.output_path,summary_file_names_d[index.row()-6]))
              print (summary_file_names_d[index.row()-5])
              self.sc3.axes.clear()
              if index.row() == 9:
                   print ("EXTRACTION")
                   print (self.tfs_input)
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities_extraction(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.max_min_value,1,self.flag_no_gap)       
              else: 
                   print ("HEREEEE")
                   print (labels_1[index.row()-6])
                   print (labels_2[index.row()-6])
                   print (file_name_d[index.row()-6])
                   print (self.tfs_input)
                   plotting_summary_files_one_target_1_4.generic_plot_no_gap_two_quantities(self,self.tfs_input,labels_1[index.row()-6],labels_2[index.row()-6],ylabel_d[index.row()-6],file_name_d[index.row()-6],legend_1[index.row()-6],legend_2[index.row()-6],self.output_path,self.target_1_value,self.target_4_value,self.week_value,self.flag_no_gap)       

              #self.sc3.draw()
              #self.sc3.show()
        self.sc3.fig.canvas.mpl_connect('pick_event', self.onpick_trends)
        self.sc3.draw()
        self.sc3.show()
