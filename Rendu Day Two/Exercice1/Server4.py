# server4.py
from threading import Thread
import threading
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
my_adress = "http://message-broker:8090"
server_3_url = "http://coordinate-service:8080"
server_maping=  {'server2': None, 'server1': None}


def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address_broker", json={"address": my_adress, "servername": "server4"})
        print("Server broker sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"
#@app.route('/get_adress_url', methods=['GET'])
def get_adress_url():
    print("..................")
    try:
        
        response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server1'})
        server_maping['server1'] = response.json()
        #print(server_maping['server1'])
        response = requests.get(server_3_url + "/server_addresses", json={"servername": 'server2'})
        server_maping['server2'] = response.json()
        #print("reponse server 4 adress ping depuis server 3--> ")
        #print(server_maping['server1'])
        #print(server_maping['server2'])
    except requests.exceptions.RequestException as e:
        #print("Error connecting to Server 3:", e)
        return "Error connecting to Server 3"

@app.route('/forward_message', methods=['POST', 'GET'])
def forward_message():
    global server_maping
    try:
        server_name= request.json.get('server_name')
        message= request.json.get('message')
        
        if message and server_name:
            print(message)
            print(server_name)
            print(server_maping[server_name])
            response = requests.get(server_maping[server_name] + "/")
        else: 
            return "Error sending ping or pong"
    except requests.exceptions.RequestException as e:
        print("Error connecting to Server 1 and 2:", e)
        return "Error connecting to Server 1 and 2"
    

if __name__ == '__main__':
    Thread(target=send_address).start()
    threading.Timer(5,get_adress_url).start()
    app.run(host='0.0.0.0', port=8090)




# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)
# my_address = "http://pong-service:8090"
# server_3_url = "http://coordinate-service:8080"
# address_ping = None
# address_pong = None

# def send_address():
#     try:
#         response = requests.post(server_3_url + "/receive_address_broker", json={"address": my_address, "servername": "server4"})
#         print("Server broker sent its address to Server 3")
#         return "Address sent to Server 3"
#     except requests.exceptions.RequestException as e:
#         print("Error sending address to Server 3:", e)
#         return "Error sending address"

# @app.route('/forward_message', methods=['POST'])
# def forward_message():
#     data = request.get_json()
#     message = data.get('message')
#     recipient = data.get('recipient')

#     if message and recipient:
#         recipient_url = get_recipient_url(recipient)
#         if recipient_url:
#             try:
#                 response = requests.post(recipient_url + "/forward_message", json=data)
#                 print(f"Server4 forwarded {message} to {recipient}:", response.text)
#                 return f"{message} forwarded to {recipient}"
#             except requests.exceptions.RequestException as e:
#                 print(f"Error forwarding {message} to {recipient}:", e)
#                 return f"Error forwarding {message} to {recipient}"
#         else:
#             return f"Recipient address not available for {recipient}"
#     else:
#         return "Invalid message format"

# def get_recipient_url(recipient):
#     global address_ping, address_pong
#     if recipient == "server1":
#         return address_ping
#     elif recipient == "server2":
#         return address_pong
#     else:
#         return None

# if __name__ == '__main__':
#     threading.Thread(target=send_address).start()
#     app.run(host='0.0.0.0', port=8090)
