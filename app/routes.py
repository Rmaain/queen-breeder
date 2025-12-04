from app import app
from flask import render_template, url_for, flash, redirect, request
from app.forms import LoginForm, RegistrationForm,  AddHivesForm
from app import db, bcrypt
from app.models import User, Hive
from flask_login import login_user, current_user, logout_user, login_required
import cv2
import numpy as np
import base64
from PIL import Image





@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/registration", methods=['GET', 'POST'])
def Registration():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash(f'você foi logado com sucesso', 'Success')
            return redirect(url_for('home'))
        flash(f'Seu email ou senha estão incorretos', 'danger')
    return render_template("login.html", form=form)

@app.route("/analysis")
def analysis():
#     plt.plot([1, 2, 3, 5], [10, 5, 6, 9])
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format="png")
#     buffer.seek(0)
#     img_bytes = buffer.getvalue()
#     img_base64 = base64.b64encode(img_bytes).decode("utf-8")
#     return render_template("analysis.html", img_data=img_base64)
    return render_template("analysis.html")

@app.route("/addHives", methods=['GET', 'POST'])
def addHives():
    #img = Image.open(file.stream)
    form = AddHivesForm()
    if form.validate_on_submit():
        file = request.files.get('frames-${index+1}-image')
    return render_template("addHives.html", form=form)

@app.route("/listHives")
def listHives():
    return render_template("listHives.html")
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/account")
@login_required
def account():
    return render_template("account.html")
