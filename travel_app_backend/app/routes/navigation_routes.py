from flask import Blueprint, request, jsonify
from app.services import maps_service

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/route', methods=['GET'])
def navigation():
    """Endpoint for navigation routes."""
    origin = request.args.get('origin')  # e.g., "lat,lon" or address
    destination = request.args.get('destination')
    mode = request.args.get('mode', 'driving')  # Default to driving

    if not origin or not destination:
        return jsonify({"error": "Missing origin or destination query parameters"}), 400

    valid_modes = ['driving', 'walking', 'bicycling', 'transit']
    if mode not in valid_modes:
        return jsonify({"error": f"Invalid mode. Valid modes are: {', '.join(valid_modes)}"}), 400

    try:
        route_details = maps_service.get_navigation_details(origin, destination, mode)
        return jsonify(route_details)
    except Exception as e:
        print(f"Error in /navigation/route endpoint: {e}")
        return jsonify({"error": "Failed to get navigation details due to an internal error"}), 500