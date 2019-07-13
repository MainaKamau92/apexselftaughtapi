import jwt
import os


def generate_web_token(user):
    secret = os.getenv('SECRET')
    return jwt.encode({'user': user}, secret, algorithm='HS256')
