# services.py
import os
from werkzeug.utils import secure_filename
from app.storage import save_file
from app.utils import validate_csv
from app.config import Config

def process_file(file):
    """
    Process the uploaded CSV file, validate its content and save it to storage.
    """
    filename = secure_filename(file.filename)  # Secure the filename to avoid issues
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)  # Construct the path to save the file

    # Validate the CSV file content
    if not validate_csv(file):
        return {'message': 'File validation failed', 'status_code': 400}

    # Save the file to storage
    try:
        save_file(file, file_path)
        return {'message': 'File uploaded successfully', 'status_code': 201, 'file_id': filename}
    except Exception as e:
        return {'message': f'File upload failed: {str(e)}', 'status_code': 500}
