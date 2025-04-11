from flask import Blueprint, request, jsonify
from app.services import translation_service

translation_bp = Blueprint('translate', __name__)

@translation_bp.route('/', methods=['POST'])
def translate():
    """Endpoint for text translation."""
    data = request.get_json()
    if not data or 'text' not in data or 'target_language' not in data:
        return jsonify({"error": "Missing 'text' or 'target_language' in request body"}), 400

    try:
        translated_text = translation_service.translate_text_via_api(data['text'], data['target_language'])
        return jsonify({"original": data['text'], "translated": translated_text, "target_language": data['target_language']})
    except Exception as e:
        print(f"Error in /translate endpoint: {e}")
        return jsonify({"error": "Translation failed due to an internal error"}), 500