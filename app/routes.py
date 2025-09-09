from flask import Blueprint, jsonify

from .models import Client, Appointment
# A Blueprint is a way to organize a group of related routes.
# We'll name it 'api' and use the '/api' prefix for all routes in this file.
api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

# This defines our first route.
# It will be accessible at http://127.0.0.1:5555/api/hello
@api_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Trainer App API!"})

@api_bp.route('/clients')
def get_clients():
    # 1. Query the database to get all Client objects
    clients = Client.query.all()

    # 2. Convert the list of objects into a list of dictionaries
    # The to_dict() method comes from the SerializerMixin
    clients_dict = [client.to_dict() for client in clients]

    # 3. Return the list as a JSON response
    return jsonify(clients_dict), 200

@api_bp.route('/clients/<int:id>')
def get_client_by_id(id):
    # 1. Query the database for the client with the given id
    client = Client.query.get(id)

    # 2. Check if a client was found
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    
    # 3. Convert the client object to a dictionary
    client_dict = client.to_dict()

    # 4. Return the dictionary as a JSON response
    return jsonify(client_dict), 200

@api_bp.route('/appointments')
def get_appointments():
    appointments = Appointment.query.all()
    appointments_dict = [appointment.to_dict() for appointment in appointments]
    return jsonify(appointments_dict), 200

@api_bp.route('/appointments/<int:id>')
def get_appointment_by_id(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({'error': 'Appointment not found'}), 404
    appointment_dict = appointment.to_dict()
    return jsonify(appointment_dict), 200




