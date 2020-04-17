import wtforms
from flask_wtf import FlaskForm
from wtforms import validators
from .models import User


class LoginForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[validators.DataRequired()])
    password = wtforms.PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = wtforms.BooleanField('Remember Me')
    submit = wtforms.SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = wtforms.StringField('Username',
        validators=[validators.DataRequired()])

    email = wtforms.StringField('Email',
        validators=[validators.DataRequired(), validators.Email()])

    password = wtforms.PasswordField('Password',
        validators=[validators.DataRequired()])

    password2 = wtforms.PasswordField('Repeat password',
        validators=[validators.DataRequired(), validators.EqualTo('password')])

    submit = wtforms.SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise validators.ValidationError('Please user a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise validators.ValidationError('Please use a different email address.')
