import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    default_db_path = "postgres://{}:{}@{}/{}".format('user', 'password', 'localhost:5432', 'db_name')
    database_path = os.getenv('DATABASE_URL', default_db_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

class Task(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    body = Column(String(500))
    created = Column(db.DateTime)
    def __init__(self, body):
        self.body = body
        self.created = db.DateTime()
    def details(self):
        return {
            'id': self.id,
            'body': self.body,
            'created': self.created,
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()