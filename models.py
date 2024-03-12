
from flask_sqlalchemy import SQLAlchemy
import hashlib
from datetime import datetime
import enum

db = SQLAlchemy()


# class Gender(enum.Enum):
#     male = 'муж'
#     female = 'жен'


# class Fags(db.Model):
#     id_ = db.Column(db.Integer, primary_key=True)
#     fag_name = db.Column(db.String(80), nullable=False)
#     student = db.relationship('Students', backref=db.backref('fags'), lazy=True)
#
#     def __repr__(self):
#         return f'Fags({self.fag_name})'


class Registers(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return f'Зарегистрирован ({self.name}, {self.lastname})'