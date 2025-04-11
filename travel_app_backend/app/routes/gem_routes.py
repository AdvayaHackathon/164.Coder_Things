from flask import Blueprint, request, jsonify
from app.services import gem_service

gem_bp = Blueprint('gems', __name__)

@gem_bp.route('/', methods=['GET'])
def hidden_gems():
    """Endpoint to get hidden gems."""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    user_prefs = {"interests": ["nature", "food"]}  # Example

    if not lat or not lon:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    try:
        gems = gem_service.get_hidden_gems_from_db({"lat": float(lat), "lon": float(lon)}, user_prefs)
        return jsonify(gems)
    except Exception as e:
        print(f"Error in /gems endpoint: {e}")
        return jsonify({"error": "Could not retrieve hidden gems due to an internal error"}), 500