from CentralTendency import*
from math import*
def obs(x,y,predict,showdata=False):
	if(len(x)==len(y)):
		sy=0
		n=len(x)
		deviation=[]
		devsqr=[]
		dvsqr=0
		xy=[]
		sumxy=0
		m=i_mean(x)
		for i in range(len(x)):
			sy+=y[i]
			deviation.append(x[i]-m)
			devsqr.append(deviation[i]**2)
			dvsqr+=devsqr[i]
			xy.append(deviation[i]*y[i])
			sumxy+=xy[i]
		#equation of st line: y=b0+b1*x
		b0=sy/n
		b1=sumxy/dvsqr
		if(showdata==False):
			y=[]

			newdev=[]
			for i in range(len(predict)):
				y.append((b0+b1*(predict[i]-m)))
				round(y[i])
			return y
		else:
			data={
			'deviation':deviation,
			'sumy':sumxy,
			'deviation sqr':devsqr,
			'X*y':xy,
			'sumxy':sumxy,
			'b0':b0,
			'b1':b1

			}
			return data
	else:
		return'Error: length of X and Y axis must be same'
#sample output: 
#print(obs([1975,1980,1985,1990,1995,2000],[10,13,15,20,22,28],[2005]))
#[30.200000000000003]
