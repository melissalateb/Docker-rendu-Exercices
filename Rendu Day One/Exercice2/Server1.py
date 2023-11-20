# server1.py
from flask import Flask, request
import requests
from threading import Thread
import time 
app = Flask(__name__)
server_intermediary_url = "http://localhost:8080"

def send_ping():
    requests.get(server_intermediary_url + "/forward_ping")

def handle_pong():
    time.sleep(0.5)
    print("send ping to server 3")
    send_ping()

@app.route('/pong')
def pong():
    thread = Thread(target=handle_pong)
    thread.start()
    print("pong receved from server 3")
    return 'Pong received!'

if __name__ == '__main__':
    app.run(port=4567)
