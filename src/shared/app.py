from flask import Flask
from flask_migrate import Migrate

from src.shared.db import Database
from src.shared.routers.health import health_bp

migrate: Migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)

    database = Database()

    app.config["SQLALCHEMY_DATABASE_URI"] = database.db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database.db.init_app(app)
    migrate.init_app(app, database.db)

    app.register_blueprint(health_bp)
    return app
