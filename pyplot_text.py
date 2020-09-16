import numpy as np
import matplotlib.pyplot as plt
import tfs
import matplotlib
matplotlib.pyplot.hist
matplotlib.pyplot.xlabel
matplotlib.pyplot.ylabel
matplotlib.pyplot.text
matplotlib.pyplot.grid
matplotlib.pyplot.show

Butter1 = '#FCE94F'
Butter2 = '#EDD400'
Butter3 = '#C4A000'
Orange1 = '#FCAF3E'
Orange2 = '#F57900'
Orange3 = '#CE5C00'
Chocolate1 = '#E9B96E'
Chocolate2 = '#C17D11'
Chocolate3 = '#8F5902'
Chameleon1 = '#8AE234'
Chameleon2 = '#73D216'
Chameleon3 = '#4E9A06'
SkyBlue1 = '#729FCF'
SkyBlue2 = '#3465A4'
SkyBlue3 = '#204A87'
Plum1 = '#AD7FA8'
Plum2 = '#75507B'
Plum3 = '#5C3566'
ScarletRed1 = '#EF2929'
ScarletRed2 = '#CC0000'
ScarletRed3 = '#A40000'
Aluminium1 = '#EEEEEC'
Aluminium2 = '#D3D7CF'
Aluminium3 = '#BABDB6'
Aluminium4 = '#888A85'
Aluminium5 = '#555753'
Aluminium6 = '#2E3436'
ForestGreen = "#228B22"



# the histogram of the data
df_isochronism_increase_tcp = tfs.read("magnet_increment_TCP.out")
df_isochronism_increase_mrs = tfs.read("magnet_increment_MRS.out")
df_isochronism_increase_dij = tfs.read("magnet_increment_DIJ_new.out")

# the histogram of the data
#weights_tcp = np.ones_like(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT)) / float(len(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT)))
#n_tcp, bins_tcp, patches_tcp = plt.hist(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT), align='left', weights=weights_tcp,edgecolor=SkyBlue3,alpha=0.9, lw=3, color= 'r', histtype='step',label="TCP")
#weights_mrs = np.ones_like(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT)) / float(len(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT)))
#n_mrs, bins_mrs, patches_mrs = plt.hist(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT), align='left', weights=weights_mrs,edgecolor=Orange3,lw=3,histtype='step',label="MRS")
#weights_dij = np.ones_like(list(df_isochronism_increase_dij.RELATIVE_INCREMENT)) / float(len(list(df_isochronism_increase_dij.RELATIVE_INCREMENT)))
#n_dij, bins_dij, patches_dij = plt.hist(list(df_isochronism_increase_dij.RELATIVE_INCREMENT), align='left', weights=weights_dij,edgecolor=ForestGreen,lw=3, histtype='step',label="DIJ")
#plt.legend(loc=1)
#n, bins, patches = plt.hist(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT), density=True, facecolor='g', alpha=0.75)
#plt.xlabel('Daily initial current increase (normalized to number of irradiations)')
#plt.ylabel('Counts')
#plt.title('Histogram of magnet current increase')
#plt.savefig("initial_magnet.pdf")

# the histogram of the data (final)
weights_tcp = np.ones_like(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT_FINAL)) / float(len(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT_FINAL)))
n_tcp, bins_tcp, patches_tcp = plt.hist(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT_FINAL), align='left', weights=weights_tcp,edgecolor=SkyBlue3,alpha=0.9, lw=3, color= 'r', histtype='step',label="TCP")
weights_mrs = np.ones_like(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT_FINAL)) / float(len(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT_FINAL)))
n_mrs, bins_mrs, patches_mrs = plt.hist(list(df_isochronism_increase_mrs.RELATIVE_INCREMENT_FINAL), align='left', weights=weights_mrs,edgecolor=Orange3,lw=3,histtype='step',label="MRS")
weights_dij = np.ones_like(list(df_isochronism_increase_dij.RELATIVE_INCREMENT_FINAL)) / float(len(list(df_isochronism_increase_dij.RELATIVE_INCREMENT_FINAL)))
n_dij, bins_dij, patches_dij = plt.hist(list(df_isochronism_increase_dij.RELATIVE_INCREMENT_FINAL), align='left', weights=weights_dij,edgecolor=ForestGreen,lw=3, histtype='step',label="DIJ")
plt.legend(loc=1)
#n, bins, patches = plt.hist(list(df_isochronism_increase_tcp.RELATIVE_INCREMENT), density=True, facecolor='g', alpha=0.75)
plt.xlabel('Daily final current increase (normalized to number of irradiations)')
plt.ylabel('Counts')
plt.title('Histogram of magnet current increase')
plt.savefig("final_magnet_new_dijon.pdf")


