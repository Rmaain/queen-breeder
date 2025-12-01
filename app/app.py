from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image_file = db.Column(db.String(100), nullable= False, default="default.jpg")
    hives = db.relationship('Hive', backref='author', lazy=True)
    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password}, {self.image_file})'
class Hive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/registration", methods=['GET', 'POST'])
def Registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,  email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sua conta foi criada! Agora você está pronto para logar', 'Success')
        return redirect(url_for('Login'))
    return render_template("registration.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Accounted created for {form.username.data}', 'Success')
        return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route("/analysis")
def analysis():
    plt.plot([1, 2, 3, 5], [10, 5, 6, 9])
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
    return render_template("analysis.html", img_data=img_base64)

@app.route("/addHives")
def addHives():
    return render_template("addHives.html")

@app.route("/listHives")
def listHives():
    return render_template("listHives.html")


if __name__ == "__main__":
    app.run(debug=True)

