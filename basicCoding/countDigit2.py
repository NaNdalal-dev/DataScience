num = abs(int(input("Enter a Number:")))
digitCounter = 0

print("Given Number:",num)
while num != 0:
	digitCounter += 1 
	num //= 10
	
print("Number of digits:",digitCounter)