# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string

from apexselftaught.utils.generate_token import generate_web_token


def send_confirmation_email(email, user):
    token = generate_web_token(user)
    context = {
        'template_type': 'Verify your email',
        'small_text_detail': 'Thank you for '
                             'creating an AST account. '
                             'Please verify your email '
                             'address to set up your account.',
        'email': email,
        'domain': config("DOMAIN"),
        'token': token,
    }
    msg_html = render_to_string('email.html', context)
    message = Mail(
        from_email='info@apexselftaught.com',
        to_emails=[email],
        subject='Account activation',
        html_content=msg_html)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(str(e))
