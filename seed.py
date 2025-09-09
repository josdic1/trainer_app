from faker import Faker
import random

# Import your Flask app and database models
from app.app import app
from app.models import db, Client, Appointment

# Initialize Faker
fake = Faker()

# Main seeding function
def seed_database():
    # This ensures the script runs within the Flask application context
    with app.app_context():
        print("Deleting old data...")
        # Clear out existing data to prevent duplicates when re-seeding
        Appointment.query.delete()
        Client.query.delete()

        print("Creating new clients...")
        clients = []
        for _ in range(10): # Create 10 fake clients
            client = Client(
                name=fake.name(),
                email=fake.unique.email()
            )
            clients.append(client)
        
        db.session.add_all(clients)
        db.session.commit()

        print("Creating new appointments...")
        appointments = []
        # Create 1 to 3 appointments for each client
        for client in clients:
            for _ in range(random.randint(1, 3)):
                appointment = Appointment(
                    date=fake.date_time_between(start_date='-1y', end_date='+1y'),
                    reason=random.choice(['Check-up', 'Consultation', 'Follow-up', 'New Program']),
                    client_id=client.id
                )
                appointments.append(appointment)
        
        db.session.add_all(appointments)
        db.session.commit()
        print("Seeding complete!")

# This makes the script runnable from the command line by typing 'python seed.py'
if __name__ == '__main__':
    seed_database()