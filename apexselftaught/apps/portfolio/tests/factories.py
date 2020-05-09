import factory
from faker import Faker
from apexselftaught.apps.portfolio.models import *
from apexselftaught.apps.authentication.tests.factories import UserFactory
from django.db.models.signals import post_save

fake = Faker()


@factory.django.mute_signals(post_save)
class BaseFactory(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    user = factory.SubFactory(UserFactory)


@factory.django.mute_signals(post_save)
class ProjectFactory(BaseFactory):
    class Meta:
        model = Project

    name = fake.word()
    link = fake.url()
    description = fake.sentence()
    user = factory.SubFactory(UserFactory)


class ProgrammingLanguageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProgrammingLanguage

    name = fake.word()


@factory.django.mute_signals(post_save)
class ProgrammingLanguageSpecificsFactory(BaseFactory):
    class Meta:
        model = ProgrammingLanguageSpecifics

    language = factory.SubFactory(ProgrammingLanguageFactory)
    proficiency = fake.random_choices(range(0, 11))[0]
    is_primary = fake.boolean()
    user = factory.SubFactory(UserFactory)


@factory.django.mute_signals(post_save)
class TechnicalSkillsFactory(BaseFactory):
    class Meta:
        model = TechnicalEngineeringProficiency

    algorithms_proficiency = fake.random_choices(range(0, 11))[0]
    backend_testing_proficiency = fake.random_choices(range(0, 11))[0]
    frontend_testing_proficiency = fake.random_choices(range(0, 11))[0]
    design_patterns_proficiency = fake.random_choices(range(0, 11))[0]
    data_structure_proficiency = fake.random_choices(range(0, 11))[0]
    object_oriented_programming_proficiency = fake.random_choices(range(0, 11))[0]
    ui_ux_proficiency = fake.random_choices(range(0, 11))[0]
    git_proficiency = fake.random_choices(range(0, 11))[0]
    databases_proficiency = fake.random_choices(range(0, 11))[0]
    user = factory.SubFactory(UserFactory)


@factory.django.mute_signals(post_save)
class FrameworkFactory(BaseFactory):
    class Meta:
        model = Framework

    name = fake.word()
    language = factory.SubFactory(ProgrammingLanguageFactory)
    proficiency = fake.random_choices(range(0, 11))[0]
    is_primary = fake.boolean()
    user = factory.SubFactory(UserFactory)


@factory.django.mute_signals(post_save)
class SoftSkillFactory(BaseFactory):
    class Meta:
        model = SoftSKillsProficiency

    team_work = fake.random_choices(range(0, 11))[0]
    logic_reason = fake.random_choices(range(0, 11))[0]
    communication_proficiency = fake.random_choices(range(0, 11))[0]
    user = factory.SubFactory(UserFactory)


class CertificationFactory(BaseFactory):
    class Meta:
        model = Certification

    title = fake.word()
    institution = fake.word()
    date_issued = fake.date()
    expiration_date = fake.date()
