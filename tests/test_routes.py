import os
import io
import pytest
from app.app import create_app, db

@pytest.fixture
def client():
    # Set up a Flask test client and application context
    app = create_app()
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = 'C:/Users/sinha/Desktop/cloud native project/uploads'  # Updated folder path
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing

    with app.app_context():
        db.create_all()  # Create tables for test database
        yield app.test_client()  # Return the test client for usage

    # Teardown: remove test files and data
    with app.app_context():
        db.drop_all()
        if os.path.exists(app.config['UPLOAD_FOLDER']):
            for f in os.listdir(app.config['UPLOAD_FOLDER']):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

# Test for the index route
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Upload Your CSV File" in response.data

# Test for file upload route with valid CSV
def test_upload_file_success(client):
    data = {
        'file': (io.BytesIO(b"sample,data\n1,2\n3,4\n"), 'test.csv')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b"file_id" in response.data

# Test for file upload route with invalid file type
def test_upload_file_invalid_type(client):
    data = {
        'file': (io.BytesIO(b"sample data"), 'test.txt')  # Invalid file extension
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert b"Invalid file type" in response.data

# Test for file status route with valid file_id
def test_file_status_success(client):
    # First upload a file to get a valid file_id
    data = {
        'file': (io.BytesIO(b"sample,data\n1,2\n3,4\n"), 'test.csv')
    }
    upload_response = client.post('/upload', data=data, content_type='multipart/form-data')
    file_id = upload_response.get_json().get('file_id')

    # Now check the status of the uploaded file
    response = client.get(f'/status/{file_id}')
    assert response.status_code == 200
    assert b"status" in response.data

# Test for file status route with invalid file_id
def test_file_status_invalid(client):
    response = client.get('/status/invalid_file_id')
    assert response.status_code == 404
    assert b"File not found" in response.data
