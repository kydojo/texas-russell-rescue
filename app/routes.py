
from flask import render_template, url_for, redirect, flash, request
from app.forms import RegistrationForm, LoginForm, ContactUsForm, OwnerSurrenderForm
from app import app, db, bcrypt
from app.pets import get_pets, get_all_pets
from app.models import User, Post, Message, OwnerSurrenderApplication
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import desc

@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Home')

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

@app.route("/owner_listing_application", methods=['GET', 'POST'])
def owner_listing_application():
    form = OwnerSurrenderForm()
    if form.validate_on_submit():
        application = OwnerSurrenderApplication(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data, 
            dog_origin=form.dog_origin.data,
            spayed_or_neutered=form.spayed_or_neutered.data,
            vaccines_current=form.vaccines_current.data,
            heartworm_meds_current=form.heartworm_meds_current.data,
            why_rehoming=form.why_rehoming.data,
            dog_friendly=form.dog_friendly.data,
            cat_friendly=form.cat_friendly.data,
            people_friendly=form.people_friendly.data,
            training=form.training.data,
            leash_behavior=form.leash_behavior.data,
            car_behavior=form.car_behavior.data,
            general_health=form.general_health.data,
            potty_trained=form.potty_trained.data,
            home_alone_behavior=form.home_alone_behavior.data,
            can_remain_home_until_adopted=form.can_remain_home_until_adopted.data,
            other_info=form.other_info.data
        )
        db.session.add(application)
        db.session.commit()
        flash('Your message has been sent.', 'success')
        return redirect(url_for('index'))
    return render_template('owner_listing_app.html', title='Owner Listing Application', form=form)

@app.route("/surrender_inbox", methods=['GET'])
@login_required
def surrender_inbox():
    applications = OwnerSurrenderApplication.query.order_by(desc(OwnerSurrenderApplication.date_sent)).all()
    return render_template(
        'surrender_inbox.html', title='Owner Surrender Inbox', applications=applications
    )

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactUsForm()
    if form.validate_on_submit():
        message = Message(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            city=form.city.data,
            state=form.state.data,
            subject=form.subject.data,
            content=form.content.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent.', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact Us', form=form)

@app.route("/contact_inbox", methods=['GET'])
@login_required
def contact_inbox():
    messages = Message.query.order_by(desc(Message.date_sent)).all()
    return render_template(
        'contact_inbox.html', title='Contact Us Inbox', messages=messages
    )

@app.route("/pet_test", methods=["GET"])
def pet_test():
    pets = get_all_pets()
    return render_template('pets_test.html', title='test title', pets=pets)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')    # .get() returns None if key does not exist

            # If applicable, redirect to page user tried to access before logging in, else to home page
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            # TODO - this executes but does not properly display the flash message
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
