from faker import Faker
import factory
from django.db.models.signals import post_save
from apexselftaught.apps.profiles.models import Profile
from apexselftaught.apps.authentication.tests.factories import UserFactory

fake = Faker()


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = fake.first_name()
    middle_name = fake.last_name()
    last_name = fake.last_name()
    secondary_email = fake.email()
    user_bio = fake.text()
    avatar = fake.url()
    county = fake.city()
    industry = fake.random_choices(["software", "graphic design"])
    github = fake.url()
    linkendin = fake.url()
    resume = fake.url()
    website = fake.url()
    user = factory.SubFactory(UserFactory)
