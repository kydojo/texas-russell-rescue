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
	urole = db.Column(db.String(20), nullable=False)
	access_level = db.Column(db.Integer, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # image_file attribute for profile pic, hash will have a max length of 20, default image will be set
	password = db.Column(db.String(60), nullable=False) # password attribute, hash will have a max length of 60
	# posts = db.relationship('HappyTailsPost', backref='author', lazy=True) # posts attribute to connect User to the Post model
	urole = db.Column(db.String(60)) # not technically needed anymore, but i'm going to keep it in. Could be useful for differentiating admins
	access_level = db.Column(db.Integer) # webmaster=500, admin=100, so all other levels can be added somewhere in between

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.urole}')"


# Post class, inherits from db.Model
class HappyTailsPost(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(100), nullable=False) # title attribute, string with a max length of 100, not null
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date_posted attribute, DateTime, set the default to the time posted unless set
	content = db.Column(db.Text, nullable=False) # content attribute, text content of the post
	# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user_id attribute, FK is the author's user.id (from the User model)

	# Dunder (magic) method to define how the object will be printed out
	def __repr__(self):
		return f"HappyTailsPost('{self.title}', '{self.date_posted}')"

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


class AdoptionApplication(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	terrier_name = db.Column(db.String(60), nullable=False)
	male_female = db.Column(db.String(15), nullable=False)
	dog_age = db.Column(db.String(40), nullable=False)
	willing_to_consider_alternative = db.Column(db.String(20), nullable=False)

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
	landlord_name = db.Column(db.String(120))
	landlord_phone = db.Column(db.String(20))
	how_long_at_address = db.Column(db.String(30), nullable=False)

	has_fenced_yard = db.Column(db.String(3), nullable=False)
	has_kennel_run = db.Column(db.String(3), nullable=False)
	fence_kennel_description = db.Column(db.Text)
	if_none_how_handle_dog_needs = db.Column(db.Text)
	has_dog_crate = db.Column(db.String(3), nullable=False)

	num_adults_in_household = db.Column(db.String(3), nullable=False)
	adults_age = db.Column(db.String(200), nullable=False)
	num_children_in_household = db.Column(db.String(3), nullable=False)
	children_age = db.Column(db.String(200))
	planning_to_have_children = db.Column(db.String(3), nullable=False)
	animal_allergies = db.Column(db.String(3), nullable=False)
	hours_terrier_must_be_alone = db.Column(db.String(30), nullable=False)
	household_visitors = db.Column(db.String(3), nullable=False)
	lifestyle = db.Column(db.String(20), nullable=False)

	own_other_dogs = db.Column(db.String(3), nullable=False)
	other_dogs_spayed_neutered = db.Column(db.String(3))
	breed_size_gender_of_other_dogs = db.Column(db.Text)
	own_cats = db.Column(db.String(3), nullable=False)
	how_many_cats = db.Column(db.String(3))
	own_other_animals = db.Column(db.String(3), nullable=False)
	other_animals_description = db.Column(db.Text)
	num_dogs_owned_past_five_years = db.Column(db.String(200), nullable=False)
	status_of_other_dogs_owned = db.Column(db.Text)

	previously_owned_jrt = db.Column(db.String(3), nullable=False)
	why_choose_jrt = db.Column(db.Text, nullable=False)
	jrt_breed_purpose = db.Column(db.Text)
	planned_activities_with_jrt = db.Column(db.String(15), nullable=False)
	indoors_or_outdoors = db.Column(db.String(10), nullable=False)
	where_will_sleep = db.Column(db.String(200), nullable=False)

	has_regular_vet = db.Column(db.String(3), nullable=False)
	vet_clinic_name = db.Column(db.String(60))
	doctor_name = db.Column(db.String(120))
	vet_street_address = db.Column(db.String(120))
	vet_city = db.Column(db.String(60))
	vet_state = db.Column(db.String(2))
	vet_zip = db.Column(db.String(15))
	vet_phone = db.Column(db.String(20))
	last_vet_visit_date = db.Column(db.String(30))	# TODO - should probably change this to a date type

	how_learned_about_us = db.Column(db.String(50), nullable=False)
	if_other = db.Column(db.String(200))
	reference_name = db.Column(db.String(120), nullable=False)
	reference_relationship = db.Column(db.String(120), nullable=False)
	reference_phone = db.Column(db.String(20), nullable=False)
	additional_comments = db.Column(db.Text)
	date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Message('Dog: {self.terrier_name}', 'Applicant: {self.first_name}', '{self.city}', '{self.date_sent}')"


class VolunteerApplication(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	
	# Section 1 - Your Information:
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

    # Section 2 - How would you like to help? (Check all that apply.)
	foster_home = db.Column(db.Boolean, default=False)
	adoption_screen_or_counseling = db.Column(db.Boolean, default=False)
	transport_dogs = db.Column(db.Boolean, default=False)
	behavior_counseling = db.Column(db.Boolean, default=False)
	fundraising = db.Column(db.Boolean, default=False)
	home_visits = db.Column(db.Boolean, default=False)
	staff_booths_info_centers = db.Column(db.Boolean, default=False) # (table at trials, pet expos, etc.)
	shelter_contact = db.Column(db.Boolean, default=False)
	web_or_social_media = db.Column(db.Boolean, default=False)
	other_role = db.Column(db.String(200))

	# Section 3 - Experience and Schedule:
	volunteer_experience = db.Column(db.Text)
	dog_handling_experience  = db.Column(db.Text)

	hours_can_volunteer = db.Column(db.String(200), nullable=False)
	schedule_flexibility = db.Column(db.Text, nullable=False)
	availability = db.Column(db.Text, nullable=False)
	ok_call_at_work = db.Column(db.String(3), nullable=False)

	# Section 4 - Your Home
	owns_cats = db.Column(db.String(3), nullable=False)
	num_cats = db.Column(db.String(3))
	owns_dogs = db.Column(db.String(3), nullable=False)
	num_dogs = db.Column(db.String(3))
	dog_descriptions = db.Column(db.Text)
	pets_spayed_neutered = db.Column(db.String(3))

	is_breeder = db.Column(db.String(3), nullable=False)
	litters_per_year = db.Column(db.String(120))

	children_in_home = db.Column(db.String(3), nullable=False)
	children_dog_contact_frequency = db.Column(db.String(200))
	children_age = db.Column(db.String(200))

	# Section 5 - Your Vet
	has_regular_vet = db.Column(db.String(3), nullable=False)
	vet_clinic_name = db.Column(db.String(60))
	doctor_name = db.Column(db.String(120))
	vet_street_address = db.Column(db.String(120))
	vet_city = db.Column(db.String(60))
	vet_state = db.Column(db.String(2))
	vet_zip = db.Column(db.String(15))
	vet_phone = db.Column(db.String(20))

	# Section 6 - Your Opinions/Preferences
	feelings_about_rescue = db.Column(db.Text, nullable=False)
	euthanasia_feelings = db.Column(db.Text, nullable=False)
	euthanasia_circumstances = db.Column(db.Text, nullable=False)

	# Are you willing to handle and/or evaluate the following? (check all that apply)*
	sick_dogs = db.Column(db.Boolean, default=False)
	pregnant_females = db.Column(db.Boolean, default=False)
	unstable_dogs = db.Column(db.Boolean, default=False)
	females_in_heat = db.Column(db.Boolean, default=False)
	dog_aggressive_dogs = db.Column(db.Boolean, default=False)
	intact_dogs = db.Column(db.Boolean, default=False)
	no_children_dogs = db.Column(db.Boolean, default=False)
	geriatric_dogs = db.Column(db.Boolean, default=False)
	dogs_not_potty_trained = db.Column(db.Boolean, default=False)
	hyper_dogs = db.Column(db.Boolean, default=False)
	escape_artists = db.Column(db.Boolean, default=False)
	other_handling_preferences = db.Column(db.Text)

	# Section 7 - References
	first_reference_name = db.Column(db.String(120), nullable=False)
	first_reference_relationship = db.Column(db.String(120), nullable=False)
	first_reference_phone = db.Column(db.String(20), nullable=False)
	second_reference_name = db.Column(db.String(120))
	second_reference_relationship = db.Column(db.String(120))
	second_reference_phone = db.Column(db.String(20))
	additional_comments = db.Column(db.Text)

	# Section 8 - Volunteer Waiver
	volunteer_waiver_agreement = db.Column(db.Boolean, default=False)

	# Section 9 - Foster Home Application
	# Please skip Section 9 and 10 if you are not applying to foster.
	has_crate = db.Column(db.String(3), nullable=False)
	has_fenced_yard = db.Column(db.String(3), nullable=False)
	has_kennel = db.Column(db.String(3), nullable=False)
	fence_kennel_description = db.Column(db.Text)
	housing_type = db.Column(db.String(15))
	housing_type_if_other = db.Column(db.String(60))
	rent_or_own = db.Column(db.String(5))
	how_long_at_address = db.Column(db.String(30), nullable=False)


	# Where will the foster dog be housed during the day (check all that apply)?
	inside_crated = db.Column(db.Boolean, default=False)
	outdoors_loose = db.Column(db.Boolean, default=False)
	inside_loose = db.Column(db.String(120), default=False)
	outdoors_kenneled = db.Column(db.Boolean, default=False)
	garage = db.Column(db.Boolean, default=False)
	barn = db.Column(db.Boolean, default=False)
	other_dog_housing = db.Column(db.Text)

	# Where will the foster dog be kept when unsupervised or when left alone? (Check all that apply)
	unsupervised_inside_crated = db.Column(db.Boolean, default=False)
	unsupervised_outdoors_loose = db.Column(db.Boolean, default=False)
	unsupervised_inside_loose = db.Column(db.String(120), default=False) 
	unsupervised_outdoors_kenneled = db.Column(db.Boolean, default=False)
	unsupervised_garage = db.Column(db.Boolean, default=False)
	unsupervised_barn = db.Column(db.Boolean, default=False)
	unsupervised_other = db.Column(db.Text)

	# Where will the foster dog sleep? (Check all that apply)
	sleep_inside_crated = db.Column(db.Boolean, default=False)
	sleep_outdoors_loose = db.Column(db.Boolean, default=False)
	sleep_inside_loose = db.Column(db.String(120), default=False)
	sleep_outdoors_kenneled = db.Column(db.Boolean, default=False)
	sleep_garage = db.Column(db.Boolean, default=False)
	sleep_barn = db.Column(db.Boolean, default=False)
	sleep_other = db.Column(db.Text)

	knows_lack_of_med_history = db.Column(db.String(3), nullable=False)
	accepts_liability = db.Column(db.String(3), nullable=False)
	will_travel_to_pick_up_foster = db.Column(db.String(3), nullable=False)
	distance_willing_to_travel = db.Column(db.String(40), nullable=False)
	travel_or_open_home_for_adopters = db.Column(db.String(3), nullable=False)
	aware_foster_is_indefinite = db.Column(db.String(3), nullable=False)
	will_take_to_vet_if_needed = db.Column(db.String(3), nullable=False)

	# Section 10 - Foster Home Application Waiver
	foster_waiver_agreement = db.Column(db.Boolean, default=False)
	date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Message('Applicant: {self.first_name}', '{self.city}', '{self.date_sent}')"