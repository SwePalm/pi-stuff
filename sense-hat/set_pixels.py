#!/usr/bin/python3
#rand.py
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

#Define some colours
g = (0, 255, 0) #Green
b = (0, 0, 0) #Black


creeper_pixels = [
	g, g, g, g, g, g, g, g, 
	g, g, g, g, g, g, g, g, 
	g, b, b, g, g, b, b, g, 
	g, b, b, g, g, b, b, g, 
	g, g, g, b, b, g, g, g, 
	g, g, b, b, b, b, g, g, 
	g, g, b, b, b, b, g, g, 
	g, g, b, g, g, b, g, g, 
]


sense.set_pixels(creeper_pixels)
sleep(3)

sense.clear()
