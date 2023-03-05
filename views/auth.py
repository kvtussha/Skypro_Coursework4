import jwt
from flask import request
from flask_restx import Resource, Namespace

import service.auth
from constants import JWT_SECRET, JWT_ALGORITHM
from implemented import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')

        if None is [username, password]:
            return '', 400

        tokens = auth_service.generate_token(username, password)
        return tokens, 201


@auth_ns.route('/<int:bid>')
class AuthView(Resource):

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.refresh_token(token)
        return tokens, 201



