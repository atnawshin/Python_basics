#For loop
'''num1 = list(range(10,51,10))
print(num1)'''

#num = [10,20,30,40,50]
#print(num)
#iterating every element
'''
index = 0
n = len(num)
while index < n:
    print(num[index])
    index = index + 1'''

num1 = [10,20,30,40,50,1,2,3,4,5,6,7,8,9,10]
#num = list(range(1,10,2))
num = sorted(num1)
print(num)

sum = 0
Evensum = 0
Oddsum = 0
#for i in num:
    #print(i) #printing every item

for x in num:
    print(x)
    sum = sum + x
print("Sum:",sum)
'''
for x in range(len(num)): #x will ittrate untill length of the sum
    if x%2==0:
        Evensum = Evensum+num[x]
print(Evensum)
'''
for x in range(len(num)): #puting the values of list num in x variable one after another
    if x%2==0:
        Evensum = Evensum + num[x]
    else:
        Oddsum = Oddsum + num[x]

print("Even sum:",Evensum)
print("Odd sum:",Oddsum)