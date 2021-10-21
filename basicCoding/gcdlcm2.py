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
#LCM of 18 and 24
print("LCM:",lcm(a,b))

#GCD of 18 and 24
gcd = a*b // lcm(a,b)
print("GCD:",gcd)

