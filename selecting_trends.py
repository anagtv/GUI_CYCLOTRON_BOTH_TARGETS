import tfs
import numpy as np
import os

def onpick_trends(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         self.coordinates_x = xdata[ind][0]
         self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str("CYCLOTRON")))
         self.tablestatistic_tab2.setItem(0,1, QTableWidgetItem(self.name))
         self.tablestatistic_tab2.setItem(1,1, QTableWidgetItem(str(self.tfs_input.DATE.iloc[self.coordinates_x][5:])))
         self.tablestatistic_tab2.setItem(2,1, QTableWidgetItem(str(self.tfs_input.FILE.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(3,1, QTableWidgetItem(str(self.tfs_input.FOIL.iloc[self.coordinates_x])))
         self.tablestatistic_tab2.setItem(1,0, QTableWidgetItem(str("DATE")))
         self.tablestatistic_tab2.setItem(2,0, QTableWidgetItem(str("FILE")))
         self.tablestatistic_tab2.setItem(3,0, QTableWidgetItem(str("FOIL")))
         print ("COLUMN INDEX")
         index = ((self.tablefiles_tab2.selectionModel().currentIndex()))
         print (index.row())
         ["PRESSURE_AVE","PRESSURE_STD"]
         COLUMNS_MAGNET = ["CURRENT_AVE","CURRENT_STD"]
         COLUMNS_RF =  ["DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD",
            "FORWARD_POWER_AVE","FORWARD_POWER_STD","REFLECTED_POWER_AVE","REFLECTED_POWER_STD"]
         COLUMNS_BEAM = ["COLL_CURRENT_L_STD","COLL_CURRENT_R_AVE","COLL_CURRENT_R_STD",
            "RELATIVE_COLL_CURRENT_L_AVE","RELATIVE_COLL_CURRENT_L_STD",
            "RELATIVE_COLL_CURRENT_R_AVE","RELATIVE_COLL_CURRENT_R_STD",
             "TARGET_CURRENT_AVE","TARGET_CURRENT_STD",
             "FOIL_CURRENT_AVE","FOIL_CURRENT_STD",
             "EXTRACTION_LOSSES_AVE","EXTRACTION_LOSSES_STD"]
         COLUMNS_EXTRACTION = ["CAROUSEL_POSITION_AVE","CAROUSEL_POSITION_STD","BALANCE_POSITION_AVE","BALANCE_POSITION_STD"]
         if index.row() in [0,1,2]:
            print (self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x])
            print (self.tfs_input.VOLTAGE_AVE.iloc[self.coordinates_x])
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("CURRENT [mA]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("VOLTAGE [V]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("RATIO [mA/uA]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            current_value = str(round(self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CURRENT_STD.iloc[self.coordinates_x],1))
            voltage_value = str(round(self.tfs_input.VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-"+ str(round(self.tfs_input.VOLTAGE_STD.iloc[self.coordinates_x],1))
            ratio_value = str(round(self.tfs_input.RATIO_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RATIO_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(current_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(voltage_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(ratio_value))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 4:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("PRESSURE [10-5 mbar]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            vacuum_value = str(round(self.tfs_input.PRESSURE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.PRESSURE_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(vacuum_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 5:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("MAGNET CURRENT [A]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            current_value = str(round(self.tfs_input.CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CURRENT_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(current_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [6,7,8]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("DEE1 VOLTAGE [kV]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("DEE2 VOLTAGE [kV]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("FORWARDED POWER [kW]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem(str("REFLECTED POWER [kW]")))
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem(str("FLAP1 POSITION [%]")))
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem(str("FLAP2 POSITION [%]")))
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            dee1_voltage_value = str(round(self.tfs_input.DEE1_VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.DEE1_VOLTAGE_STD.iloc[self.coordinates_x],1))
            dee2_voltage_value = str(round(self.tfs_input.DEE2_VOLTAGE_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.DEE2_VOLTAGE_STD.iloc[self.coordinates_x],1))
            for_power_value = str(round(self.tfs_input.FORWARD_POWER_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FORWARD_POWER_STD.iloc[self.coordinates_x],1))
            ref_power_value = str(round(self.tfs_input.REFLECTED_POWER_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.REFLECTED_POWER_STD.iloc[self.coordinates_x],1))
            flap1_pos_value = str(round(self.tfs_input.FLAP1_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FLAP1_STD.iloc[self.coordinates_x],1))
            flap2_pos_value = str(round(self.tfs_input.FLAP2_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.FLAP2_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(dee1_voltage_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(dee2_voltage_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(for_power_value))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem(ref_power_value))
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem(flap1_pos_value))
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem(flap2_pos_value))
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() == 9:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("CAROUSSEL [%]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("BALANCE [%]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            caroussel_value = str(round(self.tfs_input.CAROUSEL_POSITION_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.CAROUSEL_POSITION_STD.iloc[self.coordinates_x],1))
            balance_value = str(round(self.tfs_input.BALANCE_POSITION_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.BALANCE_POSITION_STD.iloc[self.coordinates_x],1)) 
            print ("HEREEEEEEEEEE")
            print (caroussel_value)
            print (balance_value)         
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(caroussel_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(balance_value))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [10,11,12,13]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("COLLIMATORS CURRENT L [uA]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem(str("COLLIMATORS CURRENT R [uA]")))
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem(str("COLLIMATORS [uA]")))
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem(str("COLLIMATORS CURRENT REL L[%]")))
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem(str("COLLIMATORS CURRENT REL R[%]")))
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem(str("COLLIMATORS[%]")))
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem(str("TARGET CURRENT [uA]")))
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem(str("FOIL CURRENT [uA]")))
            coll_current_value_l = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x],1))
            coll_current_value_r = str(round(self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x],1))
            coll_current_rel_value_l = str(round(self.tfs_input.RELATIVE_COLL_CURRENT_L_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_COLL_CURRENT_L_STD.iloc[self.coordinates_x],1))
            coll_current_rel_value_r = str(round(self.tfs_input.RELATIVE_COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_COLL_CURRENT_R_STD.iloc[self.coordinates_x],1))
            coll_current = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1) ) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x] ,1))
            coll_current_rel = str(round(self.tfs_input.COLL_CURRENT_L_AVE.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_AVE.iloc[self.coordinates_x],1) ) + "+-" + str(round(self.tfs_input.COLL_CURRENT_L_STD.iloc[self.coordinates_x] + self.tfs_input.COLL_CURRENT_R_STD.iloc[self.coordinates_x] ,1))
            target_current_value = str(round(self.tfs_input.TARGET_CURRENT_AVE.iloc[self.coordinates_x],1)) + " " + str(round(self.tfs_input.TARGET_CURRENT_STD.iloc[self.coordinates_x],1))
            target_current_rel_value = str(round(self.tfs_input.RELATIVE_TARGET_CURRENT_AVE.iloc[self.coordinates_x],1)) + "+-" + str(round(self.tfs_input.RELATIVE_TARGET_CURRENT_STD.iloc[self.coordinates_x],1))
            foil_current_value = str(round(self.tfs_input.FOIL_CURRENT_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.FOIL_CURRENT_STD.iloc[self.coordinates_x],1))
            extraction_losses_value = str(round(self.tfs_input.EXTRACTION_LOSSES_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.EXTRACTION_LOSSES_STD.iloc[self.coordinates_x],1))
            print ("HEREEEEEE")
            print (coll_current)
            print (coll_current_rel)
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(coll_current_value_l))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem(coll_current_value_r))
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem(coll_current))
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem(coll_current_rel_value_l))
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem(coll_current_rel_value_r))
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem(coll_current_rel))
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem(target_current_value))
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem(foil_current_value))
         elif index.row() in [14]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("EXTRACTION LOSSES [%]")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            extraction_losses_value = str(round(self.tfs_input.EXTRACTION_LOSSES_AVE.iloc[self.coordinates_x],1)) + "+- " + str(round(self.tfs_input.EXTRACTION_LOSSES_STD.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(extraction_losses_value))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())
         elif index.row() in [15]:
            self.tablestatistic_tab2.setItem(4,0, QTableWidgetItem(str("TRANSMISSION")))
            self.tablestatistic_tab2.setItem(5,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,0, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,0, QTableWidgetItem())
            transmission = str(round(self.tfs_input.TRANSMISSION.iloc[self.coordinates_x],1))
            self.tablestatistic_tab2.setItem(4,1, QTableWidgetItem(transmission))
            self.tablestatistic_tab2.setItem(5,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(6,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(7,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(8,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(9,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(10,1, QTableWidgetItem())
            self.tablestatistic_tab2.setItem(11,1, QTableWidgetItem())