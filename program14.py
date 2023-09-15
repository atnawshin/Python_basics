#summation of numbers
n = int(input("Enter the last number: "))
sum1 = 0
sum2 = 0
sum3 = 0

i = 0
while i <= n:
    sum1 = sum1 + i
    i = i+1
    print(i)     #will print sum of every two number
print("Sum of the numbers is: ",sum1)

i = 1
while i <= n:
    sum2 = sum2 +i
    i = i+2
    print(i)
print("Sum of the odd numbers is: ",sum2)

i = 0
while i <= n:
    sum3 = sum3 +i
    i = i+2
    print(i)
print("Sum of the even numbers is: ",sum3)

#initialize with 2 for printing even numbers
sum4 = 0
i=2
while i<=n:
    if i%2==0:
        sum4 = sum4 + i
        i = i+2
        print(i)
print("Even numbers: ",sum4)

#for odd numbers
sum5 = 0
i=1
while i<=n:
    if i%2==1:
        sum5 = sum5 + i
        i = i+2
        print(i)
print("Odd numbers: ",sum5)