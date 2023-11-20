# server_intermediary.py
from flask import Flask, request
import requests
from threading import Thread

app = Flask(__name__)
server1_url = "http://localhost:4567"
server2_url = "http://localhost:5372"

def forward_ping():
    requests.get(server2_url + "/ping")

def forward_pong():
    requests.get(server1_url + "/pong")

@app.route('/forward_ping')
def forward_ping_route():
    thread = Thread(target=forward_ping)
    thread.start()
    return 'Ping forwarded to Server 2!'

@app.route('/forward_pong')
def forward_pong_route():
    thread = Thread(target=forward_pong)
    thread.start()
    return 'Pong forwarded to Server 1!'

if __name__ == '__main__':
    app.run(port=8080)
