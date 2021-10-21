def square(n):
	return n*n
numbers = [1,2,3,4]

square_of_each_num = []

for num in numbers:
	square_of_each_num.append(square(num))

print(square_of_each_num)

