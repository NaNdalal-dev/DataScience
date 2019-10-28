from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x,js_dev_y,'b')
plt.title('Median salaries(USD) for Javascript developers')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.show()