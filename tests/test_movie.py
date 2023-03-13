from unittest.mock import MagicMock
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService

import pytest


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    yellowstone = Movie(
        id=1,
        title="Йеллоустоун",
        description="Владелец ранчо пытается сохранить землю своих предков.",
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1
    )

    obsession = Movie(
        id=2,
        title="Одержимость",
        description="Эндрю мечтает стать великим.",
        trailer="https: // www.youtube.com / watch?v = Q9PxDPOo1jw",
        year=2013,
        rating=8.5,
        genre_id=4,
        director_id=8
    )

    oops = Movie(
        id=3,
        title="Упс...Приплыли!",
        description="От Великого потопа зверей спас ковчег.",
        trailer="https: // www.youtube.com / watch?v = Qjpmysz4x - 4",
        year=2020,
        rating=5.9,
        genre_id=16,
        director_id=19
    )

    movie_dao.get_all = MagicMock(return_=[yellowstone, obsession, oops])
    movie_dao.get_one = MagicMock(return_=obsession)
    movie_dao.create = MagicMock(return_=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(2)
        assert movie != None
        assert movie.id != None

    # @pytest.mark.skip(reason='no way of currently testing this')
    def test_get_all(self, filters):
        movies = self.movie_service.get_all(filters)
        assert len(movies) > 0

    def test_create(self):
        new_movie = {
            "id": 4,
            "title": "Рокетмен",
            "description": "История превращения застенчивого парня",
            "trailer": "https: // youtu.be / VISiqVeKTq8",
            "year": 2019,
            "rating": 7.3,
            "genre_id": 18,
            "director_id": 19
        }

        movie = self.movie_service.create(new_movie)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(3)

    def test_update(self):
        new_movie = {
            "id": 3,
            "title": "Чикаго",
            "description": "Рокси Харт мечтает о песнях и танцах",
            "trailer": "https: // www.youtube.com / watch?v = YxzS_LzWdG8",
            "year": 2002,
            "rating": 7.2,
            "genre_id": 20,
            "director_id": 6
        }
        self.movie_service.update(new_movie)
