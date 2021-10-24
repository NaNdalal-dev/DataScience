def linearSearch(arr,search,index=0):
	
	if index < len(arr):
		if arr[index] == search:
			print("Value found at index:",index)
			return index
		linearSearch(arr,search,index+1)

	else:
		print("Value Not Found.")
		return False
linearSearch([1,2,3,4],3)

