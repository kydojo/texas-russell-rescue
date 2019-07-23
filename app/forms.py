from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed      # for image upload
from flask_login import current_user
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
# from app.models import User


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
    # def validate_field(self, field):
    # 	if True:
    # 		raise ValidationError('Validation Message')

    # Validate that username doesn't already exist in the db
    # def validate_username(self, username):
    #     # returns 'none' if the username isn't in the db
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError(
    #             'That username is taken. Please choose another.')

    # Validate that user email doesn't already exist in the db
    # def validate_email(self, email):
    #     # returns 'none' if the username isn't in the db
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError(
    #             'That email address is taken. Please choose another.')


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

class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    content = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
