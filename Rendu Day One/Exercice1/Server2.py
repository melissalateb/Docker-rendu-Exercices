# Server 2
from flask import Flask
import requests
import time

app = Flask(__name__)
SERVER1_URL = 'http://localhost:4567'

@app.route('/ping')
def ping():
    try:
        # Attend une demi-seconde avant d'envoyer une requête "pong" vers le serveur 1
        requests.get(f'{SERVER1_URL}/pong')
        return 'Pong sent!'
    
    except requests.RequestException as e:
        # return 'Error communicating with Server 1', 500
        return f'Error communicating with Server 1: {str(e)}', 500

if __name__ == '__main__':
    app.run(port=5372)

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