from math import factorial

n = int(input("Enter a Number:"))

m=n
sum_of_nums = 0

while n:
	r = n % 10
	sum_of_nums += factorial(r)
	n //= 10 #Or n = n//10 
if m == sum_of_nums:
	print(f"{m} is Strong.")
else:
	print(f"{m} is Not Strong")