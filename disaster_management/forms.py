from ast import Pass
from flask import Flask
from flask_wtf import FlaskForm
from sqlalchemy import String
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from wtforms import StringField, EmailField, PasswordField,SubmitField, BooleanField, TextAreaField, SelectField
from disaster_management.models import User

class UserRegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=40)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    email = EmailField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please use a different one')

    def validate_phone(self, phone):
        if not int(phone.data):
            raise ValidationError("Phone number must only contain digits")
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('That phone number is taken, please use a different one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please use a different one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class DisasterForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()], choices=('EarthQuake', 'Flood', 'Cyclone', 'Landslides'))
    pin_code = StringField('Pin Code', validators=[DataRequired(), Length(min=6, max=6)])
    phone = StringField('Phone number', validators=[DataRequired()])
    severeness = TextAreaField('Severeness')
    submit = SubmitField('Call help')
