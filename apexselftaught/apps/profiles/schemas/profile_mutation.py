from graphene_django import DjangoObjectType
import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

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
        for (key, value) in kwargs.items():
            if key is not None:
                setattr(profile_instance, key, value)
        profile_instance.user = user
        profile_instance.save()
        return CreateProfile(profile=profile_instance)


class UpdateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)
    message = graphene.String()

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
        date_modified = graphene.DateTime(default_value=datetime.now())

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user if info.context.user.is_authenticated else None
        profile_model = Profile.objects.get(user=user)
        if profile_model:
            for (key, value) in kwargs.items():
                if key is not None:
                    setattr(profile_model, key, value)
            profile_model.save()
            return UpdateProfile(profile=profile_model, message="Success")
        return UpdateProfile(profile=profile_model, message="Error")


class Mutation:
    create_profile = CreateProfile.Field()
    update_profile = UpdateProfile.Field()
