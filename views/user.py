from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from helpers import admin_required, auth_required
from implemented import user_service

user_ns = Namespace('users')
user_password_ns = Namespace('users/password')


@user_ns.route('/')
class UsersView(Resource):
    #@auth_required
    def get(self):
        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, uid):
        b = user_service.get_one(uid)
        sm_d = UserSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @admin_required
    def patch(self, uid):
        data = request.json
        user_service.update_partial(data, uid)
        return '', 204

user_password_ns.route('<int:uid>')
class UserPassword_View(Resource):
    @auth_required
    def put(self, uid):
        data = request.json
        user_service.update_password(data, uid)
        return '', 204

