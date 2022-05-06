from flask import Flask
from database import db
app = Flask(__name__)

from app import user, authenticated_user

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/testdb'
db.init_app(app)

with app.app_context():
    db.create_all()