from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.profiles.models import Profile
from faker import Factory
import factory
from django.db.models.signals import post_save

faker = Factory.create()


@factory.django.mute_signals(post_save)
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda x: "user_%d" % x)
    email = factory.Sequence(lambda x: "user%d@apexselftaught.com" % x)
    mobile_number = factory.LazyAttribute(lambda _: faker.phone_number())
    password = faker.password(length=10, special_chars=True,
                              digits=True, upper_case=True,
                              lower_case=True)
    profile = factory.RelatedFactory('apexselftaught.tests.factories.factories.ProfileFactory', 'user')
    is_recruiter = False


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = faker.first_name()
    last_name = faker.last_name()
    secondary_email = faker.ascii_email()
    user_bio = faker.sentences(nb=3, ext_word_list=None)
    avatar = faker.hostname()
    county = faker.country()
    industry = faker.job()
    github = faker.hostname()
    website = faker.hostname()
    date_created = faker.date(pattern="%Y-%m-%d", end_datetime=None)
    user = factory.SubFactory(UserFactory, profile=None)
