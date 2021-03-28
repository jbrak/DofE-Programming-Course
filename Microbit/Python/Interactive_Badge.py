# Docs - https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/images.htmlhttps://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/images.html
from microbit import *

#Stuff to run once at the beggining
happy =Image(
            "08080:"
            "00800:"
            "80008:"
            "08080:"
            "00800:")
confused = Image.CONFUSED
sequence = [happy, confused]

#Stuff to run repeatedly
while True:
    if button_a.is_pressed() and button_a.is_pressed():
        display.show(sequence, delay=500)