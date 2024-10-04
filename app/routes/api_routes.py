# Importing necessary modules from Flask
from flask import request, jsonify
# Importing the Flask app instance from main.py
from .main import app
# Importing the webhook receiver function from webhook_receiver.py
from .services.webhook_receiver import handle_webhook

# Defining a route for the webhook endpoint
# This route will handle POST requests sent to /webhook
@app.route('/webhook', methods=['POST'])
def receive_webhook():
    # Extracting JSON data from the incoming request
    data = request.json
    # Calling the handle_webhook function to process the data
    response = handle_webhook(data)
    # Returning the response as JSON with a status code of 200 (OK)
    return jsonify(response), 200