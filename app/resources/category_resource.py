from flask import request
from flask_restful import Resource
from pydantic import ValidationError

from app.schemas.category_schema import CategorySchema
from app.services.category_service import CategoryService


class CategoryResource(Resource):

    def post(self):

        try:

            data = CategorySchema(**request.json)

        except ValidationError as e:

            return e.errors(), 400

        category = CategoryService().create(data)

        return {
            "message": "Category created successfully.",
            "id": category.id
        }, 201