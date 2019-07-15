import os

from flask import Flask
from flask_pymongo import PyMongo                                # temp commented out

app = Flask(__name__)

# app.config['MONGO_URI'] = os.environ['MONGO_DB_URI']           # temp commented out
# mongo = PyMongo(app)                                           # temp commented out

# After app creation and initialization to avoid circular imports
from app import routes