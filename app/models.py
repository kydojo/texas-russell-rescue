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
	terrier_name = db.Column(db.String(60), nullable=False)
	male_female = db.Column(db.String(15), nullable=False)
	dog_age = db.Column(db.String(40), nullable=False)
	willing_to_consider_alternative = db.Column()
	first_name = db.Column(db.String(60), nullable=False)
	last_name = db.Column(db.String(60), nullable=False)
	email = db.Column(EmailType, nullable=False)
	home_phone = db.Column(db.String(20))
	cell_phone = db.Column(db.String(20))
	work_phone = db.Column(db.String(20))
	best_time_to_call = db.Column(db.String(10))
	street_address = db.Column(db.String(120), nullable=False)
	city = db.Column(db.String(60), nullable=False)
	state = db.Column(db.String(2), nullable=False)
	zip_code = db.Column(db.String(15), nullable=False)
	occupation = db.Column(db.String(60), nullable=False)
	when_able_to_take_posession = db.Column(db.Text, nullable=False)
	how_far_willing_to_travel = db.Column(db.String(40), nullable=False)

	housing_type = db.Column(db.String(15), nullable=False)
	housing_type_if_other = db.Column(db.String(60))
	rent_or_own = db.Column(db.String(5), nullable=False)
	landlord_permission = db.Column(db.String(5), nullable=False)
	landlord_name = db.Column(db.Sring(120))
	landlord_phone = db.Column(db.String(20))
	how_long_at_address_years = db.Column(db.String(3), nullable=False)
	how_long_at_address_months = db.Column(db.String(3), nullable=False)

	has_fenced_yard = db.Column(db.String(3), nullable=False)
    has_kennel_run = db.Column(db.String(3), nullable=False)
    fence_kennel_description = db.Column(db.Text, nullable=False)
    if_none_how_handle_dog_needs = db.Column(db.Text, nullable=False)
    has_dog_crate = db.Column(db.String(3), nullable=False)

	num_adults_in_household = db.Column(db.String(3), nullable=False)
	adults_age = db.Column(db.String(200), nullable=False)
	num_children_in_household = db.Column(db.String(3), nullable=False)
	children_age = db.Column(db.String(200), nullable=False)
	planning_to_have_children = db.Column(db.String(3), nullable=False)
	animal_allergies = db.Column(db.String(3), nullable=False)
	hours_terrier_must_be_alone = db.Column(db.String(30), nullable=False)
	household_visitors = db.Column(db.String(3), nullable=False)
	lifestyle = db.Column(db.String(20), nullable=False)

	own_other_dogs = db.Column(db., nullable=False)
	other_dogs_spayed_neutered = db.Column(db., nullable=False)
	breed_size_gender_of_other_dogs = db.Column(db., nullable=False)
	own_cats = db.Column(db., nullable=False)
	own_other_animals = db.Column(, nullable=False)
	num_dogs_owned_past_five_years = db.Column(db., nullable=False)
	status_of_other_dogs_owned = db.Column(db., nullable=False)

	previously_owned_jrt = db.Column(db., nullable=False)
	why_choose_jrt = db.Column(db., nullable=False)
	jrt_breed_purpose = db.Column(db., nullable=False)
	planned_activities_with_jrt = db.Column(db., nullable=False)
	indorrs_or_outdoors = db.Column(db., nullable=False)
	where_will_sleep = db.Column(db., nullable=False)

	has_regular_vet = db.Column(db., nullable=False)
	Vet_clinic_name = db.Column(db., nullable=False)
	doctor_name = db.Column(db., nullable=False)
	vet_street_address = db.Column(db., nullable=False)
	vet_city = db.Column(db., nullable=False)
	vet_state = db.Column(db., nullable=False)
	vet_zip = db.Column(db., nullable=False)
	vet_phone = db.Column(db., nullable=False)
	last_vet_visit_date = db.Column(db., nullable=False)

	how_learned_about_us = db.Column(db., nullable=False)
	if_other = db.Column(db., nullable=False)
	personal_reference = db.Column(db., nullable=False)
	reference_name = db.Column(db., nullable=False)
	reference_relationship = db.Column(db., nullable=False)
	reference_phone = db.Column(db., nullable=False)
	additional_comments = db.Column(db., nullable=False)
