# Formated String - It is use to avoid concatenation
# name = "Raheel"
# age = 30

# print(f'My name is {name}. I am {age} years old')

# # In python 2 used
# print('My name is {}. I am {} years old'.format(name, age))
# print('My name is {}. I am {} years old'.format('Raheel', 30))
# print('My name is {1}. I am {0} years old'.format('Raheel', 30))
# print('My name is {new_name}. I am {new_age} years old'.format(new_name = 'Raheel', new_age = 30))
# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")




#String Indexes

selfish = "12345678"
          #01234567 indexes

print(selfish[0]) # accessing string on the index 0

# String manipulation
# [start:stop:stepover] it is called slicing
print(selfish[0:8:1]) # start from 0 index end 8th index and stepover by 1
print(selfish[0:8:2]) # start from 0 index end 8th index and stepover by 2
print(selfish[1:])  # start from 1st index and everything default
print(selfish[:5])  # start from 0 index and end on 5th index and stepover by 1 (default)
print(selfish[::2]) # start and end are default stepover by 2
print(selfish[-3])  # start from reverse and take the 3rd
print(selfish[::-1]) # reverse with stepover by 1

#Guess the output of each print statement before you click RUN!
python = 'I am PYHTON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

# Strings are immutable we can not change string with giving index we have to create new variable for chaning it.

sample = "01234567" # old sample
#sample[0] = 4 # we can not do this because strings are immutable
sample = sample + '8' # now sample will be this
print(sample)