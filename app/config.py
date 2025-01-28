import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Default value for local testing
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', os.path.join(os.getcwd(), 'uploads'))  # Default to 'uploads' folder in project root
    ALLOWED_EXTENSIONS = {'csv'}  # Allowed file extensions for upload
    SQLALCHEMY_TRACK_MODIFICATIONS = False
