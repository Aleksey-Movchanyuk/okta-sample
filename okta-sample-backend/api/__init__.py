from flask import Flask
from flask_cors import CORS

from api.utils import start_garbage_cleaner

# create the Flask application instance
app = Flask(__name__)
CORS(app)

start_garbage_cleaner()

# import the views module
import api.views
