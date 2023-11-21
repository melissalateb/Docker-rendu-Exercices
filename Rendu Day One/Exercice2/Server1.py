from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server_ping_url = "http://127.0.0.1:5372"
server_3_url = "http://127.0.0.1:8080"

def send_ping():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server_ping_url + "/ping", timeout=5)
            print("Server Ping received ping from Server Pong:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending ping:", e)

@app.route('/pong')
def pong():
    return "pong"

@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address", json={"address": server_ping_url})
        print("Server Ping sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

if __name__ == '__main__':
    ping_thread = Thread(target=send_ping)
    ping_thread.start()
    
    # Envoyer l'adresse au serveur 3 au démarrage
    send_address()
    
    app.run(port=4567)