import threading
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
my_adress = "http://pong-service:5372"
server_3_url = "http://coordinate-service:8080"
adress_ping = None
#@app.route('/send_address')
def send_adress():
    try:
        response = requests.post(server_3_url + "/receive_address_pong", json={"address": my_adress, "servername": "server2"})
        print("Server Pong sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

def get_adress_ping():
    global adress_ping
    try:
        while not adress_ping:
            time.sleep(2)
            response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server1'})
            
            if response.status_code == 200:
                adress_ping = response.json()
                print("Server ping address received from server 3")
                print("Address ping received from server 3 --->")
                print(adress_ping)
            else:
                print(f"Error received address from Server 3. Status code: {response.status_code}")
                return "Error received address"
    except requests.exceptions.RequestException as e:
        print("Error connecting to Server 3:", e)
        return "Error connecting to Server 3"
    
def send_pong():
    global adress_ping
    print("------> adress ping when i send")
    print(adress_ping)
    time.sleep(0.5)
    try:
        response = requests.get(adress_ping + "/", timeout=5)
        print("Send pong:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending ping:", e)
@app.route('/')
def ping():
    print("Received ping:", adress_ping)
    threading.Timer(5,send_pong).start()
    # Thread(target=send_pong).start()
    return "ping"

if __name__ == '__main__':
    Thread(target=send_adress).start()
    threading.Timer(3,get_adress_ping).start()
    app.run(host='0.0.0.0', port=5372)