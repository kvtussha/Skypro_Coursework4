from dao.director import DirectorDAO
from dao.model.director import DirectorSchema


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, director_d):
        return self.dao.update(director_d)

    def delete(self, rid):
        self.dao.delete(rid)
