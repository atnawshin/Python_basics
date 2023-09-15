#input list from user
'''
num = input("Enter a list of number string: ")

list = num.split()
sum = 0

for num in list:
    sum = sum + int(num)
print(sum)
'''

#count letters,digits in a input
numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0

text = input("Enter a text: ")
for x in text:
    x = x.lower()
    if 'a' <= x <= 'z':
        numberOfLetters = numberOfLetters + 1
    elif '0' <= x <= '9':
        numberOfDigits = numberOfDigits + 1
    elif " " == x:
        numberOfWords = numberOfWords + 1
print("Number of letters: ",numberOfLetters)
print("Number of digits: ",numberOfDigits)
print("Number of words: ",numberOfWords+1)


