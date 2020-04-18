import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import ProgrammingLanguageSpecifics, ProgrammingLanguage


class LanguageType(DjangoObjectType):
    class Meta:
        model = ProgrammingLanguageSpecifics


class AbstractLanguageClass(graphene.Mutation):
    language_specifics = graphene.Field(LanguageType)
    message = graphene.String()

    class Arguments:
        language = graphene.Int(required=True)
        proficiency = graphene.Int(required=True)
        is_primary = graphene.Boolean()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateLanguage(AbstractLanguageClass):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        language = get_model_object(model=ProgrammingLanguage, column_name='id', column_value=kwargs.get('language'))
        kwargs["user"] = user
        kwargs["language"] = language
        language_instance = ProgrammingLanguageSpecifics()
        setattr_helper(language_instance, **kwargs)
        with SaveContextManager(model_instance=language_instance) as language:
            return CreateLanguage(language=language, message="Successfully created language")


class UpdateLanguage(AbstractLanguageClass):
    class Arguments:
        id = graphene.Int(required=True)
        language = graphene.Int(required=True)
        proficiency = graphene.Int(required=True)
        is_primary = graphene.Boolean()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        language = get_model_object(model=ProgrammingLanguage, column_name='id', column_value=kwargs.get('language'))
        language_specifics = get_model_object(model=ProgrammingLanguageSpecifics, column_name='id',
                                              column_value=kwargs.get('id'))
        if user == language_specifics.user:
            setattr_helper(language_specifics, **kwargs)
            language_specifics.language = language
            with SaveContextManager(model_instance=language_specifics) as language_specifics:
                return UpdateLanguage(language_specifics=language_specifics, message="Updated language successfully")
        return UpdateLanguage(message="You are not allowed to perform this action")


class DeleteLanguage(AbstractLanguageClass):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        language_specifics = get_model_object(model=ProgrammingLanguageSpecifics, column_name='id',
                                              column_value=kwargs.get('id'))
        language_specifics.delete() if language_specifics.user == user else DeleteLanguage(
            message="You are not allowed to perform this action")
        return DeleteLanguage(message="Language deleted succesfully")


class Mutation:
    create_language = CreateLanguage.Field()
    update_language = UpdateLanguage.Field()
    delete_language = DeleteLanguage.Field()
