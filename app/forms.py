from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed      # for image upload
from flask_login import current_user
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User, HappyTailsPost, Message


# Python classes will be converted into HTML forms. General approach
# adapted from Corey Schafer's Flask tutorial series:
# https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1

USER_ROLES=(
    ('ADMIN', 'Admin'),
    ('WEBMASTER', 'Webmaster')
)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    urole = SelectField('User Role', choices=USER_ROLES, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Add User')

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

class HappyTailsForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')

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
    ('TX', 'Texas'),
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
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('No Preference', 'No Preference')
]

ALTERNATIVES_LIST = [
    ('Age', 'Age'),
    ('Sex', 'Sex'),
    ('Both', 'Both'),
    ('Neither', 'Neither')
]

HOUSING_TYPE_LIST  = [
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Trailer', 'Trailer'),
    ('Townhome', 'Townhome'),
    ('Other', 'Other')
]

CALL_TIME_LIST = [
    ('N/A', 'N/A'),
    ('Morning', 'Morning'),
    ('Noon', 'Noon'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening')
]

RENT_OR_OWN = [
    ('Rent', 'Rent'),
    ('Own', 'Own')
]

LANDLORD_PERMISSION = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('N/A', 'I do not rent')
]

NUM_ADULTS_IN_HOUSEHOLD = [
    ('1', '1'),
    ('2', '2'),
    ('3+', '3+')
]

NUM_CHILDREN_IN_HOUSEHOLD = [
    ('0', 'None'),
    ('1', '1'),
    ('2', '2'),
    ('3+', '3+')
]

ACTIVITY_LEVEL = [
    ('Very Active', 'Very Active'),
    ('Active', 'Active'),
    ('Not very active', 'Not very active'),
    ('Inactive', 'Inactive')
]

NUM_CATS = [
    ('N/A', 'N/A'),
    ('1', '1'),
    ('2', '2'),
    ('3+', '3+')
]

ACTIVITIES_LIST = [
    ('Family Pet', 'Family Pet'),
    ('Guard', 'Guard'),
    ('Hunting', 'Hunting'),
    ('Obedience', 'Obedience'),
    ('Terrier Trials', 'Terrier Trials'),
    ('Other', 'Other')
]

HOW_FOUND_US_LIST = [
    ('Texas Russell Rescue Website', 'Texas Russell Rescue Website'), 
    ('JRTCA Website', 'JRTCA Website'),
    ('JRTCA Breeders Website', 'JRTCA Breeders Website'),
    ('True Grit Magazine', 'True Grit Magazine'),
    ('From a Friend', 'From a Friend'),
    ('From a Breeder', 'From a Breeder'),
    ('From my Vet', 'From my Vet'),
    ('Texas Russell Rescue Facebook Page', 'Texas Russell Rescue Facebook Page'),
    ('Other', 'Other')
]

INDOORS_OUTDOORS = [
    ('Indoors', "Indoors"),
    ('Outdoors', 'Outdoors')
]

YES_NO = [
    ('No', 'No'),
    ('Yes', 'Yes')
]

YES_NO_NA = [
    ('N/A', 'N/A'),
    ('Yes', 'Yes'),
    ('No', 'No')
]

