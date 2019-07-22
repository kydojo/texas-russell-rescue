import os

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGO_URI'] = os.environ['MONGO_DB_URI']
mongo = PyMongo(app)

# After app creation and initialization to avoid circular imports
from app import routes