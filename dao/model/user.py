from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	name = db.Column(db.String(255))
	surname = db.Column(db.String(255))
	password = db.Column(db.String(255))
	favourite_genre = db.Column(db.String(255))


class UserSchema(Schema):
	id = fields.Int()
	email = fields.Str()
	name = fields.Str()
	surname = fields.Str()
	password = fields.Str()
	favourite_genre = fields.Str()
