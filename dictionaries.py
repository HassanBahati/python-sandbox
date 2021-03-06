#a dictionary is a collection which is unordered , changeable an dindexed. no duplicate members

#create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#use constructor
person2 = dict(first_name = 'Sara', last_name = 'Williams')

print(person)

#get value
print(person['first_name'])  
print(person.get('last_name'))

#add key/value
person['phone'] = '555-555-5555'

print(person)

#get dict keys
print(person.keys())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

#remove an item
del(person['age'])
person.pop('phone')

#clear
person.clear()

print(person)

#get length
print(len(person2))

#list of dict
people = [
    {'name': 'martha', 'age': 30},
    {'name': 'kevin', 'age': 25}
]

print(people[1]['name'])