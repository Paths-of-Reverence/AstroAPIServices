# app/main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    # Process the data here
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=False, port=8000)
