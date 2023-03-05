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

    def get_by_name(self, username):
        return self.dao.get_by_name(username)

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        return self.dao.update(user_d)

    def generate_password(password):
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(password_hash, other_password):
        decoded = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded, hash_digest)
