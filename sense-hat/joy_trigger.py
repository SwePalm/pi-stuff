from sense_hat import SenseHat

sense = SenseHat()

def pushed(event):
	print(event)

sense.stick.direction_any = pushed

while True:
	pass
