from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from flask_jwt_extended import create_access_token

from app.models.user_model import User
from app.schemas.auth_schema import LoginSchema, RegisterSchema
from app.services.user_service import UserService
from app.utils.helpers import hash_password, verify_password

from db import db


class RegisterResource(Resource):

    def post(self):

        try:
            data = RegisterSchema(**request.json)

        except ValidationError as e:
            return e.errors(), 400

        user = UserService().find_by_email(data.email)

        if user is not None:
            return {
                'message': 'Email already exists.'
            }, 400

        new_user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password)
        )

        db.session.add(new_user)
        db.session.commit()

        return {
            'message': 'User created successfully.',
            'id': new_user.id
        }, 201
        
        
class LoginResource(Resource):

    def post(self):

        try:
            data = LoginSchema(**request.json)

        except ValidationError as e:
            return e.errors(), 400

        user = UserService().find_by_email(data.email)

        if user is None:
            return {
                'message': 'User not found.'
            }, 401

        is_valid = verify_password(
            user.password,
            data.password
        )

        if not is_valid:
            return {
                'message': 'Invalid credentials.'
            }, 401

        access_token = create_access_token(
            identity=str(user.id)
        )

        return {
            "access_token": access_token
        }, 200
    