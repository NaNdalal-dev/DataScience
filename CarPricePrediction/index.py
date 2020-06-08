from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression
df=pd.read_csv('cars.csv')
cars=pd.get_dummies(df['Car Model'],prefix='car')
new_df=pd.concat([df,cars],axis='columns')
new_df=new_df.drop(['Car Model','car_Mercedez Benz C class'],axis='columns')
x_data=new_df.drop(['Sell Price($)'],axis='columns')
y_data=new_df['Sell Price($)']

app=Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')
@app.route('/result',methods=['POST'])
def result():
	model=LinearRegression()
	model.fit(x_data,y_data)
	car=request.form['model']
	mileage=float(request.form['mileage'])
	age=float(request.form['age'])
	if car=='BMW X5':
		pred=model.predict([[mileage,age,0,1]])
	elif car=="Audi A5":
		pred=model.predict([[mileage,age,1,0]])
	else:
		pred=model.predict([[mileage,age,0,0]])
	result=[car,mileage,age,float(pred)]
	cols=['Car Model','Mileage','Age','Predicted Price']
	return render_template('result.html',result=[cols,result])

if __name__=='__main__':
	app.run(debug=True)