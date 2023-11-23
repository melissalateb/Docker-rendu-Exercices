import time
from flask import Flask, request
import json

app = Flask(__name__)
server_addresses = {
    'server1' : None,
    'server2' : None,
}
# TODO: séparer la fct en deux pour appel deux fois / rectifier le server1 et server2 
@app.route('/receive_address_ping', methods=['POST'])
def receive_address_ping():
    data = request.get_json()
    server_address = data.get('address')
    server_name = data.get('servername')
    if server_name == 'server1' and server_address:
        server_addresses['server1'] = server_address
        print(server_name+":"+server_address)
        return "Adress server 1 received"
    elif server_name == 'server2' and server_address:
        server_addresses['server2'] = server_address
        print(server_name+":"+server_address)
        return "Address server 2 received"
    else:
        return "Invalid address format"


@app.route('/receive_address_pong', methods=['POST'])
def receive_address_pong():
    data = request.get_json()
    server_address = data.get('address')
    server_name = data.get('servername')
    if server_name == 'server1' and server_address:
        server_addresses['server1'] = server_address
        print(server_name+":"+server_address)
        return "Adress server 1 received"
    elif server_name == 'server2' and server_address:
        server_addresses['server2'] = server_address
        print(server_name+":"+server_address)
        return "Address server 2 received"
    else:
        return "Invalid address format"

@app.route('/server_addresses', methods=['GET'])
def get_server_addresses():
    data = request.get_json()
    server_name = data.get('servername')

    if server_name == 'server1' and server_name in server_addresses:
        server_address = server_addresses[server_name]
        print(f"Server '{server_name}' address: {server_address}")
        return json.dumps(server_address)
    elif server_name == 'server2' and server_name in server_addresses:
        server_address = server_addresses[server_name]
        print(f"Server '{server_name}' address: {server_address}")
        return json.dumps(server_address)
    else:
        print(f"Error: Invalid server name '{server_name}'")
        return "Error send addresses"

# def get_server_addresses():
#     data = request.get_json()
#     server_name = data.get('servername')
#     if server_name == 'server1':
#         return json.dumps(server_addresses['server1'])
#     elif server_name == 'server2':
#         return json.dumps(server_addresses['server2'])
#     else: 
#         return "Error send adresses"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)