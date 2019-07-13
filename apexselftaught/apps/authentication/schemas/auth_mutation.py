import graphene
from apexselftaught.utils.generate_token import generate_web_token
from apexselftaught.utils.send_email import send_confirmation_email
from ..models import User
from .auth_queries import UserType
from apexselftaught.utils.validations import Validation
from django.db import IntegrityError
from django.contrib.auth import authenticate


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
    error = graphene.String()
    token = graphene.String()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, **kwargs):
        email = Validation.validate_email(email=kwargs.get('email'))
        password = Validation.validate_password(password=kwargs.get('password'))

        user = authenticate(username=email, password=password)
        token = generate_web_token(user.username)

        if user:
            return LoginUser(token=token)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
