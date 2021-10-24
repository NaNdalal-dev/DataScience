def traversal(arr,index=0):
	if index < len(arr):
		print(arr[index])
		traversal(arr,index+1)


mylist = [10,20,30,40,50]
print('Elements in array:')
traversal(mylist)
