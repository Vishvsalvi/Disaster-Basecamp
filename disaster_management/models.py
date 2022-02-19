from disaster_management import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin ):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'{self.username} - {self.email}'

class Disaster(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(), nullable=False)
    pin_code = db.Column(db.Integer(), nullable=False)
    severeness = db.Column(db.Text(), nullable=True)


db.create_all()
db.session.commit()

    