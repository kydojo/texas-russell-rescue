import os   # to get file extensions from the image files
import secrets  # for random hex
from PIL import Image   # Python Imaging Library; for image resizing (Pillow)
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
# import the classes from forms.py since it's in the same dir
# from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        'author': 'Kyle Johnson',
        'title': 'Happy Tails Post 1',
        'content': 'First post content',
        'date_posted': 'June 24, 2019'
    },
    {
        'author': 'Shannon Lucas',
        'title': 'Happy Tails Post 2',
        'content': 'Second post content',
        'date_posted': 'June 25, 2019'
    },
    {
        'author': 'Neal Quigley',
        'title': 'Happy Tails Post 3',
        'content': 'Third post content',
        'date_posted': 'June 26, 2019'
    }
]


# Texas Russell Rescue Routes

# Temp - has the entire original index/home template stored here
@app.route("/index")
def index():
    return render_template('index.html', title='About')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/volunteer")
def volunteer():
    return render_template('volunteer.html', title='Volunteer')

@app.route("/before_you_adopt")
def before_you_adopt():
    return render_template('before_you_adopt.html', title='Before You Adopt')

@app.route("/adoption_application")
def adoption_application():
    return render_template('adoption_app.html', title='Adoption Application')

@app.route("/rescues")
def rescues():
    return render_template('rescues.html', title='Rescues')

@app.route("/owner_listings")
def owner_listings():
    return render_template('owner_listings.html', title='Owner Listings')

@app.route("/spotlight_terriers")
def spotlight_terriers():
    return render_template('spotlight_terriers.html', title='Spotlight Terriers')

@app.route("/happy_tails")
def happy_tails():
    return render_template('happy_tails.html', title='Happy Tails', posts=posts)

@app.route("/owner_listing_application")
def owner_listing_application():
    return render_template('owner_listing_app.html', title='Owner Listing Application')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()  # create an instance of our form
    if form.validate_on_submit():
        # create a hashed pw for the pw entered into the pw field; decode makes it a string (instead of bytes)
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # instantiate a user with username, email, and the hashed pw
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()  # create an instance of our form
    if form.validate_on_submit():
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        # 	flash('You have been logged in!', 'success')
        # 	return redirect(url_for('home'))
        # else:

        # Check if the user email exists in the db
        user = User.query.filter_by(email=form.email.data).first()
        # If the user exists and their password matches what's stored in the db for them
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # if there's a 'next' param in the URL string, set it to the next page; this is for redirecting after a required login
            next_page = request.args.get('next')
            # ternary conditional
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# Function to handle picture data on account info update
def save_picture(form_picture):
    # Create random hex for the base of our file name (so we don't have conflicts)
    random_hex = secrets.token_hex(8)

    # Store the file name (not used, so named '_') and extension from the image file
    _, f_ext = os.path.splitext(form_picture.filename)
    
    # Create the picture file name
    picture_fn = random_hex + f_ext

    # Create the file path and save it to the path
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    # Resize the image to 125px (saves on space and load times)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    # Save the image
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
	# If the form field inputs are valid, update the username and email and commit to the db
    if form.validate_on_submit():
        if form.picture.data:
            # Save the current user's image to the picture file
            # save_picture() is our function, defined above
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account')) 
	# If this is a GET request (on page load), pre-populate the form fields with the current username and email
    elif request.method == 'GET':
	    form.username.data = current_user.username
	    form.email.data = current_user.email

    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)
