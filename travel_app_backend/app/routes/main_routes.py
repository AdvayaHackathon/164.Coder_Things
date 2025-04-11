from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Basic health check endpoint."""
    return jsonify({"status": "ok", "message": "TravelApp Backend is running!"})