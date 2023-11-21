from flask import Flask, request
import json

app = Flask(__name__)
server_addresses = []

@app.route('/receive_address', methods=['POST'])
def receive_address():
    data = request.get_json()
    server_address = data.get('address')
    if server_address:
        server_addresses.append(server_address)
        print("Address received:", server_address)
        return "Address received"
    else:
        return "Invalid address format"

@app.route('/server_addresses', methods=['GET'])
def get_server_addresses():
    return json.dumps(server_addresses)

if __name__ == '__main__':
    app.run(port=8080)