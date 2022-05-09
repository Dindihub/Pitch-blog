from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm



@main.route('/')
def home():
    return render_template('home.html',title='home')

@main.route('/about')
def about():
    return render_template('about.html',title='about')


@main.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title = 'register',form = form)

@main.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title = 'login',form = form)





