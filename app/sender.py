import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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


if __name__ == "__main__":
    send_application_submission_confirmation(
        "lucassha@oregonstate.edu", "shannonlucas4@gmail.com", "", "d-21bc2284cfb946ed8f0f5da52af20abf")
