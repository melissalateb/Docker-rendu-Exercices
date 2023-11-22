from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
# server_ping_url = "http://127.0.0.1:5372"
server_ping_url = "http://pong-service:5372"
server_3_url = "http://coordinate-service:8080"
def send_ping():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server_ping_url + "/", timeout=5)
            print("Server Ping received ping from Server Pong:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending ping:", e)

@app.route('/')
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
    
    app.run(host='0.0.0.0', port=4567)