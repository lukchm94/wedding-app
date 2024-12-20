from flask import Blueprint

# Create a Blueprint for the health route
health_bp = Blueprint("health", __name__)


@health_bp.route("/api/v1/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify if the server is running.
    """
    return {"status": "ok"}, 200
