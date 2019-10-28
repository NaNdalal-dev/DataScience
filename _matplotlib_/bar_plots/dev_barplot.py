from matplotlib import pyplot as pt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

pt.bar(ages_x,dev_y,color='#444444',width=0.5)
pt.xlabel("Ages")
pt.ylabel("Median salary of Devs ")
pt.title("Devs Medain salary by ages")
pt.show()