import paho.mqtt.client as mqtt

broker_host = "127.0.0.1" #iot.eclipse.org
broker_port = 1883

client = mqtt.Client()
client.connect(broker_host, broker_port)

client.publish(topic="testing", payload="This is a test message!", qos=1, retain=False)
