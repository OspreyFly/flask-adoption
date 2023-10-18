from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Define a new database table"""
    __tablename__ = "pet_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    species = db.Column(db.String(200), nullable=False)
    photo_url = db.Column(db.String(200))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(200))
    available = db.Column(db.Boolean, nullable=False, default=False)


