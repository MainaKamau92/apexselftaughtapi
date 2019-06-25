import json
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from .test_fixtures.authenticantion import login_user_query
from apexselftaught.apps.authentication.models import User



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
        print(json.dumps(body))
        response = cls.client.post(
            '/apexselftaught/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        print(json_response)
        return json_response

    # @classmethod
    # def query_with_token(cls, access_token, query: str = None):
    #     # Method to run queries and mutations using a logged in user
    #     # with an authentication token
    #     body = dict()
    #     body['query'] = query
    #     http_auth = 'JWT {}'.format(access_token)
    #     url = '/apexselftaught/'
    #     content_type = 'application/json'

    #     response = cls.client.post(
    #         url,
    #         json.dumps(body),
    #         HTTP_AUTHORIZATION=http_auth,
    #         content_type=content_type)

    #     json_response = json.loads(response.content.decode())
    #     return json_response

    # def user_login(self):
    #     """
    #     Log in registered user and return a token
    #     """
    #     response = self.query(login_user_query.format(**self.login_user))
    #     return response['data']['loginUser']['token']

    # def user2_login(self):
    #     """
    #     Log in registered user and return a token
    #     """
    #     response = self.query(login_user_query.format(**self.login_user2))
    #     return response['data']['loginUser']['token']

    # def register_user(self, user):
    #     """
    #     register a new user
    #     """
    #     email = user["email"]
    #     username = user["username"]
    #     password = user["password"]
    #     mobile_number = user["mobile_number"]
    #     user = User.objects.create_user(
    #         email=email, username=username, password=password, mobile_number=mobile_number)
    #     user.is_active = True
    #     user.save()
    #     return user

    def setUp(self):
        """
        Configurations to be made available before each
        individual test case inheriting from this class.
        """
        self.new_user = {
            "email": "johndoe@test.com",
            "username": "johndoe",
            "password": "johndoe123",
            "mobile_number": "0716567809"
        }
        # self.new_user2 = {
        #     "email": "philipdoe@test.com",
        #     "username": "philipdoe",
        #     "password": "philipdoe123",
        #     "mobile_number": "0714567809"
        # }

        # self.login_user = {
        #     "email": "johndoe@test.com",
        #     "password": "johndoe123"
        # }
        # self.login_user2 = {
        #     "email": "philipdoe@test.com",
        #     "password": "philipdoe123"
        # }
        # self.user = self.register_user(self.new_user)
        # self.user2 = self.register_user(self.new_user2)
        # self.access_token = self.user_login()
        # self.access_token2 = self.user2_login()
