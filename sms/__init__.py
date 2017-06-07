"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "FLASK_SECRET_KEY"


import sms.views
