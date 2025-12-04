from app import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image_file = db.Column(db.String(100), nullable= False, default="default.jpg")
    hives = db.relationship('Hive', backref='owner', lazy=True)
    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password}, {self.image_file})'
class Hive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    frames = db.relationship('HiveFrame', backref='hive', lazy=True)

class HiveFrame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hive_id = db.Column(db.Integer, db.ForeignKey('hive.id'), nullable=False)
    brood_cell = db.Column(db.Integer)
        # Worker cell
        # Drone cell
        # Queen cell
            #Eggs
            #Larvae
            #Pupae
        # Pollen
    # honey_combs = db.Column(db.Integer)
    # Honeycombs_full
    # Honeycombs_empty

    # Honeycomb analysis
        # new comb
        # dark comb
        # old wax 
    # wax analysis
        #   Burr comb
        #   Cross comb
    # Propolish
    # disease and contamination detection


