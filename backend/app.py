import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from db.database import db
from routes.auth import register_auth_routes
from routes.tasks import register_task_routes


def create_app():
    app = Flask(__name__)

    db_user = os.environ.get("DB_USER", "postgres")
    db_password = os.environ.get("DB_PASSWORD", "sw130706")
    db_host = os.environ.get("DB_HOST", "localhost")
    db_port = os.environ.get("DB_PORT", "5432")
    db_name = os.environ.get("DB_NAME", "flask_tasks")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your-fallback-secret-key")

    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", 587))
    app.config["MAIL_USE_TLS"] = (
        os.environ.get("MAIL_USE_TLS", "True").lower() == "true"
    )
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

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
