from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

ROLE_USER = 10
ROLE_SERVER = 20


user_server = db.Table('user_server',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('server_id',db.Integer,db.ForeignKey('server.id'))
    )


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(Base, UserMixin):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_user(self):
        return self.role == self.ROLE_USER


    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)



class Server(Base, UserMixin):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(32),unique=True, index=True, nullable=False)
    city_address = db.Column(db.String(32),unique=False, index=True, nullable=False)
    timeout = db.Column(db.Integer,unique=False, index=True, nullable=False)
    port = db.Column(db.Integer, unique=False, index=True,nullable=False)
    _password = db.Column('password',db.String(256),nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_SERVER) 
    users = db.relationship('User',secondary=user_server,backref=db.backref('_servers',lazy='dynamic'),lazy='dynamic')

    def __repr__(self):
        return '<Server:{}>'.format(self.ip_address)

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)


