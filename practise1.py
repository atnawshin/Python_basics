'''n = 10#int(input())
i = 1
while i<=n:
    #print(i)
    i=i+1

i = 1
for i in range(10,0,-1):        #printing in reverse order(1-10)
    print(i)
print("End")
j = 1
for j in reversed(range(10)):       #printing in reverse order(0-9)
    print(j)'''
'''
i = 10
while i>=1:       #printing in reverse order
    print(i)
    i = i-1
print("End")

j = 1
while j<=10:
    print(j)
    j = j+1
'''
'''
i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i+1
print("End")

i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i+1
'''
'''
fruits = ["Mango","Banana","Orange","Apple","Grape"]

print(fruits)
print(fruits[2:])
print(fruits[-1])
print(fruits+["Avocado","Bery","Guava",33])
print(fruits*2)
print("Prawn" in fruits)
print("Apple" not in fruits)
print("Apple" in fruits)'''
'''
#prime number
n = int(input())

for i in range(2,n):
    if n % i == 0:
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")
'''

n = 5
'''
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
        print(" ",end="")

    for j in range(i+1):
        print("*", end="")
    print()
