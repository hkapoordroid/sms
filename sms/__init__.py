"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager
from model.user import User

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
#app.config['SECRET_KEY'] = "FLASK_SECRET_KEY"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_page"


# Our mock database.
users = {'hkapoordroid@gmail.com': {'pw': 'test123'}}


@login_manager.user_loader
def load_user(email):
    #TODO: here based on id, AWS RDS lookup needs to be done to get the data back to LoginManager
    #user = User("hkapoordroid@gmail.com", "123456")
    #return user
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('loemail')
    if email not in users:
        return
    
    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user
    

import sms.views
