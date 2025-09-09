# app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 1. Create the Flask app instance
app = Flask(__name__)
# 2. Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db' # Corrected path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 4. Import the models AFTER the db is created to avoid circular imports
from .models import Client, Appointment

# 5. A simple route to test the app is running
@app.route('/')
def index():
    return "<h1>Trainer App Backend</h1>"

# Note: The 'if __name__ == "__main__"' block is no longer needed here
# because we will run the app using the 'flask run' command.