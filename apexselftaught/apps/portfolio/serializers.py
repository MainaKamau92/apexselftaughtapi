from rest_framework import serializers

from apexselftaught.apps.authentication.serializers import UserSerializer
from apexselftaught.apps.portfolio.models import Project, ProgrammingLanguage, ProgrammingLanguageSpecifics, \
    TechnicalEngineeringProficiency, Framework, SoftSKillsProficiency, Certification


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'link', 'description', 'user']

    def create(self, validated_data):
        user = self.context.get('user', None)
        if user is None:
            raise serializers.ValidationError("User field required.")
        return Project.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.link = validated_data.get('link', instance.link)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ['id', 'name']


class ProgrammingLanguageSpecificsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = ProgrammingLanguageSerializer(read_only=True)

    class Meta:
        model = ProgrammingLanguageSpecifics
        fields = ['id', 'language', 'proficiency', 'is_primary', 'user']

    def create(self, validated_data):
        user, language = self.context.get('user'), self.context.get('language')
        return ProgrammingLanguageSpecifics.objects.create(user=user, language=language, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.language = self.context.get('language', instance.language)
        instance.proficiency = validated_data.get('proficiency', instance.proficiency)
        instance.is_primary = validated_data.get('is_primary', instance.is_primary)
        instance.save()
        return instance


class TechnicalEngineeringProficiencySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TechnicalEngineeringProficiency
        fields = ['id', 'algorithms_proficiency', 'backend_testing_proficiency',
                  'frontend_testing_proficiency', 'design_patterns_proficiency',
                  'data_structure_proficiency', 'object_oriented_programming_proficiency',
                  'ui_ux_proficiency', 'git_proficiency', 'databases_proficiency', 'user']

    def create(self, validated_data):
        user = self.context.get('user', None)
        if user is None:
            raise serializers.ValidationError("User field is required.")
        return TechnicalEngineeringProficiency.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.algorithms_proficiency = validated_data.get('algorithms_proficiency', instance.algorithms_proficiency)
        instance.backend_testing_proficiency = validated_data.get('backend_testing_proficiency',
                                                                  instance.backend_testing_proficiency)
        instance.frontend_testing_proficiency = validated_data.get('frontend_testing_proficiency',
                                                                   instance.frontend_testing_proficiency)
        instance.design_patterns_proficiency = validated_data.get('design_patterns_proficiency',
                                                                  instance.design_patterns_proficiency)
        instance.data_structure_proficiency = validated_data.get('data_structure_proficiency',
                                                                 instance.data_structure_proficiency)
        instance.object_oriented_programming_proficiency = validated_data.get('object_oriented_programming_proficiency',
                                                                              instance.object_oriented_programming_proficiency)
        instance.ui_ux_proficiency = validated_data.get('ui_ux_proficiency', instance.ui_ux_proficiency)
        instance.git_proficiency = validated_data.get('git_proficiency', instance.git_proficiency)
        instance.databases_proficiency = validated_data.get('databases_proficiency', instance.databases_proficiency)
        instance.save()
        return instance


class FrameworkSerializer(serializers.ModelSerializer):
    language = ProgrammingLanguageSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Framework
        fields = ['id', 'language', 'proficiency', 'is_primary', 'user']

    def create(self, validated_data):
        user, language = self.context.get('user'), self.context.get('language')
        return Framework.objects.create(user=user, language=language, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.language = self.context.get('language', instance.language)
        instance.proficiency = validated_data.get('proficiency', instance.proficiency)
        instance.is_primary = validated_data.get('is_primary', instance.is_primary)
        instance.save()
        return instance


class SoftSKillsProficiencySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SoftSKillsProficiency
        fields = ['id', 'team_work', 'logic_reason', 'communication_proficiency', 'user']

    def create(self, validated_data):
        user = self.context.get('user', None)
        if user is None:
            raise serializers.ValidationError("User field is required.")
        return SoftSKillsProficiency.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.team_work = validated_data.get('team_work', instance.team_work)
        instance.logic_reason = validated_data.get('logic_reason', instance.logic_reason)
        instance.communication_proficiency = validated_data.get('communication_proficiency',
                                                                instance.communication_proficiency)
        instance.save()
        return instance


class CertificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Certification
        fields = ['id', 'title', 'institution', 'date_issued', 'expiration_date', 'user']

    def create(self, validated_data):
        user = self.context.get('user', None)
        if user is None:
            raise serializers.ValidationError('User field is required.')
        return Certification.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.institution = validated_data.get('institution', instance.institution)
        instance.date_issued = validated_data.get('date_issued', instance.date_issued)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
        instance.save()
        return instance
