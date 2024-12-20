import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import DbConfig

load_dotenv()


class Database:
    db_config: DbConfig
    db: SQLAlchemy

    def __init__(self):
        self.db_config = DbConfig(
            user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD")
        )
        self.db = SQLAlchemy()

    @property
    def db_uri(self) -> str:
        return f"mysql+pymysql://{self.db_config.user}:{self.db_config.password}@{self.db_config.host}:{self.db_config.port}/{self.db_config.name}"

    def init_app(self, app: Flask) -> None:
        """
        Initialize the database with the Flask app.
        """
        app.config["SQLALCHEMY_DATABASE_URI"] = self.db_uri
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.db.init_app(app)
