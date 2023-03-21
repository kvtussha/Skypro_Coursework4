import calendar
import datetime

import jwt

from flask_restx import abort

from constants import PWD_HASH_SALT, JWT_ALGORITHM, JWT_SECRET
from service.user import UserService


class AuthService:

    def __init__(self, user_service:  UserService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)
        if not user:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400)

        data = {
            'email' : user.email,
            'name': user.name,
            'surname': user.surname,
            'favourite_genre': user.favourite_genre
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        min30 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(min30.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {'access_token': access_token, 'refresh_token': refresh_token}


    def refresh_token(self, refresh_token):
        try:
            info = jwt.decode(
                refresh_token,
                JWT_SECRET,
                algorithms=[JWT_ALGORITHM]
            )
            email = info.get('email')
        except Exception as e:
            return False

        if info:
            return self.generate_token(email, None, is_refresh=True)

