import datetime
datetime.datetime.today().weekday()
import tfs
import numpy as np
from tabulate import tabulate
from texttable import Texttable
import latextable
import math
import decimal
import os
import matplotlib.pyplot as plt


COLORS = ['#1E90FF','#FF4500','#32CD32',"#6A5ACD","#20B2AA","#00008B","#A52A2A","#228B22","#FF3300","#3366FF","#FF9933"]
def get_dates(file_source):
    date_week = []
    date_stamp_format = []
    for date in np.array(file_source.DATE):
       date_stamp_format.append(datetime.datetime.strptime(date,"%Y-%m-%d").date())
       date_week.append(datetime.datetime.strptime(date,"%Y-%m-%d").date().isocalendar()[1])
    date_week_unique = list(dict.fromkeys(date_week))
    return date_week,date_week_unique

def get_foil_number(file_df_sorted):
    foil_numbers = []
    foil_number = file_df_sorted.FOIL
    for foil in foil_number:
    	foil_numbers.append(foil)
    foil_numbers_unique = list(dict.fromkeys(foil_numbers))
    return foil_numbers,foil_numbers_unique

def get_total_irradiations_per_target(file_source):
    total_target_1 = len(file_source.TARGET[file_source.TARGET == "1"])
    total_target_4 = len(file_source.TARGET[file_source.TARGET == "4"])
    total_target = len(file_source.TARGET)
    return total_target_1,total_target_4,total_target

def duplicates(lst, item):
   return [i for i, x in enumerate(lst) if x == item]


def get_all_values_foils(foil,foil_unique,file_df,column,target):
    file_source_foil = []
    file_source_foils = []
    #print ("SORTED")
    #print (file_df)
    for i in foil_unique:
        index_week = duplicates(foil,i)
        for index_i in index_week:
           if file_df.TARGET[index_i] == target:
               file_source_foil.append(file_df[column][index_i])
        file_source_foils.append(file_source_foil)
        file_source_foil = []
    return file_source_foils

def get_year_results(date_week,date_week_unique,file_df,column,target):
    file_source_year = []
    for i in range(len(file_df.TARGET)):
        if file_df.TARGET[i] == target:
            file_source_year.append(file_df[column][i])
    return file_source_year

def get_all_values(date_week,date_week_unique,file_df,column,target):
    file_source_week = []
    file_source_weeks = []
    print (date_week_unique)
    for i in range(0,len(date_week_unique),2):
        index_week = duplicates(date_week,date_week_unique[i])
        index_week_2 = duplicates(date_week,date_week_unique[i+1])
        index_total = index_week + index_week_2
        index_total = np.array(index_total)
        index_total = index_total[index_total < 53]
        print ("WEEKS")
        print (index_week)
        print (index_week_2)
        #print (date_week_unique[i],date_week_unique[i+1])
        #print (index_total) 
        for i in range(len(index_total)):
           print ("INDEX")
           print (index_total)
           print (i)
           print (index_total[i])
           print (file_df.TARGET)
           if file_df.TARGET[index_total[i]] == target:
                    file_source_week.append(file_df[column][index_total[i]])
           #except:
           #	   continue
        #print ("values")
        file_source_weeks.append(file_source_week)
        file_source_week = []
    print (file_source_weeks)
    return file_source_weeks


def get_average_weekly_values(file_source_weeks):
    file_source_weeks_average = []
    file_source_weeks_std = []
    for weekly_values in file_source_weeks:
        file_source_weeks_average.append(np.average(weekly_values))
        file_source_weeks_std.append(np.std(weekly_values))
    return (file_source_weeks_average,file_source_weeks_std)

def get_average_year_values(file_source_weeks):
    #file_source_weeks_average = []
    #file_source_weeks_std = []
    #for weekly_values in file_source_weeks:
    file_source_weeks_average = (np.average(file_source_weeks))
    file_source_weeks_std = (np.std(file_source_weeks))
    return (file_source_weeks_average,file_source_weeks_std)


def get_average_foil_values(file_source_weeks):
    file_source_foils_average = []
    file_source_foils_std = []
    for foil_values in file_source_weeks:
        file_source_foils_average.append(np.average(foil_values))
        file_source_foils_std.append(np.std(foil_values))
    return (file_source_foils_average,file_source_foils_std)

def get_error_decimals(file_weeks_std):
    error_bar_list = []
    error_bar_list = []
    for error_bar in file_weeks_std:
        if error_bar <= 2:
            if error_bar > 0.1:
               error_bar_list.append(1)
            elif error_bar > 0.01:
               error_bar_list.append(2)
            elif error_bar > 0.001:
               error_bar_list.append(3)
            elif error_bar == 0.0:
               error_bar_list.append(0)
            else:
               error_bar_list.append(4)
        else:
            error_bar_list.append(0)
    return error_bar_list 

def get_plot(values,values_2,value_error,value_error_2,xlabel,ylabel,titlen,namef):
    print (values)
    ind = np.arange(len(values))   # the x locations for the groups
    width = 0.25     # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, values, width, yerr=value_error,color=COLORS[4])
    p2 = plt.bar(ind+0.3, values_2, width, yerr=value_error_2,color=COLORS[8])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    #plt.title(titlen)
    plt.xticks(ind+0.15, ('2017', '2018', '2019', '2020'))
    #plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('T1', 'T4'))
    plt.savefig(namef)
    plt.show()
    

