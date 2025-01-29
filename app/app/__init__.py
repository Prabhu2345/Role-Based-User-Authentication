from flask import Flask
from app.config import Config
from app.routes import api_blueprint  # Import your routes/blueprint

def create_app():
    """
    Function to initialize and configure the Flask app
    """
    app = Flask(__name__)  # Initialize Flask app

    # Load app configuration
    app.config.from_object(Config)

    # Register any blueprints (API routes, etc.)
    app.register_blueprint(api_blueprint, url_prefix='/')  # Register routes

    return app
    
