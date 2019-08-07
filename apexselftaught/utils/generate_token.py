import jwt
import os
from graphql_jwt.utils import jwt_payload, jwt_encode


def generate_web_token(username):
    secret = os.getenv('SECRET')
    return jwt.encode({'user': username}, secret, algorithm='HS256').decode('utf-8')


def generate_login_token(user):
    token = jwt_encode(jwt_payload(user))
    return token
