'''
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to print: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()

for i in range(3):
    for j in range(1,10):
        print(j, end=" ")
    print()
'''

n = 5 #int(input())
#'''
#increacing triangle
for i in range(n):
    for j in range(i+1): #to print an incremental pattern we need to print 1 row plus 1 * so we need to set the range to i+1
        print("*", end=" ")
    print()
print(end="\n")
#'''
#decreasing triangle
for i in range(n):
    for j in range(i,n):    #(n-i) also works
        print("*",end=" ")
    print()
print()
#printing two triangles- decreasing space, increasing star

for i in range(n):
    for j in range(i,n):    #decreasing number of space
        print(" ",end=" ")
    for j in range(i+1):    #increasing number of stars
        print("*", end=" ")
    print()
print()
#right sided triangle
for i in range(n):
    for j in range(i+1): #increasing triangle
        print(" ",end=" ")
    for j in range(i,n): #decreasing triangle
        print("*", end=" ")
    print()
print()
#Hill pattern
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):  #to reduce 1 row
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):  #to reduce 1 row
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
print()
#Diamond pattarn
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()