from matplotlib import pyplot as plt

plt.title('Median salaries comparision of python,JS and Devs by age')
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]



py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.xlabel('Ages')
plt.ylabel('Median Salaries of JS,PY and Devs by ages')

plt.plot(ages_x,dev_y,'k--',label='Devs',marker='*')
plt.plot(ages_x,js_dev_y,'b',label='Javascript',marker='*')

plt.plot(ages_x,py_dev_y,'y',label='Python',marker='*')

plt.grid(1)
plt.legend()
plt.tight_layout()
plt.show()