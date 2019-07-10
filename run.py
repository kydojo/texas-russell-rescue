from app import app

# Moved to the __init__.py file
	# # from datetime import datetime
	# from flask import Flask, render_template, url_for, flash, redirect
	# from flask_sqlalchemy import SQLAlchemy
	# from forms import RegistrationForm, LoginForm # import the classes from forms.py since it's in the same dir
	# from models import User, Post

	# app = Flask(__name__)
	# app.config['SECRET_KEY'] = '1ff25615e8b3e1da366a388e2e5b25f0'
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # relative path from the current file
	# db = SQLAlchemy(app)	# instantiate a db instance

# Moved the models to models.py

	# # Each class (model) will be its own table in the db

	# # User class, inherits from db.Model
	# class User(db.Model):
	# 	id = db.Column(db.Integer, primary_key=True) # create the user id attribute and set it to the PK for the db
	# 	username = db.Column(db.String(20), unique=True, nullable=False) # username attribute, string with max length of 20, unique, not null
	# 	email = db.Column(db.String(120), unique=True, nullable=False) # email attribute, string with max length of 120, unique, not null
	# 	image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # image_file attribute for profile pic, hash will have a max length of 20, default image will be set
	# 	password = db.Column(db.String(60), nullable=False) # password attribute, hash will have a max length of 60
	# 	posts = db.relationship('Post', backref='author', lazy=True) # posts attribute to connect User to the Post model

	# 	# Dunder (magic) method to define how the object will be printed out
	# 	def __repr__(self):
	# 		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


	# # Post class, inherits from db.Model
	# class Post(db.Model):
	# 	id = db.Column(db.Integer, primary_key=True) # create the user id attribute and set it to the PK for the db
	# 	title = db.Column(db.String(100), nullable=False) # title attribute, string with a max length of 100, not null
	# 	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	# 	content = db.Column(db.Text, nullable=False) # content attribute, text content of the post
	# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user_id attribute, FK is the author's user.id (from the User model)

	# 	# Dunder (magic) method to define how the object will be printed out
	# 	def __repr__(self):
	# 		return f"Post('{self.title}', '{self.date_posted}')"

# Moved to routes.py
	# posts = [
	# 	{
	# 		'author': 'Kyle Johnson',
	# 		'title': 'Blog Post 1',
	# 		'content': 'First post content',
	# 		'date_posted': 'June 24, 2019'
	# 	},
	# 	{
	# 		'author': 'Shannon Lucas',
	# 		'title': 'Blog Post 2',
	# 		'content': 'Second post content',
	# 		'date_posted': 'June 25, 2019'
	# 	}
	# ]

	# @app.route("/")
	# @app.route("/home")
	# def home():
	# 	return render_template('home.html', posts=posts)

	# @app.route("/about")
	# def about():
	# 	return render_template('about.html', title='About')

	# @app.route("/register", methods=['GET', 'POST'])
	# def register():
	# 	form = RegistrationForm() # create an instance of our form
	# 	if form.validate_on_submit():
	# 		flash(f'Account created for { form.username.data }!', 'success')
	# 		return redirect(url_for('home'))
	# 	return render_template('register.html', title='Register', form=form)

	# @app.route("/login", methods=['GET', 'POST'])
	# def login():
	# 	form = LoginForm() # create an instance of our form
	# 	if form.validate_on_submit():
	# 		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
	# 			flash('You have been logged in!', 'success')
	# 			return redirect(url_for('home'))
	# 		else:
	# 			flash('Login unsuccessful. Please check username and password.', 'danger')
	# 	return render_template('login.html', title='Login', form=form)

# This runs the app if ran directly with python at the CL instead of using "flask run"
# Don't need the environment variables to be set if done this way
if __name__ == '__main__':
	app.run(debug=True)