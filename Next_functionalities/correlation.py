# VARIABLE CORRELATION 

def func(x, a, c):
    return a * x + c
popt_coll, pcov_coll = curve_fit(func,data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE,func(data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_coll = np.sqrt(np.diag(pcov_coll))

popt_source, pcov_source = curve_fit(func,data_df_source.SOURCE_PERFORMANCE_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_source.SOURCE_PERFORMANCE_AVE, data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_source.SOURCE_PERFORMANCE_AVE, func(data_df_source.SOURCE_PERFORMANCE_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_source = np.sqrt(np.diag(pcov_source))

popt_magnet, pcov_magnet = curve_fit(func,data_df_magnet.CURRENT_AVE,data_df_source.CURRENT_AVE)
plt.plot(data_df_magnet.CURRENT_AVE, data_df_source.CURRENT_AVE, 'o', label='data')
plt.plot(data_df_magnet.CURRENT_AVE, func(data_df_magnet.CURRENT_AVE, *popt), 'g--',
         label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
perr_magnet = np.sqrt(np.diag(pcov_magnet))

fig, ax = plt.subplots()
ax.errorbar(data_df_source.CURRENT_AVE,data_df_beam.COLL_CURRENT_L_AVE + data_df_beam.COLL_CURRENT_R_AVE)
ax.errorbar(source_performance_vacuum.PRESSURE_AVE,source_performance_vacuum.CURRENT_AVE,fmt="o")

corrMatrix_source_vacuum = source_performance_vacuum.corr()
sn.heatmap(corrMatrix_source_vacuum, annot=True)

corrMatrix_source_beam = source_performance_beam.corr()
sn.heatmap(corrMatrix_source_beam, annot=True)

corrMatrix_source_extraction = source_performance_extraction.corr()
sn.heatmap(corrMatrix_source_extraction, annot=True)