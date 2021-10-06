def factorial(n):
	if n < 0:
		return "Value cannot be Negative."
		
	if n == 1 or n == 0:
		return 1
		
	else:
		return n*factorial(n-1)
