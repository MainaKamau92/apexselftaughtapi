import graphene
from apexselftaught.apps.authentication.schemas import AuthMutation
from apexselftaught.apps.authentication.schemas import AuthQuery
from apexselftaught.apps.profiles.schemas import ProfileMutation, ProfileQuery
from apexselftaught.apps.portfolio.schemas import (ProjectMutation, LanguageMutation, TechnicalProficiencyMutation,
                                                   SoftSkillsMutation, CertificationMutation, FrameworkMutation,
                                                   PortfolioQuery)


class Query(AuthQuery, ProfileQuery, PortfolioQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, ProfileMutation, ProjectMutation, LanguageMutation, TechnicalProficiencyMutation,
               SoftSkillsMutation, CertificationMutation, FrameworkMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
