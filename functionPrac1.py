'''
def compare(x,y):
    max = 0
    if x>y:
        max = x
    else:
        max = y
    return max
print(compare(5,41))
'''
'''
def my_function(*kids):
    print("The first kid is",kids[0]) #here kids working as a tuple
my_function("Alice","Bob","Carol")
'''
'''
def my_func(*update):
    print("Updates: ",update[0],update[1],update[2],update[3])
my_func("Male:",1000,"Female:",800)
'''
'''
def my_funct(*msg):
    for x in msg:
        print(x,end=" ")

my_funct("Python","is","fun!")
'''
'''
def display(msg1,*msg):
    print(msg1)
    print(msg)
display("Python","is","fun!")
'''
#key-word arguments
'''
def my_function(child3,child2,child1):
    print("The youngest child is",child3)
my_function(child1="Ross",child2="CHandler",child3="Joye")
'''
'''
#for unknown number of key-word agrus we'll use **
def my_func(**car):
    print("Model is",car["model"])
my_func(name="Lamborghini",model="Aventador")
'''

#return statement
'''
def my_func(x):
    return 5 * x
print(my_func(3),end=" ")
print(my_func(5),end=" ")
print(my_func(8),end=" ")
'''
'''
def nsquare(x, y):
    return (x*x + 2*x*y + y*y)
print(nsquare(2,3))
'''
'''
def my_funce():
    pass
my_funce()
'''
'''
def function(x,y):
    return x+y
a = function(3,4)
print(a)
'''
#scoping of function
'''
a = 'Global a' #global variable
def my_function():
    a = 'Local a' #local variable
    a = a + ' test'
    print(a)
my_function()
print(a)
'''
'''
a = 'global a'
def my_function():
    global a    #for updating a global variable in a scope we have to use a specific keyword 'global' and then write the global variable name. it will change the value of the global variable by updating it with new value in all places
    #we can use a global variable without using global key word but for update 'global' keyword is required
    a = a + ' Test'
    print(a)
my_function()
print(a)
'''
#nested function
a = 'global a'
def outer_f():
    a = 'outer a'
    def inner_f():
        #a = 'inner a'
        nonlocal a
        a = a + ' test'
        print(a)
    inner_f()
    print(a)
outer_f()







