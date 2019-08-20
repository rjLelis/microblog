from . import app
from flask import render_template, redirect, flash, url_for
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
    user = {'username': 'Renato'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me={form.remember_me.data}')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)