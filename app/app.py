# app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 1. Create the Flask app instance
app = Flask(__name__)
# 2. Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 4. Import the models AFTER the db is created to avoid circular imports
from .models import Client, Appointment
from .routes import api_bp

app.register_blueprint(api_bp)