
import graphene
from graphene_django import DjangoObjectType
from datetime import datetime
from graphql import GraphQLError
from ..models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            return User.objects.get(pk=id)
        except:
            raise GraphQLError("User does not exist")
