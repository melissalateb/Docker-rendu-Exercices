# server2.py
from flask import Flask, request
import requests
from threading import Thread
import time
app = Flask(__name__)
server_intermediary_url = "http://localhost:8080"

def send_pong():
    requests.get(server_intermediary_url + "/forward_pong")

def handle_ping():
    time.sleep(0.5)
    print("send pong to server 3")
    send_pong()

@app.route('/ping')
def ping():
    thread = Thread(target=handle_ping)
    thread.start()
    print("ping receved from server 3")
    return 'Ping received!'

if __name__ == '__main__':
    app.run(port=5372)
