from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_123')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///givetake.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    skills_offered = db.relationship('Service', backref='provider', lazy=True)
    escrow_balance = db.Column(db.Float, default=0.0)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_required = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='available')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(20), default='pending')
    escrow_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    services = Service.query.filter_by(status='available').all()
    return render_template('index.html', services=services)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
            
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/create_service', methods=['GET', 'POST'])
@login_required
def create_service():
    if request.method == 'POST':
        service = Service(
            title=request.form.get('title'),
            description=request.form.get('description'),
            skill_required=request.form.get('skill_required'),
            provider=current_user
        )
        db.session.add(service)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('create_service.html')

@app.route('/request_exchange/<int:service_id>', methods=['POST'])
@login_required
def request_exchange(service_id):
    service = Service.query.get_or_404(service_id)
    
    # Create exchange request
    exchange = Exchange(
        service_id=service_id,
        provider_id=service.provider_id,
        requester_id=current_user.id,
        escrow_amount=50.0  # Example escrow amount
    )
    
    db.session.add(exchange)
    db.session.commit()
    
    flash('Exchange request sent!')
    return redirect(url_for('index'))

@app.route('/my_exchanges')
@login_required
def my_exchanges():
    provided_exchanges = Exchange.query.filter_by(provider_id=current_user.id).all()
    requested_exchanges = Exchange.query.filter_by(requester_id=current_user.id).all()
    return render_template('my_exchanges.html', 
                         provided_exchanges=provided_exchanges,
                         requested_exchanges=requested_exchanges)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)