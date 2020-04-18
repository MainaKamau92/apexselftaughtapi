import graphene
from apexselftaught.utils.send_email import send_confirmation_email, \
    password_reset_link
from ..models import User
from .auth_queries import UserType
from apexselftaught.utils.validations import Validation
from django.db import IntegrityError
from django.contrib.auth import authenticate
from apexselftaught.utils.generate_token import generate_login_token


class RegisterUser(graphene.Mutation):
    user = graphene.Field(UserType)
    message = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        recruiter = graphene.Boolean(required=True)

    def mutate(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        recruiter = kwargs.get('recruiter')
        password = kwargs.get('password')
        mobile_number = kwargs.get('mobile_number')

        validate_data = Validation().validate_data_fields(
            username, email, mobile_number, password)
        try:
            user = User.objects.create_user(**validate_data)
            user.is_recruiter = recruiter
            user.set_password(kwargs.get('password'))
            user.save()
            message = "User created successfully, verification email sent to {}".format(email)
            send_confirmation_email(email, username)
            return RegisterUser(user=user, message=message)
        except IntegrityError as e:
            return RegisterUser(message=str(e))


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)
    message = graphene.String()
    token = graphene.String()
    verification_prompt = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = Validation.validate_email(email=kwargs.get('email'))
        password = Validation.validate_password(
            password=kwargs.get('password'))

        user = authenticate(username=email, password=password)

        error_message = 'Invalid login credentials'
        success_message = "You logged in successfully."
        verification_error = 'Your email is not verified'
        if user:
            if user.is_verified:
                token = generate_login_token(user)
                return LoginUser(token=token, message=success_message)
            return LoginUser(verification_prompt=verification_error)
        return LoginUser(message=error_message)


class RequestPasswordReset(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    error = graphene.String()
    success = graphene.String()
    link = graphene.String()

    def mutate(self, info, email):
        valid_email = Validation.validate_email(email)
        user = User.objects.filter(email=valid_email).exists()
        if user:
            reset_link = password_reset_link(valid_email, user.username)
            return RequestPasswordReset(
                success='Email sent with password reset details',
                link=reset_link)
        return RequestPasswordReset(
            error='That email does not have a registered account,'
                  'Sign up for a new account.')


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    request_password_reset = RequestPasswordReset.Field()
