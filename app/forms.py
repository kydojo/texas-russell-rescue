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
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
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
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
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

class OwnerSurrenderForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(max=120)])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    dog_origin = TextAreaField('Where did you get your Jack Russell?  Please provide the name of shelter/rescue or name of breeder if you bought him/her from a breeder', validators=[DataRequired()])
    spayed_or_neutered = BooleanField('My Jack Russell has been spayed/neutered.')
    vaccines_up_to_date = BooleanField('My Jack Russell is up to date on vaccinations.')
    vaccine_due_date = StringField('Due Date')
    submit = SubmitField('Send')
