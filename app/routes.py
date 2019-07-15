from flask import render_template, url_for, flash, redirect, request

from app.models import User, Post       # "unused import", but "Exception: No user_loader has been installed
                                        # for this LoginManager." thrown if removed.

# from app import app, db, bcrypt, mongo
from app import app, db, bcrypt                     # temp removed mongo (above line is intact)


# Texas Russell Rescue Routes

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
    print(posts)
    return render_template('happy_tails.html', title='Happy Tails', posts=posts)


@app.route("/owner_listing_application")
def owner_listing_application():
    return render_template('owner_listing_app.html', title='Owner Listing Application')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')
