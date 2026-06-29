from flask import Flask
from flask_migrate import Migrate

from config import Config
from db import db

from app.models.user_model import User

migrate = Migrate()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app