class AdoptionApplicationForm(FlaskForm):
    # Adoption Preferences
    terrier_name = StringField('Name of terrier (if not known type \'Unknown\')', validators=[DataRequired(), Length(max=60)])
    male_female = SelectField('Do you want to adopt a ...?', choices=MALE_FEMALE_LIST, validators=[DataRequired()])
    dog_age = StringField('Age Preference', validators=[DataRequired(), Length(max=40)])
    willing_to_consider_alternative  = SelectField('I would consider a suitable dog of a different', choices=ALTERNATIVES_LIST, validators=[DataRequired()])

    # Applicant Information
    first_name = StringField('Your First Name', validators=[DataRequired(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    home_phone = StringField('Home Phone', validators=[Length(max=20)])
    cell_phone = StringField('Cell Phone', validators=[Length(max=20)]) 
    work_phone = StringField('Work Phone', validators=[Length(max=20)]) 
    best_time_to_call = SelectField('Best time to Call', choices=CALL_TIME_LIST, validators=[DataRequired()]) 
    street_address = StringField('Street Address', validators=[DataRequired(), Length(max=120)])
    city = StringField('City', validators=[DataRequired(), Length(max=60)])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    zip_code = StringField('Zip', validators=[DataRequired(), Length(max=15)])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=60)])
    when_able_to_take_posession = TextAreaField(
        'If approved, when could you take possession of a dog?', validators=[DataRequired()]
    )
    how_far_willing_to_travel = StringField('How far would you travel to pick up your terrier? (in hours)', validators=[DataRequired(), Length(max=40)])

    # Housing/landlord Information
    housing_type = SelectField('I (we) live in a', choices=HOUSING_TYPE_LIST, validators=[DataRequired()])
    housing_type_if_other = StringField('Housing type if you chose other', validators=[Length(max=60)])
    rent_or_own = SelectField('Do you own or rent your home?', choices=RENT_OR_OWN, validators=[DataRequired()])
    landlord_permission = SelectField('If you rent, do you have your landlords permission to own a dog?', choices=YES_NO_NA, validators=[DataRequired()])
    landlord_name = StringField('Landlord Name', validators=[Length(max=120)])
    landlord_phone = StringField('Landlord Phone', validators=[Length(max=20)])
    how_long_at_address = StringField('How long have you lived at this address?', validators=[DataRequired(), Length(max=30)])

    # Fence/Yard/Kennel Information
    has_fenced_yard = SelectField('Do you have a completely fenced yard suitable for a dog?', choices=YES_NO, validators=[DataRequired()])
    has_kennel_run = SelectField('Do you have a kennel run?', choices=YES_NO, validators=[DataRequired()])
    fence_kennel_description = TextAreaField('Describe fence and/or kennel run (type, height, size)')
    if_none_how_handle_dog_needs = TextAreaField('If no fence/kennel, how will you handle the dog\'s exercise/toilet needs?')
    has_dog_crate = SelectField('Do you have a suitable dog crate?', choices=YES_NO, validators=[DataRequired()])

    # Household Information
    num_adults_in_household = SelectField('How many adults in the household?', choices=NUM_ADULTS_IN_HOUSEHOLD, validators=[DataRequired()])
    adults_age = StringField('Age of Adults', validators=[DataRequired(), Length(max=200)])
    num_children_in_household = SelectField('How many children in the household?', choices=NUM_CHILDREN_IN_HOUSEHOLD, validators=[DataRequired()])
    children_age = StringField('Age of Children', validators=[Length(max=200)])
    planning_to_have_children = SelectField('Are you planning to have children within the next 5 years?', choices=YES_NO, validators=[DataRequired()])
    animal_allergies = SelectField('Are any household members allergic to animals?', choices=YES_NO, validators=[DataRequired()])
    hours_terrier_must_be_alone = StringField('How many hours a day must the terrier be alone?', validators=[DataRequired(), Length(max=30)])
    household_visitors = SelectField('Are there visitors to your home with which a new dog will have to interact?', choices=YES_NO, validators=[DataRequired()])
    lifestyle = SelectField('How would you describe your lifestyle?', choices=ACTIVITY_LEVEL, validators=[DataRequired()])

    # Other Animal Information
    own_other_dogs = SelectField('Do you own any other dogs?', choices=YES_NO, validators=[DataRequired()])
    other_dogs_spayed_neutered = SelectField('If yes, are they Spayed/Neutered?', choices=YES_NO_NA)
    breed_size_gender_of_other_dogs = TextAreaField('Please list breed, size, and gender of each dog you own')
    own_cats = SelectField('Do you own any cats?', choices=YES_NO, validators=[DataRequired()])
    how_many_cats = SelectField('If yes, how many?', choices=NUM_CATS)
    own_other_animals = SelectField('Do you own any other animals?', choices=YES_NO, validators=[DataRequired()])
    other_animals_description = TextAreaField('If yes, please describe them')
    num_dogs_owned_past_five_years = StringField('How many dogs have you owned during the past 5 years?', validators=[DataRequired(), Length(max=200)])
    status_of_other_dogs_owned = TextAreaField('If you do not still own the dog(s), what happened to them?')

    # Breed-specific Information
    previously_owned_jrt = SelectField('Have you ever owned a Jack Russell before?', choices=YES_NO, validators=[DataRequired()])
    why_choose_jrt = TextAreaField('Why did you choose this breed?', validators=[DataRequired()])
    jrt_breed_purpose = TextAreaField('What is the Jack Russell bred to do (if you know)?')
    planned_activities_with_jrt = SelectField('What primary activitiy do you plan to do with this dog?', choices=ACTIVITIES_LIST, validators=[DataRequired()])
    indoors_or_outdoors = SelectField('Where do you intend to keep this dog primarily?', choices=INDOORS_OUTDOORS, validators=[DataRequired()])
    where_will_sleep = StringField('Where will the dog sleep?', validators=[DataRequired(), Length(max=200)])

    # Veterinarian Information
    has_regular_vet = SelectField('Do you have a regular veterinarian? If no, skip this section', choices=YES_NO, validators=[DataRequired()])  
    vet_clinic_name = StringField('Vet Clinic Name', validators=[Length(max=60)])
    doctor_name = StringField('Doctor Name', validators=[Length(max=120)])
    vet_street_address = StringField('Vet Address', validators=[Length(max=120)])
    vet_city = StringField('City', validators=[Length(max=60)])
    vet_state = SelectField('State', choices=STATE_LIST)
    vet_zip = StringField('Zip', validators=[Length(max=15)])
    vet_phone = StringField('Vet Phone Number', validators=[Length(max=20)])
    last_vet_visit_date = StringField('Date of last vet visit', validators=[Length(max=30)])

    # Reference/Miscellaneous Information
    how_learned_about_us = SelectField('How did you learn of Russell Rescue, Inc.?', choices=HOW_FOUND_US_LIST, validators=[DataRequired()])
    if_other = StringField('If you selected other please describe', validators=[Length(max=200)])
    reference_name = StringField('Reference Name', validators=[DataRequired(), Length(max=120)])
    reference_relationship = StringField('Relationship', validators=[DataRequired(), Length(max=120)])
    reference_phone = StringField('Reference Phone Number', validators=[DataRequired(), Length(max=20)])
    additional_comments = TextAreaField('Additional Comments')

    submit = SubmitField('Submit Application')


