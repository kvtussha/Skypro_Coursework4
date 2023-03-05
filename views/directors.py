from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @auth_required
    def post(self):
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    @auth_required
    def get(self, gid):
        r = director_service.get_one(gid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        director_service.delete(gid)
        return "", 204
