from flask import jsonify, request
from db.database import db
from db.models import User
from services.mail_service import send_reset_email

from services.auth_service import (get_email_rate_limit_key,
                                   authenticate_user,
                                     create_user)



def register_auth_routes(app, limiter):

    @app.route("/reset-password", methods=["POST"])
    @limiter.limit("1 per 30 seconds", key_func=get_email_rate_limit_key)
    def send_password_reset_email():
        data = request.get_json() or {}
        email = data.get("email")

        if not email:
            return jsonify({"error": "Email is required"}), 400

        user = User.query.filter_by(email=email).first()

        if user:
            reset_token = user.get_reset_token()
            try:
                send_reset_email(user, reset_token)
            except Exception as e:
                return (
                    jsonify(
                        {"error": "Failed to send email", "details": str(e)}
                    ),
                    500,
                )

        return (
            jsonify(
                {
                    "message": "If an account with that email exists, a reset link has been sent.",
                    "redirect_url": "https://mail.google.com/",
                }
            ),
            200,
        )

    @app.route("/register", methods=["POST"])
    def register_user():
            data = request.get_json() or {}
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return jsonify({"error": "Email and password are required"}), 400

            email = email.lower().strip()

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return jsonify({"error": "Email is already registered"}), 409

            try:
                new_user = create_user(email, password)
                return (
                    jsonify(
                        {
                            "message": "User registered successfully",
                            "user": {"id": new_user.id, "email": new_user.email},
                        }
                    ),
                    201,
                )
            except Exception as e:
                db.session.rollback()
                return (
                    jsonify({"error": "Registration failed", "details": str(e)}),
                    500,
                )

    @app.route("/login", methods=["POST"])
    def login_user():
        data = request.get_json() or {}
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        token = authenticate_user(email, password)
        if not token:
            return jsonify({"error": "Invalid credentials, change them"}), 401

        return jsonify({"message": "Login successful", "token": token}), 200