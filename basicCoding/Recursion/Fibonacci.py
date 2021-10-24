def Fibonacci(num):
	if num <0:
		return 'Invalid Number.'
	if num == 0 or num == 1:
		return num
	return Fibonacci(num-1) + Fibonacci(num-2)

print("First 10 Fibonacci numbers:")
for i in range(10):
	print(Fibonacci(i),end=' ')