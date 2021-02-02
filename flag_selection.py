#import my_fav_gui_20200522_1_4

#def flag_max(self):
#        self.max_min_value = 1
#        #print ("CHANGIN PLOTTT")
#        my_fav_gui_20200522_1_4.handleSelectionChanged_variabletoplot(self)
#        self.sc3.draw()
#       self.sc3.show()
def flag_max_reset(self):
        self.max_min_value = 0

def flag_target4(self):
        self.target_4_value = 1
        
def flag_target4_add(self):
        self.target_4_value = 0
        
def flag_week(self):
        self.week_value = 1
        self.day_value = 0

def flag_day(self):
        self.week_value = 0
        self.day_value = 1

def flag_target1(self):
        self.target_1_value = 1

def flag_target1_add(self):
        self.target_1_value = 0
        
def flag_no_day_gap(self):
        self.flag_no_gap = 1 
        print ("REMOVING GAPS")
        print (self.flag_no_gap)

def flag_day_gap(self):
        self.flag_no_gap = 0
        print ("REMOVING GAPS")
        print (self.flag_no_gap)

if __name__ == "__main__":
    main()