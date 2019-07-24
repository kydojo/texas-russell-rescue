from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy_utils import EmailType

# The login manager needs this to be able to identify users based on their ID
# Source: LoginManager documentation
@login_manager.user_loader	# necessary decorator
def load_user(user_id):
	return User.query.get(int(user_id))


# Each class (model) will be its own table in the db
# User class, inherits from db.Model and UserMixin (UserMixin adds attributes needed by LoginManager to manage user sessions)
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True) # create the user id attribute and set it to the PK for the db
	username = db.Column(db.String(20), unique=True, nullable=False) # username attribute, string with max length of 20, unique, not null
	email = db.Column(db.String(120), unique=True, nullable=False) # email attribute, string with max length of 120, unique, not null
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # image_file attribute for profile pic, hash will have a max length of 20, default image will be set
	password = db.Column(db.String(60), nullable=False) # password attribute, hash will have a max length of 60
	posts = db.relationship('Post', backref='author', lazy=True) # posts attribute to connect User to the Post model

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# Post class, inherits from db.Model
class Post(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True) # create the user id attribute and set it to the PK for the db
	title = db.Column(db.String(100), nullable=False) # title attribute, string with a max length of 100, not null
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	content = db.Column(db.Text, nullable=False) # content attribute, text content of the post
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user_id attribute, FK is the author's user.id (from the User model)

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

# Message class, inherits from db.Model
class Message(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True) # create the user id attribute and set it to the PK for the db
	name = db.Column(db.String(60), nullable=False)
	email = db.Column(EmailType, nullable=False)
	phone = db.Column(db.String(20))
	city = db.Column(db.String(60), nullable=False)
	state = db.Column(db.String(2), nullable=False)
	date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	content = db.Column(db.Text, nullable=False) # content attribute, text content of the post

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"Message('{self.name}', '{self.city}', '{self.state}', '{self.date_sent}')"
		