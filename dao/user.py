from dao.model.user import User
from sqlalchemy.orm.scoping import ScopedSession


class UserDAO:
    def __init__(self, session: ScopedSession):
        self.session = session

    def get_all(self):
        return User.query.all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):
        users = User(**data)

        self.session.add(users)
        self.session.commit()

        return users

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()
