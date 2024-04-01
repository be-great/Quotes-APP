# routes.py

"""
Flask Blueprint for the main home page.

This module defines a Flask Blueprint named 'home_page' for handling routes related to the main home page of the application. 
The Blueprint is responsible for rendering the home page template and serving static files.

Attributes:
    home_page: A Flask Blueprint instance for the main home page.
"""

from flask import render_template
from flask import Blueprint

# Define the main Blueprint for the home page
home_page = Blueprint('home', __name__,
    template_folder='templates',
    static_folder='static')


@home_page.route("/")
@home_page.route("/home")
def home():
    """
    Route handler for the main home page.

    Returns:
        str: A string representing the HTML content to be displayed on the home page.
    """
    return ("<h1>Test from the server, the home route</h1>")


# Define the main Blueprint for the quotes author
author_page = Blueprint('author', __name__,
    template_folder='templates',
    static_folder='static')

@author_page.route("/author")
def author():
    return ("<h1>Test from the server, the author route</h1>")