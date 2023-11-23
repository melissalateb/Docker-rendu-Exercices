# server4.py
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
server_3_url = "http://coordinate-service:8080"

def get_recipient_url(recipient):
    try:
        response = requests.get(server_3_url + "/get_server_address", params={"service_name": recipient})
        return response.json().get('address')
    except requests.exceptions.RequestException as e:
        print(f"Error getting address for {recipient} from Server3:", e)
        return None

@app.route('/forward_message', methods=['POST'])
def forward_message():
    data = request.get_json()
    message = data.get('message')
    recipient = data.get('recipient')

    if message and recipient:
        recipient_url = get_recipient_url(recipient)
        if recipient_url:
            try:
                response = requests.post(recipient_url + "/forward_message", json=data)
                print(f"Server4 forwarded {message} to {recipient}:", response.text)
                return f"{message} forwarded to {recipient}"
            except requests.exceptions.RequestException as e:
                print(f"Error forwarding {message} to {recipient}:", e)
                return f"Error forwarding {message} to {recipient}"
        else:
            return f"Recipient address not available for {recipient}"
    else:
        return "Invalid message format"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
