from sense_hat import SenseHat

sense = SenseHat()

sense.show_letter("J")

while True:
	accel = sense.get_accelerometer_raw()
	x = accel['x']
	y = accel['y']
	z = accel['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

	print("x={0}, y={1}, z={2}".format(x, y, z))

	if x == -1:
		sense.set_rotation(180)
	elif y == 1:
		sense.set_rotation(90)
	elif y == -1:
		sense.set_rotation(270)
	else:
		sense.set_rotation(0)
