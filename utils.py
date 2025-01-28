# utils.py
import csv
from app.config import Config

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS  # Check extension against allowed types

def validate_csv(file):
    """
    Validate the content of the CSV file. In this case, we're just checking if it has rows of data.
    """
    try:
        file.seek(0)  # Reset file pointer to the beginning
        csv_reader = csv.reader(file)  # Read the CSV file
        for row in csv_reader:
            # Implement specific row validation rules if needed
            if len(row) == 0:  # If an empty row is found, the file is considered invalid
                return False
        return True  # If no issues, return True (file is valid)
    except Exception:
        return False  # Return False if an error occurs during CSV reading
