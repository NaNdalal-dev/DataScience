def sum_of_digits(num,total=0):
	if num!=0:
		r = num%10
		total += r
		sum_of_digits(num//10,total)
	else:
		print('sum of digits:',total)

sum_of_digits(127) #1+2+7 = 10

#Task: Reverse of Digits using Recursion