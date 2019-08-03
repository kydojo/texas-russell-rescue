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
	name = db.Column(db.String(120), nullable=False)
	email = db.Column(EmailType, nullable=False)
	phone = db.Column(db.String(20))
	city = db.Column(db.String(60), nullable=False)
	state = db.Column(db.String(2), nullable=False)
	date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	subject = db.Column(db.String(120), nullable=False)
	content = db.Column(db.Text, nullable=False) # content attribute, text content of the post

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"Message('{self.name}', '{self.city}', '{self.state}', '{self.date_sent}')"

class OwnerSurrenderApplication(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True) # create the user id attribute and set it to the PK for the db
	first_name = db.Column(db.String(60), nullable=False)
	last_name = db.Column(db.String(60), nullable=False)
	email = db.Column(EmailType, nullable=False)
	phone = db.Column(db.String(20))
	address = db.Column(db.String(120), nullable=False)
	city = db.Column(db.String(60), nullable=False)
	state = db.Column(db.String(2), nullable=False)
	date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	dog_origin = db.Column(db.Text, nullable=False)
	spayed_or_neutered = db.Column(db.Boolean, default=False)
	vaccines_current = db.Column(db.Boolean, default=False)
	heartworm_meds_current = db.Column(db.Boolean, default=False)
	why_rehoming = db.Column(db.Text, nullable=False)
	dog_friendly = db.Column(db.Boolean, default=False)
	cat_friendly = db.Column(db.Boolean, default=False)
	people_friendly = db.Column(db.Text, nullable=False)
	training = db.Column(db.Text, nullable=False)
	leash_behavior = db.Column(db.Text, nullable=False)
	car_behavior = db.Column(db.String, nullable=False)
	general_health = db.Column(db.Text, nullable=False)
	potty_trained = db.Column(db.String, nullable=False)
	home_alone_behavior = db.Column(db.Text, nullable=False)
	can_remain_home_until_adopted = db.Column(db.String, nullable=False)
	other_info = db.Column(db.Text)

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"Message('{self.name}', '{self.city}', '{self.state}', '{self.date_sent}')"


class adoptionApplication(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	terrier_name = db.Column()
	male_female = db.Column()
	dog_age = db.Column()
	willing_to_consider_alternative = db.Column()
	first_name = db.Column(db.String(60), nullable=False)
	last_name = db.Column(db.String(60), nullable=False)
	email = db.Column(EmailType, nullable=False)
	home_phone = db.Column(db.String(20))
	cell_phone = db.Column(db.String(20))
	work_phone = db.Column(db.String(20))
	best_time_to_call = db.Column()
	street_address = db.Column(db.String(120), nullable=False)
	city = db.Column(db.String(60), nullable=False)
	state = db.Column(db.String(2), nullable=False)
	zip_code = db.Column()
	occupation = db.Column()
	when_able_to_take_posession = db.Column()
	how_far_willing_to_travel = db.Column()
	housing_type = db.Column()
	housing_type_if_other = db.Column()
	rent_or_own = db.Column()
	landlord_permission = db.Column()
	landlord_name = db.Column()
	landlord_phone = db.Column()
	how_long_at_address = db.Column()
	num_adults_in_household = db.Column()
	adults_age = db.Column()
	num_children_in_household = db.Column()
	children_age = db.Column()
	planning_to_have_children = db.Column()
	animal_allergies = db.Column()
	hours_terrier_must_be_alone = db.Column()
	household_visitors = db.Column()
	lifestyle = db.Column()
	own_other_dogs = db.Column()
	other_dogs_spayed_neutered = db.Column()
	breed_size_gender_of_other_dogs = db.Column()
	own_cats = db.Column()
	own_other_animals = db.Column()
	num_dogs_owned_past_five_years = db.Column()
	status_of_other_dogs_owned = db.Column()
	previously_owned_jrt = db.Column()
	why_choose_jrt = db.Column()
	jrt_breed_purpose = db.Column()
	planned_activities_with_jrt = db.Column()
	indorrs_or_outdoors = db.Column()
	where_will_sleep = db.Column()
	has_regular_vet = db.Column()
	Vet_clinic_name = db.Column()
	doctor_name = db.Column()
	vet_street_address = db.Column()
	vet_city = db.Column()
	vet_state = db.Column()
	vet_zip = db.Column()
	vet_phone = db.Column()
	last_vet_visit_date = db.Column()
	how_learned_about_us = db.Column()
	if_other = db.Column()
	personal_reference = db.Column()
	reference_name = db.Column()
	reference_relationship = db.Column()
	reference_phone = db.Column()
	additional_comments = db.Column()
