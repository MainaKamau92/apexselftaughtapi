import jwt
import os


def generate_web_token(username):
    secret = os.getenv('SECRET')
    return jwt.encode({'user': username}, secret, algorithm='HS256').decode('utf-8')
