from disaster_management import app, db
from disaster_management.models import User
from disaster_management.forms import UserRegistrationForm, LoginForm, DisasterForm
from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
import hashlib
import geocoder
import smtplib

def hash_string(string):
    return hashlib.sha512(string.encode('utf-8')).hexdigest()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = hash_string(form.password.data)
            user = User(username=form.username.data, phone=form.phone.data,email=form.email.data, password=hashed_password )
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created you can now login', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == hash_string(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You are now logged in to the website')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/emergency', methods=['GET', 'PUT'])
def emergency():
    form = DisasterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            g = geocoder.ip('me')
            lat, lng = g[0], g[1]
            message = f"This is an emergency\nReach at this coordindates now {lat} -{lng} and contact {form.phone.data}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('vjti9952@gmail.com', 'VJTI1234')
            server.sendmail('vjti9952@gmail.com', 'vjti9952@gmail.com', message)

    return render_template('emergency.html', form=form)