from flask import request
from functools import wraps
from datetime import datetime, timedelta
import jwt
import os

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


def requires_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        my_secert_key = os.getenv('SECRET_KEY')
        my_token = None

        # Checks if the token has been supplied
        if 'X-API-KEY' in request.headers:
            my_token = request.headers['X-API-KEY']

            # create a payload
            payload = {
                'exp': datetime.utcnow() + timedelta(hours=24),
                'sub': my_token
            }

            # create a token using payload and secret key
            encode_token = jwt.encode(
                payload, my_secert_key, algorithm='HS256')

        # Checks if the token hasn't been supplied
        if not my_token:
            return {'message': 'No token was found'}, 401

        try:
            # Decode the token using the my_secret_key
            access_token = jwt.decode(encode_token, my_secert_key), 401
            print(access_token)
        except BaseException:
            return {'message': 'The token is not valid'}, 401
        return f(*args, **kwargs)
    return decorated
