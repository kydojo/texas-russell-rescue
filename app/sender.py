import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# trr_volunteers = [
#     ('heather-01@hotmail.com', 'Vol1'),
#     ('jolleyjames@sbcglobal.net', 'Vol2'),
#     ('y2alphadog@gvec.net', 'Vol3')
# ]

trr_volunteers = [
    ('shannonlucas4@gmail.com', 'shannon'),
    ('lucassha@oregonstate.edu', 'shannon')
]


def send_application_submission_confirmation(to_email, from_email, subject, template_id):
    """
    send a generic response email to the applicant
    """
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject
    )
    message.template_id = template_id

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print('could not send')
        print(e.message)


def send_contact_info(contact, template_id):
    """
    send texas russell volunteers the info submitting in the contact form
    """
    message = Mail(
        from_email='shannonlucas4@gmail.com',
        to_emails=trr_volunteers
    )
    message.reply_to = contact.email.data
    message.dynamic_template_data = {
        'name': contact.name.data,
        'email': contact.email.data,
        'phone': contact.phone.data,
        'city': contact.city.data,
        'state': contact.state.data,
        'subject': contact.subject.data,
        'content': contact.content.data
    }
    message.template_id = template_id

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print('could not send')
        print(e.message)


def send_surrender_applicant_info(contact, template_id):
    """
    send form information from /owner_listing_application
    """
    message = Mail(
        from_email='shannonlucas4@gmail.com',
        to_emails=trr_volunteers
    )
    message.reply_to = contact.email.data
    message.dynamic_template_data = {
        'first_name': contact.first_name.data,
        'last_name': contact.last_name.data,
        'email': contact.email.data,
        'phone': contact.phone.data,
        'address': contact.address.data,
        'city': contact.city.data,
        'state': contact.state.data,
        'dog_origin': contact.dog_origin.data,
        'spayed_or_neutered': contact.spayed_or_neutered.data,
        'vaccines_current': contact.vaccines_current.data,
        'heartworm_meds_current': contact.heartworm_meds_current.data,
        'why_rehoming': contact.why_rehoming.data,
        'dog_friendly': contact.dog_friendly.data,
        'cat_friendly': contact.cat_friendly.data,
        'people_friendly': contact.people_friendly.data,
        'training': contact.training.data,
        'leash_behavior': contact.leash_behavior.data,
        'car_behavior': contact.car_behavior.data,
        'general_health': contact.general_health.data,
        'potty_trained': contact.potty_trained.data,
        'home_alone_behavior': contact.home_alone_behavior.data,
        'can_remain_home_until_adopted': contact.can_remain_home_until_adopted.data,
        'other_info': contact.other_info.data
    }
    message.template_id = template_id

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print('could not send')
        print(e.message)


def send_adoption_application(contact, template_id):
    """
    send form information from /owner_listing_application
    """
    message = Mail(
        from_email='shannonlucas4@gmail.com',
        to_emails=trr_volunteers
    )
    message.reply_to = contact.email.data
    message.dynamic_template_data = {
        'terrier_name': contact.terrier_name.data,
        'male_female': contact.male_female.data,
        'dog_age': contact.dog_age.data,
        'willing_to_consider_alternative': contact.willing_to_consider_alternative.data,
        'first_name': contact.first_name.data,
        'last_name': contact.last_name.data,
        'email': contact.email.data,
        'home_phone': contact.home_phone.data,
        'cell_phone': contact.cell_phone.data,
        'work_phone': contact.work_phone.data,
        'best_time_to_call': contact.best_time_to_call.data,
        'street_address': contact.street_address.data,
        'city': contact.city.data,
        'state': contact.state.data,
        'zip_code': contact.zip_code.data,
        'occupation': contact.occupation.data,
        'when_able_to_take_posession': contact.when_able_to_take_posession.data,
        'how_far_willing_to_travel': contact.how_far_willing_to_travel.data,
        'housing_type': contact.housing_type.data,
        'housing_type_if_other': contact.housing_type_if_other.data,
        'rent_or_own': contact.rent_or_own.data,
        'landlord_permission': contact.landlord_permission.data,
        'landlord_name': contact.landlord_name.data,
        'landlord_phone': contact.landlord_phone.data,
        'how_long_at_address': contact.how_long_at_address.data,
        'has_fenced_yard': contact.has_fenced_yard.data,
        'has_kennel_run': contact.has_kennel_run.data,
        'fence_kennel_description': contact.fence_kennel_description.data,
        'if_none_how_handle_dog_needs': contact.if_none_how_handle_dog_needs.data,
        'has_dog_crate': contact.has_dog_crate.data,
        'num_adults_in_household': contact.num_adults_in_household.data,
        'adults_age': contact.adults_age.data,
        'num_children_in_household': contact.num_children_in_household.data,
        'children_age': contact.children_age.data,
        'planning_to_have_children': contact.planning_to_have_children.data,
        'animal_allergies': contact.animal_allergies.data,
        'hours_terrier_must_be_alone': contact.hours_terrier_must_be_alone.data,
        'household_visitors': contact.household_visitors.data,
        'lifestyle': contact.lifestyle.data,
        'own_other_dogs': contact.own_other_dogs.data,
        'other_dogs_spayed_neutered': contact.other_dogs_spayed_neutered.data,
        'breed_size_gender_of_other_dogs': contact.breed_size_gender_of_other_dogs.data,
        'own_cats': contact.own_cats.data,
        'how_many_cats': contact.how_many_cats.data,
        'own_other_animals': contact.own_other_animals.data,
        'other_animals_description': contact.other_animals_description.data,
        'num_dogs_owned_past_five_years': contact.num_dogs_owned_past_five_years.data,
        'status_of_other_dogs_owned': contact.status_of_other_dogs_owned.data,
        'previously_owned_jrt': contact.previously_owned_jrt.data,
        'why_choose_jrt': contact.why_choose_jrt.data,
        'jrt_breed_purpose': contact.jrt_breed_purpose.data,
        'planned_activities_with_jrt': contact.planned_activities_with_jrt.data,
        'indoors_or_outdoors': contact.indoors_or_outdoors.data,
        'where_will_sleep': contact.where_will_sleep.data,
        'has_regular_vet': contact.has_regular_vet.data,
        'vet_clinic_name': contact.vet_clinic_name.data,
        'doctor_name': contact.doctor_name.data,
        'vet_street_address': contact.vet_street_address.data,
        'vet_city': contact.vet_city.data,
        'vet_state': contact.vet_state.data,
        'vet_zip': contact.vet_zip.data,
        'vet_phone': contact.vet_phone.data,
        'last_vet_visit_date': contact.last_vet_visit_date.data,
        'how_learned_about_us': contact.how_learned_about_us.data,
        'if_other': contact.if_other.data,
        'reference_name': contact.reference_name.data,
        'reference_relationship': contact.reference_relationship.data,
        'reference_phone': contact.reference_phone.data,
        'additional_comments': contact.additional_comments.data
    }
    message.template_id = template_id

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print('could not send')
        print(e.message)


if __name__ == "__main__":
    send_application_submission_confirmation(
        "lucassha@oregonstate.edu", "shannonlucas4@gmail.com", "", "d-21bc2284cfb946ed8f0f5da52af20abf")
