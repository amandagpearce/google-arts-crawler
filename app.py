import os

from flask_cors import CORS
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from resources.image import blp as ImageBlueprint

from db import db
import models  # noqa


def create_app(db_url=None):  # factory pattern
    app = Flask(__name__)
    CORS(app)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Google Arts Crawler REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/doc"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL",
        "sqlite:///database.db",  # default to sqlite if no database_url
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)  # initializes sqlalchemy
    migrate = Migrate(app, db)  # noqa
    api = Api(app)

    with app.app_context():
        db.create_all()  # creating the db

    api.register_blueprint(ImageBlueprint)

    return app
