import os
from app import create_app

# Determine the configuration name from environment variable or default
# Example: Set FLASK_ENV=production or FLASK_ENV=development
config_name = os.getenv('FLASK_ENV', 'default')

# Create the Flask app instance using the factory
app = create_app(config_name)

if __name__ == '__main__':
    # Get port from environment variable or default to 8080 (common for cloud)
    port = int(os.environ.get('PORT', 8080))

    # Get host from environment variable. Default to '0.0.0.0' to be accessible
    # externally (important for Docker/Cloud Run). Use '127.0.0.1' for local only.
    host = os.environ.get('HOST', '0.0.0.0')

    # Run the app using Flask's development server (for development)
    # For production, use a WSGI server like Gunicorn:
    # gunicorn --bind 0.0.0.0:8080 run:app
    print(f"Starting Flask app on {host}:{port}...")
    app.run(host=host, port=port)