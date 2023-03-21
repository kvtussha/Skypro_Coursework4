import jwt
from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201

@auth_ns.route('/login')
class Auth_View(Resource):
    def post(self):
        data = request.json
        if None in [data.get("email"), data.get("password")]:
            return '', 400
        tokens = auth_service.generate_token(data.get("email"), data.get("password"))
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.refresh_token(token)
        return tokens, 201
