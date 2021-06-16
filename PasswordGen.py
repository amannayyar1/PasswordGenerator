'''
Random Password Generator using Python
Author: Aman Nayyar
'''

# import the necessary modules!
import random
import string 

print('hello, Welcome to Password generator!')  # greet the user

# input the length of password
length = int(input('\nEnter the length of password: '))                      

# define data using string module
lower = string.ascii_lowercase       # using the ascii to store the upper and lowercase alphabet
upper = string.ascii_uppercase
num = string.digits                  # the numbers
symbols = string.punctuation         # for special characters which is important 
# string.ascii_letters

# combine the data to make the strong password
all = lower + upper + num + symbols      

# use random to make the password with evrything and the length which comes with user input
temp = random.sample(all,length)

# create the password by using the temp variable
password = "".join(temp)    

# print the password
print(password)