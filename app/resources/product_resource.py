from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.schemas.product_schema import ProductSchema
from app.services.product_service import ProductService


class ProductResource(Resource):
    
    @jwt_required()
    def post(self):

        try:
            data = ProductSchema(**request.json)

        except ValidationError as e:
            return e.errors(), 400

        product = ProductService().create(data)

        return {
            'message': 'Product created successfully.',
            'id': product.id
        }, 201

    def get(self):

        products = ProductService().get_all()

        return [
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'stock': product.stock,
                'image_url': product.image_url,
                'category_id': product.category_id,
                'is_active': product.is_active
            }
            for product in products
        ], 200