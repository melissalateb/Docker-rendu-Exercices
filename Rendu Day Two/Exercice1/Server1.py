import threading
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
my_adress = "http://ping-service:4567"
server_3_url = "http://coordinate-service:8080"
adress_broker = None
# adress_pong = None
#@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address_ping", json={"address": my_adress, "servername": "server1"})
        print("1 --> 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

def get_adress_broker():
    global adress_broker
    try:
        response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server4'})
        adress_broker = response.json()   
        print("1 <-- 4 :  %s" % adress_broker)
    except requests.exceptions.RequestException as e:
        print("Error connecting to Server 3:", e)
        return "Error connecting to Server 3"


def send_ping():
    global adress_broker
    print("send ping --> : %s" % adress_broker)
    time.sleep(0.5)
    try:
        requests.post(adress_broker + "/forward_message", json={"server_name": "server2", "message":"ping"})
        print("Send ping ok")
    except requests.exceptions.RequestException as e:
        print("Error sending ping:", e)

@app.route('/')
def pong():
    print("Received pong from :%s" % adress_broker)
    send_ping()
    return "pong"

if __name__ == '__main__':
    Thread(target=send_address).start()
    threading.Timer(3,get_adress_broker).start()
    threading.Timer(10,send_ping).start()
    
    app.run(host='0.0.0.0', port=4567)