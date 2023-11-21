from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server_pong_url = "http://127.0.0.1:4567"
server_3_url = "http://127.0.0.1:8080"

def send_pong():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server_pong_url + "/pong", timeout=5)  # Définissez un timeout approprié
            if response.status_code == 200:
                print("Server Pong received ping from Server Ping:", response.text)
            else:
                print(f"Received an unexpected status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Error sending pong:", e)

@app.route('/ping')
def ping():
    return "ping"

@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address", json={"address": server_pong_url})
        print("Server Pong sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

if __name__ == '__main__':
    pong_thread = Thread(target=send_pong)
    pong_thread.start()
    
    # Envoyer l'adresse au serveur 3 au démarrage
    send_address()
    
    app.run(port=5372)