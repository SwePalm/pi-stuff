#!/usr/bin/pyhton3
#hello.py
from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
sense.show_message("Hej Jessica!", text_colour=red)

