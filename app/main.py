# Importing necessary modules from Flask
from flask import Flask

# Creating an instance of the Flask class
app = Flask(__name__)

# Importing the routes from api_routes.py
from .api_routes import *

# The main entry point of the application
if __name__ == '__main__':
    # Running the Flask application
    # debug=False means no debug information will be shown
    # port=8000 specifies the port number on which the app will run
    app.run(debug=False, port=8000)