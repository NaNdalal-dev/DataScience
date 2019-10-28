from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x,py_dev_y,'y')
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.title('Median salaries(USD) for Python Developers')


plt.show()