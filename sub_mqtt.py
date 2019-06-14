import paho.mqtt.client as mqtt #import the client1
import time,json
############
def on_message(client, userdata, message):
    print("message received " ,json.loads(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

broker_address="calupietru.duckdns.org"

client = mqtt.Client("P1") #create new instance
client.username_pw_set(username="test1",password="test1")
client.on_message=on_message #attach function to callback
client.connect(broker_address,1883) #connect to broker
client.loop_start() #start the loop
client.subscribe("/maia/2")

while True:
    pass
    time.sleep(1)