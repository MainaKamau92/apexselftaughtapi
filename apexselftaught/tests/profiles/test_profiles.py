from graphql import GraphQLError
from apexselftaught.tests.BaseConfig import BaseConfiguration
from apexselftaught.tests.test_queries.profiles import update_profile_mutation
from ..test_queries.profiles import get_single_profile, get_all_profiles
from ..factories.factories import ProfileFactory


class ProfileTestCase(BaseConfiguration):

    def test_user_can_get_multiple_profiles(self):
        [ProfileFactory() for _ in range(0, 10)]
        response = self.query_with_token(self.access_token, get_all_profiles)
        profile_list = response["data"]["profiles"]
        self.assertEqual(len(profile_list), 11)

    def test_user_cannot_get_an_in_existent_profile(self):
        response = self.query_with_token(self.access_token, get_single_profile.format(id=10000))
        self.assertEqual(response["errors"][0]["message"], "Profile does not exist")
        self.assertRaises(GraphQLError)

    def test_user_update_profile(self):
        response = self.query_with_token(self.access_token, update_profile_mutation.format(
            firstName="John",
            github="github.com/john",
            industry="software",
            lastName="Doe",
            userBio="This is a profile"
        ))
        response_data = response.get("data")
        self.assertEqual(response_data["updateProfile"]["profile"]["lastName"], "Doe")
        self.assertEqual(response_data["updateProfile"]["message"], "Successfully updated profile")
