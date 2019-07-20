import os

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY_URI']
app.config['SECRET_KEY'] = "1ff25615e8b3e1da366a388e2e5b25f0"
app.config['MONGO_URI'] = os.environ['MONGO_DB_URI']
mongo = PyMongo(app)

# After app creation and initialization to avoid circular imports
from app import routes