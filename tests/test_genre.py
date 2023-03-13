from unittest.mock import MagicMock
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService

import pytest


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    cartoon = Genre(id=1, name='cartoon')
    horror = Genre(id=2, name='horror')
    anime = Genre(id=3, name='anime')

    genre_dao.get_all = MagicMock(return_=[cartoon, horror, anime])
    genre_dao.get_one = MagicMock(return_=horror)
    genre_dao.create = MagicMock(return_=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_director = {
            "name": 'triller'
        }
        genre = self.genre_service.create(new_director)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(3)

    def test_update(self):
        new_genre = {
            "id": 1,
            "name": 'drama'
        }
        self.genre_service.update(new_genre)
