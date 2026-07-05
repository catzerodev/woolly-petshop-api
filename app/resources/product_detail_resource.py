from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.schemas.product_schema import ProductSchema
from app.services.product_service import ProductService

class ProductDetailResource(Resource):
    
    def get(self, product_id):

        product = ProductService().get_by_id(product_id)

        if product is None:
            return {'message': 'Product not found.'}, 404

        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'stock': product.stock,
            'image_url': product.image_url,
            'category_id': product.category_id,
            'is_active': product.is_active
        }, 200
        
    @jwt_required()
    def put(self, product_id):

        try:
            data = ProductSchema(**request.json)

        except ValidationError as e:
            return e.errors(), 400

        product = ProductService().update(product_id, data)

        if product is None:
            return {'message': 'Product not found.'}, 404

        return {
            'message': 'Product updated successfully.',
            'data': {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'stock': product.stock,
                'image_url': product.image_url,
                'category_id': product.category_id,
                'is_active': product.is_active
            },
        }, 200
        
    @jwt_required()
    def delete(self, product_id):
        deleted = ProductService().delete(product_id)
        if not deleted:
            return {'message': 'Product not found.'}, 404
            
        return {'message': 'Product deleted successfully.'}, 200
    
    