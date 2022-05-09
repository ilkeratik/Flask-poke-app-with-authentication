from flask import Flask
from db.database import db
from db.mongodb import db as mdb
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

from app import user, authenticated_user


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/testdb'
app.config['MONGODB_SETTINGS'] = {
    'db': 'testdb',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)
mdb.init_app(app)

with app.app_context():
    db.create_all()