import os

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ['MONGO_DB_URI']
mongo = PyMongo(app)

# After app creation and initialization to avoid circular imports
from app import routes