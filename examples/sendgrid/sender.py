# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='shannonlucas4@gmail.com',
    to_emails='lucassha@oregonstate.edu',
    subject='Submission confirmation',
    html_content="<h3>Thanks for your submission! We'll be in touch soon.</h3> <div>And test here</div>")
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print('accepted')
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print('could not send')
    print(e.message)
