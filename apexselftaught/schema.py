import graphene
from apexselftaught.apps.authentication.schemas import AuthMutation
from apexselftaught.apps.authentication.schemas import AuthQuery


class Query(AuthQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
