from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from helpers import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        d_year = request.args.get("year")
        all_movies = movie_service.get_all(director=director, genre=genre, d_year=d_year, status=status, page=page)
        return MovieSchema(many=True).dump(all_movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
