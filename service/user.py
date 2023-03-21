import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, HASH_STR


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user_d):
        user_d["password"] = self.generate_password(user_d["password"])
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d["password"] = self.generate_password(user_d["password"])
        return self.dao.update(user_d)

    def update_partial(self, data, uid):
        user = self.get_one(uid)
        if "email" in data:
            user.email = data.get("email")
        if "name" in data:
            user.name = data.get("name")
        if "surname" in data:
            user.surname = data.get("surname")
        if "favourite_genre" in data:
            user.favourite_genre = data.get("favourite_genre")
        self.dao.update(user)

    def update_password(self, data, uid):
        user = self.get_one(uid)
        if self.compare_password(user.password, data.get('old_password')):
            data["new_password"] = self.generate_password(data["new_password"])
            user.password = data["new_password"]
            self.dao.update(user)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        decoded = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded, hash_digest)
