import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import TechnicalEngineeringProficiency


class TechnicalProficiencyType(DjangoObjectType):
    class Meta:
        model = TechnicalEngineeringProficiency


class AbstractTechnicalProficiencyClass(graphene.Mutation):
    technical_proficiency = graphene.Field(TechnicalProficiencyType)
    message = graphene.String()

    class Arguments:
        algorithms_proficiency = graphene.Int()
        backend_testing_proficiency = graphene.Int()
        frontend_testing_proficiency = graphene.Int()
        design_patterns_proficiency = graphene.Int()
        data_structure_proficiency = graphene.Int()
        object_oriented_programming_proficiency = graphene.Int()
        ui_ux_proficiency = graphene.Int()
        git_proficiency = graphene.Int()
        databases_proficiency = graphene.Int()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateTechnicalProficiency(AbstractTechnicalProficiencyClass):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        kwargs["user"] = user
        technical_proficiency_instance = TechnicalEngineeringProficiency()
        setattr_helper(technical_proficiency_instance, **kwargs)
        with SaveContextManager(model_instance=technical_proficiency_instance) as technical_proficiency:
            return CreateTechnicalProficiency(technical_proficiency=technical_proficiency,
                                              message="Successfully created technical proficiency record")


class UpdateTechnicalProficiency(AbstractTechnicalProficiencyClass):
    class Arguments:
        id = graphene.Int(required=True)
        algorithms_proficiency = graphene.Int()
        backend_testing_proficiency = graphene.Int()
        frontend_testing_proficiency = graphene.Int()
        design_patterns_proficiency = graphene.Int()
        data_structure_proficiency = graphene.Int()
        object_oriented_programming_proficiency = graphene.Int()
        ui_ux_proficiency = graphene.Int()
        git_proficiency = graphene.Int()
        databases_proficiency = graphene.Int()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        technical_proficiency = get_model_object(model=TechnicalEngineeringProficiency, column_name='id',
                                                 column_value=kwargs.get('id'))
        if user == technical_proficiency.user:
            setattr_helper(technical_proficiency, **kwargs)
            with SaveContextManager(model_instance=technical_proficiency) as technical_proficiency:
                return UpdateTechnicalProficiency(technical_proficiency=technical_proficiency,
                                                  message="Updated proficiency successfully")
        return UpdateTechnicalProficiency(message="You are not allowed to perform this action")


class DeleteTechnicalProficiency(AbstractTechnicalProficiencyClass):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        technical_proficiency = get_model_object(model=TechnicalEngineeringProficiency, column_name='id',
                                                 column_value=kwargs.get('id'))
        technical_proficiency.delete() if technical_proficiency.user == user else DeleteTechnicalProficiency(
            message="You are not allowed to perform this action")
        return DeleteTechnicalProficiency(message="Proficiency deleted successfully")


class Mutation:
    create_technical_proficiency = CreateTechnicalProficiency.Field()
    update_technical_proficiency = UpdateTechnicalProficiency.Field()
    delete_technical_proficiency = DeleteTechnicalProficiency.Field()
