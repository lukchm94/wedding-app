from app import create_app

from src.shared.db.migrate import run_migrations

if __name__ == "__main__":
    run_migrations()

    app = create_app()
    app.run(host="localhost", port=3000)
