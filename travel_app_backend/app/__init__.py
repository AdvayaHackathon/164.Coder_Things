from flask import Flask
# Firebase/Firestore import commented out
# from google.cloud import firestore
import os

# Import configuration
from config import config_by_name

# --- Initialize Firestore DB ---
# Commented out Firebase initialization
# db = None
# try:
#     db = firestore.Client()
#     print("Firestore client initialized successfully.")
# except Exception as e:
#     print(f"Error initializing Firestore client: {e}")

# Dummy in-memory database to replace Firestore
class DummyDB:
    """A simple in-memory database to replace Firestore functionality."""
    def __init__(self):
        self.collections = {
            'hidden_gems': [
                {"name": "Secret Waterfall", "lat": 12.9716, "lon": 77.5946, 
                 "description": "A beautiful hidden waterfall surrounded by lush greenery.", "source": "dummy_db"},
                {"name": "Local Artisan Market", "lat": 12.9720, "lon": 77.5950, 
                 "description": "Great local crafts and authentic cultural items sold by locals.", "source": "dummy_db"},
                {"name": "Hidden Viewpoint", "lat": 12.9730, "lon": 77.5940, 
                 "description": "A secluded spot with panoramic city views, perfect at sunset.", "source": "dummy_db"},
                {"name": "Underground Cafe", "lat": 12.9700, "lon": 77.5980, 
                 "description": "A charming cafe known only to locals with amazing coffee.", "source": "dummy_db"}
            ]
        }
    
    def collection(self, name):
        """Mock Firestore collection method"""
        if name not in self.collections:
            self.collections[name] = []
        return DummyCollection(self.collections[name])

class DummyCollection:
    """A simple collection implementation to mimic Firestore collections."""
    def __init__(self, data):
        self.data = data
    
    def stream(self):
        """Mock Firestore stream method"""
        return [DummyDocument(item, i) for i, item in enumerate(self.data)]
    
    def document(self, doc_id=None):
        """Mock Firestore document method"""
        if doc_id is None:
            # Generate a new document ID
            new_id = str(len(self.data))
            self.data.append({})
            return DummyDocument({}, new_id)
        else:
            # Find existing document or create new
            for i, item in enumerate(self.data):
                if str(i) == doc_id:
                    return DummyDocument(item, doc_id)
            self.data.append({})
            return DummyDocument({}, doc_id)

class DummyDocument:
    """A simple document implementation to mimic Firestore documents."""
    def __init__(self, data, doc_id):
        self.data = data
        self.id = doc_id
    
    def get(self):
        """Mock Firestore get method"""
        return DummySnapshot(self.data)
    
    def set(self, data):
        """Mock Firestore set method"""
        self.data.update(data)
        return True

class DummySnapshot:
    """A simple snapshot implementation to mimic Firestore snapshots."""
    def __init__(self, data):
        self.data = data
    
    def exists(self):
        """Mock Firestore exists method"""
        return bool(self.data)
    
    def to_dict(self):
        """Mock Firestore to_dict method"""
        return self.data

# Initialize our dummy database
db = DummyDB()
print("Dummy database initialized as replacement for Firestore.")

# --- Initialize Third-Party API Clients (Example) ---
# You might initialize these here or within specific services if preferred
# from google.cloud import translate_v2 as translate
# from google.cloud import vision
# translate_client = translate.Client()
# vision_client = vision.ImageAnnotatorClient()


def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)

    # Load configuration
    config_object = config_by_name[config_name]
    app.config.from_object(config_object)

    print(f"Running with config: {config_name}")
    if config_object.DEBUG:
        print("Debug mode is ON")

    # --- Register Blueprints ---
    # Import blueprint objects here to avoid circular dependencies
    from .routes.main_routes import main_bp
    from .routes.gem_routes import gem_bp
    from .routes.translation_routes import translation_bp
    from .routes.itinerary_routes import itinerary_bp
    from .routes.image_routes import image_bp
    from .routes.navigation_routes import navigation_bp
    from .routes.transport_routes import transport_bp
    from .routes.pricing_routes import pricing_bp
    from .routes.guide_routes import guide_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(gem_bp, url_prefix='/gems')
    app.register_blueprint(translation_bp, url_prefix='/translate')
    app.register_blueprint(itinerary_bp, url_prefix='/itinerary')
    app.register_blueprint(image_bp, url_prefix='/image')
    app.register_blueprint(navigation_bp, url_prefix='/navigation')
    app.register_blueprint(transport_bp, url_prefix='/transport')
    app.register_blueprint(pricing_bp, url_prefix='/prices')
    app.register_blueprint(guide_bp, url_prefix='/guide')

    # You could add extensions like Flask-Login, CORS handling etc. here
    # from flask_cors import CORS
    # CORS(app) # Example: Enable CORS for all routes

    return app