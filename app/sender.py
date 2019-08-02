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


if __name__ == "__main__":
    send_application_submission_confirmation(
        "lucassha@oregonstate.edu", "shannonlucas4@gmail.com", "", "d-21bc2284cfb946ed8f0f5da52af20abf")
