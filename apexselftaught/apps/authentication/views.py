from decouple import config
import jwt

from django.conf import settings
from django.shortcuts import redirect, render

from apexselftaught.apps.authentication.models import User

REDIRECT_LINK = settings.REDIRECT_LINK


def activate_account(request, token):
    link = None
    secret = config("SECRET")
    username = jwt.decode(token, secret, algorithms=['HS256'])["user"]
    print(username)
    user = User.objects.get(username=username)
    if username:
        user.is_verified = True
        user.save()
        return redirect(f'{REDIRECT_LINK}/apexselftaught/')

    if not username:
        if user.is_verified:
            message = "account_verification"
            link = f'{REDIRECT_LINK}/apexselftaught/'
            status = 409  # conflict
        else:  # token may be expired
            message = "account_verification_fail"
            status = 401  # unauthorised
    if username:  # token tampered with/corrupted
        # link tampered with
        message = "verification_link_corrupt"
        status = 401
    context = {
        'template_type': 'Email Verification Failed',
        'small_text_detail': message,
        'link': link
    }
    return render(
        request, 'verification.html',
        context=context, status=status)
