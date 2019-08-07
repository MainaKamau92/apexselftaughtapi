from graphql import GraphQLError

from apexselftaught.tests.BaseConfig import BaseConfiguration
from ..test_fixtures.profiles import create_profile_mutation, get_single_profile, get_all_profiles, update_profile, \
    foreign_update_profile
from ..factories.factories import UserFactory, ProfileFactory


class ProfileTestCase(BaseConfiguration):

    def test_user_can_create_profile(self):
        token = self.access_token
        res = self.query_with_token(token, create_profile_mutation)
        profile_id = res["data"]["createProfile"]["profile"]["id"]
        self.assertEquals(profile_id, str(1))

    def test_user_can_get_a_profile(self):
        token = self.access_token
        self.query_with_token(token, create_profile_mutation)
        response = self.query_with_token(self.access_token, get_single_profile)
        response_data = response["data"]["profile"]
        self.assertAlmostEquals(response_data, {'id': '2', 'firstName': 'John', 'lastName': 'Doe'})

    def test_user_can_get_multiple_profiles(self):
        self.user = UserFactory()
        self.user2 = UserFactory()
        self.user3 = UserFactory()
        ProfileFactory(user=self.user)
        ProfileFactory(user=self.user2)
        ProfileFactory(user=self.user3)
        token = self.access_token
        response = self.query_with_token(token, get_all_profiles)
        profile_list = response["data"]["profiles"]
        self.assertGreater(len(profile_list), 1)

    def test_user_cannot_get_an_inexistent_profile(self):
        response = self.query_with_token(self.access_token, get_single_profile)
        self.assertRaises(GraphQLError)

    def test_user_cannot_create_profile_twice(self):
        token = self.access_token
        self.query_with_token(token, create_profile_mutation)
        self.query_with_token(token, create_profile_mutation)
        self.assertRaises(GraphQLError)

    def test_user_can_update_profile(self):
        token = self.access_token
        self.query_with_token(token, create_profile_mutation)
        response = self.query_with_token(token, update_profile)
        print(response)
        self.assertIn(response["data"]["updateProfile"]["profile"]["lastName"], "Maina")

    def test_user_cant_update_foreign_profile(self):
        self.user = UserFactory()
        ProfileFactory(user=self.user)
        token = self.access_token
        response = self.query_with_token(token, foreign_update_profile)
        self.assertIn("errors", response)
