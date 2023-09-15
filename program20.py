#Series

#Summation series
#1+2+3+.....+n

n = int(input("Enter the last number: "))
sum = 0

for i in range(1,n+1,1): #n dile n er ag porjonto cholbe tai n+1 dite hobe
    sum = sum + i
print("Total sum: ",sum)

#2+4+6+....+n
evenSum = 0
for i in range(2,n+1,2):
    evenSum = evenSum + i
print("Sum of even numbers: ",evenSum)

#1+3+5+....+n
oddSum = 0
for i in range(1,n+1,2):
    oddSum = oddSum+i
print("Sum of odd numbers: ",oddSum)

#1*1+2*2+3*3+....+n*n

squareSum = 0
for i in range(1,n+1,1):
    squareSum = squareSum + i*i
print("Sum of square series: ", squareSum)

#2*2+4*4+6*6+....+n*n
evenSquareSum = 0
for i in range(2,n+1,2):
    evenSquareSum = evenSquareSum + i*i
print("Sum of even square series: ",evenSquareSum)

#1*1+3*3+5*5+...+n*n
oddSquareSum = 0
for i in range(1,n+1,2):
    oddSquareSum = oddSquareSum + i*i
print("Sum of odd square series: ",oddSquareSum)

#1 + 1/2 + 1/3 + ... + 1/n
divideSum = 0
for i in range(1,n+1,1):
    divideSum = divideSum + 1/i
print(divideSum)

#Multiplication series

#1*2*3*.....*n
mul = 1 #it has to be 1 otherwisw if it's 0 it will make everything 0
for i in range(1,n+1,1):
    mul = mul * i
print("Multiplication: ",mul)

#1*3*5*....*n
oddMul = 1 #it has to be 1 otherwisw if it's 0 it will make everything 0
for i in range(1,n+1,2):
    oddMul = oddMul * i
print("Multiplication of odd numbers: ",oddMul)

#2*4*6*....*n
evenMul = 1 #it has to be 1 otherwisw if it's 0 it will make everything 0
for i in range(2,n+1,2):
    evenMul = evenMul * i
print("Multiplication of even numbers: ",evenMul)

#1*1 * 2*2 * 3*3 * ... * n*n
squareMul = 1 #it has to be 1 otherwisw if it's 0 it will make everything 0
for i in range(1,n+1,1):
    squareMul = squareMul * i*i
print("Multiplication of square numbers: ",squareMul)

#2*2 * 4*2 * 6*2 * ... * n*2
evenSquareMul = 1 #it has to be 1 otherwisw if it's 0 it will make everything 0
for i in range(2,n+1,2):
    evenSquareMul = evenSquareMul * i*i
print("Multiplication of even square numbers: ",evenSquareMul)

#Factorial(n!)
factorial = 1

if n < 0:
    print("Invalid! Factorial does not exist for negative numbers.")
elif n == 0:
    print("Factorial of 0 is, 0! = 1")
else:
    for i in range(1,n+1,1):
        factorial = factorial * i
    print("Factorial of",n,end="",)
    print("! is:",factorial)

#Prime Number
if n == 1:
    print(n,"is not a prime number")
elif n > 1:
    for i in range(2,n):
        if n%i == 0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is a prime number")

'''for i in range(2,n,1): #it's not going to nth number because once it' there it will be divided by that completely that would make it not prime so it will check uptill n-1
    if n % i == 0:
        print(n,"is not a prime number.")
        break
else:
    print(n,"is a prime number.")'''

#GCD,LCM

#GCD
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1,smaller+1):
    if(num1 % i == 0 and num2 % i == 0):
        gcd = i
print("The GCD of",num1,"and",num2,"is:",gcd)
'''
lcm = (num1*num2)/gcd
print("LCM",lcm)
'''
#LCM
if num1 > num2:
    grater = num1
else:
    grater = num2

for i in range(1,grater+1):
    if (num1 % i == 0 and num2 % i == 0):
        gcd = i
        lcm = (num1 * num2)/gcd
print("The LCM of",num1,"and",num2,"is:",lcm)
'''
maxNum = max(num1,num2)

while(True):
    if(maxNum % num1 == 0 and maxNum % num2 == 0):
        break
    maxNum = maxNum + 1

print(f"The LCM of {num1} and {num2} is {maxNum}")'''

