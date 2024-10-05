# Importing necessary modules from Flask
from flask import Flask

# Creating an instance of the Flask class
app = Flask(__name__)

# Importing the routes from api_routes.py
from routes.api_routes import *