#dictionary
dictionary = {
    "name" : "Adam",
    "id" : "0140",
    "year" : "4th"
}
dictionary["name"] = "Joye" #editing data
print(dictionary['name'])
print(dictionary.get('id'))

for x in dictionary:
    print(x) #only printing the keys
    print(dictionary[x]) #accessing elements
print()

#using methods
for x in dictionary.values():
    print(x)
print()
for x in dictionary.items():
    print(x)
print()
for x,y in dictionary.items():
    print(x)
    print("-")
    print(y)

del dictionary["name"]
print(dictionary)

'''
studentID = {
    101 : "Jhon Doe",
    102 : "Jane Doe",
    103 : "Rahim Khan",
    104 : "Karim Khan",
}
print(studentID.get(103,"Not a vlid key"))
'''