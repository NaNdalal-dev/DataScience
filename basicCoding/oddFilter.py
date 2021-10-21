numbers = [1, 2, 3, 4, 5, 6, 7]
print('Before filter:',numbers)

# returns True if number is odd
def check_odd(number):
    if number % 2 == 1:
          return True  
    return False

# Extract elements from the numbers list for which check_odd() returns True
odd_numbers_iterator = filter(check_odd, numbers)

# converting to list
odd_numbers = list(odd_numbers_iterator)

print('After filtering even numbers:',odd_numbers)
