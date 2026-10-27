# Import the Flask class so we can create a web application.
from flask import Flask

# Create the Flask application object.
app = Flask(__name__)

# Tell Flask that this function handles requests to the home page.
@app.route("/")
# Define the function that runs when someone opens the home page.
def home():
    # Display a welcome message in the browser.
    return "Welcome to Café Calle Ocho"

# Tell Flask that this function handles requests to the about page.
@app.route("/about")
# Define the function that runs when someone opens the about page.
def about():
    # Display information about the café in the browser.
    return "Café Calle Ocho is a neighborhood café serving coffee and light meals."
