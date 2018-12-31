from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

#define colours
red = (255, 0, 0)
green = (0, 255, 0)

press = sense.get_pressure()
print("pressure= ", press)

temp = sense.get_temperature()
print("temp= ", temp)

humidity = sense.get_humidity()
print("humidity= ", humidity)

p = round(press, 1)
t = round(temp, 1)
h = round(humidity, 1)

message = "Temp: " + str(t) + " Pressure: " + str(p) + " Humidity: "+ str(h)

if t > 18.3 and t < 26.7:
	bg = green
else:
	bg = red


sense.show_message(message, scroll_speed=0.05, back_colour=bg)

sense.clear()


