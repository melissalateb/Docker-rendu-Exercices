from flask import Flask, request
import time
import requests
from threading import Thread

app = Flask(__name__)
server1_url = "http://localhost:4567"

def send_ping():
    requests.get(server1_url + "/ping")

def handle_pong():
    time.sleep(0.5)
    send_ping()

@app.route('/pong')
def pong():
    thread = Thread(target=handle_pong)
    thread.start()
    return 'Pong received!'

if __name__ == '__main__':
    app.run(port=5372)
