from flask import Flask

# create the Flask application instance
app = Flask(__name__)

# import the views module
import api.views
