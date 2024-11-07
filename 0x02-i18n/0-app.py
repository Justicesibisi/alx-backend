#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Config class to hold app settings
class Config:
    """Configuration for language and timezone."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply the Config settings
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)
