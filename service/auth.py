import calendar
import datetime

import jwt as jwt

from flask_restx import abort

from constants import PWD_HASH_SALT, JWT_ALGORITHM
from service.user import UserService


class AuthService:

    def __init__(self, user_service:  UserService):
        self.user_service = user_service

    def generate_token(self, username, password):
        user = self.user_service.get_by_name(username)
        if not user:
            abort(400)

        if not self.user_service.compare_password(user.password, password):
            abort(400)

        data = {
            'username': user.username,
            'role': user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, PWD_HASH_SALT, algorithm=JWT_ALGORITHM)

        min30 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(min30.timetuple())
        refresh_token = jwt.encode(data, PWD_HASH_SALT, algorithm=JWT_ALGORITHM)

        return {'access_token': access_token, 'refresh_token': refresh_token}


    def refresh_token(self, refresh_token):
        try:
            info = jwt.decode(refresh_token, PWD_HASH_SALT, algorithms=[JWT_ALGORITHM])
            username = info.get('username')
        except Exception as e:
            return False

        if info:
            return self.generate_token(username, None, is_refresh=True)

