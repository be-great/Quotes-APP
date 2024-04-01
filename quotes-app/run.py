# run.py
"""
Main script to run the Flask application.

This script serves as the entry point for running the Flask application. It creates an instance of the Flask app using the create_app function from the app module, and then runs the app using the run method.

Usage:
    Run this script directly to start the Flask application.

Example:
    To start the Flask application:
        $ python run.py
"""

# Import the create_app function from the app module
from app import create_app

# Create an instance of the Flask app
quotes_app = create_app()

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    quotes_app.run()
