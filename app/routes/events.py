from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

from app.models.user import User
from app.models.url import Url
from app.models.event import Event

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["GET"])
def getEvent():
    events = Event.select()
    return jsonify([{
        "id": event.id,
        "url_id" : event.url.id,
        "user_id" : event.user.id,
        "event_type": event.event_type,
        "timestamp": event.timestamp.isoformat(),
        "details": {
            "short_code": event.url.short_code,
            "original_url": event.url.original_url,
        },
    } for event in events]), 200