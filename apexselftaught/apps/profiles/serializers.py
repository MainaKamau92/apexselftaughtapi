from rest_framework import serializers
from apexselftaught.apps.profiles.models import Profile
from apexselftaught.apps.authentication.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "first_name", "middle_name", "last_name", "secondary_email", "user_bio", "avatar",
                  "county", "industry", "github", "linkendin", "resume", "website", "user")

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.middle_name = validated_data.get("middle_name", instance.middle_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.secondary_email = validated_data.get("secondary_email", instance.secondary_email)
        instance.user_bio = validated_data.get("user_bio", instance.user_bio)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.county = validated_data.get("county", instance.county)
        instance.industry = validated_data.get("industry", instance.industry)
        instance.github = validated_data.get("github", instance.github)
        instance.linkendin = validated_data.get("linkendin", instance.linkendin)
        instance.resume = validated_data.get("resume", instance.resume)
        instance.website = validated_data.get("website", instance.website)
        instance.save()
        return instance
