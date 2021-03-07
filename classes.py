#a class is like a blueprint fr createing objects. an object  has properties and methods 
#(functions) associated with it. almost everything in python is an object

#create class
class User:
    #constructor-function that runs when an obh=ject is instantiated from a class
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        #creating a method
    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'
    
    def has_birthday(self):
        self.age += 1


#extend user class
class Customer(User):
#constructor-function that runs when an obh=ject is instantiated from a class
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am  {self.age} and i am {self.balance}'
    

#init user object
joe = User('Joe Deo', 'Joe@mail.com', 37)

#init user object
janet = Customer('Janet Johnson', 'jane@mail.com', 25)

janet.set_balance(500)
print(janet.greeting())

joe.has_birthday()
print(joe.greeting())