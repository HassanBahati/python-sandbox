#if/else conditions are used to decide to do something based on something being true or false

x = 20
y = 20

#comaprison operators (==, !=, >, <, >=, <=) used to comapre values

#simple if
# if x > y:
#     print(f'{x} is greater than {y}')

#if else
if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

 
#nested if 
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


#logical operators (and, or, not) used to combine conditional statements

#and
if x > 2 and x <=10:
    print(f'{x} is greater than 2 and less than or equal to 10')

#or
if x < 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')
 
#not 
if not(x == y):
    print(f'{x} is not equal to {y}')

#membership operators (not, not in) membership operators are used to test if a sequence is presented in an object
numbers = [1,2,3,4,5]

#in
if x in numbers:
    print(x in numbers)

#not in
if x not in numbers:
    print(x not in numbers)

#identifying operators (is, is not ) compare the onjects, not if they are equal , but if they are actually the same object with tthe same memory location

#is
if x is y:
    print(x is y)

#is not - print true if x is not y
if x is not y:
    print(x is not y)