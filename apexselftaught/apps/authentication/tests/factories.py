from faker import Faker
import factory
from django.db.models.signals import post_save

from apexselftaught.apps.authentication.models import User

fake = Faker()


@factory.django.mute_signals(post_save)
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda x: "user_%d" % x)
    email = factory.Sequence(lambda x: "user%d@apexselftaught.com" % x)
    mobile_number = factory.Sequence(lambda x: "+1-560-257-17%d" % x)
    password = factory.PostGenerationMethodCall('set_password',
                                                fake.password(length=10, special_chars=True,
                                                              digits=True, upper_case=True,
                                                              lower_case=True))
