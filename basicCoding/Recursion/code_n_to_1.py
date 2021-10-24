def print_n_to_1(lastnum):
	if lastnum != 0:
		print(lastnum,end=" ")

		print_n_to_1(lastnum-1)

print_n_to_1(10)


