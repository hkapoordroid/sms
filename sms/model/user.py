from uuid import uuid4
import random
import flask_login


class User(flask_login.UserMixin):
    pass

#class User(object):
#    """User class for storing the logged in user data"""
    
    
#    def __init__(self, email, password_plaintext):
#        #self.id = uuid4().hex
#        self.id = 1#TODO: This needs to change
#        self.email = email
#        self.password_plaintext = password_plaintext
 
#    def __repr__(self):
#        return '<User {0}>'.format(self.email)

#    @property
#    def is_authenticated(self):
#        #TODO: Change the logic here to check with the AWS RDS db
#        return True

#    @property
#    def is_active(self):
#        """Always True, as all users are active."""
#        return True
 
#    @property
#    def is_anonymous(self):
#        """Always False, as anonymous users aren't supported."""
#        return False
 
#    def get_id(self):
#        """Return the email address to satisfy Flask-Login's requirements."""
#        """Requires use of Python 3"""
#        return str(self.id)

    

    


