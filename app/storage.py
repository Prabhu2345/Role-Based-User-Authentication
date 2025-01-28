# storage.py
import os
from app.config import Config

def save_file(file, file_path):
    """
    Save the uploaded file to the specified location.
    """
    try:
        file.save(file_path)  # Save the file to the specified path
    except Exception as e:
        raise e  # If saving fails, raise the exception to be handled by the calling function

def get_file_status(file_id):
    """
    Retrieve the status of the uploaded file based on its file_id.
    """
    file_path = os.path.join(Config.UPLOAD_FOLDER, file_id)  # Construct the file path
    if os.path.exists(file_path):  # Check if the file exists
        return {'file_id': file_id, 'status': 'Uploaded'}  # Return status if file exists
    return None  # Return None if file doesn't exist
