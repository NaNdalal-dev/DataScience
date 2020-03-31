def i_mean(x):
		s=0
		for i in range(len(x)):
			s+=x[i]
		return s/len(x)
def d_mean(x,f):
	for i in range(len(f)):
		if(type(f[i]!=int)):
			return 'Error:Frequencies should have type int'
	if(len(x)==len(f)):
		s=0
		fx=[]
		s1=0
		for i in range(len(f)):
			s+=f[i]
			fx.append(x[i]*f[i])
			s1+=fx[i]
		return s1/s 
	else:
		return 'Error: length of x and frequency must be same'
def i_median(x):
	l=len(x)//2
	if(len(x)%2!=0):
		return x[l]
	else:
		return (x[l]+x[l-1])/2
def d_median(x,f):
	N=0
	cf=[]
	for i in range(len(f)):
		if(type(f[i]!=int)):
			return 'Error:Frequencies should have type int'
	if(len(x)==len(f)):
		for i in range(len(f)):
			N+=f[i]
			cf.append(N)
		for i in range(len(f)):
			if(cf[i]>N/2):
				return x[i]
	else:
		return 'Error:Length of x and Frequencies should be same'
def i_mode(x,count=False):
	c=0
	mode=[]
	for i in range(len(x)):
		for j in range(len(x)):
			if(x[i] == x[j]):
				c+=1
		mode.append([c,x[i]])
		c=0
	mode.sort(reverse=True)
	if(count==False):
		return mode[0][1]
	else:
		return mode[0]

