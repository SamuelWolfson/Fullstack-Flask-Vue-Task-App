import os
from datetime import datetime, timedelta, timezone
from functools import wraps
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS  # type: ignore
from flask_mailman import EmailMessage, Mail  # type: ignore
from flask_sqlalchemy import SQLAlchemy
import jwt  # type: ignore
from werkzeug.security import check_password_hash, generate_password_hash

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "flask_tasks")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "super-secret-dev-key")

ENCODED_PASSWORD = quote_plus(DB_PASSWORD)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{ENCODED_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Mail Configuration
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")

mail = Mail(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    tasks = db.relationship(
        "Task", backref="user", lazy=True, cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=86400):
        payload = {
            "user_id": self.id,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in),
        }
        return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    def get_reset_token(self, expires_in=900):
        payload = {
            "user_id": self.id,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in),
        }
        return jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    @staticmethod
    def verify_reset_token(token):
        try:
            payload = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            return db.session.get(User, payload["user_id"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError):
            return None

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "user_id": self.user_id,
        }


# Authentication Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token is missing"}), 401

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = db.session.get(User, payload["user_id"])
            if not current_user:
                return jsonify({"error": "User no longer exists"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# User Routes
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}

    if not all(k in data for k in ("email", "password")):
        return (
            jsonify({"error": "Email and password are required"}),
            400,
        )

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(email=data["email"])
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    token = new_user.generate_auth_token()
    return jsonify({"user": new_user.to_dict(), "token": token}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    token = user.generate_auth_token()
    return jsonify({"user": user.to_dict(), "token": token}), 200


@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json() or {}
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        reset_token = user.get_reset_token()
        reset_url = f"http://localhost:5173/reset-password?token={reset_token}"
        msg = EmailMessage(
            subject="Password Reset Request",
            body=(
                f"Hello,\n\n"
                "You requested a password reset. Click the link below to set a new password:\n\n"
                f"{reset_url}\n\n"
                "This link will expire in 15 minutes.\n\n"
                "If you did not request this, please ignore this email."
            ),
            to=[user.email],
        )
        try:
            msg.send()
        except Exception as e:
            return (
                jsonify({"error": "Failed to send email", "details": str(e)}),
                500,
            )

    return (
        jsonify(
            {
                "message": "If an account with that email exists, a reset link has been sent."
            }
        ),
        200,
    )


@app.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json() or {}
    token = data.get("token")
    new_password = data.get("password")

    if not token or not new_password:
        return jsonify({"error": "Token and new password are required"}), 400

    user = User.verify_reset_token(token)
    if not user:
        return jsonify({"error": "Invalid or expired token"}), 400

    user.set_password(new_password)
    db.session.commit()

    return jsonify({"message": "Password updated successfully"}), 200


# Protected Task Routes
@app.route("/tasks", methods=["GET"])
@token_required
def get_tasks(current_user):
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([t.to_dict() for t in tasks])


@app.route("/tasks/<int:task_id>", methods=["GET"])
@token_required
def get_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict())


@app.route("/tasks", methods=["POST"])
@token_required
def create_task(current_user):
    data = request.get_json() or {}

    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(
        title=data["title"],
        completed=data.get("completed", False),
        user_id=current_user.id,
    )

    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201


@app.route("/tasks/<int:task_id>", methods=["PATCH"])
@token_required
def update_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json() or {}

    if "title" in data:
        task.title = data["title"]
    if "completed" in data:
        task.completed = data["completed"]

    db.session.commit()
    return jsonify(task.to_dict()), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@token_required
def delete_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": f"Task {task_id} deleted successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)