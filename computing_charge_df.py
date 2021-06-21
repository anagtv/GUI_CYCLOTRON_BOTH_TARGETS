import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os 
import pandas as pd
import saving_files_summary_list_20200420


COLUMN_NAMES = ["DATE","FILE","FOIL","TARGET","CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R"]
df_information = pd.DataFrame(columns=["DATE","FILE","FOIL","TARGET","CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R"])
TIME_PERIOD = [['2021-01-01','2021-01-31'],['2021-02-01','2021-02-31'],['2021-03-01','2021-03-31']]
LIST_NAMES = ["Arc_I","Foil_I","Coll_l_I","Target_I","Coll_r_I"]
FOIL_LIST_NAME = ["CURRENT_SOURCE","CURRENT_FOIL","CURRENT_COLL_L","CURRENT_TARGET","CURRENT_COLL_R"]
class target_cumulative_current:
    def __init__(self,df_information):
        self.df_information = df_information
        self.df_information_foil = df_information
        self.df_information["DATE"] = []
        self.df_information["FOIL"] = [] 
        self.df_information["TARGET"] = []
        self.df_information["CURRENT_SOURCE"] = [] 
        self.df_information["CURRENT_FOIL"] = []
        self.df_information["CURRENT_COLL_L"] = []
        self.df_information["CURRENT_TARGET"] = []
        self.df_information["CURRENT_COLL_R"] = []
    def selecting_data_to_plot_reset(self,file_df,target,date_stamp_i,file_number):
        foil_total = (file_df.Foil_No.iloc[-1])
        target_number_list = (int(target[1]))
        total_list = [date_stamp_i,float(file_number),foil_total,target_number_list]
        for name in LIST_NAMES: 
             total_list.append(getattr(file_df,name).astype(float).sum()*3/3600)
        df_individual = pd.DataFrame([total_list],columns=COLUMN_NAMES)
        self.df_information = self.df_information.append(df_individual)    
    def selecting_foil(self,file_df):       
        total_foil_list = [np.min(file_df.DATE),len(file_df.FILE),np.min(file_df.FOIL),np.min(file_df.TARGET)]
        for name in FOIL_LIST_NAME:
            total_foil_list.append(getattr(file_df,name).astype(float).sum())
        foil_total = (file_df.FOIL.iloc[-1])
        df_individual = pd.DataFrame([total_foil_list],columns=COLUMN_NAMES)
        self.df_information_foil = self.df_information_foil.append(df_individual) 

#selecting folder to analyze

def get_logfiles_from_folder(folder):
    filename_completed = []
    for file in os.listdir(folder):
        filename_completed.append(os.path.join(folder,file))
    return filename_completed 

def get_target_division(file,target_1,target_2):
    [target_number,date_stamp,name,file_number] = saving_files_summary_list_20200420.get_headers(file)
    real_values = saving_files_summary_list_20200420.get_irradiation_information(file)
    data_df = saving_files_summary_list_20200420.get_data(real_values)
    data_df_not_zero = data_df[data_df.Arc_I != "0"]
    if target_number[1] == "2": 
        target_1.selecting_data_to_plot_reset(data_df,target_number,date_stamp,file_number)
    else:
        target_2.selecting_data_to_plot_reset(data_df,target_number,date_stamp,file_number)

def get_summation_per_period(target):
    for i in range(len(TIME_PERIOD)):
        target.df_information_month = target.df_information[(target.df_information['DATE'] > TIME_PERIOD[i][0]) & (target.df_information['DATE'] < TIME_PERIOD[i][1])].sort_values(by="FILE").reset_index(drop=True)
    target.df_information_month.reset_index(drop=True)    
    foil_list = list(target.df_information_month.FOIL.drop_duplicates().index)
    foil_list.append(target.df_information_month.FOIL.index[-1])
    for i in range(len(foil_list)-1):
        df_information_foil = target.df_information_month[foil_list[i]:foil_list[i+1]-1]
        target.selecting_foil(df_information_foil)

def main():
    folder = "/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/MRS/LOGS/2021"
    filename_completed  = get_logfiles_from_folder(folder)
    target_1 = target_cumulative_current(df_information)
    target_2 = target_cumulative_current(df_information)
    for file in filename_completed:
         get_target_division(file,target_1,target_2)
    get_summation_per_period(target_1)

if __name__ == "__main__":
    main()






