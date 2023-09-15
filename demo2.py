num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
'''
if int(num1) > int(num2):
    print(int(num1))
else:
    print(int(num2)'''

max = int(num1) if int(num1)>int(num2) else int(num2)
print("Maximum =",max)
