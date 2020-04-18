from graphene_django import DjangoObjectType
import graphene
from graphql_jwt.decorators import login_required
from apexselftaught.utils.database import SaveContextManager, get_model_object
from apexselftaught.utils.helpers import setattr_helper
from ..models import Profile
from datetime import datetime


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class CreateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        secondary_email = graphene.String()
        user_bio = graphene.String()
        avatar = graphene.String()
        county = graphene.String()
        industry = graphene.String()
        github = graphene.String()
        website = graphene.String()
        date_created = graphene.DateTime(default_value=datetime.now())

    @login_required
    def mutate(self, info, **kwargs):
        pass


class UpdateProfile(CreateProfile, graphene.Mutation):
    profile = graphene.Field(ProfileType)
    message = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        profile_model = get_model_object(model=Profile, column_name='user', column_value=user)
        if profile_model:
            setattr_helper(profile_model, **kwargs)
            with SaveContextManager(profile_model) as profile:
                return UpdateProfile(profile=profile, message="Successfully updated profile")
        return UpdateProfile(profile=profile_model, message="Could not update profile")


class Mutation:
    update_profile = UpdateProfile.Field()
