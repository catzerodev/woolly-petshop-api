from flask_restful import Api
from app.resources.category_resource import CategoryResource
from app.resources.category_detail_resource import CategoryDetailResource


def register_routes(app):

    api = Api(app)

    api.add_resource(
        CategoryResource,
        "/categories"
    )
    api.add_resource(
        CategoryDetailResource,
        "/categories/<int:category_id>"
    )   
    
    