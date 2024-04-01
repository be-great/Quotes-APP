"""
__init__.py file serves as the entry point for the Flask application package.
we call the libs that we need and create un instance of the flask main class called "quotes_app", set the config file and database connection settings and then return
the app instance
"""

from flask import Flask
from app.config import Config

# The app instance function
def create_app(config_class=Config):
    # The Flask class instaince 
    quotes_app = Flask(__name__)
    # Import the configration from config file
    quotes_app.config.from_object(Config)
    
    # Import routes module to ensure routes are registered using blueprrint
    from app.routes import home_page, author_page
    quotes_app.register_blueprint(home_page)
    quotes_app.register_blueprint(author_page)

    # Return the app object 
    return quotes_app
