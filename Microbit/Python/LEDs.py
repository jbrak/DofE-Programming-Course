# Docs - https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html
from microbit import *
import neopixel

#Stuff to run once at the beggining
np = neopixel.NeoPixel(pin1, 24)

"""
for i in range(len(np)):
        np[i] = (255,255,255)
        np[i-1] = (150-int(i**1.5),int(i**1.5),0)
        np.show()
        sleep(100)
"""
def zebra():
    for i in range(len(np)):
        if i % 2 == 0:
            np[i] = (200,255,255)
        else:
            np[i] = (0,0,0)
        np.show()
        sleep(100)

def green():
    for i in range(len(np)):
        np[i]= (0,255,0)
    np.show()
    sleep(500)

    for i in range(len(np)):
        np[i]= (0,0,255)
    np.show()
    sleep(500)

    for i in range(len(np)):
        np[i]= (255,0,0)
    np.show()
    sleep(500)

    for i in range(len(np)):
        np[i]= (20,0,255)
    np.show()
    sleep(1000)

    for i in range(len(np)):
        np[i]= (100,255,0)
    np.show()
    sleep(100)

    for i in range(len(np)):
        np[i]= (20,0,255)
    np.show()


#Stuff to run repeatedly
while True:
    if accelerometer.was_gesture("shake"):
        zebra()
    elif button_b.is_pressed():
        np.clear()
    elif button_a.is_pressed():
        green()


    
