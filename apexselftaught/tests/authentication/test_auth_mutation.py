from apexselftaught.apps.authentication.models import User
from apexselftaught.tests.BaseConfig import BaseConfiguration
from apexselftaught.tests.test_fixtures.authenticantion import \
    register_user_query, invalid_register_query, login_query, \
    get_all_users_query, get_single_user_query, get_inexistent_user_query, login_user_query
from ..factories.factories import UserFactory


class UserTestCase(BaseConfiguration):
    def test_create_user(self):
        response = self.query(register_user_query)
        data = response.get('data')
        self.assertEqual(data, {"registerUser": {
            'errors': None,
            "user": {
                "email": "johnydoe@test.com"
            }}
        })

    def test_create_user_with_invalid_email(self):
        response = self.query(invalid_register_query)
        data = response.get('data')
        self.assertRaises(TypeError, data)

    def test_model_models(self):
        User.objects.create_user(username="username",
                                 email="test@test.com",
                                 mobile_number="056109870",
                                 password="Testuser123")
        user = User.objects.get(username="username")
        short_name = User.objects.get(username="username").get_short_name()
        full_name = User.objects.get(username="username").get_full_name()
        self.assertEqual(str(user), "test@test.com")
        self.assertEqual(str(short_name), "username")
        self.assertEqual(str(full_name), "username")

    def test_double_registration(self):
        self.query(register_user_query)
        response = self.query(register_user_query)
        data_response = response.get("data")["registerUser"]["errors"]
        self.assertIn("duplicate key value violates unique",
                      str(data_response))

    def test_login_user_mutation(self):
        self.query(register_user_query)
        user = User.objects.get(username="johnydoe")
        user.is_verified = True
        user.save()
        response = self.query(login_query)
        data = response.get('data')["loginUser"]["token"]
        self.assertIsNotNone(data)

    def test_get_all_users(self):
        for i in range(0, 7):
            UserFactory()
        token = self.access_token
        response = self.query_with_token(token, get_all_users_query)
        data = response.get('data')["users"]
        # Eight due to the user created on setUp in BaseConfig
        self.assertEqual(len(data), 8)

    def test_get_a_single_user(self):
        self.query(register_user_query)
        token = self.access_token
        response = self.query_with_token(token, get_single_user_query)
        data = response.get('data')["user"]["username"]
        self.assertEqual(data, "johnydoe")

    def test_inexistent_single_user(self):
        self.query(register_user_query)
        token = self.access_token
        response = self.query_with_token(token, get_inexistent_user_query)
        data = response.get('errors')[0]["message"]
        self.assertIn("does not exist", data)
