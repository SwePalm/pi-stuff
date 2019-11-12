import paho.mqtt.client as mqtt

broker_host = "127.0.0.1" # iot.eclipse.org
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code "+rc)

def on_message(client, userdata, message):
   print("Message Recieved: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_host, broker_port)

client.subscribe("testing", qos=1)

client.loop_forever()
