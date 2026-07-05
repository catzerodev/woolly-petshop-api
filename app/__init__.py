from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Config
from db import db

from app.models.user_model import User
from app.models.category_model import Category
from app.models.product_model import Product
from app.router import register_routes



migrate = Migrate()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    register_routes(app)

    return app

