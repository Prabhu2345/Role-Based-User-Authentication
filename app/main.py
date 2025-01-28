from app.app import create_app  # Import the create_app function

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
