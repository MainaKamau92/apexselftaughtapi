from graphene_django import DjangoObjectType
import graphene
from graphql_jwt.decorators import login_required

from apexselftaught.utils.helpers import setattr_helper
from ..models import Profile
from datetime import datetime


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class CreateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)
    success_message = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        secondary_email = graphene.String()
        user_bio = graphene.String()
        avatar = graphene.String()
        country = graphene.String()
        county = graphene.String()
        industry = graphene.String()
        github = graphene.String()
        website = graphene.String()
        date_created = graphene.DateTime(default_value=datetime.now())

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        profile_instance = Profile()
        if Profile.objects.filter(user=user).exists():
            raise GraphQLError("This User already has an existing profile")
        setattr_helper(profile_instance, **kwargs)
        profile_instance.user = user
        profile_instance.save()
        success = "Profile created successfully"
        return CreateProfile(profile=profile_instance, success_message=success)


class UpdateProfile(CreateProfile, graphene.Mutation):
    profile = graphene.Field(ProfileType)
    message = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        profile_model = Profile.objects.get(user=user)
        if profile_model:
            setattr_helper(profile_model, **kwargs)
            profile_model.save()
            return UpdateProfile(profile=profile_model, message="Successfully updated profile")
        return UpdateProfile(profile=profile_model, message="Could not update profile")


class Mutation:
    update_profile = UpdateProfile.Field()
