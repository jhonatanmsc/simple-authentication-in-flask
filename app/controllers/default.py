from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app import app, db
from app.models.forms import LoginForm
from app.models.forms import RegisterForm
from app.models.tables import User
import pdb

@app.route("/")
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    username = form.username.data
    password = form.password.data
    name = form.name.data
    email = form.email.data
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username, password, name, email)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for('login'))

    else:
        return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    username = form.username.data
    password = form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        
        if user and user.verify_password(password):
            login_user(user)
            flash("User logged-in!")
        else:
            flash("Invalid login!")
    else:
        print(form.errors)

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