class VolunteerForm(FlaskForm):
    # Section 1 - Your Information:
    first_name = StringField('Your First Name', validators=[DataRequired(), Length(max=60)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=60)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    home_phone = StringField('Home Phone', validators=[Length(max=20)])
    cell_phone = StringField('Cell Phone', validators=[Length(max=20)]) 
    work_phone = StringField('Work Phone', validators=[Length(max=20)]) 
    best_time_to_call = SelectField('Best time to Call', choices=CALL_TIME_LIST, validators=[DataRequired()]) 
    street_address = StringField('Street Address', validators=[DataRequired(), Length(max=120)])
    city = StringField('City', validators=[DataRequired(), Length(max=60)])
    state = SelectField('State', choices=STATE_LIST, validators=[DataRequired()])
    zip_code = StringField('Zip', validators=[DataRequired(), Length(max=15)])

    # Section 2 - How would you like to help? (Check all that apply.)
    foster_home = BooleanField('Foster Home')
    adoption_screen_or_counseling = BooleanField('Screen Applicants/Adoption Counseling')
    transport_dogs = BooleanField('Transport Dogs')
    behavior_counseling = BooleanField('Behavior Counseling')
    fundraising = BooleanField('Fundraising')
    home_visits = BooleanField('Home Visits')
    staff_booths_info_centers = BooleanField('Staff booths/info centers (at trials, pet expos, etc.)') # (table at trials, pet expos, etc.)
    shelter_contact = BooleanField('Shelter Contact')
    web_or_social_media = BooleanField('Post dogs available for adoption on our websites and social media')
    other_role = StringField('Other (please describe):')

    # Section 3 - Experience and Schedule:
    volunteer_experience = TextAreaField('Please describe previous volunteer and/or rescue experience')
    dog_handling_experience = TextAreaField('Please describe any special dog handling experience you might have')
    hours_can_volunteer = StringField('How many hours per week can you devote to Russell Rescue?  Please be realistic.', validators=[DataRequired()])
    schedule_flexibility = TextAreaField('How flexible is your schedule? For example, could you make time during the day to pick up a dog in an emergency situation?',  validators=[DataRequired()]) 
    availability = TextAreaField('Please describe your availability',  validators=[DataRequired()])
    ok_call_at_work = SelectField('Is it okay for us to contact you at your work number?', choices=YES_NO, validators=[DataRequired()])

    # Section 4 - Your Home
    owns_cats = SelectField('Do you own any cats?', choices=YES_NO, validators=[DataRequired()])
    num_cats = SelectField('If yes, how many live with you?', choices=NUM_CATS)
    owns_dogs = SelectField('Do you own dogs?', choices=YES_NO, validators=[DataRequired()])
    num_dogs = SelectField('If yes, how many live with you?', choices=NUM_CATS)
    dog_descriptions = TextAreaField('Please list breed, gender, and age of each dog')
    pets_spayed_neutered = SelectField('Are your pets spayed/neutered?', choices=YES_NO_NA, validators=[DataRequired()])

    is_breeder = SelectField('Do you breed?', choices=YES_NO)
    litters_per_year = StringField('If so, how many litters per year?', validators=[Length(max=120)])

    children_in_home = SelectField('Are there children in your home that would come in contact with a dog?', choices=YES_NO)
    children_dog_contact_frequency = StringField('If yes, how often would this contact occur?', validators=[Length(max=200)])
    children_age = StringField('What are the ages of the children?', validators=[Length(max=200)])

    # Section 5 - Your Vet
    has_regular_vet = SelectField('Do you have a regular veterinarian? If no, skip this section', choices=YES_NO, validators=[DataRequired()])  
    vet_clinic_name = StringField('Vet Clinic Name', validators=[Length(max=60)])
    doctor_name = StringField('Doctor Name', validators=[Length(max=120)])
    vet_street_address = StringField('Vet Address', validators=[Length(max=120)])
    vet_city = StringField('City', validators=[Length(max=60)])
    vet_state = SelectField('State', choices=STATE_LIST)
    vet_zip = StringField('Zip', validators=[Length(max=15)])
    vet_phone = StringField('Vet Phone Number', validators=[Length(max=20)])

    # Section 6 - Your Opinions/Preferences
    feelings_about_rescue = TextAreaField('Please describe your feelings about what rescue is', validators=[DataRequired()])
    euthanasia_feelings = TextAreaField('How would you feel if you had to recommend euthanasia of a Jack Russell Terrier?', validators=[DataRequired()])
    euthanasia_circumstances = TextAreaField('Under what circumstances could you see yourself recommending euthanasia?', validators=[DataRequired()])

    # Are you willing to handle and/or evaluate the following? (check all that apply)*
    sick_dogs = BooleanField('Sick dogs')
    pregnant_females = BooleanField('Pregnant females')
    unstable_dogs = BooleanField('Dogs deemed mentally unstable')
    females_in_heat = BooleanField('Females in heat')
    dog_aggressive_dogs = BooleanField('Dog-aggressive dogs')
    intact_dogs = BooleanField('Intact dogs (until spay or neuter can be arranged)')
    no_children_dogs = BooleanField('Dogs that don\'t like children')
    geriatric_dogs = BooleanField('Geriatric dogs')
    dogs_not_potty_trained = BooleanField('Dogs that are not housebroken or crate trained')
    hyper_dogs = BooleanField('Extremely hyper dogs')
    escape_artists = BooleanField('Escape artists')
    other_handling_preferences = TextAreaField('Please list anything else you are or are not willing/able to work with')

    # Section 7 - References
    first_reference_name = StringField('First Reference Name', validators=[DataRequired(), Length(max=120)])
    first_reference_relationship = StringField('Relationship', validators=[DataRequired(), Length(max=120)])
    first_reference_phone = StringField('First Reference Phone Number', validators=[DataRequired(), Length(max=20)])
    second_reference_name = StringField('Second Reference Name', validators=[Length(max=120)])
    second_reference_relationship = StringField('Relationship', validators=[Length(max=120)])
    second_reference_phone = StringField('Second Reference Phone Number', validators=[Length(max=20)])
    additional_comments = TextAreaField('Please provide any additional comments that you might have')

    # Section 8 - Volunteer Waiver
    volunteer_waiver_agreement = BooleanField('I Agree', validators=[DataRequired()])

    # Section 9 - Foster Home Application
    # Please skip Section 9 and 10 if you are not applying to foster.
    has_crate = SelectField('Do you have a dog crate?', choices=YES_NO)
    has_fenced_yard = SelectField('Do you have a fenced yard?', choices=YES_NO)
    has_kennel = SelectField('Do you have a kennel run?', choices=YES_NO)
    fence_kennel_description = TextAreaField('Describe fence and/or kennel run (type, height, size)')
    rent_or_own = SelectField('Do you own or rent your home?', choices=RENT_OR_OWN, validators=[DataRequired()])
    housing_type = SelectField('What type of home do you live in?', choices=HOUSING_TYPE_LIST, validators=[DataRequired()])
    housing_type_if_other = StringField('Housing type if you chose other', validators=[Length(max=60)])
    how_long_at_address = StringField('How long have you lived at this address?', validators=[DataRequired(), Length(max=30)])

    # Where will the foster dog be housed during the day (check all that apply)?
    inside_crated = BooleanField('Inside crated')
    outdoors_loose = BooleanField('Outdoors loose (in fenced area only)')
    inside_loose = StringField('Inside loose (describe location)',  validators=[Length(max=120)]) 
    outdoors_kenneled = BooleanField('Outdoors kenneled')
    garage = BooleanField('Garage')
    barn = BooleanField('Barn')
    other_dog_housing = TextAreaField('Other (if other please explain)')

    # Where will the foster dog be kept when unsupervised or when left alone? (Check all that apply)
    unsupervised_inside_crated = BooleanField('Inside crated')
    unsupervised_outdoors_loose = BooleanField('Outdoors loose (in fenced area only)')
    unsupervised_inside_loose = StringField('Inside loose (describe location)',  validators=[Length(max=120)]) 
    unsupervised_outdoors_kenneled = BooleanField('Outdoors kenneled')
    unsupervised_garage = BooleanField('Garage')
    unsupervised_barn = BooleanField('Barn')
    unsupervised_other = TextAreaField('Other (if other please explain)')

    # Where will the foster dog sleep? (Check all that apply)
    sleep_inside_crated = BooleanField('Inside crated')
    sleep_outdoors_loose = BooleanField('Outdoors loose (in fenced area only)')
    sleep_inside_loose = StringField('Inside loose (describe location)',  validators=[Length(max=120)]) 
    sleep_outdoors_kenneled = BooleanField('Outdoors kenneled')
    sleep_garage = BooleanField('Garage')
    sleep_barn = BooleanField('Barn')
    sleep_other = TextAreaField('Other (if other please explain)')

    knows_lack_of_med_history = SelectField('Did you know that most foster dogs have no medical and behavior history?', choices=YES_NO)
    accepts_liability = SelectField('Are you willing to accept all responsibility and liability of a foster dog\'s actions on or off your property while in your care?', choices=YES_NO)
    will_travel_to_pick_up_foster = SelectField('Are you willing to travel to pick up a foster dog?', choices=YES_NO)
    distance_willing_to_travel = StringField('Distance you are willing to travel (round trip in hours)',  validators=[Length(max=40), DataRequired()])
    travel_or_open_home_for_adopters = SelectField('Are you willing to travel and/or open your home for potential adopters to visit the dog?', choices=YES_NO)
    aware_foster_is_indefinite = SelectField('Are you aware that a foster dog may be in your home for an indefinite period of time?', choices=YES_NO)
    will_take_to_vet_if_needed = SelectField('Are you willing to transport the foster dog to the vet if it is required?', choices=YES_NO)

    # Section 10 - Foster Home Application Waiver
    foster_waiver_agreement = BooleanField('I Agree', validators=[DataRequired()])

    submit = SubmitField('Submit Application')
