# Get the speed and flat position     
        self.motor_extraction = float(self.motor_speed(self.file_df,self.max_current,"Extr_pos"))*60
        self.motor_flap_1 = float(self.motor_speed(self.file_df,self.max_current,"Flap1_pos"))*60
        self.motor_flap_2 = float(self.motor_speed(self.file_df,self.max_current,"Flap2_pos"))*60
        self.motor_extraction_pos = float(self.motor_position_difference(self.file_df,self.max_current,"Extr_pos"))
        self.motor_flap_1_pos = float(self.motor_position_difference(self.file_df,self.max_current,"Flap1_pos"))
        self.motor_flap_2_pos = float(self.motor_position_difference(self.file_df,self.max_current,"Flap2_pos"))


 def motor_position_difference(self,data_df,steady_current,value_motor):
        df_extraction_position_zero_current_source = data_df[value_motor].astype(float).iloc[0]
        #df_extraction_time_zero_current_source = data_df.Time[data_df['Target_I'].astype(float) == 0]
        df_extraction_position_steady_current_source = data_df[value_motor][data_df['Target_I'].astype(float) > steady_current].astype(float)
        #df_extraction_time_steady_current_source = data_df.Time[data_df['Target_I'].astype(float) > steady_current]
        position_difference = - df_extraction_position_zero_current_source + df_extraction_position_steady_current_source.iloc[0]
        motor_flap = position_difference
        print ("MOTOR POSITION DIFFERENCE")
        print (position_difference)
        print (df_extraction_position_zero_current_source)
        print (df_extraction_position_steady_current_source.iloc[0])
        return motor_flap
        #  
    def motor_speed(self,data_df,steady_current,value_motor):
        df_extraction_position_steady_current_source = data_df[value_motor][data_df['Target_I'].astype(float) > steady_current].astype(float)
        df_extraction_time_steady_current_source = data_df.Time[data_df['Target_I'].astype(float) > steady_current]
        df_extraction_position_steady_current_source_average = np.mean(df_extraction_position_steady_current_source) 
        print (df_extraction_time_steady_current_source)
        hour_i = df_extraction_time_steady_current_source.iloc[0][0:2]
        minute_i = df_extraction_time_steady_current_source.iloc[0][3:5]
        seconds_i = df_extraction_time_steady_current_source.iloc[0][6:8]
        hour_f = df_extraction_time_steady_current_source.iloc[-1][0:2]
        minute_f = df_extraction_time_steady_current_source.iloc[-1][3:5]
        seconds_f = df_extraction_time_steady_current_source.iloc[-1][6:8]
        hour_i_total = int(hour_i)*3600+int(minute_i)*60+int(seconds_i)
        hour_f_total = int(hour_f)*3600+int(minute_f)*60+int(seconds_f)
        position_difference = float(- df_extraction_position_steady_current_source.iloc[0] + df_extraction_position_steady_current_source.iloc[-1])
        time_difference = float(hour_f_total - hour_i_total)
        motor_flap = position_difference/time_difference*60
        return motor_flap