def get_correct_format(file_average,file_weeks_std,error_bar_list):
    file_source_weeks_correct_format = []
    for i in range(len(file_average)):
        if error_bar_list[i] == 0:
        	 if math.isnan(file_average[i]):
        	 	file_average[i] = 0
        	 	file_weeks_std[i] = 0
        	 	file_source_weeks_correct_format.append(str("-") + " $\pm$ " + str("-"))
        	 else:
        	    file_source_weeks_correct_format.append(str(math.trunc(file_average[i])) + " $\pm$ " + str(math.trunc(file_weeks_std[i])))
        else:
        	 file_source_weeks_correct_format.append(str(round(file_average[i],error_bar_list[i])) + " $\pm$ " + str(round(file_weeks_std[i],error_bar_list[i])))
    return file_source_weeks_correct_format

def get_latex_table_suumary(file_weeks_average_1,file_weeks_average_4,file_weeks_std_1,file_weeks_std_4,label_1,label_4,caption_text,labelf,namef):
    error_bar_list_1 = get_error_decimals(file_weeks_std_1)
    error_bar_list_4 = get_error_decimals(file_weeks_std_4)
    file_source_weeks_1_correct_format = get_correct_format(file_weeks_average_1,file_weeks_std_1,error_bar_list_1)
    file_source_weeks_4_correct_format = get_correct_format(file_weeks_average_4,file_weeks_std_4,error_bar_list_4)
    file_source_weeks_1_correct_format.insert(0, label_1)
    file_source_weeks_4_correct_format.insert(0, label_4)
    top_row = ["","Before PM"]
    for i in range(1,2*len(file_weeks_average_1)-1,2):
        top_row.append("Week " + str(i)+ "-" + str(i+1))
    rows = [top_row, file_source_weeks_1_correct_format,
        file_source_weeks_4_correct_format]
    print (rows)
    table = Texttable()
    table.set_cols_align(["c"] * len(file_source_weeks_4_correct_format))
    table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.BORDER) 
    table.add_rows(rows)
    print('\nTexttable Latex:')
    print(latextable.draw_latex(table, caption=caption_text,label=labelf))
    f = open(namef, 'w')
    f.write(latextable.draw_latex(table, caption=caption_text,label=labelf))


def get_latex_table_suumary_foils(file_foils_average_1,file_foils_average_4,file_foils_std_1,file_foils_std_4,label_1,label_4,caption_text,labelf,namef):
    error_bar_list_1 = get_error_decimals(file_foils_std_1)
    error_bar_list_4 = get_error_decimals(file_foils_std_4)
    file_source_foils_1_correct_format = get_correct_format(file_foils_average_1,file_foils_std_1,error_bar_list_1)
    file_source_foils_4_correct_format = get_correct_format(file_foils_average_4,file_foils_std_4,error_bar_list_4)
    file_source_foils_1_correct_format.insert(0, label_1)
    file_source_foils_4_correct_format.insert(0, label_4)
    print ("hereee")
    print (file_source_foils_1_correct_format)
    print (file_source_foils_4_correct_format)
    rows = [["","Foil 1","Foil 2", "Foil 3", "Foil 4", "Foil 5","Foil 6"], file_source_foils_1_correct_format,
        file_source_foils_4_correct_format]
    table = Texttable()
    table.set_cols_align(["c"] * len(file_source_foils_4_correct_format))
    table.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.BORDER) 
    table.add_rows(rows)
    print('\nTexttable Latex:')
    print(latextable.draw_latex(table, caption=caption_text,label=labelf))
    f = open(namef, 'w')
    f.write(latextable.draw_latex(table, caption=caption_text,label=labelf))

