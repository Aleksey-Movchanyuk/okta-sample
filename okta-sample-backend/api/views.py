from api import app
from flask import render_template, request


@app.route("/api/")
def api():
    return 'Welcome to API\n'

@app.route('/')
def root():
    return 'root\n'

@app.errorhandler(404)
def page_not_found(error):
    return f"404 Error: Page not found {request.path}\n"