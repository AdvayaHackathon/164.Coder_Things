from flask import Blueprint, request, jsonify
from app.services import itinerary_service

itinerary_bp = Blueprint('itinerary', __name__)

@itinerary_bp.route('/generate', methods=['POST'])
def create_itinerary():
    """Endpoint to generate a travel itinerary."""
    prefs = request.get_json()
    if not prefs:
        return jsonify({"error": "Missing preferences in request body"}), 400

    try:
        itinerary = itinerary_service.generate_itinerary_logic(prefs)
        return jsonify(itinerary)
    except Exception as e:
        print(f"Error in /itinerary/generate endpoint: {e}")
        return jsonify({"error": "Failed to generate itinerary due to an internal error"}), 500