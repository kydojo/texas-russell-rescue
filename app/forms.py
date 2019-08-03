from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed      # for image upload
from flask_login import current_user
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User, Post, Message


# Python classes will be converted into HTML forms. General approach
# adapted from Corey Schafer's Flask tutorial series:
# https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1

# Registration form class that inherits from FlaskForm
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validation function template
    def validate_field(self, field):
    	if True:
    		raise ValidationError('Validation Message')

    # Validate that username doesn't already exist in the db
    def validate_username(self, username):
        # returns 'none' if the username isn't in the db
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose another.')

    # Validate that user email doesn't already exist in the db
    def validate_email(self, email):
        # returns 'none' if the username isn't in the db
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email address is taken. Please choose another.')


# Login form class that inherits from FlaskForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# Update account form class that inherits from FlaskForm
class UpdateAccountForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


    # If the username is changed, validate that the new username doesn't already exist in the db
    def validate_username(self, username):
        if username.data != current_user.username:
        # returns 'none' if the username isn't in the db
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose another.')

    # If the email is changed, validate that the new email doesn't already exist in the db
    def validate_email(self, email):
        if email.data != current_user.email:
            # returns 'none' if the username isn't in the db
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email address is taken. Please choose another.')


STATE_LIST = [
    ('TX', 'Texas'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MI', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsyvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
]

class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    city = StringField('City', validators=[DataRequired(), Length(max=120)])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=120)])
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')


# TODO - Vaccination due date field needs to be added in concert with the vaccines_current field
# TODO - Need to replace the boolean checkboxes with radio fields
# TODO - Need to add ability to upload at least 3 photos and 1 video
# TODO - Validation seems wonky. If I try to submit an empty form the notifications are not helpful
class OwnerSurrenderForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(max=120)])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    dog_origin = TextAreaField(
        'Where did you get your Jack Russell?  Please provide the name of shelter/rescue or name of breeder if you bought him/her from a breeder.', validators=[DataRequired()]
    )
    spayed_or_neutered = BooleanField('My Jack Russell has been spayed/neutered.')
    vaccines_current = BooleanField('My Jack Russell is up to date on vaccinations.')
    vaccine_due_date = StringField('Due Date')
    heartworm_meds_current = BooleanField(
        'My Jack Russell is current on a heartworm prevention medication such as Heartgard.'
    )
    why_rehoming = TextAreaField(
        'We would like to understand your unique situation.  Please tell us how long you have owned your dog & why you are rehoming him/her?', validators=[DataRequired()]
        )
    dog_friendly = BooleanField('My Jack Russell gets along with other dogs.')
    cat_friendly = BooleanField('My Jack Russell gets along with cats.')
    people_friendly = TextAreaField(
        'How does your Jack Russell interact with people?  Are they friendly around people or are they anxious and/or aggressive?  How are they around children?', validators=[DataRequired()]
    )
    training = TextAreaField(
        'Does your Jack Russell know any tricks or have any type of training?', validators=[DataRequired()]
    )
    leash_behavior = TextAreaField(
        'How does your Jack Russell do when walking on a leash?', validators=[DataRequired()]
    )
    car_behavior = StringField(
        'Does your Jack Russell enjoy rides in the car?', validators=[DataRequired()]
    )
    general_health = TextAreaField(
        'Is your Jack Russell healthy?  Are there any special medical needs they might have? Do they have any separation anxiety?', validators=[DataRequired()])
    potty_trained = StringField('Is your Jack Russell house trained and crate trained?', validators=[DataRequired()]
    )
    home_alone_behavior = TextAreaField(
        'When you leave the house, where does your dog stay?  How long is he/she used to you being gone?', validators=[DataRequired()])
    can_remain_home_until_adopted = StringField(
        'All dogs entering rescue are either temporarily placed in a foster home or must remain with their owners until a suitable home can be found.  Foster space is limited, so foster homes are generally reserved for dogs that are in danger of euthanasia at local shelters or are in an emergency situation.  Is your dog able to remain in your home while we find a suitable home for him/her?', validators=[DataRequired()]
    )
    other_info = TextAreaField(
        'Is there anything else you would want us to know about your Jack Russell?', validators=[DataRequired()]
    )
    submit = SubmitField('Send')


