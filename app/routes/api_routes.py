from flask import request, jsonify
from main import app
from services.webhook_receiver import handle_webhook

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    response = handle_webhook(data)
    return jsonify(response), 200