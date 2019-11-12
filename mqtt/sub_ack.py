import paho.mqtt.client as mqtt

broker_host = "127.0.0.1" # iot.eclipse.org
broker_port = 1883

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code " (rc))

def on_message_from_testing(client, userdata, message):
   print("Testing: "+message.payload.decode())
   client.publish("testing_ack", message.payload.decode() , qos=0)

def on_message_from_testing_ack(client, userdata, message):
   print("Testing Acknowledge: "+message.payload.decode())

def on_message(client, userdata, message):
   print("Message Recieved from Others: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
#To Process Every Other Message
client.on_message = on_message
client.connect(broker_host, broker_port)

client.subscribe("testing", qos=1)
client.subscribe("testing_ack", qos=1)
client.message_callback_add("testing", on_message_from_testing)
client.message_callback_add("testing_ack", on_message_from_testing_ack)

client.loop_forever()
