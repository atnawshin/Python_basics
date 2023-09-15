'''n = input("Enter a text of numbers: ")

list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)'''

numberOfWords = 0
numberOfDigits = 0
numberOfLetters = 0

text = input("Enter a text: ")

for x in text:
    x = x.lower()
    if 'a'<= x <= 'y':
        numberOfLetters = numberOfLetters + 1
    elif '0'<= x <='9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 1

print(numberOfLetters)
print(numberOfDigits)
print(numberOfWords+1)