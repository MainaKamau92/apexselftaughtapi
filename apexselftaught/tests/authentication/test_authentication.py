from apexselftaught.tests.BaseConfig import BaseConfiguration
from apexselftaught.tests.test_queries.authenticantion import (register_user_query,
                                                               get_all_users_query,
                                                               get_single_user_query,
                                                               login_user_query)
from ..factories.factories import UserFactory


class UserTestCase(BaseConfiguration):
    def test_user_can_register_for_account(self):
        response = self.query(register_user_query.format(
            username="apex_user",
            email="user@apexselftaught.com",
            mobileNumber="0711009988",
            password="password123",
            recruiter="false"
        ))
        data = response.get('data')
        self.assertEqual(data["registerUser"]["message"],
                         "User created successfully, verification email sent to user@apexselftaught.com")

    def test_user_cant_register_with_invalid_email(self):
        response = self.query(register_user_query.format(
            username="apex_user",
            email="apexselftaught.com",
            mobileNumber="0711009988",
            password="password123",
            recruiter="false"
        ))
        self.assertEqual(response["errors"][0]["message"],
                         "'apexselftaught.com', is an invalid email, please provide a valid email and then try again")

    def test_cannot_double_register(self):
        self.test_user_can_register_for_account()
        response = self.query(register_user_query.format(
            username="apex_user",
            email="user@apexselftaught.com",
            mobileNumber="0711009988",
            password="password123",
            recruiter="false"
        ))
        response_data = response.get("data")
        self.assertIn("duplicate key value violates unique",
                      str(response_data["registerUser"]["message"]))

    def test_user_can_login(self):
        user = UserFactory(
            email="user@apexselftaught.com",
            is_verified=True
        )
        user.set_password("password123")
        user.save()
        response = self.query(login_user_query.format(
            email="user@apexselftaught.com",
            password="password123"
        ))
        response_data = response.get('data')
        self.assertIn("token", response_data["loginUser"])
        self.assertEqual(response_data["loginUser"]["message"], "You logged in successfully.")

    def test_user_can_get_all_users(self):
        [UserFactory() for _ in range(0, 10)]
        response = self.query_with_token(self.access_token, get_all_users_query)
        data = response.get('data')["users"]
        # Eleven due to the user created on setUp in BaseConfig
        self.assertEqual(len(data), 11)

    def test_user_can_get_a_single_user(self):
        [UserFactory() for _ in range(0, 10)]
        response = self.query_with_token(self.access_token, get_single_user_query.format(id=5))
        data = response.get('data')
        self.assertEqual(data["user"]["id"], str(5))

    def test_cannot_get_an_in_existent_user(self):
        response = self.query_with_token(
            self.access_token,
            get_single_user_query.format(id=10))
        data = response.get('errors')[0]["message"]
        self.assertIn("does not exist", data)
