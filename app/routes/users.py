from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

from app.models.user import User
from app.services.csv_import import import_users_from_file

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods = ["GET"])
def list_users():
    page = request.args.get("page",1, type = int)
    per_page = request.args.get("per_page", 10, type = int)
    users = User.select().paginate(page,per_page)
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

@users_bp.route("/users", methods=["POST"])
def createUser():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No Json Provided"}),400
    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"error": "username and email are required"}), 400

    if not isinstance(username, str):
        return jsonify({"error": "Can't have integer as Username"}),422
    
    if not isinstance(email, str):
        return jsonify({"error": "email must be a string"}), 422

    user = User.create(username= username, email= email)
    return jsonify(
        model_to_dict(user)
    ), 201

@users_bp.route("/users/<id>", methods=["PUT"])
def updateUser(id: int):
    data = request.get_json()
    if not data:
        return jsonify({"error": "New username needed"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "User not found"}), 400
    try:
        user = User.get_by_id(id)
    except User.DoesNotExist:
        return jsonify({"error": "User not found"}), 404
    
    user.username = username
    user.save()
    return jsonify(model_to_dict(user)), 200