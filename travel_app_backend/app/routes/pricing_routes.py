from flask import Blueprint, request, jsonify
from app.services import pricing_service

pricing_bp = Blueprint('prices', __name__)

@pricing_bp.route('/guide', methods=['GET'])
def price_guide():
    """Endpoint for the price guide."""
    category = request.args.get('category')  # e.g., "museum", "meal", "taxi"
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not category or not lat or not lon:
        return jsonify({"error": "Missing category, latitude, or longitude query parameters"}), 400

    try:
        # Validate lat/lon format if necessary
        location = {"lat": float(lat), "lon": float(lon)}
        prices = pricing_service.get_price_guide_info(category, location)
        return jsonify(prices)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude format"}), 400
    except Exception as e:
        print(f"Error in /prices/guide endpoint: {e}")
        return jsonify({"error": "Failed to get price information due to an internal error"}), 500