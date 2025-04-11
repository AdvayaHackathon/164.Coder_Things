from flask import Blueprint, request, jsonify
from app.services import guide_service

guide_bp = Blueprint('guide', __name__)

@guide_bp.route('/ask', methods=['GET'])
def digital_guide():
    """Endpoint for the digital guide."""
    topic = request.args.get('topic')  # e.g., "Eiffel Tower", "Louvre Museum"
    personality = request.args.get('personality', 'serious')  # 'serious', 'funny', 'friendly'

    if not topic:
        return jsonify({"error": "Missing topic query parameter"}), 400

    # Validate personality
    valid_personalities = ['serious', 'funny', 'friendly']
    if personality not in valid_personalities:
        personality = 'serious'  # Default to serious if invalid

    try:
        response_text = guide_service.get_digital_guide_response(topic, personality)
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error in /guide/ask endpoint: {e}")
        return jsonify({"error": "Failed to get guide response due to an internal error"}), 500