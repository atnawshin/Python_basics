#xargs
def student(*details): #*details(or something else) allows to print all the informations passes through the function no matter how many
    print(details)
    print(details[0]) #will work like tuples

student(101,"Joye",3.56)
student(102,"Jhon",3.64)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(10,20)
add(10,20,50)
add(10,20,50,70)