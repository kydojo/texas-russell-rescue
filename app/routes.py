
from functools import wraps
from flask import render_template, url_for, redirect, flash, request
from app.forms import RegistrationForm, LoginForm, ContactUsForm, OwnerSurrenderForm, AdoptionApplicationForm, HappyTailsForm, VolunteerForm
from app import app, db, bcrypt, login_manager
from app.pets import get_pets, get_all_pets
from app.sender import send_application_submission_confirmation, send_contact_info, send_surrender_applicant_info, send_adoption_application
from app.models import User, HappyTailsPost, Message, OwnerSurrenderApplication, AdoptionApplication, VolunteerApplication
from flask_login import login_user, logout_user, current_user
from sqlalchemy import desc

# Global vars for tiered access levels
WEBMASTER = 500
ADMIN = 100


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


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/volunteer")
def volunteer():
    return render_template('volunteer.html', title='Volunteer')


@app.route("/volunteer_form")
def volunteer_form():
    form = VolunteerForm()
    if form.validate_on_submit():
        application = VolunteerApplication(
            # Section 1 - Your Information:
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

            # Section 2 - How would you like to help? (Check all that apply.)
            foster_home=form.foster_home.data,
            adoption_screen_or_counseling=form.adoption_screen_or_counseling.data,
            transport_dogs=form.transport_dogs.data,
            behavior_counseling=form.behavior_counseling.data,
            fundraising=form.fundraising.data,
            home_visits=form.home_visits.data,
            staff_booths_info_centers=form.staff_booths_info_centers.data, # (table at trials, pet expos, etc.)
            shelter_contact=form.shelter_contact.data,
            web_or_social_media=form.web_or_social_media.data,
            other_role=form.other_role.data,

            # Section 3 - Experience and Schedule:
            volunteer_experience=form.volunteer_experience.data,
            dog_handling_experience=form.dog_handling_experience.data,

            hours_can_volunteer=form.hours_can_volunteer.data,
            schedule_flexibility=form.schedule_flexibility.data,  # For example, if you receive a call in the morning, can you make time during the day to pick up a dog in an emergency situation?  
            availability=form.availability.data,
            ok_call_at_work=form.ok_call_at_work.data,

            # Section 4 - Your Home
            owns_cats=form.owns_cats.data,
            num_cats=form.num_cats.data,
            owns_dogs=form.owns_dogs.data,
            num_dogs=form.num_dogs.data,
            dog_descriptions=form.dog_descriptions.data,
            pets_spayed_neutered=form.pets_spayed_neutered.data,

            is_breeder=form.is_breeder.data,
            litters_per_year=form.litters_per_year.data,

            children_in_home=form.children_in_home.data,
            children_dog_contact_frequency=form.children_dog_contact_frequency.data,
            children_age=form.children_age.data,

            # # Section 5 - Your Vet
            has_regular_vet=form.has_regular_vet.data,
            vet_clinic_name=form.vet_clinic_name.data,
            doctor_name=form.doctor_name.data,
            vet_street_address=form.vet_street_address.data,
            vet_city=form.vet_city.data,
            vet_state=form.vet_state.data,
            vet_zip=form.vet_zip.data,
            vet_phone=form.vet_phone.data,

            # Section 6 - Your Opinions/Preferences
            feelings_about_rescue=form.feelings_about_rescue.data,
            euthanasia_feelings=form.euthanasia_feelings.data,
            euthanasia_circumstances=form.euthanasia_circumstances.data,

            # Are you willing to handle and/or evaluate the following? (check all that apply)*
            sick_dogs=form.sick_dogs.data,
            pregnant_females=form.pregnant_females.data,
            unstable_dogs=form.unstable_dogs.data,
            females_in_heat=form.females_in_heat.data,
            dog_aggressive_dogs=form.dog_aggressive_dogs.data,
            intact_dogs=form.intact_dogs.data,
            no_children_dogs=form.no_children_dogs.data,
            geriatric_dogs=form.geriatric_dogs.data,
            dogs_not_potty_trained=form.dogs_not_potty_trained.data,
            hyper_dogs=form.hyper_dogs.data,
            escape_artists=form.escape_artists.data,
            other_handling_preferences=form.other_handling_preferences.data,

            # Section 7 - References
            first_reference_name=form.first_reference_name.data,
            first_reference_relationship=form.first_reference_relationship.data,
            first_reference_phone=form.first_reference_phone.data,
            second_reference_name=form.second_reference_name.data,
            second_reference_relationship=form.second_reference_relationship.data,
            second_reference_phone=form.second_reference_phone.data,
            additional_comments=form.additional_comments.data,

            # Section 8 - Volunteer Waiver
            volunteer_waiver_agreement=form.volunteer_waiver_agreement.data,

            # Section 9 - Foster Home Application
            # Please skip Section 9 and 10 if you are not applying to foster.
            has_crate=form.has_crate.data,
            has_fenced_yard=form.has_fenced_yard.data,
            has_kennel=form.has_kennel.data,
            fence_kennel_description=form.fence_kennel_description.data,
            housing_type=form.housing_type.data,
            housing_type_if_other=form.housing_type_if_other.data,
            rent_or_own=form.rent_or_own.data,
            how_long_at_address=form.how_long_at_address.data,

            # Where will the foster dog be housed during the day (check all that apply)?
            inside_crated=form.inside_crated.data,
            outdoors_loose=form.outdoors_loose.data,
            inside_loose=form.inside_loose.data,
            outdoors_kenneled=form.outdoors_kenneled.data,
            garage=form.garage.data,
            barn=form.barn.data,
            other_dog_housing=form.other_dog_housing.data,

            # Where will the foster dog be kept when unsupervised or when left alone? (Check all that apply)
            unsupervised_inside_crated=form.unsupervised_inside_crated.data,
            unsupervised_outdoors_loose=form.unsupervised_outdoors_loose.data,
            unsupervised_inside_loose=form.unsupervised_inside_loose.data,
            unsupervised_outdoors_kenneled=form.unsupervised_outdoors_kenneled.data,
            unsupervised_garage=form.unsupervised_garage.data,
            unsupervised_barn=form.unsupervised_barn.data,
            unsupervised_other=form.unsupervised_other.data,

            # Where will the foster dog sleep? (Check all that apply)
            sleep_inside_crated=form.sleep_inside_crated.data,
            sleep_outdoors_loose=form.sleep_outdoors_loose.data,
            sleep_inside_loose=form.sleep_inside_loose.data,
            sleep_outdoors_kenneled=form.sleep_outdoors_kenneled.data,
            sleep_garage=form.sleep_garage.data,
            sleep_barn=form.sleep_barn.data,
            sleep_other=form.sleep_other.data,

            knows_lack_of_med_history=form.knows_lack_of_med_history.data,
            accepts_liability=form.accepts_liability.data,
            will_travel_to_pick_up_foster=form.will_travel_to_pick_up_foster.data,
            distance_willing_to_travel=form.distance_willing_to_travel.data,
            travel_or_open_home_for_adopters=form.travel_or_open_home_for_adopters.data,
            aware_foster_is_indefinite=form.aware_foster_is_indefinite.data,
            will_take_to_vet_if_needed=form.will_take_to_vet_if_needed.data,

            # Section 10 - Foster Home Application Waiver
            foster_waiver_agreement=form.foster_waiver_agreement.data
        )
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('volunteer_form.html', title='Volunteer Form', form=form)


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
        send_adoption_application(
            form, "d-eb6b1f21737c4b0fa5b014bcf99e1d80")
        send_application_submission_confirmation(
            form.email.data, "texasrussell@test.com", "", "d-21bc2284cfb946ed8f0f5da52af20abf")
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


