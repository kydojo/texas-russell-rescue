
from functools import wraps
from flask import render_template, url_for, redirect, flash, request
from app.forms import RegistrationForm, LoginForm, ContactUsForm, OwnerSurrenderForm, AdoptionApplicationForm
from app import app, db, bcrypt, login_manager
from app.pets import get_pets, get_all_pets
from app.sender import send_application_submission_confirmation, send_contact_info, send_surrender_applicant_info
from app.models import User, Post, Message, OwnerSurrenderApplication, AdoptionApplication
from flask_login import login_user, logout_user, current_user
from sqlalchemy import desc

# add multiple tiers of login levels
# def login_required(role="ANY"):
#     def wrapper(fn):
#         @wraps(fn)
#         def decorated_view(*args, **kwargs):
#             if not current_user.is_authenticated:
#               return login_manager.unauthorized()
#             if ((current_user.urole != role) and (role != "ANY")):
#                 return login_manager.unauthorized()
#             return fn(*args, **kwargs)
#         return decorated_view
#     return wrapper

# Global vars for tiered access levels
ADMIN = 500
WEBMASTER = 100


def login_required(level):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if current_user.access_level < level:
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Home')


@app.route("/test0")
@login_required(ADMIN)
def test0():
    return render_template('about.html', title='About')


@app.route("/test1")
@login_required(ADMIN)
def test1():
    return render_template('about.html', title='About')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/volunteer")
def volunteer():
    return render_template('volunteer.html', title='Volunteer')


@app.route("/volunteer_form")
def volunteer_form():
    return render_template('volunteer_form.html', title='Volunteer Form')


@app.route("/meet_our_volunteers")
def meet_our_volunteers():
    return render_template('meet_our_volunteers.html', title='Meet Our Volunteers')


@app.route("/events")
def events():
    return render_template('events.html', title='Events')


@app.route("/before_you_adopt")
def before_you_adopt():
    return render_template('before_you_adopt.html', title='Before You Adopt')


@app.route("/adoption_application", methods=['GET', 'POST'])
def adoption_application():
    form = AdoptionApplicationForm()
    if form.validate_on_submit():
        application = AdoptionApplication(
            terrier_name=form.terrier_name.data,
            male_female=form.male_female.data,
            dog_age=form.dog_age.data,
            willing_to_consider_alternative=form.willing_to_consider_alternative.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            home_phone=form.home_phone.data,
            cell_phone=form.cell_phone.data,
            work_phone=form.work_phone.data,
            best_time_to_call=form.best_time_to_call.data,
            street_address=form.street_address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            occupation=form.occupation.data,
            when_able_to_take_posession=form.when_able_to_take_posession.data,
            how_far_willing_to_travel=form.how_far_willing_to_travel.data,

            housing_type=form.housing_type.data,
            housing_type_if_other=form.housing_type_if_other.data,
            rent_or_own=form.rent_or_own.data,
            landlord_permission=form.landlord_permission.data,
            landlord_name=form.landlord_name.data,
            landlord_phone=form.landlord_phone.data,
            how_long_at_address=form.how_long_at_address.data,

            has_fenced_yard=form.has_fenced_yard.data,
            has_kennel_run=form.has_kennel_run.data,
            fence_kennel_description=form.fence_kennel_description.data,
            if_none_how_handle_dog_needs=form.if_none_how_handle_dog_needs.data,
            has_dog_crate=form.has_dog_crate.data,

            num_adults_in_household=form.num_adults_in_household.data,
            adults_age=form.adults_age.data,
            num_children_in_household=form.num_children_in_household.data,
            children_age=form.children_age.data,
            planning_to_have_children=form.planning_to_have_children.data,
            animal_allergies=form.animal_allergies.data,
            hours_terrier_must_be_alone=form.hours_terrier_must_be_alone.data,
            household_visitors=form.household_visitors.data,
            lifestyle=form.lifestyle.data,

            own_other_dogs=form.own_other_dogs.data,
            other_dogs_spayed_neutered=form.other_dogs_spayed_neutered.data,
            breed_size_gender_of_other_dogs=form.breed_size_gender_of_other_dogs.data,
            own_cats=form.own_cats.data,
            how_many_cats=form.how_many_cats.data,
            own_other_animals=form.own_other_animals.data,
            other_animals_description=form.other_animals_description.data,
            num_dogs_owned_past_five_years=form.num_dogs_owned_past_five_years.data,
            status_of_other_dogs_owned=form.status_of_other_dogs_owned.data,

            previously_owned_jrt=form.previously_owned_jrt.data,
            why_choose_jrt=form.why_choose_jrt.data,
            jrt_breed_purpose=form.jrt_breed_purpose.data,
            planned_activities_with_jrt=form.planned_activities_with_jrt.data,
            indoors_or_outdoors=form.indoors_or_outdoors.data,
            where_will_sleep=form.where_will_sleep.data,

            has_regular_vet=form.has_regular_vet.data,
            vet_clinic_name=form.vet_clinic_name.data,
            doctor_name=form.doctor_name.data,
            vet_street_address=form.vet_street_address.data,
            vet_city=form.vet_city.data,
            vet_state=form.vet_state.data,
            vet_zip=form.vet_zip.data,
            vet_phone=form.vet_phone.data,
            last_vet_visit_date=form.last_vet_visit_date.data,

            how_learned_about_us=form.how_learned_about_us.data,
            if_other=form.if_other.data,
            reference_name=form.reference_name.data,
            reference_relationship=form.reference_relationship.data,
            reference_phone=form.reference_phone.data,
            additional_comments=form.additional_comments.data
        )
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('adoption_app.html', title='Adoption Application', form=form)


