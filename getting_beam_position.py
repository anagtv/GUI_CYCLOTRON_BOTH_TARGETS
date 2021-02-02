fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

x_values = np.linspace(0,0.1,50)
erf_values = []
for i in x_values:
    erf_values.append(math.erf(i))
... 

# calculations for target 4

distance_upper = []
distance_lower = []
x_values_negative = np.linspace(-2,0,500)
x_values_positive = np.linspace(0,2,500)
x_all = np.linspace(-2,2,1000)
for i in x_values_negative:
   distance_lower.append(abs(np.average(file_2nd_4.COLL_CURRENT_L_AVE/file_2nd_4.FOIL_CURRENT_AVE)/6.2/1.22-(1/2*(1+math.erf(i)))))
for i in x_values_positive: 
   distance_upper.append(abs(np.average(file_2nd_4.COLL_CURRENT_R_AVE/file_2nd_4.FOIL_CURRENT_AVE)/6.2-(1/2*(1-math.erf(i)))))
distance_lower_minimum = np.min(distance_lower)
distance_upper_minimum = np.min(distance_upper)
x_values_lower = x_values_negative[distance_lower.index(distance_lower_minimum)]
x_values_upper = x_values_positive[distance_upper.index(distance_upper_minimum)]
difference = x_values_upper - x_values_lower
sigma_i = 2/2**0.5*(5.225)/difference
suma = x_values_upper + x_values_lower 
mu = -suma*2**0.5/2*sigma_i

# calculatons for target 1

distance_upper = []
distance_lower = []
x_values_negative = np.linspace(-2,0,500)
x_values_positive = np.linspace(0,2,500)
x_all = np.linspace(-2,2,1000)
for i in x_values_negative:
   distance_lower.append(abs(np.average(file_1st_1.COLL_CURRENT_L_AVE/file_1st_1.FOIL_CURRENT_AVE)/6.2/1.22-(1/2*(1+math.erf(i)))))
for i in x_values_positive: 
   distance_upper.append(abs(np.average(file_1st_1.COLL_CURRENT_R_AVE/file_1st_1.FOIL_CURRENT_AVE)/6.2-(1/2*(1-math.erf(i)))))
distance_lower_minimum = np.min(distance_lower)
distance_upper_minimum = np.min(distance_upper)
x_values_lower = x_values_negative[distance_lower.index(distance_lower_minimum)]
x_values_upper = x_values_positive[distance_upper.index(distance_upper_minimum)]
difference = x_values_upper - x_values_lower
sigma_i = 2/2**0.5*(5.225)/difference
suma = x_values_upper + x_values_lower 
mu = -suma*2**0.5/2*sigma_i

directory = "../Documents/OneDrive/Ana_GTV_Compartida/Mantenimientos_ciclotrones/TCP/Analysis_all_20201211/"

list_of_files = ["table_summary_source.out","table_summary_transmission.out","table_summary_vacuum.out","table_summary_beam.out","target_foil_evolution.pdf","table_summary_extraction.out","table_summary_magnet.out","table_summary_rf.out"]			

intervals = [["4125","4233"],["4238","4431"],["4442","4540"],["4543","4689"],["4699","4823"],["4830","4968"],["4977","5091"]]
file_all.COLL_CURRENT_L_AVE[(file_all.FILE > intervals[0][0]) & (file_all.FILE < intervals[0][1])]

getattr(file_all,"COLL_CURRENT_L_AVE")[(getattr(file_all,"FILE") > "5000") & (getattr(file_all,"FILE") < "5200")]
file_name = os.path.join(directory,list_of_files[7])
file_name_tfs = tfs.read(file_name)
average_quantity_total = []
std_quantity_total = []
for interval in intervals:
	average_quantity,std_quantity = get_average_values_for_interval(file_name_tfs,interval,"FORWARD_POWER_AVE")
	average_quantity_total.append(average_quantity)
	std_quantity_total.append(std_quantity)
def get_average_values_for_interval(summary_file,interval,column_name):
	print (getattr(summary_file,column_name))
	filer_quantity = getattr(summary_file,column_name)[(getattr(summary_file,"FILE") > (interval[0])) & (getattr(summary_file,"FILE") < (interval[1]))]
	print (filer_quantity)
	average_quantity = np.average(filer_quantity)
	std_quantity = np.std(filer_quantity)
	return average_quantity,std_quantity

sigma_i_all_1 = []
mu_all_1 = []
file_name = os.path.join(directory,list_of_files[3])
file_name_tfs = tfs.read(file_name)
file_name_tfs = file_name_tfs[file_name_tfs.TARGET == "1"]
for interval in intervals:
    sigma_i,mu = beam_position(file_name_tfs,interval)
    sigma_i_all_1.append(sigma_i)
    mu_all_1.append(mu)
def beam_position(summary_file,interval):
    distance_upper = []
    distance_lower = []
    x_values_negative = np.linspace(-2,0,500)
    x_values_positive = np.linspace(0,2,500)
    x_all = np.linspace(-2,2,1000)
    for i in x_values_negative:
       distance_lower.append(abs(np.average(summary_file.COLL_CURRENT_L_AVE[(summary_file.FILE > interval[0]) & (summary_file.FILE < interval[1]) ]/summary_file.FOIL_CURRENT_AVE[(summary_file.FILE > interval[0]) & (summary_file.FILE < interval[1]) ])/6.4/1.42-(1/2*(1+math.erf(i)))))
    for i in x_values_positive: 
       distance_upper.append(abs(np.average(summary_file.COLL_CURRENT_R_AVE[(summary_file.FILE > interval[0]) & (summary_file.FILE < interval[1]) ]/summary_file.FOIL_CURRENT_AVE[(summary_file.FILE > interval[0]) & (summary_file.FILE < interval[1]) ])/6.4-(1/2*(1-math.erf(i)))))
    distance_lower_minimum = np.min(distance_lower)
    distance_upper_minimum = np.min(distance_upper)
    x_values_lower = x_values_negative[distance_lower.index(distance_lower_minimum)]
    x_values_upper = x_values_positive[distance_upper.index(distance_upper_minimum)]
    difference = x_values_upper - x_values_lower
    sigma_i = 2/2**0.5*(5.225)/difference
    suma = x_values_upper + x_values_lower 
    mu = -suma*2**0.5/2*sigma_i
    return sigma_i,mu

 