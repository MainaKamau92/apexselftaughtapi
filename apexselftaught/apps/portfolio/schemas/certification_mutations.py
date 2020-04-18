import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import Certification


class CertificationType(DjangoObjectType):
    class Meta:
        model = Certification


class AbstractCertification(graphene.Mutation):
    certification = graphene.Field(CertificationType)
    message = graphene.String()

    class Arguments:
        title = graphene.String()
        institution = graphene.String()
        date_issued = graphene.Date()
        expiration_date = graphene.Date()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateCertification(AbstractCertification):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        kwargs["user"] = user
        certification = Certification()
        setattr_helper(certification, **kwargs)
        with SaveContextManager(model_instance=certification) as certification:
            return CreateCertification(certification=certification,
                                       message="Successfully created certification record")


class UpdateCertification(AbstractCertification):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        institution = graphene.String()
        date_issued = graphene.Date()
        expiration_date = graphene.Date()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        certification = get_model_object(model=Certification, column_name='id',
                                         column_value=kwargs.get('id'))
        if user == certification.user:
            setattr_helper(certification, **kwargs)
            with SaveContextManager(model_instance=certification) as certification:
                return UpdateCertification(certification=certification,
                                           message="Updated certification successfully")
        return UpdateCertification(message="You are not allowed to perform this action")


class DeleteCertification(AbstractCertification):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        certification = get_model_object(model=Certification, column_name='id',
                                         column_value=kwargs.get('id'))
        certification.delete() if certification.user == user else DeleteCertification(
            message="You are not allowed to perform this action")
        return DeleteCertification(message="Certification deleted successfully")


class Mutation:
    create_certification = CreateCertification.Field()
    update_certification = UpdateCertification.Field()
    delete_certification = DeleteCertification.Field()
