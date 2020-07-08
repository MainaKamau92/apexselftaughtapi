# from faker import Faker
# import factory
# from datetime import datetime, timedelta
# from apexselftaught.apps.tenant.models import Client
#
# fake = Faker()
#
#
# class ClientFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = Client
#
#     tenant_name = factory.Sequence(lambda n: f"tenant{n}")
#     tenant_uuid = fake.uuid4()
#     paid_until = fake.date_time_between(datetime.now() + timedelta(days=360), datetime.now() + timedelta(days=380))
#     on_trial = fake.boolean()
#     domain_url = fake.url()
#     schema_name = tenant_name
