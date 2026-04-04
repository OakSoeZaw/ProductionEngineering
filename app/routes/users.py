from flask import Blueprint, jsonify
from playhouse.shortcuts import model_to_dict

from app.models.user import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/users")
def list_users():
    users = User.select()
    return jsonify([model_to_dict(u) for u in users])