@app.route("/adoption_app_inbox", methods=['GET'])
@login_required(ADMIN)
def application_inbox():
    applications = AdoptionApplication.query.order_by(
        desc(AdoptionApplication.date_sent)).all()
    return render_template(
        'adoption_app_inbox.html', title='Adoption Application Inbox', applications=applications
    )


@app.route("/available_dogs", methods=["GET"])
def available_dogs():
    pets = get_all_pets()
    return render_template('available_dogs.html', title='test title', pets=pets)


@app.route("/donate")
def donate():
    return render_template('donate.html', title='Donate')


@app.route("/owner_listings")
def owner_listings():
    return render_template('owner_listings.html', title='Owner Listings')


@app.route("/spotlight_terriers")
def spotlight_terriers():
    return render_template('spotlight_terriers.html', title='Spotlight Terriers')


@app.route("/happy_tails")
def happy_tails():
    return render_template('happy_tails.html', title='Happy Tails')


@app.route("/surrender")
def surrender():
    return render_template('surrender.html', title='Surrender Program')


@app.route("/surrender_form", methods=['GET', 'POST'])
def surrender_form():
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
        send_surrender_applicant_info(
            form, "d-ebfdb4df66d94dd6a97c89dea35fb438")
        send_application_submission_confirmation(
            form.email.data, "texasrussell@test.com", "", "d-21bc2284cfb946ed8f0f5da52af20abf")
        return redirect(url_for('index'))
    return render_template('surrender_form.html', title='Surrender Form', form=form)


@app.route("/surrender_inbox", methods=['GET'])
@login_required(ADMIN)
def surrender_inbox():
    applications = OwnerSurrenderApplication.query.order_by(
        desc(OwnerSurrenderApplication.date_sent)).all()
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
        send_application_submission_confirmation(
            form.email.data, "texasrussell@test.com", "", "d-91e54bb8d19b473ba12dac4dbe04c0d0")
        send_contact_info(form, "d-138e4074de7c49ea9dde946259d49777")
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact Us', form=form)


@app.route("/contact_inbox", methods=['GET'])
@login_required(ADMIN)
def contact_inbox():
    messages = Message.query.order_by(desc(Message.date_sent)).all()
    return render_template(
        'contact_inbox.html', title='Contact Us Inbox', messages=messages
    )


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_pw, urole="admin", access_level=100)
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
            # .get() returns None if key does not exist
            next_page = request.args.get('next')

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
@login_required(ADMIN)
def account():
    return render_template('account.html', title='Account')


@app.route("/admin")
@login_required(ADMIN)
def admin():
    return render_template('admin.html', title='Admin Dashboard')


@app.route("/webmaster")
@login_required(ADMIN)
def webmaster():
    return render_template('webmaster.html', title='Webmaster Dashboard')
