from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

press = sense.get_pressure()
print("pressure= ", press)

temp = sense.get_temperature()
print("temp= ", temp)

humidity = sense.get_humidity()
print("humidity= ", humidity)



