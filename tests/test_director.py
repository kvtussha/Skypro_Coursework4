from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService

import pytest


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    steven = Director(id=1, name='Steven Spielberg')
    david = Director(id=2, name='David Fincher')
    ridley = Director(id=3, name='Ridley Scott')

    director_dao.get_all = MagicMock(return_value=[steven, david, ridley])
    director_dao.get_one = MagicMock(return_value=david)
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(2)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        new_director = {
            "name": 'Innokenty Vasilievich'
        }
        director = self.director_service.create(new_director)
        assert director.id != None

    def test_delete(self):
        self.director_service.delete(3)

    def test_update(self):
        new_director = {
            "id": 1,
            "name": 'Maria Svintsova'
        }
        self.director_service.update(new_director)
