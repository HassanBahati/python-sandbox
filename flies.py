#python has fucnctions for creating , reading , updating and deleting files

#open a file
myFile = open('myfile.txt', 'w')

#get some info
print('name:', myFile.name)
print('is closed:', myFile.closed)
print('opening mode', myFile.mode)

#write to file
myFile.write('Python is interesting')
myFile.write(' and Javascript')
myFile.close()

#append to file
myFile = open('myfile.txt', 'a')
myFile.write(' i also like react')


#read from file 
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)