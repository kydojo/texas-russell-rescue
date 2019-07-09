from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1ff25615e8b3e1da366a388e2e5b25f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'		# relative path from the current file
db = SQLAlchemy(app)	# instantiate a db instance
bcrypt = Bcrypt(app)	# for encrypting passwords
login_manager = LoginManager(app)	# handles user sessions
login_manager.login_view = 'login' 	# pass in the function name of the route with the login_required decorator
login_manager.login_message_category = 'danger' 	# the BS class for the flashed message (danger = red)

# This has to be after app is created and initialized to avoid circular imports 
from flaskblog import routes