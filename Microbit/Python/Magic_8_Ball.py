# Docs - https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/gestures.html
from microbit import *

#Create A Magic 8 ball that prints a magic 8 ball awnser when you shake the microbit
#list of magic 8 ball awnsers:
answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]
#Stuff to run once at the beggining
from random import choice


#Stuff to run repeatedly
while True:
    if accelerometer.was_gesture("shake"):
        display.scroll(choice(answers))
        sleep(5000)
