from flask import Blueprint, request, jsonify
from app.services import transport_service

transport_bp = Blueprint('transport', __name__)

@transport_bp.route('/assist', methods=['GET'])
def transport_assist():
    """Endpoint for local transport assistance."""
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Missing latitude or longitude query parameters"}), 400

    try:
        # Validate lat/lon format if necessary
        location = {"lat": float(lat), "lon": float(lon)}
        transport_options = transport_service.get_local_transport_info(location)
        return jsonify(transport_options)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude format"}), 400
    except Exception as e:
        print(f"Error in /transport/assist endpoint: {e}")
        return jsonify({"error": "Failed to get transport information due to an internal error"}), 500