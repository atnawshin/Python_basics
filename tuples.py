#tuples - vales change kora jabe na
list = [2,5,6,7,3,7,9] #lists can be modified
print(list[0])
list[0] = 1
print(list[0])
print(list)

students = (
    ("Jhon Doe",27,3,56), #tuples inside of a tuple
    "Jane Doe",
    "Rahim Khan",
    "Karim Khan",
)
print(students[0])
print(students[1:]) #slicing-starting the values printing from index 1