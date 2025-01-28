from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.utils import allowed_file
from app.services import process_file
from app.storage import get_file_status

# Define the main blueprint
api_blueprint = Blueprint('api', __name__)

# Route to serve the frontend HTML page
@api_blueprint.route('/')
def index():
    return render_template('index.html')

# API route for file upload
@api_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # Save the file to the specified upload folder

        # Process the file and return any results or status
        result = process_file(file)
        return jsonify(result), result['status_code']
    
    return jsonify({'error': 'Invalid file type'}), 400

# API route to check the file upload status
@api_blueprint.route('/status/<file_id>', methods=['GET'])
def file_status(file_id):
    status = get_file_status(file_id)
    if status:
        return jsonify(status), 200
    return jsonify({'error': 'File not found'}), 404
