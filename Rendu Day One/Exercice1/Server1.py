# Server 1
import time
from flask import Flask
import requests

app = Flask(__name__)
SERVER2_URL = 'http://localhost:5372'

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
if __name__ == '__main__':
    app.run(port=4567)
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