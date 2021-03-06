#a funciton is a block of code which only runs when it is callled.
#in python, we do not use curly brackets , we use indention with tabs or spaces


#create function
def sayHello(name = 'Sam'):
    print(f'hello {name}')


#return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3, 4)

print(num)



'''
a lambda function is a small anonymous function
a lambda function can take any number of arguments, but can only have one expresssion. 
very similar to js arrow function
'''

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))