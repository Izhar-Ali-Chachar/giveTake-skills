from app import app, db, User, Service, Exchange
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_db():
    """Initialize the database with tables and sample data."""
    with app.app_context():
        # Drop all existing tables
        db.drop_all()
        
        # Create all tables
        db.create_all()
        
        # Create sample users
        users = [
            User(
                username='john_dev',
                email='john@example.com',
                password_hash=generate_password_hash('password123'),
                escrow_balance=100.0
            ),
            User(
                username='alice_coder',
                email='alice@example.com',
                password_hash=generate_password_hash('password123'),
                escrow_balance=100.0
            ),
            User(
                username='bob_programmer',
                email='bob@example.com',
                password_hash=generate_password_hash('password123'),
                escrow_balance=100.0
            )
        ]
        
        # Add users to database
        for user in users:
            db.session.add(user)
        db.session.commit()
        
        # Create sample services
        services = [
            Service(
                title='Python Web Development',
                description='I can help you build web applications using Flask or Django.',
                provider_id=1,
                skill_required='React Development',
                status='available'
            ),
            Service(
                title='Mobile App UI Design',
                description='Will design beautiful and intuitive mobile app interfaces.',
                provider_id=2,
                skill_required='Backend Development',
                status='available'
            ),
            Service(
                title='Database Optimization',
                description='Help optimize your database queries and structure.',
                provider_id=3,
                skill_required='UI/UX Design',
                status='available'
            )
        ]
        
        # Add services to database
        for service in services:
            db.session.add(service)
        db.session.commit()
        
        # Create sample exchanges
        exchanges = [
            Exchange(
                service_id=1,
                provider_id=1,
                requester_id=2,
                status='pending',
                escrow_amount=50.0,
                created_at=datetime.utcnow()
            ),
            Exchange(
                service_id=2,
                provider_id=2,
                requester_id=3,
                status='in_progress',
                escrow_amount=50.0,
                created_at=datetime.utcnow()
            )
        ]
        
        # Add exchanges to database
        for exchange in exchanges:
            db.session.add(exchange)
        db.session.commit()
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    # Confirm with user before proceeding
    response = input("This will reset the database. Are you sure? (y/n): ")
    if response.lower() == 'y':
        init_db()
        print("Database has been reset and initialized with sample data.")
    else:
        print("Database initialization cancelled.")