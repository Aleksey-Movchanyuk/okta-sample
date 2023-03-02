from api import app
from flask import render_template, request

from api.decorators import validate_token


@app.route('/')
def root():
    return 'root\n'

@app.route("/api/")
def api():
    return 'Welcome to API\n'

@app.route('/api/echo/')
@validate_token
def echo(username: str):
    return {'message': f'Welcome {username} from the Backend'}

@app.errorhandler(404)
def page_not_found(error):
    return f"404 Error: Page not found {request.path}\n"