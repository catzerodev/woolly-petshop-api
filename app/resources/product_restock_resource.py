from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from flasgger import swag_from

from app.schemas.restock_schema import RestockSchema
from app.services.product_service import ProductService

class ProductRestockResource(Resource):
    
    @swag_from({
    'tags': ['Business Logic'],
    'summary': 'Restock product',
    'description': 'Increase the stock of an existing product.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'integer'
            }
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'quantity': {
                        'type': 'integer',
                        'example': 10
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Product restocked successfully.'
        },
        404: {
            'description': 'Product not found.'
        }
    }
})
    
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
        