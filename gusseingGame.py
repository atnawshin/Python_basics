from random import randint

for x in range(1,6):
    guessNumber = int(input("Enter your guess between 1 to 5: "))
    randomNumber = randint(1,5)

    if guessNumber == randomNumber:
        print("You have won! Congratulations!")
    else:
        print("You have Lost :(")
        print("Random number was: ",randomNumber)