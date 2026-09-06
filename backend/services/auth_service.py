from datetime import datetime, timedelta, timezone
import jwt
from flask import current_app, jsonify, request

from db.database import db
from db.models import User

def create_user(email, password):
    if not email or not password:
        return None

    email = email.lower().strip()

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return None

    new_user = User(email=email)
    new_user.set_password(password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return None, "Database error accurred while creating the user: " + str(e)
    return {
        "id": new_user.id,
        "email": new_user.email
        }, None
            


def authenticate_user(email, password):

    if not email or not password:
        return None

    email = email.lower().strip()

    user = User.query.filter_by(email=email).first()
    if not user:
        return None
    if not user.check_password(password):
        return None

    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    

def get_current_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None, (jsonify({"error": "Authorization token missing"}), 401)

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        user = db.session.get(User, payload["user_id"])
        if not user:
            return None, (jsonify({"error": "User no longer exists"}), 401)
        return user, None
    except jwt.ExpiredSignatureError:
        return None, (jsonify({"error": "Token has expired"}), 401)
    except jwt.InvalidTokenError:
        return None, (jsonify({"error": "Invalid token"}), 401)


def process_password_reset(token, new_password):
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        user = db.session.get(User, payload["user_id"])

        if not user:
            return "User not found", 404

        if payload.get("pwd_hash") != user.password_hash:
            return (
                "The password has already been updated using this link.",
                400,
            )

        user.set_password(new_password)
        db.session.commit()
        return "Password updated successfully", 200

    except jwt.ExpiredSignatureError:
        return "Reset link has expired", 400
    except jwt.InvalidTokenError:
        return "Invalid token", 400


def get_token_from_request():
    data = request.get_json(silent=True) or {}
    token = data.get("token") or request.args.get("token")

    if token:
        return f"token:{token}"

    return request.remote_addr

def get_email_rate_limit_key():
    data = request.get_json(silent=True) or {}
    email = data.get("email")

    if email:
        return f"reset_email:{email.lower().strip()}"

    return request.remote_addr