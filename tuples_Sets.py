#a tuple is a collection that is ordered and unchangeable.allows duplicate memebrs

#create tuple
fruits = ('Apples', 'oranges', 'grapes')

fruits3 = tuple(('apples', 'oranges', 'grapes'))

print(fruits, fruits3)
 
fruits2 = ('banana',)
#sinlge value needs a trailing comma
print(fruits2, type(fruits2))

print(fruits[1])

print(len(fruits2))


#a set is a collection ehich is unordered and unindexed. no duplicate members

#create set
fruits_set = {'Apples', 'Oranges', 'Magoes'}

#check if in set
print('Apples' in fruits_set)

#add to set 
fruits_set.add('Grapes')

#remove from set
fruits_set.remove("Grapes")

#clear set
fruits_set.clear()


print(fruits_set)