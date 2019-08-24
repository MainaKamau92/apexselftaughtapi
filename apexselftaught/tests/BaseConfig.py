import json
from decouple import config
from django.test import Client, TestCase
from .factories.factories import UserFactory
from apexselftaught.utils.generate_token import generate_login_token

GRAPHQL_ENDPOINT = config('GRAPHQL_ENDPOINT')


class BaseConfiguration(TestCase):

    @classmethod
    def setUpClass(cls):
        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(BaseConfiguration, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            GRAPHQL_ENDPOINT, json.dumps(body),
            content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    @classmethod
    def query_with_token(cls, access_token, query: str = None):
        # Method to run queries and mutations using a logged in user
        # with an authentication token
        body = dict()
        body['query'] = query
        http_auth = 'JWT {}'.format(access_token)
        url = GRAPHQL_ENDPOINT
        content_type = 'application/json'

        response = cls.client.post(
            url,
            json.dumps(body),
            HTTP_AUTHORIZATION=http_auth,
            content_type=content_type)

        json_response = json.loads(response.content.decode())
        return json_response

    def setUp(self):
        """
        Configurations to be made available before each
        individual test case inheriting from this class.
        """
        self.user = UserFactory()
        self.access_token = generate_login_token(self.user)
