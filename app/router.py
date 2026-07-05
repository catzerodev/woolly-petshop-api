from flask_restful import Api

from app.resources.category_resource import CategoryResource
from app.resources.category_detail_resource import CategoryDetailResource
from app.resources.product_detail_resource import ProductDetailResource
from app.resources.product_resource import ProductResource
from app.resources.auth_resource import RegisterResource
from app.resources.auth_resource import LoginResource
from app.resources.product_restock_resource import ProductRestockResource


def register_routes(app):

    api = Api(app)

    api.add_resource(
        CategoryResource,
        '/categories'
    )
    api.add_resource(
        CategoryDetailResource,
        '/categories/<int:category_id>'
    )
    
    api.add_resource(
        ProductResource,
        '/products'
    )
    api.add_resource(
        ProductDetailResource,
        '/products/<int:product_id>'
    )
    
    api.add_resource(
        RegisterResource,
        '/register'
    )
    
    api.add_resource(
        LoginResource,
        '/login'
    )
    
    api.add_resource(
        ProductRestockResource,
        '/products/<int:product_id>/restock'
    )
    
    
    
    
    
    
    
    