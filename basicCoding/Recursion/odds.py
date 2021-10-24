def odds(firstnum,lastnum):
	if firstnum <= lastnum:
		if firstnum % 2 == 1:
			print(firstnum)
		odds(firstnum+1,lastnum)

#Odd Numbers between 10 to 20
odds(10,20)

#Task Print Even Numbers in a given range