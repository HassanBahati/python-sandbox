# a varible is a container for a value, wich can can be of various types

'''
VARIABLE RULES
 -variable names are case sentitive (name and NAME are different variables)
 -must start with a letter or an underscore
 - can have numbers but can not start with one 
'''

x = 1  #integer
y = 2.5   #float
name = 'John'  #string
is_cool = True   #bool

#multiple assignment 
x, y, name, is_cool = 1, 2.5, 'John', True


#casting 
x =str(x)
y = int(y)


print(type(y))