MALE_FEMALE_LIST = [
    ('MALE', 'Age'),
    ('FEMALE', 'Sex'),
    ('NO PREFERENCE', 'No Preference')
]

ALTERNATIVES_LIST = [
    ('AGE', 'Age'),
    ('SEX', 'Sex'),
    ('NEITHER', 'Neither')
]

HOUSING_TYPE_LIST  = [
    ('HOUSE', 'House'),
    ('APARTMENT', 'Apartment'),
    ('TRAILER', 'Trailer'),
    ('TOWNHOME', 'Townhome'),
    ('OTHER', 'Other')
]

CALL_TIME_LIST = [
    ('MORNING', 'Morning'),
    ('NOON', 'Noon'),
    ('AFTERNOON', 'Afternoon'),
    ('EVENING', 'Evening')
]

class AdoptionApplicationForm(FlaskForm):
    # Adoption Preferences
    terrier_name = StringField('Name of terrier you would like to adopt (if unknown, type 'Unknown')', validators=[DataRequired(), Length(max=60)])
    male_female = SelectField('State', choices=MALE_FEMALE_LIST, validators=[DataRequired()])
    dog_age = StringField('Age Preference', validators=[DataRequired(), Length(max=60)])
    willing_to_consider_alternative  = SelectField('I am willing to consider a suitable dog of a different', choices=ALTERNATIVES_LIST, validators=[DataRequired()])

    # Applicant Information
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    home_phone = StringField('Home Phone', validators=[Length(max=20)])
    cell_phone = StringField('Cell Phone', validators=[Length(max=20)]) 
    work_phone = StringField('Work Phone', validators=[Length(max=20)]) 
    best_time_to_call = SelectField('Best time to Call', choices=CALL_TIME_LIST validators=[DataRequired()]) 
    street_address = StringField('Street Address', validators=[DataRequired(), Length(max=120)])
    city = StringField('City', validators=[DataRequired(), Length(max=60)])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    zip_code = StringField('Zip', validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired()])
    when_able_to_take_posession = TextAreaField(
        'If approved, when could you take possession of a dog?', validators=[DataRequired()]
    )
    how_far_willing_to_travel = StringField

    # Housing/landlord Information
    housing_type = SelectField('I (we) live in a:', choices=HOUSING_TYPE_LIST, validators=[DataRequired()])
    housing_type_if_other = StringField('', validators=[Length(max=60)])
    rent_or_own = StringField('', validators=[DataRequired()])
    landlord_permission
    landlord_name
    landlord_phone
    how_long_at_address

    # Household Information
    num_adults_in_household
    adults_age
    num_children_in_household
    children_age
    planning_to_have_children
    animal_allergies
    hours_terrier_must_be_alone
    household_visitors
    lifestyle

    # Other Animal Information
    own_other_dogs
    other_dogs_spayed_neutered
    breed_size_gender_of_other_dogs
    own_cats
    own_other_animals
    num_dogs_owned_past_five_years
    status_of_other_dogs_owned

    # Breed-specific Information
    previously_owned_jrt
    why_choose_jrt
    jrt_breed_purpose
    planned_activities_with_jrt
    indorrs_or_outdoors
    where_will_sleep

    # Veterinarian Information
    has_regular_vet  
    Vet_clinic_name
    doctor_name
    vet_street_address
    vet_city
    vet_state 
    vet_zip
    vet_phone
    last_vet_visit_date

    # Reference/Miscellaneous Information
    how_learned_about_us
    if_other
    personal_reference
    reference_name
    reference_relationship
    reference_phone
    additional_comments
