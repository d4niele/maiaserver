import paho.mqtt.client as mqtt
import time,json,requests
URL = 'http://localhost:8000/records/'

def on_message(client, userdata, message):
    m = message.payload.decode("utf-8")
    t = message.topic
    qos = message.qos
    retain_flag = message.retain
    print("message received " ,message.payload.decode("utf-8"))
    m_dict = json.loads(m)
    m_dict['topic'] = t
    print(json.dumps(m_dict))
    r = requests.post(URL, data = json.dumps(m_dict),headers = {'content-type':'application/json'})



broker_address="calupietru.duckdns.org"
client = mqtt.Client("MAIA2") 
client.username_pw_set(username="test1",password="test1")
client.on_message=on_message 
client.connect(broker_address,1883) 
client.loop_start() 
client.subscribe("/maia/2")
client.subscribe("/maia/3")
while True:
    time.sleep(1)

#curl -X POST  http://localhost:8000/records/ -d '{"espid":"1","topic":"111","timestamp":1,"peso":1.1,"temperatura":122,"umidita":12}'
#{"espid": "Prato", "timestamp": 219182, "peso": 11.7, "memoria_libera": "108480", "temperatura": 26.8, "umidita": 57.2}