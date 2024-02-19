#   extensions.py


from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, AnonymousUserMixin
from flask_admin import Admin
from flask_migrate import Migrate







db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()
migrate = Migrate()

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

def init_app(app):
    login_manager.init_app(app)
    login_manager.anonymous_user = Anonymous