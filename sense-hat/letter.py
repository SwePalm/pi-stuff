#!/usr/bin/pyhton3
#hello.py
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

paint = (0, 0, 255)
sense.show_letter("Z", text_colour=paint)
sleep(2)
sense.clear()
