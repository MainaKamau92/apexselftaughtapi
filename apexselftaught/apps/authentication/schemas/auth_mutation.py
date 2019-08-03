import graphene
from apexselftaught.utils.send_email import send_confirmation_email, password_reset_link
from ..models import User
from .auth_queries import UserType
from apexselftaught.utils.validations import Validation
from django.db import IntegrityError
from django.contrib.auth import authenticate
from graphql_jwt.utils import jwt_encode, jwt_payload


class RegisterUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        mobile_number = graphene.String()

    errors = graphene.String()

    def mutate(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        mobile_number = kwargs.get('mobile_number')

        validate_data = Validation().validate_data_fields(
            username, email, mobile_number, password)
        try:
            user = User.objects.create_user(**validate_data)
            user.set_password(kwargs.get('password'))
            user.save()
            send_confirmation_email(email, username)
            return RegisterUser(user=user)
        except IntegrityError as e:
            return RegisterUser(errors=str(e))


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)
    errors = graphene.String()
    token = graphene.String()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, **kwargs):
        email = Validation.validate_email(email=kwargs.get('email'))
        password = Validation.validate_password(password=kwargs.get('password'))

        user = authenticate(username=email, password=password)
        error_message = 'Invalid login credentials'
        if user:
            payload = jwt_payload(user)
            token = jwt_encode(payload)
            return LoginUser(token=token)
        return LoginUser(errors=error_message)


class RequestRequestPassword(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    error = graphene.String()
    success = graphene.String()
    link = graphene.String()

    def mutate(self, info, email):
        valid_email = Validation.validate_email(email)
        user = User.objects.get(email=valid_email)
        if user:
            reset_link = password_reset_link(valid_email, user.username)
            return RequestRequestPassword(success='Email sent', link=reset_link)
        return RequestRequestPassword(error='Invalid email')


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    request_password_reset = RequestRequestPassword.Field()
