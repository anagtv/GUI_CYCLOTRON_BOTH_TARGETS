people = ('Foil 1 (2)', 'Foil 2 (2)', 'Foil 3 (2)', 'Foil 4 (2)', 'Foil 5 (2)', 'Foil 6 (2)')
y_pos = np.arange(len(people))
performance = np.array(total_foil_relative_4)*100
print ("Before")
print (performance)
performance_2 = performance.copy()
performance_3 = performance.copy()
performance_index = [i for i, x in enumerate(performance > 90) if x]
performance_index_2 = [i for i, x in enumerate(performance > 70) if x]
print (people)
print (performance_index)
print (performance_index_2)
for i in performance_index:
    performance_3[i] = 90
for i in performance_index_2:
	performance[i] = 70
error = np.random.rand(len(people))
ax.barh(y_pos, performance_2,color=red, align='center')
ax.barh(y_pos, performance_3,color=yellow, align='center')
ax.barh(y_pos, performance,color=green, align='center')
print ("Performance 3")
print (performance_3)
print ("Performance 2")
print (performance_2)
print ("After")
print (performance)
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Accumulated Charge relative to relative values [%]')
plt.savefig("foils_4_before.pdf")
