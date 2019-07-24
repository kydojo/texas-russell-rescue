import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY_URI']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trr.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# TODO - this still displays weirdly (to check, go to account page while logged out)
login_manager.login_message_category = 'info'

# After app creation and initialization to avoid circular imports
from app import routes, models
