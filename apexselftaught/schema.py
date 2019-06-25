import graphene
import graphql_jwt
from apexselftaught.apps.authentication.schemas import AuthMutation
from apexselftaught.apps.authentication.schemas import AuthQuery


class Query(AuthQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    loginUser = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
