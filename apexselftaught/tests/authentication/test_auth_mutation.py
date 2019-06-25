from apexselftaught.tests.BaseConfig import BaseConfiguration
from apexselftaught.tests.test_fixtures.authenticantion import\
     register_user_query
from graphql import GraphQLError


class UserTestCase(BaseConfiguration):

    def test_create_user(self):
        response = self.query(register_user_query)
        # print(response)
        data = response.get('data')
        self.assertEquals(data, {"registerUser": {
            "user": {
                "id": "1",
                "email": "johnydoe@test.com"
            }}
        })
