import graphene
from graphql import GraphQLError
from ..models import (ProgrammingLanguageSpecifics, Certification, Project, SoftSKillsProficiency,
                      TechnicalEngineeringProficiency, Framework)
from .language_mutations import LanguageType
from .certification_mutations import CertificationType
from .project_mutations import ProjectType
from .soft_skills_mutations import SoftSKillsProficiencyType
from .technical_mutations import TechnicalProficiencyType
from graphql_jwt.decorators import login_required


class PortfolioUnion(graphene.Union):
    class Meta:
        types = (
            LanguageType, CertificationType, ProjectType, SoftSKillsProficiencyType, TechnicalEngineeringProficiency)


class Query(graphene.ObjectType):
    id = graphene.Int(required=True)
    # language_specifics = graphene.Field(LanguageType)
    # certification = graphene.Field(CertificationType)
    # project = graphene.Field(ProjectType)
    # soft_skills = graphene.Field(SoftSKillsProficiencyType)
    # technical_proficiency = graphene.Field(TechnicalProficiencyType)
    portfolio = graphene.List(PortfolioUnion)

    @login_required
    def resolve_portfolio(self, info, **kwargs):
        # id = kwargs.get('id')
        language_specifics = ProgrammingLanguageSpecifics.objects.all()
        certification = Certification.objects.all()
        project = Project.objects.all()
        soft_skills = SoftSKillsProficiency.objects.all()
        technical = TechnicalEngineeringProficiency.objects.all()
        portfolio = [language_specifics, certification, project, soft_skills, technical]
        return portfolio

    # @login_required
    # def resolve_profile(self, info, **kwargs):
    #     profile_id = kwargs.get('id')
    #     try:
    #         return Profile.objects.get(pk=profile_id)
    #     except Exception:
    #         raise GraphQLError("Profile does not exist")
    #
    # @login_required
    # def resolve_me(self, info, **kwargs):
    #     logged_in_user_profile = info.context.user if info.context.user.is_authenticated else None
    #     return Profile.objects.get(user=logged_in_user_profile)
