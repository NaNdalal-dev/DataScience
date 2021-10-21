#Function to get Maximum value 
def getMax(array):
	max_val = array[0]
	for val in array[1:]:
		if val > max_val:
			max_val = val
	return max_val

#Function to get Minimum value 
def getMin(array):
	min_val = array[0]
	for val in array[1:]:
		if val < min_val:
			min_val = val
	return min_val

myArray = [19,-3, 4, 1, 2, 5,-10]


min_val = getMin(myArray)

max_val = getMax(myArray)

print("Given Array:",myArray)
print("Minimum Value:",min_val)
print("Maximum Value:",max_val)

