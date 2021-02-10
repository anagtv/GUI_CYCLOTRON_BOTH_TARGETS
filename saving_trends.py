import os 
import numpy as np
import saving_files_summary_list_20200420
import managing_files
import tfs

def getting_summary(self):
        input_path_filtered = []
        file_path = []
        for file in os.listdir(self.fileName_folder):
            print (file)
            file_path.append(file)
            input_path_filtered.append(os.path.getsize(os.path.join(self.fileName_folder, file)))
            input_path_filtered_array = np.array(input_path_filtered)
        file_path_array = np.array(file_path)
        file_path_array_max = file_path_array[input_path_filtered_array > 0.1*max(input_path_filtered_array)]
        possible_normal = []
        possible_pre_irradiation = []
        for file in file_path_array_max:
            file_path = os.path.join(self.fileName_folder, file)
            [target_number,date_stamp,name,file_number] = saving_files_summary_list_20200420.get_headers(file_path)
            real_values = saving_files_summary_list_20200420.get_irradiation_information(file_path)
            # Get the dataframe from logfile 
            excel_data_df = saving_files_summary_list_20200420.get_data(real_values)
            target_current = excel_data_df.Target_I.astype(float)
            pre_irradiation_len = (len(excel_data_df.Target_I[excel_data_df['Target_I'].astype(float) == 50.0].astype(float))) + (len(excel_data_df.Target_I[excel_data_df['Target_I'].astype(float) == 25.0].astype(float))) + (len(excel_data_df.Target_I[excel_data_df['Target_I'].astype(float) == 0.0].astype(float)))
            pre_irradiation_len_relative = (pre_irradiation_len/len(excel_data_df.Target_I.astype(float)))
            if (pre_irradiation_len_relative) > 0.3:
                possible_pre_irradiation.append(file)
            else:
                possible_normal.append(file)
        reasons_small_file = []
        for file in (possible_normal):
            self.fileName = os.path.join(self.fileName_folder, file)
            managing_files.file_open(self)
            managing_files.file_open_summary(self)
            # GETTING STADISTIC NUMBERS
            # summary voltage 
        
        self.df_rf = self.df_rf.dropna()
        self.df_extraction = self.df_extraction.dropna()
        self.df_source = self.df_source.dropna()
        self.df_vacuum = self.df_vacuum.dropna()
        self.df_magnet = self.df_magnet.dropna()
        self.df_beam = self.df_beam.dropna()

        self.df_rf = self.df_rf.sort_values(by=['FILE'])
        self.df_extraction = self.df_extraction.sort_values(by=['FILE'])
        self.df_source = self.df_source.sort_values(by=['FILE'])
        self.df_vacuum = self.df_vacuum.sort_values(by=['FILE'])
        self.df_magnet = self.df_magnet.sort_values(by=['FILE'])
        self.df_beam = self.df_beam.sort_values(by=['FILE'])
        self.df_transmission = self.df_transmission.sort_values(by=['FILE'])

        self.tfs_output_source = os.path.join(self.output_path,"table_summary_source.out")
        self.tfs_output_vacuum = os.path.join(self.output_path,"table_summary_vacuum.out")
        self.tfs_output_magnet = os.path.join(self.output_path,"table_summary_magnet.out")
        self.tfs_output_beam = os.path.join(self.output_path,"table_summary_beam.out")
        self.tfs_output_extraction = os.path.join(self.output_path,"table_summary_extraction.out")
        self.tfs_output_rf = os.path.join(self.output_path,"table_summary_rf.out")
        self.tfs_output_trans = os.path.join(self.output_path,"table_summary_transmission.out")
        self.tfs_output_pressure_fluctuations = os.path.join(self.output_path,"table_summary_pressure_fluctuations.out")
        self.tfs_output_filling_volume = os.path.join(self.output_path,"table_summary_filling_volume.out")

        tfs.write(self.tfs_output_source, self.df_source)
        tfs.write(self.tfs_output_vacuum, self.df_vacuum)
        tfs.write(self.tfs_output_magnet, self.df_magnet)
        tfs.write(self.tfs_output_beam, self.df_beam)
        tfs.write(self.tfs_output_extraction, self.df_extraction)
        tfs.write(self.tfs_output_rf, self.df_rf)
        tfs.write(self.tfs_output_trans,self.df_transmission)
