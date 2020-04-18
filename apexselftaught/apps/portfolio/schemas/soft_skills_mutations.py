import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import SoftSKillsProficiency


class SoftSKillsProficiencyType(DjangoObjectType):
    class Meta:
        model = SoftSKillsProficiency


class AbstractSoftSKillsProficiency(graphene.Mutation):
    soft_skills_proficiency = graphene.Field(SoftSKillsProficiencyType)
    message = graphene.String()

    class Arguments:
        team_work = graphene.Int()
        logic_reason = graphene.Int()
        communication_proficiency = graphene.Int()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateSoftSKillsProficiency(AbstractSoftSKillsProficiency):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        kwargs["user"] = user
        soft_skills_proficiency = SoftSKillsProficiency()
        setattr_helper(soft_skills_proficiency, **kwargs)
        with SaveContextManager(model_instance=soft_skills_proficiency) as soft_skills_proficiency:
            return CreateSoftSKillsProficiency(soft_skills_proficiency=soft_skills_proficiency,
                                               message="Successfully created soft skill proficiency record")


class UpdateSoftSKillsProficiency(AbstractSoftSKillsProficiency):
    class Arguments:
        id = graphene.Int(required=True)
        team_work = graphene.Int()
        logic_reason = graphene.Int()
        communication_proficiency = graphene.Int()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        soft_skill = get_model_object(model=SoftSKillsProficiency, column_name='id',
                                      column_value=kwargs.get('id'))
        if user == soft_skill.user:
            setattr_helper(soft_skill, **kwargs)
            with SaveContextManager(model_instance=soft_skill) as soft_skill:
                return UpdateSoftSKillsProficiency(soft_skills_proficiency=soft_skill,
                                                   message="Updated proficiency successfully")
        return UpdateSoftSKillsProficiency(message="You are not allowed to perform this action")


class DeleteSoftSKillsProficiency(AbstractSoftSKillsProficiency):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        soft_skill = get_model_object(model=SoftSKillsProficiency, column_name='id',
                                      column_value=kwargs.get('id'))
        soft_skill.delete() if soft_skill.user == user else DeleteSoftSKillsProficiency(
            message="You are not allowed to perform this action")
        return DeleteSoftSKillsProficiency(message="Proficiency deleted successfully")


class Mutation:
    create_soft_skills_proficiency = CreateSoftSKillsProficiency.Field()
    update_soft_skills_proficiency = UpdateSoftSKillsProficiency.Field()
    delete_soft_skills_proficiency = DeleteSoftSKillsProficiency.Field()
