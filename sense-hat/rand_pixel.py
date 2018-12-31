#!/usr/bin/python3
#rand.py
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def pick_random_colour():
	random_red = randint(0, 255)
	random_green = randint(0, 255)
	random_blue = randint(0, 255)
	return (random_red, random_green, random_blue)
def randpix():
	random_pixel = randint(0, 7)
	return (random_pixel)

sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)
sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)
sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)
sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)
sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)
sense.set_pixel(randpix(), randpix(), pick_random_colour())
sleep(1)

sense.clear()
