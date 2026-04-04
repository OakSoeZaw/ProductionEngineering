from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

from app.models.user import User
from app.services.csv_import import import_users_from_file

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods = ["GET"])
def list_users():
    users = User.select()
    return jsonify([{
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "created_at": u.created_at,
    } for u in users])

@users_bp.route("/users/bulk", methods = ["POST"])
def post_users():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    
    try:
        imported = import_users_from_file(file.stream)
        return jsonify({"imported": imported}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@users_bp.route("/users/<id>", methods=["GET"])
def getUserByID(id: int):
    user = User.get_or_none(User.id == id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(model_to_dict(user))
