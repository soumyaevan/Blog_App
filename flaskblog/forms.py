from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20), 
                            Regexp("^[a-zA-Z]+[\._-]?[a-zA-Z0-9]+")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passsword', validators=[DataRequired(), Length(min=3, max=15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists. Please choose a different one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email address already exists. Please choose a different one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passsword', validators=[DataRequired(), Length(min=3, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')