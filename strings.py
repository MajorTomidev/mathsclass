# String Concatination
first_name = 'Tomisin'
last_name = 'Odukoya'
print (first_name + ' ' + last_name)

f= ('tomisin' + 'odukoya') *3
print (f)

#  String interpolation
x = 10 + 5 +5
print (f"the answer is {x}")

# # Input Function

first_name = input('First name:')
last_name = input ('Last name:')
year_of_birth = int(input('Year of birth:'))
state = input('State of Origin:')
occupation = input('Occupation:')

current_year = 2022

age = current_year - year_of_birth

print (f'Welcome,{first_name}{last_name} you are {age} years old, you were born in {state} state and you currently work as a {occupation}')

b = 'i am just good you know'
print(b[5:9])

print(b[0:4] + " " + b[10:14])

first_name = input('What is your first name:')
last_name = input('What is your last name:')

print (f'Username: @{last_name[:3] + first_name[-3:]}')
print (first_name + last_name)

# Mr Desmonds solution
username = last_name[:3] + first_name[-3:]
print (username)

name = 'tomisin'
print(name.upper())

a = 'i am a good bad guy'
# upper method
print(a.upper())
# lower method
print(a.lower())
# title method
print(a.title())
# capitalize method
print(a.capitalize())
# split method
print(a.split())
# count method
print(a.count('a'))
# replace method
print(a.replace('bad', 'fresh'))

# is_numeric method
f= 'tomisinisnumber1'
print(f.isnumeric())
# is_alphanumeric method
print(f.isalnum())


d = 'tomisinodukoya'
print(len(d))
last = d[-1]
print(last)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
        print(count)

from hashlib import new
from sys import prefix


prefix = 'mango', 'apple', 'orange'
suffix = '+234'
for fruits in prefix: 
    print(fruits + suffix)

    greeting = 'Hello, world!'
    new_greeting = 'T' + greeting[1:]
    print (new_greeting)

    print(type(-1))

    a= 'tomisin'
    for letter in a: print(letter)
    
    a= 'prosp'
    
    print(a.replace('s', ''))
    print(a.upper())

    if len(a) > 5: print('yes')
    elif len(a) == 5: print('accurate')
    else: print('no')

username = input('Enter a Username:')

if len(username) > 10: print('Your Username is too Long')
elif len(username) == 7: print('Username Accepted')
else: print('Your Username is too short')

name = input('Enter a Username:')

if 'a' in name: print('Invalid Name')
elif 'c' in name: print('Not Allowed')
elif 'e' in name: print('Error')
else: print('Username saved successfully')

a = [1,2,3,4,5,6,7,8,9,10]


print(a[1:8])

b= [5,2,2,4,4,1,1,7,7,7,8]
print (set(b))

a = 'tomisin'
b = list(a)
print(b)

a = [2,3,4,5,8]
first_number= a[0]
last_number = a[-1]

a.remove(first_number)
a.remove(last_number)
print(a)

my_dict = { 
    'a': 1,
    'b': 2,
    'c': 3
}
print(my_dict['a'])

a = [2,4,8,15,22,55]

total_num = sum(a)
amount_num = len(a)

average = total_num // amount_num
print(average)