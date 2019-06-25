import graphene
from graphene_django import DjangoObjectType
from datetime import datetime
from graphql import GraphQLError
from ..models import User
from .auth_queries import UserType
from apexselftaught.utils.validations import Validation


class RegisterUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        mobile_number = graphene.String()

    def mutate(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        mobile_number = kwargs.get('mobile_number')

        validate_data = Validation().validate_data_fields(
            username, email, mobile_number, password)
        user = User.objects.create_user(**validate_data)

        user.set_password(kwargs.get('password'))
        user.save()
        return RegisterUser(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
