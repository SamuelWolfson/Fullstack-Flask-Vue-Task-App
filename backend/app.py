import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from db.database import db
from routes.auth import register_auth_routes
from routes.tasks import register_task_routes


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "your-fallback-secret-key"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///app.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    limiter = Limiter(get_remote_address, app=app)

    register_auth_routes(app, limiter)
    register_task_routes(app, limiter)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)