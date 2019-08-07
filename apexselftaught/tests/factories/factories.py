from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.profiles.models import Profile
from faker import Factory
import factory

faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.user_name())  # faker.user_name()
    email = factory.LazyAttribute(lambda _: faker.ascii_email())  # faker.email()
    mobile_number = factory.LazyAttribute(lambda _: faker.phone_number())  # faker.phone_number()
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = faker.first_name()
    last_name = faker.last_name()
    secondary_email = faker.ascii_email()
    user_bio = faker.sentences(nb=3, ext_word_list=None)
    avatar = faker.hostname()
    country = faker.country()
    county = faker.country()
    industry = faker.job()
    github = faker.hostname()
    website = faker.hostname()
    date_created = faker.date(pattern="%Y-%m-%d", end_datetime=None)
    user = factory.SubFactory(UserFactory)
