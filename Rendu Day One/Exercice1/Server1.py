import threading
from flask import Flask
import requests
import time
import Server2

app = Flask(__name__)

server2_url = "http://localhost:5372"

def send_pong():
    response = requests.get(f"{server2_url}/ping")
    print(f"Received Ping from Server 2: {response.text}")
    time.sleep(0.5)
    Server2.send_ping()

@app.route('/pong', methods=['GET'])
def ping():
    return "Pong from Server 1"

if __name__ == '__main__':
    threading.Thread(target=send_pong).start()
    app.run(host='localhost', port=4567)
