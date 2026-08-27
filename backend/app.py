import os
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote_plus
from flask import request, Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "flask_tasks")

app = Flask(__name__)

ENCODED_PASSWORD = quote_plus(DB_PASSWORD)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{ENCODED_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


def to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed,
    }


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([to_dict(t) for t in tasks])


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)

    return jsonify(to_dict(task))


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=data["title"], completed=data.get("completed", False))

    db.session.add(new_task)
    db.session.commit()
    return (
        jsonify(to_dict(new_task)),
        201,
    )


@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):

    task = Task.query.get_or_404(task_id)
    data = request.get_json() or {}

    if "title" in data:
        task.title = data["title"]
    if "completed" in data:
        task.completed = data["completed"]

    db.session.commit()

    return (
        jsonify(to_dict(task)),
        200,
    )


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": f"Task {task_id} deleted successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
