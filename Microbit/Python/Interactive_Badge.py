# Docs - https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/images.html
from microbit import *

#Stuff to run once at the beggining
happy = Image(
            "08080:"
            "00800:"
            "80008:"
            "08080:"
            "00800:")
confused = Image.CONFUSED
sequenceA_B = [happy, confused]

sicsorseOpen = Image(
            "80008:"
            "08080:"
            "00800:"
            "08080:"
            "88088:")
strin = Image(
       "80808:"
        "08080:"
        "00800:"
        "08080:"
        "88088:")

closedScisors = Image(
            "00800:"
            "00800:"
            "00800:"
            "08080:"
            "88088:")

sequenceA = [sicsorseOpen, strin, closedScisors]

sequenceB = [Image.STICKFIGURE,Image.SWORD,Image.SKULL,Image.GHOST,Image.GIRAFFE]

#Stuff to run repeatedly
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(sequenceA_B, delay=500)
    elif button_a.is_pressed():
        display.show(sequenceA, delay=500)
    elif button_b.is_pressed():
        display.show(sequenceB, delay=700)
