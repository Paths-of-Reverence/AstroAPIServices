from flask import Flask

app = Flask(__name__)

# Importing the routes from api_routes.py
from .routes.api_routes import *

if __name__ == '__main__':
    app.run(debug=True, port=8000)