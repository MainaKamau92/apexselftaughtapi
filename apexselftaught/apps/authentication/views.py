from decouple import config
import jwt
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from apexselftaught.apps.authentication.models import User
from apexselftaught.utils.validations import Validation

REDIRECT_LINK = settings.REDIRECT_LINK

secret = config("SECRET")


def activate_account(request, token):
    link = None
    username = jwt.decode(token, secret, algorithms=['HS256'])["user"]
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


class PasswordResetView(View):

    def put(self, request, token):
        data = json.loads(request.body)
        username = jwt.decode(token, secret, algorithms=['HS256'])["user"]
        user = User.objects.get(username=username)
        if username:
            try:
                new_password = data.get('user').get('password')
                valid_password = Validation.validate_password(new_password)
                user.set_password(valid_password)
                user.save()
                status = 200
                return JsonResponse({"response": "Success"}, status=status)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)

        return JsonResponse({"fail": "Invalid token"}, status=400)