@app.route("/happy_tails", methods=['GET'])
def happy_tails():
    posts = HappyTailsPost.query.order_by(
        desc(HappyTailsPost.date_posted)).all()
    return render_template('happy_tails.html', title='Happy Tails', posts=posts)


@app.route("/happy_tails_post", methods=['GET', 'POST'])
@login_required(WEBMASTER)
def happy_tails_post():
    form = HappyTailsForm()
    if form.validate_on_submit():
        post = HappyTailsPost(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('happy_tails'))
    return render_template('happy_tails_post.html', title='New Happy Tails Post', form=form)


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
@login_required(ADMIN)
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(username=form.username.data,
                    email=form.email.data,
                    urole=form.urole.data,
                    access_level=WEBMASTER if form.urole.data == 'WEBMASTER' else ADMIN,
                    password=hashed_pw)

        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/manage_admins", methods=['GET', 'POST'])
@login_required(WEBMASTER)
def manage_admins():
    users = User.query.all()
    return render_template('manage_admins.html', title='Manage Admins', users=users)


@app.route("/manage_admins/<user_id>", methods=['GET', 'POST'])
@login_required(WEBMASTER)
def manage_admin_users(user_id):
    if request.method == 'POST':
        User.query.filter_by(id=user_id).delete()
        print("Deleted user_id: ", user_id)
        users = User.query.all()
        return render_template('manage_admins.html', title='Manage Admins', users=users)


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
