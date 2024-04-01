"""
Configuration settings for the Flask application.

This file contains configuration variables used by the Flask app. These variables
control various aspects of the application, such as database connection settings,
security configurations, and other options.

Attributes:
    SECRET_KEY (str): Secret key used by Flask for cryptographic functions. It's
        recommended to set this to a random string of characters to enhance security.
    SQLALCHEMY_DATABASE_URI (str): URI for the database connection. This specifies
        the database type, location, credentials, and database name.
    DEBUG (bool): Flag indicating whether debug mode is enabled. Debug mode provides
        detailed error messages and enables various debugging features. It should be
        disabled in production environments.
"""

from dotenv import load_dotenv
import os

class Config:
    # Load environment variables from .env file
    load_dotenv()

    # The app secret key string for usnig cockies and sessions
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    # The app database link ("if not created the flask app will create it")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # This logic var tell the flask app if we where in devolpment env or production env
    DEBUG = True
