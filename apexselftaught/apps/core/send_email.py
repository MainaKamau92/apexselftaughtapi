import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.template.loader import render_to_string

from apexselftaught.apps.authentication.models import User


def send_confirmation_email(user):
    token = user.token
    email = user.email
    context = {
        'template_type': 'Verify your email',
        'small_text_detail': 'Thank you for '
                             'creating an AST account. '
                             'Please verify your email '
                             'address to set up your account.',
        'email': email,
        'domain': os.getenv("DOMAIN"),
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


def send_password_reset_link(email_resp):
    email = email_resp.get("email")
    token = User.objects.get(email=email).token
    domain = os.getenv("DOMAIN")

    context = {
        'template_type': 'Password Reset',
        'small_text_detail': 'Click link below to reset your password',
        'email': email,
        'domain': domain,
        'token': token,
        'button_text': 'Reset Password'
    }
    msg_html = render_to_string("password_reset.html", context)
    message = Mail(
        from_email="info@apexselftaught.com",
        to_emails=[email],
        subject="Password Reset Request",
        html_content=msg_html
    )
    try:
        sendgrid = SendGridAPIClient(
            os.getenv("SENDGRID_API_KEY")
        )
        sendgrid.send(message=message)
        return "{}/api/v1/password-reset/{}".format(domain, token)
    except Exception as e:
        print(str(e))