def main():
    #file_source = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_source.out")
    #file_beam = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_beam.out")
    #file_magnet = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_magnet.out")			
    #file_vacuum = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_vacuum.out")
    #file_extraction = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_extraction.out")
    #file_rf = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_rf.out")
    #file_transmission = tfs.read("/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_20200901/table_summary_transmission.out")
    file_vacuum_average_1_all = []
    file_vacuum_weeks_std_1_all = []
    file_vacuum_average_4_all = []
    file_vacuum_weeks_std_4_all = []
    file_source_foil_average_1_all = []
    file_source_foil_std_1_all = []
    file_source_foil_average_4_all = []
    file_source_foil_std_4_all = []
    file_magnet_average_1_all = [] 
    file_magnet_weeks_std_1_all = []
    file_magnet_average_4_all = [] 
    file_magnet_weeks_std_4_all = []
    file_caroussel_average_1_all = []
    file_caroussel_weeks_std_1_all = []
    file_caroussel_average_4_all = []
    file_caroussel_weeks_std_4_all = []
    file_balance_average_1_all = []
    file_balance_weeks_std_1_all = []
    file_balance_average_4_all = []
    file_balance_weeks_std_4_all = []
    file_dee1_average_1_all = []
    file_dee1_weeks_std_1_all = []
    file_dee1_average_4_all = []
    file_dee1_weeks_std_4_all = []
    file_dee2_average_1_all = []
    file_dee2_weeks_std_1_all = []
    file_dee2_average_4_all = []
    file_dee2_weeks_std_4_all = []
    file_forward_average_1_all = []
    file_forward_weeks_std_1_all = []
    file_forward_average_4_all = []
    file_forward_weeks_std_4_all = []
    file_reflected_average_1_all = []
    file_reflected_weeks_std_1_all = []
    file_reflected_average_4_all = []
    file_reflected_weeks_std_4_all = []
    file_flap_1_average_1_all = []
    file_flap_1_weeks_std_1_all = []
    file_flap_1_average_4_all = []
    file_flap_1_weeks_std_4_all = []
    file_flap_2_average_1_all = []
    file_flap_2_weeks_std_1_all = []
    file_flap_2_average_4_all = []
    file_flap_2_weeks_std_4_all = []
    file_col_l_average_1_all = []
    file_col_l_weeks_std_1_all = []
    file_col_l_average_4_all = []
    file_col_l_weeks_std_4_all = []
    file_col_r_average_1_all = []
    file_col_r_weeks_std_1_all = []
    file_col_r_average_4_all = []
    file_col_r_weeks_std_4_all = []
    file_col_l_relative_average_1_all = []
    file_col_l_relative_weeks_std_1_all = []
    file_col_l_relative_average_4_all = []
    file_col_l_relative_weeks_std_4_all = []
    file_col_r_relative_average_1_all = []
    file_col_r_relative_weeks_std_1_all = []
    file_col_r_relative_average_4_all = []
    file_col_r_relative_weeks_std_4_all = []
    file_target_average_1_all = []
    file_target_weeks_std_1_all = []
    file_target_average_4_all = []
    file_target_weeks_std_4_all = []
    file_foil_average_1_all = []
    file_foil_weeks_std_1_all = []
    file_foil_average_4_all = []
    file_foil_weeks_std_4_all = []
    file_extraction_average_1_all = []
    file_extraction_weeks_std_1_all = []
    file_extraction_average_4_all = []
    file_extraction_weeks_std_4_all = []
    file_transmission_average_1_all = []
    file_transmission_weeks_std_1_all = []
    file_transmission_average_4_all = []
    file_transmission_weeks_std_4_all = []
    file_col_relative_average_1_all = []
    file_col_relative_weeks_std_1_all = []
    file_col_relative_average_4_all = []
    file_col_relative_weeks_std_4_all = []
    all_paths = ["/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_logs_2017","/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_logs_2018","/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_logs_2019",
    "/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_JNS_20200921/"]
    #all_paths = ["/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_logs_2018","/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/JNS/Analysis_logs_2017"]
    file_source_performance_foil_average_1_all = []
    file_source_performance_foil_std_1_all = []
    file_source_performance_foil_average_4_all = []
    file_source_performance_foil_std_4_all = []
    for path_year in all_paths:
         file_source = tfs.read(os.path.join(path_year,"table_summary_source.out"))
         file_beam = tfs.read(os.path.join(path_year,"table_summary_beam.out"))
         file_magnet = tfs.read(os.path.join(path_year,"table_summary_magnet.out"))			
         file_vacuum = tfs.read(os.path.join(path_year,"table_summary_vacuum.out"))
         file_extraction = tfs.read(os.path.join(path_year,"table_summary_extraction.out"))
         file_rf = tfs.read(os.path.join(path_year,"table_summary_rf.out"))
         file_transmission = tfs.read(os.path.join(path_year,"table_summary_transmission.out"))
         file_df_sorted = file_source.sort_values(by=['FOIL'])
         date_week,date_week_unique = get_dates(file_source)
         foil_numbers,foil_numbers_unique = get_foil_number(file_source)
         #source
         file_source_weeks_1 = get_year_results(date_week,date_week_unique,file_source,"CURRENT_AVE","1")
         file_source_weeks_4 = get_year_results(date_week,date_week_unique,file_source,"CURRENT_AVE","4")
         #herreeeee
         [file_source_average_1,file_source_weeks_std_1] = get_average_year_values(file_source_weeks_1)
         [file_source_average_4,file_source_weeks_std_4] = get_average_year_values(file_source_weeks_4)
         #file_foils_1 = get_all_values_foils(foil_numbers,foil_numbers_unique,file_source,"CURRENT_AVE","1")
         #file_foils_4 = get_all_values_foils(foil_numbers,foil_numbers_unique,file_source,"CURRENT_AVE","4")
         #[file_source_foil_average_1,file_source_foil_std_1] = get_average_year_values(file_foils_1)
         #[file_source_foil_average_4,file_source_foil_std_4] = get_average_year_values(file_foils_4)
         file_source_foil_average_1_all.append(file_source_average_1)
         file_source_foil_std_1_all.append(file_source_weeks_std_1)
         file_source_foil_average_4_all.append(file_source_average_4)
         file_source_foil_std_4_all.append(file_source_weeks_std_4)
         # source current latex
         print ("COLL L (RELATIVE)")
         file_col_l_relative_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"RELATIVE_COLL_CURRENT_L_AVE","1")
         file_col_l_relative_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"RELATIVE_COLL_CURRENT_L_AVE","4")
         [file_col_l_relative_average_1,file_col_l_relative_weeks_std_1] = get_average_year_values(file_col_l_relative_weeks_1)
         [file_col_l_relative_average_4,file_col_l_relative_weeks_std_4] = get_average_year_values(file_col_l_relative_weeks_4)
         #get_latex_table_suumary(file_col_l_relative_average_1,file_col_l_relative_average_4,file_col_l_relative_weeks_std_1,file_col_l_relative_weeks_std_4,"T1 [\%]","T4 [\%]","Average relative collimator (lower) current per two week","tab:collimators_l_relative","collimators_l_relative.tex")
         file_col_l_relative_average_1_all.append(file_col_l_relative_average_1)         
         file_col_l_relative_weeks_std_1_all.append(file_col_l_relative_weeks_std_1)
         file_col_l_relative_average_4_all.append(file_col_l_relative_average_4)
         file_col_l_relative_weeks_std_4_all.append(file_col_l_relative_weeks_std_4)
         print ("SOURCE")
         #get_latex_table_suumary(file_source_average_1,file_source_average_4,file_source_weeks_std_1,file_source_weeks_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average ion source current per two weeks","tab:ion_source","source_current.tex")
         #get_latex_table_suumary_foils(file_source_foil_average_1,file_source_foil_average_4,file_source_foil_std_1,file_source_foil_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average ion source current per foil","tab:ion_source_foil","ion_source_vs_foil.tex")
         #source performance
         file_source_performance_weeks_1 = get_year_results(date_week,date_week_unique,file_source,"SOURCE_PERFORMANCE","1")
         file_source_performance_weeks_4 = get_year_results(date_week,date_week_unique,file_source,"SOURCE_PERFORMANCE","4")
         [file_source_performance_average_1,file_source_performance_weeks_std_1] = get_average_year_values(file_source_performance_weeks_1)
         [file_source_performance_average_4,file_source_performance_weeks_std_4] = get_average_year_values(file_source_performance_weeks_4)
         file_source_performance_foil_average_1_all.append(file_source_performance_average_1)
         file_source_performance_foil_std_1_all.append(file_source_performance_weeks_std_1)
         file_source_performance_foil_average_4_all.append(file_source_performance_average_4)
         file_source_performance_foil_std_4_all.append(file_source_performance_weeks_std_4)
         #get_latex_table_suumary(file_source_performance_average_1,file_source_performance_average_4,file_source_performance_weeks_std_1,file_source_performance_weeks_std_4,"T1 [$\mu$A/mA]","T4 [$\mu$A/mA]","Average ion source performance per week","tab:source_performance","source_performance.tex")
         #vacuum
         file_vacuum_weeks_1 = get_year_results(date_week,date_week_unique,file_vacuum,"PRESSURE_AVE","1")
         file_vacuum_weeks_4 = get_year_results(date_week,date_week_unique,file_vacuum,"PRESSURE_AVE","4")
         [file_vacuum_average_1,file_vacuum_weeks_std_1] = get_average_year_values(file_vacuum_weeks_1)
         [file_vacuum_average_4,file_vacuum_weeks_std_4] = get_average_year_values(file_vacuum_weeks_4)
         file_vacuum_average_1_all.append(file_vacuum_average_1)
         file_vacuum_weeks_std_1_all.append(file_vacuum_weeks_std_1)
         file_vacuum_average_4_all.append(file_vacuum_average_4)
         file_vacuum_weeks_std_4_all.append(file_vacuum_weeks_std_4)
         print ("VACUUM")
         # source current latex
         #get_latex_table_suumary(file_vacuum_average_1,file_vacuum_average_4,file_vacuum_weeks_std_1,file_vacuum_weeks_std_4,"T1 [$10^{-5}$ mbar]","T4 [$10^{-5}$s mbar]","Average vacuum value per two week","tab:vacuum","vacuum.tex")
         #magnet 
         print ("MAGNET")
         file_magnet_weeks_1 = get_year_results(date_week,date_week_unique,file_magnet,"CURRENT_AVE","1")
         file_magnet_weeks_4 = get_year_results(date_week,date_week_unique,file_magnet,"CURRENT_AVE","4")
         [file_magnet_average_1,file_magnet_weeks_std_1] = get_average_year_values(file_magnet_weeks_1)
         [file_magnet_average_4,file_magnet_weeks_std_4] = get_average_year_values(file_magnet_weeks_4)
         #get_latex_table_suumary(file_magnet_average_1,file_magnet_average_4,file_magnet_weeks_std_1,file_magnet_weeks_std_4,"T1 [A]","T4 [A]","Average magnet current per two week","tab:magnet","magnet.tex")
         file_magnet_average_1_all.append(file_magnet_average_1)
         file_magnet_weeks_std_1_all.append(file_magnet_weeks_std_1)
         file_magnet_average_4_all.append(file_magnet_average_4)
         file_magnet_weeks_std_4_all.append(file_magnet_weeks_std_4)
         #extraction
         print ("CAROUSSEL")
         file_caroussel_weeks_1 = get_year_results(date_week,date_week_unique,file_extraction,"CAROUSEL_POSITION_AVE","1")
         file_caroussel_weeks_4 = get_year_results(date_week,date_week_unique,file_extraction,"CAROUSEL_POSITION_AVE","4")
         [file_caroussel_average_1,file_caroussel_weeks_std_1] = get_average_year_values(file_caroussel_weeks_1)
         [file_caroussel_average_4,file_caroussel_weeks_std_4] = get_average_year_values(file_caroussel_weeks_4)
         file_caroussel_average_1_all.append(file_caroussel_average_1)
         file_caroussel_weeks_std_1_all.append(file_caroussel_weeks_std_1)
         file_caroussel_average_4_all.append(file_caroussel_average_4)
         file_caroussel_weeks_std_4_all.append(file_caroussel_weeks_std_4)
         #get_latex_table_suumary(file_caroussel_average_1,file_caroussel_average_4,file_caroussel_weeks_std_1,file_caroussel_weeks_std_4,"T1 [\%]","T4 [\%]","Average caroussel position per two week","tab:carousel","carousel.tex")
         print ("BALANCE")
         file_balance_weeks_1 = get_year_results(date_week,date_week_unique,file_extraction,"BALANCE_POSITION_AVE","1")
         file_balance_weeks_4 = get_year_results(date_week,date_week_unique,file_extraction,"BALANCE_POSITION_AVE","4") 
         [file_balance_average_1,file_balance_weeks_std_1] = get_average_year_values(file_balance_weeks_1)
         [file_balance_average_4,file_balance_weeks_std_4] = get_average_year_values(file_balance_weeks_4)
         file_balance_average_1_all.append(file_balance_average_1)
         file_balance_weeks_std_1_all.append(file_balance_weeks_std_1)
         file_balance_average_4_all.append(file_balance_average_4)
         file_balance_weeks_std_4_all.append(file_balance_weeks_std_4)
         #get_latex_table_suumary(file_balance_average_1,file_balance_average_4,file_balance_weeks_std_1,file_balance_weeks_std_4,"T1 [\%]","T4 [\%]","Average balance position per two week","tab:balance","balance.tex")
         #rf
         print ("RF (DEE 1)")
         file_dee1_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"DEE1_VOLTAGE_AVE","1")
         file_dee1_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"DEE1_VOLTAGE_AVE","4")
         [file_dee1_average_1,file_dee1_weeks_std_1] = get_average_year_values(file_dee1_weeks_1)
         [file_dee1_average_4,file_dee1_weeks_std_4] = get_average_year_values(file_dee1_weeks_4)
         file_dee1_average_1_all.append(file_dee1_average_1)
         file_dee1_weeks_std_1_all.append(file_dee1_weeks_std_1)
         file_dee1_average_4_all.append(file_dee1_average_4)
         file_dee1_weeks_std_4_all.append(file_dee1_weeks_std_4)
         #get_latex_table_suumary(file_dee1_average_1,file_dee1_average_4,file_dee1_weeks_std_1,file_dee1_weeks_std_4,"T1 [kV]","T4 [kV]","Average dee 1 voltage per two week","tab:rf_dee1","dee1_voltage.tex")
         print ("RF (DEE 2)")
         file_dee2_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"DEE2_VOLTAGE_AVE","1")
         file_dee2_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"DEE2_VOLTAGE_AVE","4") 
         [file_dee2_average_1,file_dee2_weeks_std_1] = get_average_year_values(file_dee2_weeks_1)
         [file_dee2_average_4,file_dee2_weeks_std_4] = get_average_year_values(file_dee2_weeks_4)
         file_dee2_average_1_all.append(file_dee2_average_1)
         file_dee2_weeks_std_1_all.append(file_dee2_weeks_std_1)
         file_dee2_average_4_all.append(file_dee2_average_4)
         file_dee2_weeks_std_4_all.append(file_dee2_weeks_std_4)
         #get_latex_table_suumary(file_dee2_average_1,file_dee2_average_4,file_dee2_weeks_std_1,file_dee2_weeks_std_4,"T1 [kV]","T4 [kV]","Average dee 2 voltage per two week","tab:rf_dee2","dee2_voltage.tex")
         print ("RF FORWARD")
         file_forward_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"FORWARD_POWER_AVE","1")
         file_forward_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"FORWARD_POWER_AVE","4")
         [file_forward_average_1,file_forward_weeks_std_1] = get_average_year_values(file_forward_weeks_1)
         [file_forward_average_4,file_forward_weeks_std_4] = get_average_year_values(file_forward_weeks_4)
         file_forward_average_1_all.append(file_forward_average_1)
         file_forward_weeks_std_1_all.append(file_forward_weeks_std_1)
         file_forward_average_4_all.append(file_forward_average_4)
         file_forward_weeks_std_4_all.append(file_forward_weeks_std_4)
         #get_latex_table_suumary(file_forward_average_1,file_forward_average_4,file_forward_weeks_std_1,file_forward_weeks_std_4,"T1 [kW]","T4 [kW]","Average forwarded power per two week","tab:rf_forwarded","forward_power.tex")
         print ("RF REFLECTED")
         file_reflected_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"REFLECTED_POWER_AVE","1")
         file_reflected_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"REFLECTED_POWER_AVE","4") 
         [file_reflected_average_1,file_reflected_weeks_std_1] = get_average_year_values(file_reflected_weeks_1)
         [file_reflected_average_4,file_reflected_weeks_std_4] = get_average_year_values(file_reflected_weeks_4)
         file_reflected_average_1_all.append(file_reflected_average_1)
         file_reflected_weeks_std_1_all.append(file_reflected_weeks_std_1)
         file_reflected_average_4_all.append(file_reflected_average_4)
         file_reflected_weeks_std_4_all.append(file_reflected_weeks_std_4)
         #get_latex_table_suumary(file_reflected_average_1,file_reflected_average_4,file_reflected_weeks_std_1,file_reflected_weeks_std_4,"T1 [kW]","T4 [kW]","Average reflected power per two week","tab:rf_reflected","reflected_power.tex")
         print ("RF FLAP 1")
         file_flap_1_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"FLAP1_AVE","1")
         file_flap_1_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"FLAP1_AVE","4") 
         [file_flap_1_average_1,file_flap_1_weeks_std_1] = get_average_year_values(file_flap_1_weeks_1)
         [file_flap_1_average_4,file_flap_1_weeks_std_4] = get_average_year_values(file_flap_1_weeks_4)
         file_flap_1_average_1_all.append(file_flap_1_average_1)
         file_flap_1_weeks_std_1_all.append(file_flap_1_weeks_std_1)
         file_flap_1_average_4_all.append(file_flap_1_average_4)
         file_flap_1_weeks_std_4_all.append(file_flap_1_weeks_std_4)
         #get_latex_table_suumary(file_flap_1_average_1,file_flap_1_average_4,file_flap_1_weeks_std_1,file_flap_1_weeks_std_4,"T1 [\%]","T4 [\%]","Average flap 1 position per two week","tab:rf_flap1","flap1.tex")
         print ("RF FLAP 2")
         file_flap_2_weeks_1 = get_year_results(date_week,date_week_unique,file_rf,"FLAP2_AVE","1")
         file_flap_2_weeks_4 = get_year_results(date_week,date_week_unique,file_rf,"FLAP2_AVE","4") 
         [file_flap_2_average_1,file_flap_2_weeks_std_1] = get_average_year_values(file_flap_2_weeks_1)
         [file_flap_2_average_4,file_flap_2_weeks_std_4] = get_average_year_values(file_flap_2_weeks_4)
         file_flap_2_average_1_all.append(file_flap_2_average_1)
         file_flap_2_weeks_std_1_all.append(file_flap_2_weeks_std_1)
         file_flap_2_average_4_all.append(file_flap_2_average_4)
         file_flap_2_weeks_std_4_all.append(file_flap_2_weeks_std_4)
         #get_latex_table_suumary(file_flap_2_average_1,file_flap_2_average_4,file_flap_2_weeks_std_1,file_flap_2_weeks_std_4,"T1 [\%]","T4 [\%]","Average flap 2 position per two week","tab:rf_flap2","flap2.tex")
         #beam at extraction
         print ("COLL L")
         print (path_year)
         print (file_beam.TARGET)
         print ("DATE WEEK")
         print (date_week)
         print (date_week_unique)
         file_col_l_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"COLL_CURRENT_L_AVE","1")
         file_col_l_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"COLL_CURRENT_L_AVE","4")
         [file_col_l_average_1,file_col_l_weeks_std_1] = get_average_year_values(file_col_l_weeks_1)
         [file_col_l_average_4,file_col_l_weeks_std_4] = get_average_year_values(file_col_l_weeks_4)
         #get_latex_table_suumary(file_col_l_average_1,file_col_l_average_4,file_col_l_weeks_std_1,file_col_l_weeks_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average collimator (lower) current per two week","tab:collimators_l","collimators_l.tex")
         file_col_l_average_1_all.append(file_col_l_average_1)         
         file_col_l_weeks_std_1_all.append(file_col_l_weeks_std_1)
         file_col_l_average_4_all.append(file_col_l_average_4)
         file_col_l_weeks_std_4_all.append(file_col_l_weeks_std_4)
         print ("COLL R")
         file_col_r_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"COLL_CURRENT_R_AVE","1")
         file_col_r_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"COLL_CURRENT_R_AVE","4") 
         [file_col_r_average_1,file_col_r_weeks_std_1] = get_average_year_values(file_col_r_weeks_1)
         [file_col_r_average_4,file_col_r_weeks_std_4] = get_average_year_values(file_col_r_weeks_4)
         #get_latex_table_suumary(file_col_r_average_1,file_col_r_average_4,file_col_r_weeks_std_1,file_col_r_weeks_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average collimator (upper) current per two week","tab:collimators_r","collimators_r.tex")
         file_col_r_average_1_all.append(file_col_r_average_1)         
         file_col_r_weeks_std_1_all.append(file_col_r_weeks_std_1)
         file_col_r_average_4_all.append(file_col_r_average_4)
         file_col_r_weeks_std_4_all.append(file_col_r_weeks_std_4)
         print ("COLL R (RELATIVE)")
         file_col_r_relative_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"RELATIVE_COLL_CURRENT_R_AVE","1")
         file_col_r_relative_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"RELATIVE_COLL_CURRENT_R_AVE","4") 
         [file_col_r_relative_average_1,file_col_r_relative_weeks_std_1] = get_average_year_values(file_col_r_relative_weeks_1)
         [file_col_r_relative_average_4,file_col_r_relative_weeks_std_4] = get_average_year_values(file_col_r_relative_weeks_4)
         #get_latex_table_suumary(file_col_r_relative_average_1,file_col_r_relative_average_4,file_col_r_relative_weeks_std_1,file_col_r_relative_weeks_std_4,"T1 [\%]","T4 [\%]","Average relative collimator (upper) current per two week","tab:collimators_r_relative","collimators_r_relative.tex")   
         file_col_r_relative_average_1_all.append(file_col_r_relative_average_1)         
         file_col_r_relative_weeks_std_1_all.append(file_col_r_relative_weeks_std_1)
         file_col_r_relative_average_4_all.append(file_col_r_relative_average_4)
         file_col_r_relative_weeks_std_4_all.append(file_col_r_relative_weeks_std_4)
         print ("COLL TOTAL (RELATIVE)")
         file_col_relative_average_1_all.append(file_col_r_relative_average_1 + file_col_l_relative_average_1)         
         file_col_relative_weeks_std_1_all.append(file_col_r_relative_weeks_std_1 + file_col_l_relative_weeks_std_1)
         file_col_relative_average_4_all.append(file_col_r_relative_average_4 + file_col_l_relative_average_4)
         file_col_relative_weeks_std_4_all.append(file_col_r_relative_weeks_std_4 + file_col_l_relative_weeks_std_4)
         print ("TARGET")
         file_target_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"TARGET_CURRENT_AVE","1")
         file_target_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"TARGET_CURRENT_AVE","4")
         [file_target_average_1,file_target_weeks_std_1] = get_average_year_values(file_target_weeks_1)
         [file_target_average_4,file_target_weeks_std_4] = get_average_year_values(file_target_weeks_4)
         #get_latex_table_suumary(file_target_average_1,file_target_average_4,file_target_weeks_std_1,file_target_weeks_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average target current per two week","tab:target","target.tex")
         file_target_average_1_all.append(file_target_average_1)         
         file_target_weeks_std_1_all.append(file_target_weeks_std_1)
         file_target_average_4_all.append(file_target_average_4)
         file_target_weeks_std_4_all.append(file_target_weeks_std_4)
         print ("FOIL")
         file_foil_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"FOIL_CURRENT_AVE","1")
         file_foil_weeks_4 = (date_week,date_week_unique,file_source,"FOIL_CURRENT_AVE","4")
         [file_foil_average_1,file_foil_weeks_std_1] = get_average_year_values(file_target_weeks_1)
         [file_foil_average_4,file_foil_weeks_std_4] = get_average_year_values(file_target_weeks_4)
         #get_latex_table_suumary(file_foil_average_1,file_foil_average_4,file_foil_weeks_std_1,file_foil_weeks_std_4,"T1 [$\mu$A]","T4 [$\mu$A]","Average foil current per two week","tab:foil","foil.tex")
         file_foil_average_1_all.append(file_foil_average_1)
         file_foil_weeks_std_1_all.append(file_foil_weeks_std_1)
         file_foil_average_4_all.append(file_foil_average_4)
         file_foil_weeks_std_4_all.append(file_foil_weeks_std_4)
         print ("LOSSES")
         file_extraction_weeks_1 = get_year_results(date_week,date_week_unique,file_beam,"EXTRACTION_LOSSES_AVE","1")
         file_extraction_weeks_4 = get_year_results(date_week,date_week_unique,file_beam,"EXTRACTION_LOSSES_AVE","4")
         [file_extraction_average_1,file_extraction_weeks_std_1] = get_average_year_values(file_extraction_weeks_1)
         [file_extraction_average_4,file_extraction_weeks_std_4] = get_average_year_values(file_extraction_weeks_4)
         file_extraction_average_1_all.append(file_extraction_average_1)
         file_extraction_weeks_std_1_all.append(file_extraction_weeks_std_1)
         file_extraction_average_4_all.append(file_extraction_average_4)
         file_extraction_weeks_std_4_all.append(file_extraction_weeks_std_4)  
         print ("TRANSMISSION")
         file_transmission_weeks_1 = get_year_results(date_week,date_week_unique,file_transmission,"TRANSMISSION","1")
         file_transmission_weeks_4 = get_year_results(date_week,date_week_unique,file_transmission,"TRANSMISSION","4")
         [file_transmission_average_1,file_transmission_weeks_std_1] = get_average_year_values(file_transmission_weeks_1)
         [file_transmission_average_4,file_transmission_weeks_std_4] = get_average_year_values(file_transmission_weeks_4)
         file_transmission_average_1_all.append(file_transmission_average_1)
         file_transmission_weeks_std_1_all.append(file_transmission_weeks_std_1)
         file_transmission_average_4_all.append(file_transmission_average_4)
         file_transmission_weeks_std_4_all.append(file_transmission_weeks_std_4)        
         print ("AVERAGE")
         print (file_transmission_average_1)
         print (file_transmission_average_4)
         #get_latex_table_suumary(file_extraction_average_1,file_extraction_average_4,file_extraction_weeks_std_1,file_extraction_weeks_std_4,"T1 [\%]","T4 [\%]","Average extraction losses per two week","tab:beam_losses","beam_losses.tex")
         #
         [target_1,target_4,target_all] = get_total_irradiations_per_target(file_source)
         print ([target_1,target_4,target_all])
    print ("TEST")
    print ([2017,2018,2019,2020])
    print (file_extraction_average_1_all)
    print (file_extraction_average_4_all)
    print (file_dee2_average_1_all,file_dee2_weeks_std_1_all)
    print ("SOURCE")
    print (file_source_foil_average_1_all,file_source_foil_average_4_all,file_source_foil_std_1_all,file_source_foil_std_4_all)
    print ("VACUUM")
    print (file_vacuum_average_1_all,file_vacuum_average_4_all,file_vacuum_weeks_std_1_all,file_vacuum_weeks_std_4_all)
    print ("TRANSMISSION")
    print (file_transmission_average_1_all,file_transmission_average_4_all,file_transmission_weeks_std_1_all,file_transmission_weeks_std_4_all)
    print ("MAGNET")
    print (file_magnet_average_1_all,file_magnet_average_4_all,file_magnet_weeks_std_1_all,file_magnet_weeks_std_4_all)
    print ("DEE 1")
    print (file_dee1_average_1_all,file_dee1_average_4_all,file_dee1_weeks_std_1_all,file_dee1_weeks_std_4_all)
    print ("DEE 2")
    print (file_dee2_average_1_all,file_dee2_average_4_all,file_dee2_weeks_std_1_all,file_dee2_weeks_std_4_all)
    print (file_col_relative_average_1_all,file_col_relative_average_4_all,file_col_relative_weeks_std_1_all,file_col_relative_weeks_std_4_all)
    print ("SOURCE PERFORMANCE")
    print (file_source_performance_foil_average_1_all,file_source_performance_foil_average_4_all,file_source_performance_foil_std_1_all,file_source_performance_foil_std_4_all)
    print ("AVERAGE COLLIMATOR")
    print (file_col_relative_average_1_all,file_col_relative_average_4_all,file_col_relative_weeks_std_1_all,file_col_relative_weeks_std_4_all)
    print ("COLLIMATOR LOW")
    print (file_col_l_relative_average_1_all,file_col_l_relative_average_4_all,file_col_l_relative_weeks_std_1_all,file_col_l_relative_weeks_std_4_all)
    print ("COLLIMATOR UPPER")
    print (file_col_r_relative_average_1_all,file_col_r_relative_average_4_all,file_col_r_relative_weeks_std_1_all,file_col_r_relative_weeks_std_4_all)
    print ("BEAM LOSSES")
    print (file_extraction_average_1_all,file_extraction_average_4_all,file_extraction_weeks_std_1_all,file_extraction_weeks_std_4_all)
    get_plot(file_extraction_average_1_all,file_extraction_average_4_all,file_extraction_weeks_std_1_all,file_extraction_weeks_std_4_all,"Year","Beam losses [%]","Beam losses","losses.pdf")
    get_plot(file_transmission_average_1_all,file_transmission_average_4_all,file_transmission_weeks_std_1_all,file_transmission_weeks_std_4_all,"Year","Transmission [%]","Transmission","transmission.pdf")
    get_plot(file_foil_average_1_all,file_foil_average_4_all,file_foil_weeks_std_1_all,file_foil_weeks_std_4_all,"Year","Foil current [$\mu$A]","Foil current","foil_current.pdf")
    get_plot(file_target_average_1_all,file_target_average_4_all,file_target_weeks_std_1_all,file_target_weeks_std_4_all,"Year","Target current [$\mu$A]","Target current","target_current.pdf")
    get_plot(file_col_r_relative_average_1_all,file_col_r_relative_average_4_all,file_col_r_relative_weeks_std_1_all,file_col_r_relative_weeks_std_4_all,"Year","Collimator upper current [%]","Collimator upper current","coll_r_current.pdf")
    get_plot(file_col_l_relative_average_1_all,file_col_l_relative_average_4_all,file_col_l_relative_weeks_std_1_all,file_col_l_relative_weeks_std_4_all,"Year","Collimator lower current [%]","Collimator lower current","coll_l_current.pdf")
    get_plot(file_flap_1_average_1_all,file_flap_1_average_4_all,file_flap_1_weeks_std_1_all,file_flap_1_weeks_std_4_all,"Year","Flap 1 [%]", "Flap position","flap_1.pdf")
    get_plot(file_flap_2_average_1_all,file_flap_2_average_4_all,file_flap_2_weeks_std_1_all,file_flap_2_weeks_std_4_all,"Year","Flap 2 [%]", "Flap position","flap_2.pdf")
    get_plot(file_dee1_average_1_all,file_dee1_average_4_all,file_dee1_weeks_std_1_all,file_dee1_weeks_std_4_all,"Year","Dee 1 voltage [kV]", "Dee voltage","dee_voltage_1.pdf")
    get_plot(file_dee2_average_1_all,file_dee2_average_4_all,file_dee2_weeks_std_1_all,file_dee2_weeks_std_4_all,"Year","Dee 2 voltage [kV]", "Dee voltage","dee_voltage_2.pdf")
    get_plot(file_forward_average_1_all,file_forward_average_4_all,file_forward_weeks_std_1_all,file_forward_weeks_std_4_all,"Year","Forwared power [kW]", "Forwarded power [kW]","forwarded_power.pdf")
    get_plot(file_reflected_average_1_all,file_reflected_average_4_all,file_reflected_weeks_std_1_all,file_reflected_weeks_std_4_all,"Year","Reflected power [kW]", "Reflected power","reflected_power.pdf")
    get_plot(file_caroussel_average_1_all,file_caroussel_average_4_all,file_caroussel_weeks_std_1_all,file_caroussel_weeks_std_4_all,"Year","Position [%]","Carousel position [%]","carousel_position.pdf")
    get_plot(file_balance_average_1_all,file_balance_average_4_all,file_balance_weeks_std_1_all,file_balance_weeks_std_4_all,"Year","Position [%]","Balance position [%]","balance_position.pdf")
    get_plot(file_vacuum_average_1_all,file_vacuum_average_4_all,file_vacuum_weeks_std_1_all,file_vacuum_weeks_std_4_all,"Year",r"Pressure [$10^{-5}$ mbar]", "Vacuum","vacuum.pdf")
    get_plot(file_magnet_average_1_all,file_magnet_average_4_all,file_magnet_weeks_std_1_all,file_magnet_weeks_std_4_all,"Year","Current [A]","Magnet","magnet.pdf")
    get_plot(file_source_foil_average_1_all,file_source_foil_average_4_all,file_source_foil_std_1_all,file_source_foil_std_4_all,"Year","Source current [mA]","Ion Source","ion_source.pdf")
    get_plot(file_source_performance_foil_average_1_all,file_source_performance_foil_average_4_all,file_source_performance_foil_std_1_all,file_source_performance_foil_std_4_all,"Year",r"Source performance [$mu$A/mA]","Ion Source","ion_source_performance.pdf")
    get_plot(file_col_relative_average_1_all,file_col_relative_average_4_all,file_col_relative_weeks_std_1_all,file_col_relative_weeks_std_4_all,"Year","Collimators current [%]","Collimators current","coll_current.pdf")


 



# transmission

if __name__ == "__main__":
	main()