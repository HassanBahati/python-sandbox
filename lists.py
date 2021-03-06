#a list os a collection which is ordered and chageable. allows duplicate members

#create list
numbers = [1,2,3,4,5]

#use a constructor 
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(fruits[1])

#get length
print(len(fruits))

#append a list
fruits.append('mangoes')

#remove from list 
fruits.remove('Grapes')

#insert into given position
fruits.insert(2, 'Strawberry')

#change value
fruits[0] = 'Blueberries'

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)

