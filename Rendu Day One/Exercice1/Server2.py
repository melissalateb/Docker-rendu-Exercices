import threading
from flask import Flask
import requests
import time
import Server1

app = Flask(__name__)

server1_url = "http://localhost:4567"

def send_ping():
    
    print("Sending Ping to Server 1")
    response = requests.get(f"{server1_url}/pong")
    print(f"Received Pong from Server 1: {response.text}")
    time.sleep(0.5)  # Simulating some processing time
    Server1.send_pong()

@app.route('/ping', methods=['GET'])
def ping():
    send_ping()
    return "Pong from Server 2"

if __name__ == '__main__':
    threading.Thread(target=send_ping).start()
    app.run(host='localhost', port=5372)
