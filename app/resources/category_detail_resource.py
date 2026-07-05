from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.schemas.category_schema import CategorySchema
from app.services.category_service import CategoryService


class CategoryDetailResource(Resource):

    def get(self, category_id):

        category = CategoryService().get_by_id(category_id)

        if category is None:

            return {'message': 'Category not found.'}, 404

        return {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'is_active': category.is_active,
        }, 200

    @jwt_required()
    def put(self, category_id):

        try:

            data = CategorySchema(**request.json)

        except ValidationError as e:

            return e.errors(), 400

        category = CategoryService().update(category_id, data)

        if category is None:

            return {'message': 'Category not found.'}, 404

        return {
            'message': 'Category updated successfully.',
            'data': {
                'id': category.id,
                'name': category.name,
                'description': category.description,
                'is_active': category.is_active,
            },
        }, 200

    @jwt_required()
    def delete(self, category_id):
        deleted = CategoryService().delete(category_id)
        if not deleted:
            return {'message': 'Category not found.'}, 404
            
        return {'message': 'Category deleted successfully.'}, 200
        
        
        