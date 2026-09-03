import os
import jwt
from flask import jsonify, request

SECRET_KEY = os.environ.get("SECRET_KEY", "your-fallback-secret-key")


def verify_auth_token(token):
    """Decodes the JWT token and returns user_id if valid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id"), None
    except jwt.ExpiredSignatureError:
        return None, (jsonify({"error": "Token has expired"}), 401)
    except jwt.InvalidTokenError:
        return None, (jsonify({"error": "Invalid authentication token"}), 401)


def get_current_user_id():
    """Validates the Authorization header and returns (user_id, error_response)."""
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return None, (jsonify({"error": "Authorization token required"}), 401)

    token = auth_header.split(" ")[1]
    return verify_auth_token(token)