from flask import jsonify, request
from services.task_service import (
    create_task,
    delete_task,
    get_current_user_id,
    get_user_tasks,
    update_task,
)


def register_task_routes(app):
    @app.route("/tasks", methods=["GET"])
    def get_tasks_handler():
        user_id, error = get_current_user_id()
        if error:
            return error

        tasks = get_user_tasks(user_id)
        return jsonify({"tasks": tasks}), 200

    @app.route("/tasks", methods=["POST"])
    def create_task_handler():
        user_id, error = get_current_user_id()
        if error:
            return error

        data = request.get_json() or {}
        title = data.get("title")

        if not title:
            return jsonify({"error": "Task title is required"}), 400

        task = create_task(
            user_id=user_id,
            title=title,
            description=data.get("description", ""),
        )
        return (
            jsonify({"message": "Task created successfully", "task": task}),
            201,
        )

    @app.route("/tasks/<task_id>", methods=["PUT"])
    def update_task_handler(task_id):
        user_id, error = get_current_user_id()
        if error:
            return error

        data = request.get_json() or {}
        task = update_task(task_id=task_id, user_id=user_id, updates=data)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        return (
            jsonify({"message": "Task updated successfully", "task": task}),
            200,
        )

    @app.route("/tasks/<task_id>", methods=["DELETE"])
    def delete_task_handler(task_id):
        user_id, error = get_current_user_id()
        if error:
            return error

        success = delete_task(task_id=task_id, user_id=user_id)
        if not success:
            return jsonify({"error": "Task not found"}), 404

        return jsonify({"message": "Task deleted successfully"}), 200