#coparison among three numbers to find maximum
'''
num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")
num3 = input("Enter Third Number: ")

if int(num1)>int(num2) and int(num1)>int(num3):     #every conditions thar are used must be true
    print(num1)
elif int(num2)>int(num1) and int(num2)>int(num3):
    print(int(num2))
else:
    print(int(num3))
'''

#vowel and consonent finding

charecter = input("Enter a character: ")
#charecter = 'c'

if charecter == 'a' or charecter == 'e' or charecter == 'i' or  charecter == 'o' or charecter == 'u':       #works when any one condition is true
    print("Vowel")
else:
    print("Consonent")