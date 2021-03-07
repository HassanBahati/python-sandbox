#a looop is used for iterating over a sequence (than is either a list , a tuple , a dictionary , a set , or a string)

people = ['John', 'Pual', 'Sara', 'Suzan']

#simple for loop
# for person in people:
#     print(f'current person: {person}')

#break -when you reach sara stop
for person in people:
    if person == 'Sara':
        break
    print(f'current person: {person}')

#continue -when you reach sara skip it and continue
for person in people:
    if person == 'Sara':
        continue
    print(f'current person: {person}')

#range
for i in range(len(people)):
    print(people[i])

for i in range(0, 10):
    print(f'Numbers: {i}')


#while loops execute a set of statements as long as a condition is true

count = 0
while count <= 10:
    print(f'count : {count}')
    count += 1