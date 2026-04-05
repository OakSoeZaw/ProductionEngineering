from flask import Blueprint, jsonify, request
from peewee import DoesNotExist
from datetime import datetime

from app.models.url import Url
from app.models.user import User
from app.models.event import Event
from app.services.generateShortCode import generate_short_code

urls_bp = Blueprint("urls", __name__)

@urls_bp.route("/urls", methods=["POST"])
def postUrl():
    data = request.get_json()
    if not data:
        return jsonify({"error": "need Json data"}), 400
    userId = data.get("user_id")
    user = User.get_or_none(User.id == userId)
    if not user:
        return jsonify({"error": "User not found"}), 400
    originalUrl = data.get("original_url")
    title = data.get("title")

    shortUrl = generate_short_code()
    url = Url.create(
        user = user,
        short_code = shortUrl,
        original_url = originalUrl,
        title = title,
        is_active = True,
    )
    Event.create(
        url = url,
        user = user,
        event_type ="created",
        details = {
            "short_code" : url.short_code,
            "original_url" : url.original_url 
        }
    )

    return jsonify({
        "id": url.id,
        "user_id": url.user.id,
        "short_code": url.short_code,
        "original_url": url.original_url,
        "title": url.title,
        "is_active": url.is_active,
        "created_at": url.created_at.isoformat(),
        "updated_at": url.updated_at.isoformat(),
    }), 201

@urls_bp.route("/urls", methods=["GET"])
def getUrl():
    urls = Url.select()
    return jsonify([{
        "id": url.id,
        "user_id": url.user.id,
        "short_code": url.short_code,
        "original_url": url.original_url,
        "title": url.title,
        "is_active": url.is_active,
        "created_at": url.created_at.isoformat(),
        "updated_at": url.updated_at.isoformat(),
    } for url in urls]), 200

@urls_bp.route("/urls/<id>", methods=["GET"])
def getUrlById(id : int):
    try:
        url = Url.get_by_id(id)
    except DoesNotExist:
        return jsonify({"error": "Id not found"}), 404
    return jsonify({
        "id": url.id,
        "user_id": url.user.id,
        "short_code": url.short_code,
        "original_url": url.original_url,
        "title": url.title,
        "is_active": url.is_active,
        "created_at": url.created_at.isoformat(),
        "updated_at": url.updated_at.isoformat(),
    } ), 200

@urls_bp.route("/urls/<id>", methods =["PUT"])
def updateUrl(id: int):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data found "}), 400
    title = data.get("title")
    is_active = data.get("is_active")
    try:
        url = Url.get_by_id(id)
    except DoesNotExist :
        return jsonify({"error": "Url not found"}), 404
    url.title = title
    url.is_active = is_active
    url.updated_at = datetime.now()
    url.save()

    Event.create(
        url = url,
        user = url.user,
        event_type = "updated",
        details = {
            "short-code" : url.short_code,
            "original_url" : url.original_url
        }
    )

    return jsonify({
        "id": url.id,
        "user_id": url.user.id,
        "short_code": url.short_code,
        "original_url": url.original_url,
        "title": url.title,
        "is_active": url.is_active,
        "created_at": url.created_at.isoformat(),
        "updated_at": url.updated_at.isoformat(),
    }), 200