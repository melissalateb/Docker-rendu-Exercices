from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server2_url = "http://localhost:5372"

def send_pong():
    requests.get(server2_url + "/pong")

def handle_ping():
    time.sleep(0.5)
    send_pong()

@app.route('/ping')
def ping():
    thread = Thread(target=handle_ping)
    thread.start()
    return 'Ping received!'

if __name__ == '__main__':
    app.run(port=4567)
