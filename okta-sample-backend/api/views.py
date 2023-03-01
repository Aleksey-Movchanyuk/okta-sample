from api import app
from flask import render_template

# define a route for the homepage
@app.route("/")
def index():
    return render_template("index.html")
