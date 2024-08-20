from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # ForeignKey is a column that references the id of another database column
    # in this case we are referencing the id column of the User table
    # ForeignKey - must pass a valid id of an existing user to this field
    # one to many relationship - one user can have many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user.id is the table name and column name

# UserMixin is a class that has default implementations of the methods that Flask-Login expects user objects to have.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # no two users can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # one to many relationship - one user can have many notes