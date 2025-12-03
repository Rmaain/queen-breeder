from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
from app import routes
