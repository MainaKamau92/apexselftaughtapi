import re
from graphql import GraphQLError
from apexselftaught.utils.messages.authentication import AUTH_ERROR_RESPONSES


class Validation:

    def validate_data_fields(self, username, email, mobile_number, password):
        return dict(email=self.validate_email(email),
                    username=self.validate_username(username),
                    password=self.validate_password(password),
                    mobile_number=self.validate_mobile(mobile_number))

    @staticmethod
    def validate_email(email):
        try:
            match = re.search(
                r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
            return match.group()
        except Exception:
            raise GraphQLError(
                AUTH_ERROR_RESPONSES["invalid_email"].format(email))

    @staticmethod
    def validate_password(password):
        try:
            match = re.match(r'[A-Za-z0-9@#$%^&+_*()=]{8,}', password, re.I)
            return match.group()
        except Exception:
            raise GraphQLError(
                AUTH_ERROR_RESPONSES["invalid_password"].format(password))

    @staticmethod
    def validate_username(username):
        try:
            match = re.match(r'^[a-zA-Z0-9_.-]+$', username, re.I)
            return match.group()
        except Exception:
            raise GraphQLError(
                AUTH_ERROR_RESPONSES["invalid_username"].format(username))

    @staticmethod
    def validate_mobile(moblie_number):
        try:
            match = re.match(r'^(?:\+?44)?[07]\d{9,13}$', moblie_number, re.I)
            return match.group()
        except Exception:
            raise GraphQLError(
                AUTH_ERROR_RESPONSES["invalid_mobile_number"].format(moblie_number))
