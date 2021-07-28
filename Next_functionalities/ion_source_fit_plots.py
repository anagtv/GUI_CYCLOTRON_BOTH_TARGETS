plt.errorbar(average_target,ion_source_average,xerr=std_target,yerr=ion_source_std,fmt="o")			
plt.errorbar(average_collimators,ion_source_average,xerr=std_collimators,yerr=ion_source_std,fmt="o")
plt.errorbar(vacuum_average_absolute,ion_source_average,xerr=vacuum_std_absolute,yerr=ion_source_std,fmt="o")


plt.errorbar(file_values,x_list,yerr=x_list_sigma)
plt.errorbar(file_values,z_list,yerr=z_list_sigma)

plt.scatter(X_test.I_TARGET,func((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1],popt[2]))
plt.scatter(X_test.I_TARGET,y_test)
plt.show()
plt.scatter(X_test.I_COLLIMATOR,func((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1]))
plt.scatter(X_test.I_COLLIMATOR,y_test)
plt.show()
plt.scatter(X_test.VACUUM,func((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1],popt[2]))
plt.scatter(X_test.VACUUM,y_test)
plt.show()
plt.scatter(X_test.VACUUM*1e5,func((X_test.I_TARGET,X_test.I_COLLIMATOR,X_test.VACUUM*1e5),popt[0],popt[1]))
plt.scatter(X_test.VACUUM*1e5,y_test)
