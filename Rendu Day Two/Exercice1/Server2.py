from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
# server_pong_url = "http://127.0.0.1:4567"
server_pong_url = "http://ping-service:4567"
def send_pong():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server_pong_url + "/", timeout=5) 
            if response.status_code == 200:
                print("Server Pong received ping from Server Ping:", response.text)
            else:
                print(f"Received an unexpected status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Error sending pong:", e)

@app.route('/')
def ping():
    return "ping"

if __name__ == '__main__':
    
    pong_thread = Thread(target=send_pong)
    pong_thread.start()
    app.run(port=5372)