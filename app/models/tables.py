from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f'<User {self.username}>'

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
