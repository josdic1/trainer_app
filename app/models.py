from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
# Add 'association_proxy' to this import line
from sqlalchemy.ext.associationproxy import association_proxy

# Connect to the database instance from app.py
from .app import db

# Client 
class Client(db.Model, SerializerMixin):
    __tablename__ = 'clients'

    serialize_rules = ('-appointments.client',)

    appointment_reasons = association_proxy('appointments', 'reason')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)

    # One-to-many: one client → many appointments
    appointments = db.relationship("Appointment", back_populates="client")

    def __repr__(self):
        return f'<Client {self.id}: {self.name}>'

# Appointment    
class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    # Serialization
    # This rule does the reverse to prevent the same infinite loop.
    # It says: "When you serialize my client, don't serialize its 'appointments' attribute."
    serialize_rules = ('-client.appointments',)

    client_name = association_proxy("client", "name")

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String)

    # Foreign Key to CLIENT table
    client_id = db.Column(db.Integer,db.ForeignKey('clients.id'))

    # Many-to-one: each appointment belongs to one client
    client = db.relationship("Client", back_populates="appointments")

    def __repr__(self):
        return f'<Appointment {self.id} on {self.date}>'