n = 5
#increasing row numbers
p = 1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
print("")
#decreasing row numbers
q = 5
for i in range(n):
    for j in range(i+1):
        print(q,end=" ")
    q-=1
    print()
print()
#Even increasing row numbers
e = 0
for i in range(n):
    for j in range(i+1):
        print(e,end=" ")
    e+=2
    print()
#alternate numbers
a = 5
for i in range(a):
    for j in range(i+1):
        if (i%2==0):
            print("1",end=" ")
        else:
            print("2",end=" ")
    print()
print()
#incrimental diamond pattern
c = 1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(c,end=" ")
    for j in range(i+1):
        print(c,end=" ")
    c+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(c,end=" ")
    for j in range(i,n):
        print(c,end=" ")
    c+=1
    print()
print()
#Decrementing diamond pattern
c = 1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(c,end=" ")
    for j in range(i+1):
        print(c,end=" ")
    c+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(c,end=" ")
    for j in range(i,n):
        print(c,end=" ")
    c-=1
    print()

#change in column numbers

for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()
print()

#reverse column numbers
for i in range(n):
    p = 1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i, n):
        print(p, end=" ")
        p+=1
    print()
print()
#hill pattern
for i in range(n):
    p = 1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i):
        print(p, end=" ")
        p+=1
    print()
print()

#Diamond pattern
for i in range(n-1):
    p = 1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i):
        print(p, end=" ")
        p+=1
    print()
for i in range(n):
    p = 1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(p,end=" ")
        p+=1
    for j in range(i,n):
        print(p, end=" ")
        p+=1
    print()
print()

#starting numbers of the column are same
for i in range(n):
    p = 5
    for j in range(i+1):
        print(p,end=" ")
        p-=1
    print()
print()
#different start value(variable starting number)
k = 5
for i in range(n):
    p=k
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print( p,end=" ")
        p-=1
    k-=1
    print()
print()
#Hill triangle

for i in range(n):
    p = 1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p-=1
    print()
print()
#Floyed triangle
n = 4
p = 1
for i in range(n):
    for i in range(i+1):
        print(p,end=" ")
        p+=1
    print()