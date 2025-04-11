from flask import Blueprint, request, jsonify
from app.services import vision_service

image_bp = Blueprint('image', __name__)

@image_bp.route('/info', methods=['POST'])
def image_info():
    """Endpoint to get info from an image."""
    if 'image' not in request.files:
        return jsonify({"error": "No image file found in request (expected key 'image')"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        image_data = file.read()  # Read image bytes
        info = vision_service.get_info_from_image_via_api(image_data)
        return jsonify(info)
    except Exception as e:
        print(f"Error in /image/info endpoint: {e}")
        return jsonify({"error": "Failed to process image due to an internal error"}), 500