from flask import Flask
from flask_cors import CORS

# create the Flask application instance
app = Flask(__name__)
CORS(app)

# import the views module
import api.views
