def factorial(n):
	if n < 0:
		return "Value cannot be Negative."
		
	result = 1
	while n:
		result *= n #result = result * n
		
		n -= 1	#n = n - 1
	return result
