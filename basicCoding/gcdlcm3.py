#Function to find GCD
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

#Function to find LCM
def lcm(a,b):
	#Find Maximum of a and b 
	max_val = max(a,b)

	while True:
		if max_val % a == 0 and max_val % b == 0:
			return max_val
		max_val += 1
a = 18
b = 24
print('Given Values:',a,b)
print('GCD:',gcd(a,b))
print('LCM:',lcm(a,b))

