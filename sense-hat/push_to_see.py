from sense_hat import SenseHat
from time import sleep
import subprocess

sense = SenseHat()
sense.set_rotation(90)

while True:
	for event in sense.stick.get_events():
		print(event.direction, event.action)
		if event.direction == 'up':
			sense.show_letter("L")
		elif event.direction == 'down':
			sense.show_letter("R")
		elif event.direction == 'left':
			message = str(subprocess.check_output("hostname -I", shell=True))
			message = message[2:-3]
			sense.show_message(message, scroll_speed=0.05)
		elif event.direction == 'right':
			sense.show_letter("U")
		elif event.direction == 'middle':
			sense.show_letter("M")

		sleep(0.5)
		sense.clear()
   
