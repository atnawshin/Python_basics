#sum of two numbers that returns value
def add(a,b):
    sum = a + b
    return sum

result = add(20,30)
print("Result = ",result)

def large(a,b):
    if a>b:
        return a
    else:
        return b
#we can use a function as a variale also
max = large
print("Large num is: ",large(30,57))
print("Large num is: ",max(30,57))
