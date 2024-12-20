from app import create_app
from flask_migrate import upgrade


def run_migrations():
    app = create_app()
    with app.app_context():
        upgrade()
