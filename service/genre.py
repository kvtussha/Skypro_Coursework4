from dao.genre import GenreDAO
from dao.model.genre import GenreSchema


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao
        self.genres_schema = GenreSchema(many=True)
        self.genre_schema = GenreSchema()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        return self.dao.update(genre_d)

    def delete(self, rid):
        self.dao.delete(rid)
