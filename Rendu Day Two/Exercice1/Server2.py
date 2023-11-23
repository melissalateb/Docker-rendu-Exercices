import threading
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
my_adress = "http://pong-service:5372"
server_3_url = "http://coordinate-service:8080"
adress_broker = None

def send_adress():
    try:
        response = requests.post(server_3_url + "/receive_address_pong", json={"address": my_adress, "servername": "server2"})
        print("2 --> 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

def get_adress_broker():
    global adress_broker
    try:
        response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server4'})
        adress_broker = response.json()
        print("2 <-- 4 :  %s" % adress_broker)
    except requests.exceptions.RequestException as e:
        print("Error connecting to Server 3:", e)
        return "Error connecting to Server 3"
    
def send_pong():
    global adress_broker
    print("send pong --> : %s" % adress_broker)
    time.sleep(0.5)
    try:
        requests.post(adress_broker + "/forward_message", json={"server_name": "server1", "message":"pong"})
        print("Send pong ok")
    except requests.exceptions.RequestException as e:
        print("Error sending pong:", e)
        
@app.route('/')
def ping():
    print("Received ping from %s" % adress_broker)
    threading.Thread(target=send_pong).start()
    return "ping"

if __name__ == '__main__':
    Thread(target=send_adress).start()
    threading.Timer(3,get_adress_broker).start()
    app.run(host='0.0.0.0', port=5372)