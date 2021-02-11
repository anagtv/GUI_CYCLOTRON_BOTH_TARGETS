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
