#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# add your Flask app directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# set the SCRIPT_NAME environment variable to the new virtual path
os.environ['SCRIPT_NAME'] = '/api'

# import your Flask application instance
from api import app

# set up the FastCGI server
from flup.server.fcgi import WSGIServer
WSGIServer(app).run()
