import graphene
from apexselftaught.apps.authentication.schemas import AuthMutation
from apexselftaught.apps.authentication.schemas import AuthQuery
from apexselftaught.apps.profiles.schemas import ProfileMutation, ProfileQuery


class Query(AuthQuery, ProfileQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, ProfileMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
