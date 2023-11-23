import threading
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
my_adress = "http://ping-service:4567"
server_3_url = "http://coordinate-service:8080"
adress_pong = None
#@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address_ping", json={"address": my_adress, "servername": "server1"})
        print("Server Ping sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"


def get_adress_pong():
    global adress_pong
    try:
        while not adress_pong:
            time.sleep(2)
            response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server2'})
            
            if response.status_code == 200:
                adress_pong = response.json()
                print("Server pong address received from server 3")
                print("Address pong received from server 3 --->")
                print(adress_pong)
            else:
                print(f"Error received address from Server 3. Status code: {response.status_code}")
                return "Error received address"
    except requests.exceptions.RequestException as e:
        print("Error connecting to Server 3:", e)
        return "Error connecting to Server 3"

def send_ping():
    global adress_pong
    print("when i send ping there is adress  ----> ")
    print(adress_pong)
    time.sleep(0.5)
    try:
        response = requests.get(adress_pong + "/", timeout=5)
        print("Send ping:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending ping:", e)

@app.route('/')
def pong():
    print("Received pong:", adress_pong)
    send_ping()
    return "pong"

if __name__ == '__main__':
    Thread(target=send_address).start()
    threading.Timer(3,get_adress_pong).start()
    threading.Timer(5,send_ping).start()
    
    app.run(host='0.0.0.0', port=4567)