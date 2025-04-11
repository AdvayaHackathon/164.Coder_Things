import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists (for local development)
load_dotenv()

class Config:
    """Base configuration class."""
    # Secret key for Flask sessions, CSRF protection, etc.
    # Generate a strong random key in production!
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_default_secret_key_for_dev')

    # Google Cloud Project ID (often needed by client libraries)
    GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT')
    
    # Google Cloud API credentials path
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    
    # API Keys
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
    GOOGLE_TRANSLATE_API_KEY = os.environ.get('GOOGLE_TRANSLATE_API_KEY')
    GOOGLE_VISION_API_KEY = os.environ.get('GOOGLE_VISION_API_KEY')
    
    # Firebase/Firestore Configuration (COMMENTED OUT)
    # FIREBASE_API_KEY = os.environ.get('FIREBASE_API_KEY')
    # FIREBASE_AUTH_DOMAIN = os.environ.get('FIREBASE_AUTH_DOMAIN')
    # FIREBASE_PROJECT_ID = os.environ.get('FIREBASE_PROJECT_ID')
    # FIREBASE_STORAGE_BUCKET = os.environ.get('FIREBASE_STORAGE_BUCKET')
    # FIREBASE_MESSAGING_SENDER_ID = os.environ.get('FIREBASE_MESSAGING_SENDER_ID')
    # FIREBASE_APP_ID = os.environ.get('FIREBASE_APP_ID')
    
    # Optional Third-party Services
    # OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
    # CURRENCY_CONVERSION_API_KEY = os.environ.get('CURRENCY_CONVERSION_API_KEY')

class DevelopmentConfig(Config):
    """Development specific configuration."""
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'

class ProductionConfig(Config):
    """Production specific configuration."""
    DEBUG = False
    # Add any production-specific settings here

# Select configuration based on environment variable (e.g., FLASK_ENV)
config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
)