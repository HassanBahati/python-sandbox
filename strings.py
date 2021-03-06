'''
strings in python are surrounded by either single or double quotation marks. lets look at string formatting and some string methods
'''

name = 'joe'
age = 37

#concatenate 
print('Hello, my name is ' + name + ' and I am ' + str(age))


#string formatting

#f-string 
print(f'My name is {name} and i am {age}')

#string methods
s = 'hello world'
l = 'HELLO WORLD'
#capitalize 
print(s.capitalize())

#make all uppercase
print(s.upper())

#make all lower case
print(l.lower())

#swap case -alternate case
print(s.swapcase())

#get length
print(len(s))

#replace
print(s.replace('world', 'everyone'))

#count number of a given character in the string
sub = 'h'
print(s.count(sub))
print(s.count('h'))

#starts with
print(s.startswith('hello'))

#ends with
print(s.endswith('d'))

#split into a list
print(s.split())

#find position 
print(s.find('r'))

#is all alphanumeric
print(s.isalnum())

#is all aphabetic
print(s.isalpha())

#is all numeric
print(s.isnumeric())


