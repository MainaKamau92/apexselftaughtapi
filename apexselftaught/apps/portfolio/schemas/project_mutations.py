import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class AbstractProjectClass(graphene.Mutation):
    project = graphene.Field(ProjectType)
    message = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        link = graphene.String()
        description = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        pass


class CreateProject(AbstractProjectClass):
    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        kwargs["user"] = user
        project_instance = Project()
        setattr_helper(project_instance, **kwargs)
        with SaveContextManager(model_instance=project_instance) as project:
            return CreateProject(project=project, message="Successfully created project")


class UpdateProject(AbstractProjectClass):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        link = graphene.String()
        description = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        project = get_model_object(model=Project, column_name='id', column_value=kwargs.get('id'))
        if user == project.user:
            setattr_helper(project, **kwargs)
            with SaveContextManager(model_instance=project) as project:
                return UpdateProject(project=project, message="Updated project successfully")
        return UpdateProject(message="You are not the owner of this project")


class DeleteProject(AbstractProjectClass):
    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        project = get_model_object(model=Project, column_name='id', column_value=kwargs.get('id'))
        project.delete() if project.user == user else DeleteProject(message="You don't own this project")
        return DeleteProject(message="Project deleted succesfully")


class Mutation:
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
