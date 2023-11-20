# Server 1
import json
import socket
import time
from flask import Flask, jsonify
import requests

app = Flask(__name__)
SERVER2_URL = 'http://localhost:5002'


def write_own_address_to_file():
    own_address = {'own_address': f'http://localhost:4002'}
    
    # Écrit l'adresse dans un fichier JSON ou le crée s'il n'existe pas
    with open('server1_config.json', 'w') as config_file:
        json.dump(own_address, config_file)

@app.route('/pong')
def ping_pong():
    try:
        # Envoie une requête "pong" vers le serveur 2
        # time.sleep(0.5)
        requests.get(f'{SERVER2_URL}/ping', timeout=0.5)
        # requests.get(f'{SERVER2_URL}/ping')
        return 'Ping successful!'
    except requests.RequestException as e:
        return f'Error communicating with Server 2: {str(e)}', 500
    
# @app.route('/get_own_address')
# def get_own_address():
#     return jsonify({'own_address': 'http://localhost:5002'})
# @app.route('/get_own_address')
# def get_own_address():
#     # Obtient l'adresse IP et le numéro de port du serveur 1
#     own_ip = socket.gethostbyname(socket.gethostname())
#     own_port = 4002
#     return jsonify({'own_address': f'http://{own_ip}:{own_port}'})
@app.route('/')
def get_own_address():
    write_own_address_to_file()

    with open('server1_config.json', 'r') as config_file:
        own_address = json.load(config_file)

    return jsonify(own_address)

if __name__ == '__main__':
    app.run(port=4002)
# from flask import Flask, request
# import requests
# import time
# import threading

# app = Flask(__name__)

# #l'dresse du serveur 2
# server2_url = "http://localhost:5002/"

# def send_pong():
#     while True:
#         time.sleep(0.5)
#         requests.get(server2_url + "/ping")
#         print("Sent Pong")
#         time.sleep(0.5)

# @app.route('/pong', methods=['GET'])
# def ping():
#     print("Received Ping")
#     return 'Pong'

# if __name__ == 'main':
#     threading.Thread(target=send_pong).start()
#     app.run(port=5000)  # Exécution du serveur sur le port 5000
# from flask import Flask, request
# import requests
# import time
# import threading

# app = Flask(__name__)