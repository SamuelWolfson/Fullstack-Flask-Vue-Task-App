import os
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:YOUR_ACTUAL_PASSWORD@localhost:5432/flask_tasks'