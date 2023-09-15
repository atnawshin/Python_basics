#pattern
'''
n = 4
*
**
***
****
'''

n = 5
'''
for i in range(n+1):
    print((2*i-1) * "*")

#even
for i in range(n+1):
    print(i*"*")

#odd
for i in range(n+1):
    print((2*i) * "*")

for i in range(n+1):
    print((i)*"*")
    
for i in range(n):
    for j in range(n-i-1):
       print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
'''
for i in range(n):  #determine rows
    for j in range(i+1): #determine columns
        print("* ",end="") #print 1 row
    print()

for i in range(n):  #determine rows
    for j in range(i,n): #determine columns
        print("* ",end="") #print 1 row
    print()

for i in range(n):  #determine rows
    for j in range(i,n):
        print("  ",end="")

    for j in range(i+1):
        print("* ", end="")
    print()

for i in range(n):
    for j in range(i+1):
        print('',end='')
    for j in range(i,n):
        print('*',end='')
    print()

for i in range(n):
    for j in range(i,n):
        print('',end='')

    for j in range(i):
        print('*',end='')

    for j in range(i+1):
        print('*',end='')
    print()
print()
#for reverse mountain
for i in range(n):
    for j in range(i+1):
        print(" ",end="")

    for j in range(i,n-1):
        print("*",end="")

    for j in range(i,n):
        print("*",end="")
    print()

