import jwt
from flask import request, abort

from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorisation' not in request.header():
            abort(401)
        data = request.headers['Authorisation']
        token = data.split(' Bearer')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algoritm=JWT_ALGORITHM)
        except Exception as e:
            print('decode error')
            abort(401)

        return func

    return wrapper()


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorisation' not in request.header():
            abort(401)
        data = request.headers['Authorisation']
        token = data.split(' Bearer')[-1]

        try:
            user = jwt.decode(token, JWT_SECRET, algoritm=JWT_ALGORITHM)
            if user.get('role') != 'admin':
                abort(401)
        except Exception as e:
            print('decode error')
            abort(401)

        return func

    return wrapper()
