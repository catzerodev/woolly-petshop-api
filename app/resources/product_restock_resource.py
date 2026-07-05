from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.schemas.restock_schema import RestockSchema
from app.services.product_service import ProductService

class ProductRestockResource(Resource):
    
    @jwt_required()
    def patch(self, product_id):
        try:
            data = RestockSchema(**request.json)
        except ValidationError as e:
            return e.errors(), 400
        product = ProductService().restock(
            product_id,
            data.quantity       
        )
        
        if product is None:
            return {
                'message': 'Product not found.'
            }, 404
            
        return {
            'message': 'Product restocked successfully.',
            'product_id': product.id,
            'new_stock': product.stock
        }, 200
        