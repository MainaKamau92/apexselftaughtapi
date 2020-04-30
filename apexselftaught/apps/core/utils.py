import jwt
import os


def jwt_decode(token=None):
    if token:
        payload = jwt.decode(
            token,
            os.getenv("SECRET"),
            algorithms='HS256'
        )
        return payload
    else:
        return None
