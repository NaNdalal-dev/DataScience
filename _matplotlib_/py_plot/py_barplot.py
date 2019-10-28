from matplotlib import pyplot as plt




ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(ages_x,py_dev_y,width=.5,color="yellow")
plt.xlabel("Ages")
plt.ylabel("Median salaries of py devs")
plt.title("Median salaries of pydevs by ages")

plt.legend()
plt.show()