import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import Framework, ProgrammingLanguage


class FrameworkType(DjangoObjectType):
    class Meta:
        model = Framework


class AbstractFramework(graphene.Mutation):
    framework = graphene.Field(FrameworkType)
    message = graphene.String()

    class Arguments:
        name = graphene.String()
        language_id = graphene.Int()
        proficiency = graphene.Int()
        is_primary = graphene.Boolean()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateFramework(AbstractFramework):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        language = get_model_object(model=ProgrammingLanguage, column_name='id', column_value=kwargs.get('language_id'))
        kwargs["user"] = user
        kwargs["language"] = language
        framework = Framework()
        setattr_helper(framework, **kwargs)
        with SaveContextManager(model_instance=framework) as framework:
            return CreateFramework(framework=framework,
                                   message="Successfully created framework record")


class UpdateFramework(AbstractFramework):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        language_id = graphene.Int()
        proficiency = graphene.Int()
        is_primary = graphene.Boolean()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        language = get_model_object(model=ProgrammingLanguage, column_name='id', column_value=kwargs.get('language_id'))
        kwargs["language"] = language
        framework = get_model_object(model=Framework, column_name='id', column_value=kwargs.get('id'))
        if user == framework.user:
            setattr_helper(framework, **kwargs)
            with SaveContextManager(model_instance=framework) as framework:
                return UpdateFramework(framework=framework,
                                       message="Updated framework successfully")
        return UpdateFramework(message="You are not allowed to perform this action")


class DeleteFramework(AbstractFramework):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        framework = get_model_object(model=Framework, column_name='id',
                                     column_value=kwargs.get('id'))
        framework.delete() if framework.user == user else DeleteFramework(
            message="You are not allowed to perform this action")
        return DeleteFramework(message="Framework deleted successfully")


class Mutation:
    create_framework = CreateFramework.Field()
    update_framework = UpdateFramework.Field()
    delete_framework = DeleteFramework.Field()
