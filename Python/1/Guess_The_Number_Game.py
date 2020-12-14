#Write a game that does the following:
#1.Computer generates random interger
#2.Player guesses
#3.Computer tells the player if there number is too high or too low
#4.Repeats step 2&3 until they guess the right number
#5.Offers the player another round
#Put your Code Below:
from random import randint

playAgain = "y"

while playAgain == "y":
    num = randint(1,50)
    guess = 0

    while guess != num:
        guess = int(input("guess the number:\n"))
        if num < guess:
            print("too high")
        elif num > guess:
            print("too low")

    print("well done")
    playAgain = input("\nDo you want to play again y/n\n").lower()

print("Thanks for playing!")
