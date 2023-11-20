# Server 2
import json
import socket
from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)
SERVER1_URL = 'http://localhost:4002'

def write_own_address_to_file():
    own_address = {'own_address': f'http://localhost:5002'}
    
    # Écrit l'adresse dans un fichier JSON ou le crée s'il n'existe pas
    with open('server2_config.json', 'w') as config_file:
        json.dump(own_address, config_file)

@app.route('/ping')
def ping():
    try:
        # Attend une demi-seconde avant d'envoyer une requête "pong" vers le serveur 1
        print('Received Ping from Server 1')
        time.sleep(0.5)
        requests.get(f'{SERVER1_URL}/pong')
        return 'Pong sent!'
    
    except requests.RequestException as e:
        # return 'Error communicating with Server 1', 500
        return f'Error communicating with Server 1: {str(e)}', 500

# @app.route('/get_own_address')
# def get_own_address():
#     return jsonify({'own_address': 'http://localhost:4002'})

# @app.route('/get_own_address')
# def get_own_address():
#     # Obtient l'adresse IP et le numéro de port du serveur 1
#     own_ip = socket.gethostbyname(socket.gethostname())
#     own_port = 5002
#     return jsonify({'own_address': f'http://{own_ip}:{own_port}'})

@app.route('/')
def get_own_address():
    write_own_address_to_file()

    with open('server1_config.json', 'r') as config_file:
        own_address = json.load(config_file)

    return jsonify(own_address)
if __name__ == '__main__':
    app.run(port=5002)

# from flask import Flask, request
# import requests
# import time
# import threading

# app = Flask(__name__)

# #l'adresse du serveur 1
# server1_url = "http://localhost:5000/" 

# def send_ping():
#     while True:
#         time.sleep(0.5)
#         requests.get(server1_url + "/pong")
#         print("Sent Ping")
#         time.sleep(0.5)

# @app.route('/ping', methods=['GET'])
# def ping():
#     # time.sleep(0.5)
#     # requests.get(server1_url + "/ping")
#     print("Received Pong")
#     return 'Ping'

# if __name__ == 'main':
#     threading.Thread(target=send_ping).start()
#     app.run(port=5002)  # Exécution du serveur sur le port 5002