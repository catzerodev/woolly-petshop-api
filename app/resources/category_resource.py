from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.schemas.category_schema import CategorySchema
from app.services.category_service import CategoryService


class CategoryResource(Resource):

    @jwt_required()
    def post(self):

        try:

            data = CategorySchema(**request.json)

        except ValidationError as e:

            return e.errors(), 400

        category = CategoryService().create(data)

        return {
            'message': 'Category created successfully.',
            'id': category.id
        }, 201
        
    def get(self):

        categories = CategoryService().get_all()

        return [
        {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'is_active': category.is_active
        }
        for category in categories
    ], 200
        
    
       

        
    