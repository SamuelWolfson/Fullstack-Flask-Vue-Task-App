import os
import jwt
from flask import jsonify, request
from db.database import db
from db.models import Task

SECRET_KEY = os.environ.get("SECRET_KEY", "your-fallback-secret-key")


def create_task(user_id, title, description=""):
    if not title:
        return None

    new_task = Task(
        user_id=user_id, title=title.strip(), description=description.strip()
    )
    try:
        db.session.add(new_task)
        db.session.commit()

        if hasattr(new_task, "to_dict"):
            return new_task.to_dict()

        return {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed,
            "user_id": new_task.user_id,
        }
    except Exception as e:
        db.session.rollback()
        return None


def verify_auth_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id"), None
    except jwt.ExpiredSignatureError:
        return None, (jsonify({"error": "Token has expired"}), 401)
    except jwt.InvalidTokenError:
        return None, (jsonify({"error": "Invalid authentication token"}), 401)


def get_current_user_id():
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return None, (jsonify({"error": "Authorization token required"}), 401)

    token = auth_header.split(" ")[1]
    return verify_auth_token(token)


def get_user_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return [task.to_dict() for task in tasks]


def update_task(task_id, user_id, updates):
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return None

    if "title" in updates and updates["title"]:
        task.title = updates["title"].strip()
    if "description" in updates:
        task.description = updates["description"].strip()
    if "completed" in updates:
        task.completed = bool(updates["completed"])

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return None

    if hasattr(task, "to_dict"):
        return task.to_dict()

    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "user_id": task.user_id,
    }


def delete_task(task_id, user_id):
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return None

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return None
