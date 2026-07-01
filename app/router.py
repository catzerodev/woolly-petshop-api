from flask_restful import Api

from app.resources.category_resource import CategoryResource


def register_routes(app):

    api = Api(app)

    api.add_resource(
        CategoryResource,
        "/categories"
    )