#tuples - values are not changable but way faster than list
'''For list we use [], for dictionary we use {}'''

students = (
    "Jhon Doe",27,3.53,
    "Jane Doe",27,3.53,
    "Sharlock Holmes",27,3.53,
    "Jhon Wattson",27,3.53,
)
'''students[0]="jsh" #wouldn't work because values are not changable'''
print(students[0:])
#print(students)