import os

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_pymongo import PyMongo                                # temp commented out

app = Flask(__name__)
# app.config['SECRET_KEY'] = '1ff25615e8b3e1da366a388e2e5b25f0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['MONGO_URI'] = os.environ['MONGO_DB_URI']           # temp commented out
# mongo = PyMongo(app)                                           # temp commented out

# db = SQLAlchemy(app)  # instantiate a db instance
# bcrypt = Bcrypt(app)  # for encrypting passwords
# login_manager = LoginManager(app)  # handles user sessions
# pass in the function name of the route with the login_required decorator
# login_manager.login_view = 'login'
# the BS class for the flashed message (danger = red)
# login_manager.login_message_category = 'danger'

# This has to be after app is created and initialized to avoid circular imports
from app import routes