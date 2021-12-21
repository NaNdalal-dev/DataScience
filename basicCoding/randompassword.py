import random
import string

password_size = int(input("Enter Size of the password:"))

lower = string.ascii_lowercase
#Includes lower case alphabets (a-z)

upper = string.ascii_uppercase
#Includes Upper case alphabets(A-Z)

digits = string.digits
#includes Digits (0-9)

symbols = string.punctuation
#Includes Punctuation Symbols

allChars = lower + upper + digits + symbols
#Combining all characters

random_password = random.sample(allChars,password_size)
#Returns random characters for given size
password = "".join(random_password)

#Prints random password
print(password)