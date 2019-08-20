import wtforms
from flask_wtf import FlaskForm
from wtforms import validators


class LoginForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[validators.DataRequired()])
    password = wtforms.PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = wtforms.BooleanField('Remember Me')
    submit = wtforms.SubmitField('Sign In')
