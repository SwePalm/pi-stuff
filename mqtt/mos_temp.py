import os
import time
from sense_hat import SenseHat
import json
from datetime import datetime
# Import MQTT packages
import paho.mqtt.client as mqtt

# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)

sense = SenseHat()
sense.clear()

broker_host = "127.0.0.1"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_host, broker_port)


while True:
  for event in sense.stick.get_events():
    print("The joystick was {} {}".format(event.action, event.direction))
    if event.action == "pressed" and event.direction == "down" :
      t1 = sense.get_temperature_from_humidity()
      t2 = sense.get_temperature_from_pressure()
      t_cpu = get_cpu_temp()
      t = (t1+t2)/2
      t_corr = t - ((t_cpu-t)/1.5)
      t_corr = get_smooth(t_corr)
      msg = "%s C"  % int(round(t_corr))
      sense.show_message(msg)
      timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
      result_json = {'temperature' : t_corr  , 'timestamp' : timestamp }
      # update to a better topic...
      client.publish("testing", json.dumps(result_json) , qos=0)

