from flask import render_template, url_for, redirect, flash, request
from app import app, mongo
from app.pets import get_pets, get_all_pets
from app.forms import ContactUsForm

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
    posts = mongo.db.posts.find()
    print(type(posts))
    return render_template('happy_tails.html', title='Happy Tails', posts=posts)

@app.route("/owner_listing_application")
def owner_listing_application():
    return render_template('owner_listing_app.html', title='Owner Listing Application')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactUsForm()
    if form.validate_on_submit():
        flash('Your message has been sent.', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact Us', form=form)

@app.route("/pet_test", methods=["GET"])
def pet_test():
    pets = get_all_pets()
    return render_template('pets_test.html', title='test title', pets=pets)
