# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/get_servers_addresses')
# def get_servers_addresses():
#     try:
#         # Demande les adresses des serveurs 1 et 2 au troisième serveur
#         response_server1 = requests.get('///get_own_address')
#         response_server2 = requests.get('///get_own_address')

#         # Récupère les adresses des serveurs 1 et 2
#         server1_address = response_server1.json()['own_address']
#         server2_address = response_server2.json()['own_address']

#         return jsonify({'server1': server1_address, 'server2': server2_address})
#     except requests.RequestException as e:
#         return f'Error getting server addresses: {str(e)}', 500

# if __name__ == '__main__':
#     app.run(port=6001)

import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_servers_addresses():
    try:
        # Lit les adresses depuis les fichiers JSON
        with open('server1_config.json', 'r') as config_file:
            server1_address = json.load(config_file)

        with open('server2_config.json', 'r') as config_file:
            server2_address = json.load(config_file)

        return {'server1': server1_address['own_address'], 'server2': server2_address['own_address']}
    except Exception as e:
        return f'Error getting server addresses: {str(e)}', 500

@app.route('/')
def expose_servers_addresses():
    addresses = get_servers_addresses()
    return jsonify(addresses)

if __name__ == '__main__':
    app.run(port=6003)
