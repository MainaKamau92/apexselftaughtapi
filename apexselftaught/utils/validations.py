import re
from graphql import GraphQLError


class Validation:

    def validate_data_fields(self, username, email, mobile_number, password):
        return dict(email=self.validate_email(email),
                    username=self.validate_username(username),
                    password=self.validate_password(password),
                    mobile_number=self.validate_mobile(mobile_number))

    def validate_email(self, email):
        try:
            match = re.search(
                r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
            return match.group()
        except NoneType as e:
            raise AttributeError(str(e))

    def validate_password(self, password):
        try:
            match = re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password, re.I)
            return match.group()
        except NoneType as e:
            raise AttributeError(str(e))

    def validate_username(self, username):
        try:
            match = re.match(r'^[a-zA-Z0-9_.-]+$', username, re.I)
            return match.group()
        except NoneType as e:
            raise AttributeError(str(e))

    def validate_mobile(self, moblie_number):
        try:
            match = re.match(r'^(?:\+?44)?[07]\d{9,13}$', moblie_number, re.I)
            return match.group()
        except NoneType as e:
            raise AttributeError(str(e))
