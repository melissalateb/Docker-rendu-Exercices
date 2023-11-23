import time
from flask import Flask, request
import json

app = Flask(__name__)
server_addresses = {
    'server1' : None,
    'server2' : None,
    'server4' : None,
}
@app.route('/receive_address_ping', methods=['POST'])
def receive_address_ping():
    data = request.get_json()
    server_address = data.get('address')
    server_name = data.get('servername')
    if server_name == 'server1' and server_address:
        server_addresses['server1'] = server_address
        print(server_name+":"+server_address)
        return "Adress server 1 received"
    else:
        return "Invalid address format"


@app.route('/receive_address_pong', methods=['POST'])
def receive_address_pong():
    data = request.get_json()
    server_address = data.get('address')
    server_name = data.get('servername')
    if server_name == 'server2' and server_address:
        server_addresses['server2'] = server_address
        print(server_name+":"+server_address)
        return "Address server 2 received"
    else:
        return "Invalid address format"

@app.route('/receive_address_broker', methods=['POST'])
def receive_address_broker():
    data = request.get_json()
    server_address = data.get('address')
    server_name = data.get('servername')
    if server_name == 'server4' and server_address:
        server_addresses['server4'] = server_address
        print(server_name+":"+server_address)
        return "Address server 4 received"
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
    elif server_name == 'server4' and server_name in server_addresses:
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)