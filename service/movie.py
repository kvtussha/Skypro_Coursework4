from flask import request

from dao.model.movie import Movie, MovieSchema
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao
        self.movies_schema = MovieSchema(many=True)
        self.movie_schema = MovieSchema()

    def get_all(self, genre, director, year):

        movies = Movie.query
        if director:
            movies = movies.filter(Movie.director_id == director)
        elif genre:
            movies = movies.filter(Movie.genre_id == genre)
        elif year:
            movies = movies.filter(Movie.year == year)

        return self.dao.get_all(movies)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')

        return self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)
